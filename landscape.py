#!/usr/bin/env python3
import argparse
import random

BIOMES = [
    "forest", "desert", "tundra", "ocean", "mountain range",
    "swamp", "cave system", "plain", "volcanic field", "coral reef",
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

# Weight tiers for word selection — common words appear more often, rare words less so
COMMON_WORDS = {
    "crystal", "shadow", "ancient", "forgotten", "silent",
    "mist", "light", "silence", "darkness",
    "trees", "stones", "ruins", "crystals",
    "whisper", "glow", "shimmer", "drift",
    "a gentle rain falls", "a still calm lingers", "mist curls along the ground",
}

RARE_WORDS = {
    "brass", "ivory", "glass",
    "fragrance", "radiance",
    "geodes", "fungi", "archways",
    "resonate", "vibrate",
    "ash drifts slowly downward",
}


def _word_weight(word):
    if word in RARE_WORDS:
        return 1
    if word in COMMON_WORDS:
        return 10
    return 5


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
        "verbs": ["wave", "stretch", "roll", "sway", "stretch"],
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
}


def _pick(category, biomes):
    """Pick a random word from the biome-specific pool(s) blended with the global pool.
    `biomes` is a list of biome names; words from all specified biomes are included.
    Words are weighted: common (10), normal (5), rare (1)."""
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
    }[category]
    pool = specific + global_pool
    weights = [_word_weight(w) for w in pool]
    return random.choices(pool, weights=weights, k=1)[0]


def generate_landscape(seed=None, biome=None, show_biome=False, fmt="prose", combine=None):
    if seed is not None:
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
        chosen = random.choice(BIOMES)
        biomes = [chosen]
        display = chosen

    adj = _pick("adjectives", biomes)
    element = _pick("elements", biomes)
    noun = _pick("nouns", biomes)
    verb = _pick("verbs", biomes)
    weather = _pick("weathers", biomes)

    parts = [
        f"A vast {adj} {display} stretches before you.",
        f"{element.capitalize()} {verb}s between the {noun}.",
        f"{weather.capitalize()}.",
    ]

    if random.random() < 0.3:
        parts.append(_pick("anomalies", biomes))

    joiner = "\n" if fmt == "poetic" else " "
    output = joiner.join(parts)
    if show_biome:
        if combine:
            output += f" [{', '.join(biomes)}]"
        else:
            output += f" [{display}]"
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
        "--format", type=str, default="prose", choices=["prose", "poetic"],
        help="Output format: prose (single line) or poetic (line breaks)",
    )
    parser.add_argument(
        "--combine", "-c", type=str, default=None,
        help="Combine multiple biomes (comma-separated, e.g. 'forest,desert')",
    )
    args = parser.parse_args()

    for i in range(args.count):
        print(generate_landscape(seed=args.seed, biome=args.biome, show_biome=args.show_biome, fmt=args.format, combine=args.combine))
        if args.count > 1 and i < args.count - 1:
            print()


if __name__ == "__main__":
    main()
