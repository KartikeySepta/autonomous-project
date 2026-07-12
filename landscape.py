#!/usr/bin/env python3
import argparse
import json
import random

BIOMES = [
    "forest", "desert", "tundra", "ocean", "mountain range",
    "swamp", "cave system", "plain", "volcanic field", "coral reef",
    "ruined city", "fungal grove", "sky islands",
]

# Global fallback word pools
ADJECTIVES = [
    "crystal", "shadow", "ember", "frost", "silent", "ancient",
    "forgotten", "bone", "iron", "glass", "crimson", "amethyst",
    "obsidian", "ivory", "brass", "moss-covered",
]

ELEMENTS = [
    "mist", "light", "sound", "stillness", "fragrance", "warmth",
    "echo", "silence", "radiance", "darkness",
]

NOUNS = [
    "trees", "spires", "stones", "ruins", "pillars", "archways",
    "roots", "crystals", "geodes", "fungi", "vines", "shells",
]

VERBS = [
    "whisper", "hum", "glow", "shimmer", "drift", "pulse",
    "vibrate", "sway", "glimmer", "resonate",
]

WEATHERS = [
    "a gentle rain falls",
    "a still calm lingers",
    "a warm breeze drifts through",
    "an unnatural silence hangs",
    "a faint humming fills the air",
    "ash drifts slowly downward",
    "mist curls along the ground",
    "the air shimmers with heat",
]

ANOMALIES = [
    "The gravity here feels wrong.",
    "Time seems to flow backward.",
    "Colors shift as you watch.",
    "The horizon curves upward.",
    "There is no sky — only stone above.",
    "Your footsteps make no sound.",
    "The shadows move against the wind.",
    "Everything is slightly out of focus.",
]

ADVERBS = [
    "softly", "endlessly", "gently", "relentlessly",
    "patiently", "eternally", "silently", "slowly",
    "constantly", "subtly", "quietly", "ceaselessly",
]

# Weight tiers for word selection — common words appear more often, rare words less so
COMMON_WORDS = {
    "crystal", "shadow", "ancient", "forgotten", "silent",
    "mist", "light", "silence", "darkness",
    "trees", "stones", "ruins", "crystals",
    "whisper", "glow", "shimmer", "drift",
    "a gentle rain falls", "a still calm lingers", "mist curls along the ground",
    "softly", "gently", "silently", "quietly",
}

RARE_WORDS = {
    "brass", "ivory", "glass",
    "fragrance", "radiance",
    "geodes", "fungi", "archways",
    "resonate", "vibrate",
    "ash drifts slowly downward",
    "relentlessly", "patiently", "eternally", "ceaselessly",
}


BIAS_MODES = {
    "normal":  {"common": 10, "normal": 5, "rare": 1},
    "common":  {"common": 20, "normal": 5, "rare": 1},
    "rare":    {"common": 5,  "normal": 5, "rare": 3},
    "flat":    {"common": 1,  "normal": 1, "rare": 1},
}

MOOD_BOOST = 5

MOOD_WORDS = {
    "eerie": {
        "adjectives": ["shadow", "silent", "forgotten", "bone", "obsidian", "pale", "deep"],
        "elements": ["echo", "silence", "darkness", "stillness", "cave wind"],
        "nouns": ["ruins", "stones", "crystals", "archways", "spires", "fissures"],
        "verbs": ["whisper", "hum", "vibrate", "resonate", "creak", "echo"],
        "adverbs": ["silently", "slowly", "eternally", "patiently", "ceaselessly"],
        "weathers": [
            "a still calm lingers",
            "an unnatural silence hangs",
            "mist curls along the ground",
            "the darkness presses in from all sides",
        ],
        "anomalies": [
            "Time seems to flow backward.",
            "Colors shift as you watch.",
            "The horizon curves upward.",
            "Your footsteps make no sound.",
            "The shadows move against the wind.",
            "Passages rearrange when you blink.",
            "The ice sings when the wind blows across it.",
        ],
    },
    "vibrant": {
        "adjectives": ["crystal", "crimson", "amethyst", "golden", "luminous", "vibrant", "bioluminescent", "reef-born"],
        "elements": ["light", "radiance", "warmth", "fragrance", "birdsong", "leaf rustle"],
        "nouns": ["crystals", "geodes", "glades", "canopies", "polyps", "groves"],
        "verbs": ["glow", "shimmer", "pulse", "glimmer", "resonate", "wave"],
        "adverbs": ["gently", "softly", "endlessly", "quietly"],
        "weathers": [
            "a warm breeze drifts through",
            "sunlight filters through the canopy in golden beams",
            "the water is clear and impossibly blue",
            "sunlight dances on the water in shifting patterns",
        ],
        "anomalies": [
            "The water glows with an inner light.",
            "The coral pulses in unison like a single heart.",
            "Fish leave trails of light as they swim.",
            "Every shell contains a tiny, perfect melody.",
            "Fungal spores hang in the air like tiny lanterns.",
        ],
    },
    "desolate": {
        "adjectives": ["forgotten", "bone", "scorched", "barren", "frozen", "rotting", "windswept", "cracked"],
        "elements": ["stillness", "silence", "darkness", "dry air", "ash fall"],
        "nouns": ["ruins", "dunes", "ice fields", "crevasses", "slag heaps", "permafrost"],
        "verbs": ["crack", "freeze", "drift", "scour", "bake", "stagnate"],
        "adverbs": ["relentlessly", "constantly", "slowly", "eternally"],
        "weathers": [
            "ash drifts slowly downward",
            "a biting wind carries ice crystals",
            "the sun beats down without mercy",
            "a hot wind scours the dunes",
        ],
        "anomalies": [
            "The sand falls upward here.",
            "There is no sky — only stone above.",
            "Shapes move beneath the frozen surface.",
            "The heat does not burn — it freezes.",
            "Distant figures never get closer no matter how far you walk.",
        ],
    },
}


def _word_weight(word, bias="normal", mood=None, category=None, mood_weight=MOOD_BOOST, mood_weight_overrides=None):
    weights = BIAS_MODES[bias]
    if word in RARE_WORDS:
        base = weights["rare"]
    elif word in COMMON_WORDS:
        base = weights["common"]
    else:
        base = weights["normal"]
    if mood and category:
        moods = mood if isinstance(mood, (list, tuple)) else [mood]
        for m in moods:
            if m in MOOD_WORDS and word in MOOD_WORDS[m].get(category, []):
                effective_mw = (mood_weight_overrides or {}).get(category, mood_weight)
                base *= effective_mw
                break
    return base


def _conjugate(verb):
    if verb.endswith(("s", "sh", "ch", "x", "z", "o")):
        return verb + "es"
    if verb.endswith("y") and len(verb) > 1 and verb[-2] not in "aeiou":
        return verb[:-1] + "ies"
    return verb + "s"


# Named template sets — "random" uses random.choice per slot; others force a fixed index
TEMPLATE_SETS = {
    "random": None,
    "first": 0,
    "second": 1,
    "third": 2,
}


def _pick_template(slot, template_set, template_overrides=None):
    effective = (template_overrides or {}).get(slot, template_set)
    templates = SENTENCE_TEMPLATES[slot]
    if effective == "random":
        return random.choice(templates)
    idx = min(TEMPLATE_SETS[effective], len(templates) - 1)
    return templates[idx]


# Sentence templates for landscape generation — randomly selected each time for variety
def _format_tmpl(template, **kwargs):
    result = template.format(**kwargs)
    return result.replace("  ", " ").replace(" .", ".")


SENTENCE_TEMPLATES = {
    "opening": [
        "A vast {adj} {display} stretches {adverb} before you.",
        "Before you, a {adj} {display} comes into view {adverb}.",
        "The {adj} {display} lies {adverb} ahead.",
    ],
    "middle": [
        "{Element} {verb_conjugated} between the {noun}.",
        "Among the {adj} {noun}, {element} {verb_conjugated}.",
        "The {adj} {noun} {verb} with {element}.",
        "{Element} {verb_conjugated} {adverb} through the {noun}.",
        "Beneath the {noun}, {element} {verb_conjugated} {adverb}.",
    ],
    "weather": [
        "{Weather} {adverb}.",
        "The air tells its own story: {weather}.",
        "{Weather}, as if the {display} itself breathes.",
    ],
    "anomaly": [
        "{anomaly}",
        "Something is not right — {anomaly}",
        "A strange detail catches your eye: {anomaly_lower}",
        "There is a quiet wrongness here: {anomaly_lower}",
    ],
}

# Biome-specific word enrichments — blended with global pools for more evocative output
BIOME_WORDS = {
    "forest": {
        "adjectives": ["dappled", "verdant", "whispering", "mossy", "deep"],
        "elements": ["birdsong", "leaf rustle", "sap scent", "shade"],
        "nouns": ["canopies", "trunks", "glades", "ferns", "branches"],
        "verbs": ["rustle", "whisper", "breathe", "creak", "shade"],
        "weathers": [
            "sunlight filters through the canopy in golden beams",
            "a soft wind stirs the leaves overhead",
            "the undergrowth glistens with morning dew",
        ],
        "anomalies": [
            "Every leaf faces the same direction.",
            "The rings on every stump glow faintly.",
            "Fungal spores hang in the air like tiny lanterns.",
        ],
    },
    "desert": {
        "adjectives": ["scorched", "barren", "windswept", "blazing", "golden"],
        "elements": ["heat shimmer", "sand grain", "dry air", "sun flare"],
        "nouns": ["dunes", "mesas", "canyons", "plateaus", "oases"],
        "verbs": ["bake", "crack", "drift", "shimmer", "scour"],
        "weathers": [
            "heat ripples rise from the sand in waves",
            "a hot wind scours the dunes",
            "the sun beats down without mercy",
        ],
        "anomalies": [
            "The sand falls upward here.",
            "A second sun hangs low on the horizon.",
            "The dunes form perfect geometric spirals.",
        ],
    },
    "ocean": {
        "adjectives": ["deep", "abyssal", "endless", "bioluminescent", "saline"],
        "elements": ["salt spray", "current pull", "ocean scent", "pressure"],
        "nouns": ["trenches", "currents", "reefs", "abysses", "swells"],
        "verbs": ["crash", "surge", "drift", "plunge", "churn"],
        "weathers": [
            "waves roll in from an unseen horizon",
            "a fine salt mist hangs in the air",
            "the water is eerily still and black",
        ],
        "anomalies": [
            "The water glows with an inner light.",
            "Fish swim in geometric formation overhead.",
            "The surface is a mirror to a different sky.",
        ],
    },
    "tundra": {
        "adjectives": ["frozen", "barren", "windswept", "auroral", "pale"],
        "elements": ["frost", "aurora light", "wind howl", "hoar"],
        "nouns": ["ice fields", "glaciers", "crevasses", "permafrost", "snowdrifts"],
        "verbs": ["freeze", "howl", "crack", "gleam", "drift"],
        "weathers": [
            "the aurora pulses in silent sheets of green",
            "a biting wind carries ice crystals",
            "snow falls in a world of white and silence",
        ],
        "anomalies": [
            "The ice sings when the wind blows across it.",
            "Shapes move beneath the frozen surface.",
            "The aurora casts shadows that move on their own.",
        ],
    },
    "mountain range": {
        "adjectives": ["jagged", "towering", "snow-capped", "ancient", "granite"],
        "elements": ["stone echo", "thin air", "alpine scent", "cold light"],
        "nouns": ["peaks", "ridges", "cliffs", "valleys", "crags"],
        "verbs": ["tower", "loom", "echo", "rise", "cut"],
        "weathers": [
            "wind howls through the narrow passes",
            "clouds cling to the peaks like shawls",
            "thin air carries every sound for miles",
        ],
        "anomalies": [
            "The peaks rearrange themselves at night.",
            "Echoes return minutes after you speak.",
            "A stone bridge arcs between clouds.",
        ],
    },
    "swamp": {
        "adjectives": ["fetid", "murky", "choked", "rotting", "drowned"],
        "elements": ["marsh gas", "decay scent", "still water", "humidity"],
        "nouns": ["bayous", "mangroves", "bogs", "quicksand", "thickets"],
        "verbs": ["bubble", "fester", "seep", "creep", "stagnate"],
        "weathers": [
            "fog rolls low over the black water",
            "the air is thick and heavy with moisture",
            "gnats swarm in the stagnant heat",
        ],
        "anomalies": [
            "Will-o'-wisps flicker in perfect constellations.",
            "The water reflects a world that no longer exists.",
            "Bubbles rise spelling out words in an old language.",
        ],
    },
    "cave system": {
        "adjectives": ["subterranean", "echoing", "pitch-dark", "limestone", "dripping"],
        "elements": ["drip sound", "stone scent", "darkness", "cave wind"],
        "nouns": ["stalactites", "caverns", "tunnels", "chambers", "fissures"],
        "verbs": ["drip", "echo", "glimmer", "resonate", "collapse"],
        "weathers": [
            "water drips in a slow, endless rhythm",
            "a draft carries the scent of deep earth",
            "the darkness presses in from all sides",
        ],
        "anomalies": [
            "The crystals here glow without a light source.",
            "Passages rearrange when you blink.",
            "The cave breathes — a slow, deep rhythm.",
        ],
    },
    "plain": {
        "adjectives": ["endless", "golden", "wide", "wind-scoured", "open"],
        "elements": ["grass rustle", "open sky", "distant haze", "earth scent"],
        "nouns": ["grasses", "horizons", "fields", "bluffs", "meadows"],
        "verbs": ["wave", "stretch", "roll", "sway", "bend"],
        "weathers": [
            "a warm wind sends ripples across the grass",
            "clouds cast slow-moving shadows on the land",
            "the sky stretches forever, blue and empty",
        ],
        "anomalies": [
            "The grass bends in patterns that spell something.",
            "There is no horizon — land and sky merge as one.",
            "Distant figures never get closer no matter how far you walk.",
        ],
    },
    "volcanic field": {
        "adjectives": ["scorched", "smoldering", "obsidian", "sulfurous", "cracked"],
        "elements": ["sulfur scent", "heat haze", "lava glow", "ash fall"],
        "nouns": ["vents", "fissures", "calderas", "magma chambers", "slag heaps"],
        "verbs": ["smolder", "hiss", "crack", "erupt", "seethe"],
        "weathers": [
            "ash falls like gray snow from a black sky",
            "steam vents hiss in ragged chorus",
            "lava illuminates the smoke from below",
        ],
        "anomalies": [
            "Lava flows uphill without reason.",
            "Obsidian shards show visions of the past.",
            "The heat does not burn — it freezes.",
        ],
    },
    "coral reef": {
        "adjectives": ["luminous", "vibrant", "underwater", "reef-born", "crystalline"],
        "elements": ["coral scent", "underwater light", "current hum", "salt"],
        "nouns": ["polyps", "anemones", "lagoon beds", "drop-offs", "groves"],
        "verbs": ["pulse", "drift", "glow", "wave", "filter"],
        "weathers": [
            "sunlight dances on the water in shifting patterns",
            "warm currents drift through the coral canyons",
            "the water is clear and impossibly blue",
        ],
        "anomalies": [
            "The coral pulses in unison like a single heart.",
            "Fish leave trails of light as they swim.",
            "Every shell contains a tiny, perfect melody.",
        ],
    },
    "ruined city": {
        "adjectives": ["crumbling", "hollow", "rusted", "fallen", "skeletal", "gutted", "fractured", "ashen"],
        "elements": ["distant hum", "dust", "rust scent", "broken light", "stifled echo"],
        "nouns": ["facades", "girders", "husks", "plazas", "overpasses", "broken windows"],
        "verbs": ["creak", "settle", "sway", "crumble", "groan"],
        "weathers": [
            "ash drifts through broken windows like snow",
            "a pale sun filters through smog",
            "the wind moans through empty streets",
        ],
        "anomalies": [
            "The street signs point in directions that don't exist.",
            "Every clock reads the same time.",
            "Shadows of people who aren't there move along the walls.",
        ],
    },
    "fungal grove": {
        "adjectives": ["bioluminescent", "spongy", "spore-filled", "mycelial", "phosphorescent", "thriving", "veined", "delicate"],
        "elements": ["spore glow", "fungal scent", "mycelium hum", "rot warmth"],
        "nouns": ["caps", "gills", "stalks", "hyphae", "puffballs", "tendrils"],
        "verbs": ["pulse", "glow", "release", "expand", "spore"],
        "weathers": [
            "spores drift through the air like slow-motion snow",
            "the ground pulses with faint blue light",
            "a warm dampness carries the scent of growth",
        ],
        "anomalies": [
            "The mushrooms sing at frequencies only bones can feel.",
            "Spores form faces when they settle.",
            "The entire grove shares one consciousness.",
        ],
    },
    "sky islands": {
        "adjectives": ["floating", "cloud-wreathed", "sun-bleached", "sky-born", "ethereal", "exposed", "high", "wind-bitten"],
        "elements": ["cloud vapor", "wind shear", "sky-blue light", "thin air"],
        "nouns": ["archipelagos", "peaks", "bridges", "precipices", "cloud banks", "updrafts"],
        "verbs": ["float", "drift", "soar", "hover", "ride"],
        "weathers": [
            "clouds churn far below like a white sea",
            "lightning arcs silently between nearby islands",
            "the wind is constant and unforgiving",
        ],
        "anomalies": [
            "The islands orbit each other in a slow dance.",
            "Waterfalls flow upward into the clouds.",
            "A bell tolls from an island that no one has ever reached.",
        ],
    },
}


def _pick(category, biomes, bias="normal", mood=None, mood_weight=MOOD_BOOST, bias_overrides=None, mood_weight_overrides=None, used_words=None):
    """Pick a random word from the biome-specific pool(s) blended with the global pool.
    `biomes` is a list of biome names; words from all specified biomes are included.
    Words are weighted per the given bias mode and optionally boosted for mood.
    `bias_overrides` is an optional dict mapping category name -> bias mode,
    allowing per-category bias that takes precedence over the global `bias`.
    `mood_weight_overrides` is an optional dict mapping category name -> float,
    allowing per-category mood-weight that takes precedence over the global `mood_weight`.
    `used_words` is an optional set of words already used in this generation — the
    chosen word is added to it, and already-used words are excluded from selection."""
    effective_bias = (bias_overrides or {}).get(category, bias)
    specific = []
    for b in biomes:
        specific.extend(BIOME_WORDS.get(b, {}).get(category, []))
    global_pool = {
        "adjectives": ADJECTIVES,
        "elements": ELEMENTS,
        "nouns": NOUNS,
        "verbs": VERBS,
        "weathers": WEATHERS,
        "anomalies": ANOMALIES,
        "adverbs": ADVERBS,
    }[category]
    pool = specific + global_pool
    if used_words is not None:
        available = [w for w in pool if w not in used_words]
        if available:
            pool = available
    weights = [_word_weight(w, effective_bias, mood, category, mood_weight, mood_weight_overrides) for w in pool]
    chosen = random.choices(pool, weights=weights, k=1)[0]
    if used_words is not None:
        used_words.add(chosen)
    return chosen


def generate_landscape(seed=None, biome=None, show_biome=False, fmt="prose", combine=None, detail=1, bias="normal", show_seed=False, mood=None, mood_weight=MOOD_BOOST, template_set="random", bias_overrides=None, mood_weight_overrides=None, template_overrides=None, anomaly_prob=0.3, anomaly_count=1, dedup=True, adverb_enabled=True, biome_weights=None):
    if seed is not None:
        random.seed(seed)
    elif show_seed:
        seed = random.randint(0, 2**31 - 1)
        random.seed(seed)

    if biome is not None:
        biomes = [biome.lower()]
        display = biome.lower()
    elif combine is not None:
        biomes = [b.strip().lower() for b in combine.split(",")]
        if len(biomes) == 0:
            biomes = [random.choice(BIOMES)]
        display = " and ".join(biomes)
    else:
        if biome_weights:
            weights = [biome_weights.get(b, 1) for b in BIOMES]
            if all(w == 0 for w in weights):
                chosen = random.choice(BIOMES)
            else:
                chosen = random.choices(BIOMES, weights=weights, k=1)[0]
        else:
            chosen = random.choice(BIOMES)
        biomes = [chosen]
        display = chosen

    used_words = set() if dedup else None

    adj = _pick("adjectives", biomes, bias=bias, mood=mood, mood_weight=mood_weight, bias_overrides=bias_overrides, mood_weight_overrides=mood_weight_overrides, used_words=used_words)
    if adverb_enabled:
        adverb = _pick("adverbs", biomes, bias=bias, mood=mood, mood_weight=mood_weight, bias_overrides=bias_overrides, mood_weight_overrides=mood_weight_overrides, used_words=used_words)
    else:
        adverb = ""
    opening_tmpl = _pick_template("opening", template_set, template_overrides)
    parts = [_format_tmpl(opening_tmpl, adj=adj, display=display, adverb=adverb)]

    for _ in range(max(detail, 0)):
        element = _pick("elements", biomes, bias=bias, mood=mood, mood_weight=mood_weight, bias_overrides=bias_overrides, mood_weight_overrides=mood_weight_overrides, used_words=used_words)
        noun = _pick("nouns", biomes, bias=bias, mood=mood, mood_weight=mood_weight, bias_overrides=bias_overrides, mood_weight_overrides=mood_weight_overrides, used_words=used_words)
        verb = _pick("verbs", biomes, bias=bias, mood=mood, mood_weight=mood_weight, bias_overrides=bias_overrides, mood_weight_overrides=mood_weight_overrides, used_words=used_words)
        verb_conjugated = _conjugate(verb)
        if adverb_enabled:
            adverb = _pick("adverbs", biomes, bias=bias, mood=mood, mood_weight=mood_weight, bias_overrides=bias_overrides, mood_weight_overrides=mood_weight_overrides, used_words=used_words)
        else:
            adverb = ""
        middle_tmpl = _pick_template("middle", template_set, template_overrides)
        parts.append(
            _format_tmpl(middle_tmpl, Element=element.capitalize(), element=element, adj=adj, noun=noun, verb=verb, verb_conjugated=verb_conjugated, adverb=adverb)
        )

        weather = _pick("weathers", biomes, bias=bias, mood=mood, mood_weight=mood_weight, bias_overrides=bias_overrides, mood_weight_overrides=mood_weight_overrides, used_words=used_words)
        weather_tmpl = _pick_template("weather", template_set, template_overrides)
        parts.append(
            _format_tmpl(weather_tmpl, Weather=weather.capitalize(), weather=weather, display=display, adverb=adverb)
        )

    if detail >= 1 and anomaly_count > 0:
        for _ in range(anomaly_count):
            if random.random() < anomaly_prob:
                anomaly_tmpl = _pick_template("anomaly", template_set, template_overrides)
                anomaly_word = _pick("anomalies", biomes, bias=bias, mood=mood, mood_weight=mood_weight, bias_overrides=bias_overrides, mood_weight_overrides=mood_weight_overrides, used_words=used_words)
                anomaly_lower = anomaly_word[0].lower() + anomaly_word[1:]
                parts.append(_format_tmpl(anomaly_tmpl, anomaly=anomaly_word, anomaly_lower=anomaly_lower, adverb=adverb))

    joiner = "\n" if fmt == "poetic" else " "
    output = joiner.join(parts)

    if fmt == "json":
        data = {"text": output}
        data["biome"] = biomes if combine else display
        if combine:
            data["biomes"] = biomes
        if seed is not None:
            data["seed"] = seed
        if mood:
            data["mood"] = mood if isinstance(mood, (list, tuple)) else [mood]
        data["mood_weight"] = mood_weight
        data["detail"] = detail
        data["bias"] = bias
        data["template_set"] = template_set
        data["anomaly_prob"] = anomaly_prob
        data["anomaly_count"] = anomaly_count
        if bias_overrides:
            data["bias_overrides"] = bias_overrides
        if mood_weight_overrides:
            data["mood_weight_overrides"] = mood_weight_overrides
        if template_overrides:
            data["template_overrides"] = template_overrides
        if biome_weights:
            data["biome_weights"] = biome_weights
        return json.dumps(data)

    if show_biome:
        if combine:
            output += f" [{', '.join(biomes)}]"
        else:
            output += f" [{display}]"
    if show_seed:
        output += f" [seed={seed}]"
    return output


def main():
    parser = argparse.ArgumentParser(
        prog="landscape",
        description="Generate procedural landscape descriptions",
    )
    parser.add_argument(
        "--count", "-n", type=int, default=1,
        help="Number of landscapes to generate (default: 1)",
    )
    parser.add_argument(
        "--seed", type=int, default=None,
        help="Random seed for reproducible output",
    )
    parser.add_argument(
        "--biome", type=str, default=None,
        help="Force a specific biome (overrides random selection)",
    )
    parser.add_argument(
        "--show-biome", action="store_true",
        help="Reveal the biome name in the output",
    )
    parser.add_argument(
        "--format", type=str, default="prose", choices=["prose", "poetic", "json"],
        help="Output format: prose (single line), poetic (line breaks), or json (structured metadata)",
    )
    parser.add_argument(
        "--combine", "-c", type=str, default=None,
        help="Combine multiple biomes (comma-separated, e.g. 'forest,desert')",
    )
    parser.add_argument(
        "--detail", "-d", type=int, default=1, choices=[0, 1, 2, 3],
        help="Number of middle/weather sentence pairs (0-3, default: 1)",
    )
    parser.add_argument(
        "--anomaly-prob", type=float, default=0.3,
        help="Probability of an anomaly appearing (0.0 to 1.0, default: 0.3)",
    )
    parser.add_argument(
        "--anomaly-count", type=int, default=1, choices=[0, 1, 2, 3],
        help="Number of anomaly chances per landscape (default: 1)",
    )
    parser.add_argument(
        "--bias", type=str, default="normal", choices=["normal", "common", "rare", "flat"],
        help="Word selection bias: normal (default), common (favors common words), rare (favors rare words), flat (uniform, no weighting)",
    )
    parser.add_argument("--bias-adjective", type=str, default=None, choices=["normal", "common", "rare", "flat"],
        help="Per-category override: bias for adjectives (overrides --bias)")
    parser.add_argument("--bias-element", type=str, default=None, choices=["normal", "common", "rare", "flat"],
        help="Per-category override: bias for elements")
    parser.add_argument("--bias-noun", type=str, default=None, choices=["normal", "common", "rare", "flat"],
        help="Per-category override: bias for nouns")
    parser.add_argument("--bias-verb", type=str, default=None, choices=["normal", "common", "rare", "flat"],
        help="Per-category override: bias for verbs")
    parser.add_argument("--bias-weather", type=str, default=None, choices=["normal", "common", "rare", "flat"],
        help="Per-category override: bias for weathers")
    parser.add_argument("--bias-anomaly", type=str, default=None, choices=["normal", "common", "rare", "flat"],
        help="Per-category override: bias for anomalies")
    parser.add_argument(
        "--mood", action="append", type=str, default=None,
        choices=list(MOOD_WORDS.keys()),
        help="Mood overlay(s) that boost tone-matched words. Use multiple times to blend moods (e.g. --mood eerie --mood vibrant)",
    )
    parser.add_argument(
        "--mood-weight", type=float, default=MOOD_BOOST,
        help=f"Weight multiplier for mood-matched words (default: {MOOD_BOOST}, higher = stronger mood influence)",
    )
    parser.add_argument("--mood-weight-adjective", type=float, default=None,
        help="Per-category override: mood weight for adjectives (overrides --mood-weight)")
    parser.add_argument("--mood-weight-element", type=float, default=None,
        help="Per-category override: mood weight for elements")
    parser.add_argument("--mood-weight-noun", type=float, default=None,
        help="Per-category override: mood weight for nouns")
    parser.add_argument("--mood-weight-verb", type=float, default=None,
        help="Per-category override: mood weight for verbs")
    parser.add_argument("--mood-weight-weather", type=float, default=None,
        help="Per-category override: mood weight for weathers")
    parser.add_argument("--mood-weight-anomaly", type=float, default=None,
        help="Per-category override: mood weight for anomalies")
    parser.add_argument(
        "--show-seed", action="store_true",
        help="Display the random seed used for reproducibility",
    )
    parser.add_argument(
        "--template-set", type=str, default="random", choices=list(TEMPLATE_SETS.keys()),
        help="Template selection mode: random (default), first, second, or third",
    )
    parser.add_argument("--template-opening", type=str, default=None, choices=list(TEMPLATE_SETS.keys()),
        help="Per-slot override: template for opening (overrides --template-set)")
    parser.add_argument("--template-middle", type=str, default=None, choices=list(TEMPLATE_SETS.keys()),
        help="Per-slot override: template for middle sentences")
    parser.add_argument("--template-weather", type=str, default=None, choices=list(TEMPLATE_SETS.keys()),
        help="Per-slot override: template for weather sentences")
    parser.add_argument("--template-anomaly", type=str, default=None, choices=list(TEMPLATE_SETS.keys()),
        help="Per-slot override: template for anomaly sentences")
    parser.add_argument(
        "--output", "-o", type=str, default=None,
        help="Write output to a file instead of stdout",
    )
    parser.add_argument(
        "--no-dedup", action="store_true",
        help="Disable cross-sentence word deduplication (allow repeated words)",
    )
    parser.add_argument(
        "--no-adverb", action="store_true",
        help="Disable adverb insertion in landscape descriptions",
    )
    parser.add_argument(
        "--biome-weight", type=str, default=None,
        help="Weight biomes for random selection (comma-separated biome=weight pairs, e.g. forest=5,desert=1)",
    )
    args = parser.parse_args()

    bias_overrides = {}
    cat_map = {
        "bias_adjective": "adjectives",
        "bias_element": "elements",
        "bias_noun": "nouns",
        "bias_verb": "verbs",
        "bias_weather": "weathers",
        "bias_anomaly": "anomalies",
    }
    for flag_cat, internal_cat in cat_map.items():
        val = getattr(args, flag_cat)
        if val is not None:
            bias_overrides[internal_cat] = val

    mood_weight_overrides = {}
    mw_cat_map = {
        "mood_weight_adjective": "adjectives",
        "mood_weight_element": "elements",
        "mood_weight_noun": "nouns",
        "mood_weight_verb": "verbs",
        "mood_weight_weather": "weathers",
        "mood_weight_anomaly": "anomalies",
    }
    for flag_cat, internal_cat in mw_cat_map.items():
        val = getattr(args, flag_cat)
        if val is not None:
            mood_weight_overrides[internal_cat] = val

    template_overrides = {}
    tmpl_slot_map = {
        "template_opening": "opening",
        "template_middle": "middle",
        "template_weather": "weather",
        "template_anomaly": "anomaly",
    }
    for flag_cat, slot in tmpl_slot_map.items():
        val = getattr(args, flag_cat)
        if val is not None:
            template_overrides[slot] = val

    biome_weights = None
    if args.biome_weight:
        biome_weights = {}
        for pair in args.biome_weight.split(","):
            b, w = pair.split("=")
            biome_weights[b.strip().lower()] = float(w)

    lines = []
    for i in range(args.count):
        effective_seed = args.seed + i if args.seed is not None else None
        lines.append(generate_landscape(seed=effective_seed, biome=args.biome, show_biome=args.show_biome, fmt=args.format, combine=args.combine, detail=args.detail, bias=args.bias, show_seed=args.show_seed, mood=args.mood, mood_weight=args.mood_weight, template_set=args.template_set, anomaly_prob=args.anomaly_prob, anomaly_count=args.anomaly_count, bias_overrides=bias_overrides, mood_weight_overrides=mood_weight_overrides, template_overrides=template_overrides, dedup=not args.no_dedup, adverb_enabled=not args.no_adverb, biome_weights=biome_weights))
    if args.format == "json" and len(lines) > 1:
        output = "[" + ",\n".join(lines) + "]\n"
    else:
        output = "\n\n".join(lines) + ("\n" if lines else "")
    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
    else:
        print(output, end="")


if __name__ == "__main__":
    main()
