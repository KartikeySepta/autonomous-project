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
    "snow falls in heavy flakes",
    "a cold fog rolls in from nowhere",
    "the ground exhales a thin vapor",
    "lightning flickers on the horizon",
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
    "You remember this landscape from a dream you have never had.",
    "Every breath tastes of a season that does not exist.",
    "The geometry of the landscape follows rules you cannot quite recall.",
    "Something is just beyond sight — a presence that never arrives.",
]

ECHOES = [
    "The {adj} {display} remembers {adverb}.",
    "The {display} has been waiting {adverb} for you {time_word}.",
    "Nothing in the {display} has changed in a thousand years.",
    "The echoes of the past linger {adverb} in the air of the {display}.",
    "You feel as though you are being watched by the {color} {element} itself.",
    "There is a sense of deep time here, pressing down {adverb} {time_word}.",
    "This place exists outside of time, in the {color} {element}.",
    "The stones remember {adverb} what the wind has forgotten.",
    "Something important happened in the {adj} {display} once.",
    "The silence here is older than any sound.",
    "Light {adverb} bends through the {adj} air of the {display} like something {color} is calling.",
    "The wind carries a memory through the {display} {time_word}, a voice with no mouth.",
    "Deep beneath the {display}, something vast turns over {adverb} in its sleep.",
    "The {display} holds its breath {time_word}, waiting for something that has not yet arrived.",
    "There is a {color} scent of {element} caught in the {adj} air of the {display}.",
]

LEGENDS = [
    "The oldest maps leave the {display} blank.",
    "Locals say the {display} was not here a century ago.",
    "Pilgrims once walked through the {display} in silence, never speaking.",
    "Beneath the {display}, something older than stone is buried.",
    "The {display} has many names, all of them forgotten.",
    "No one who enters the {display} returns unchanged.",
    "There is a song about the {display}, but no one sings it anymore.",
    "The {display} is marked on no map, yet everyone knows of it.",
    "They say the {display} dreams of a time before people.",
    "A hermit once lived in the {display} — they found only silence.",
    "The {display} remembers those who built it, even if no one else does.",
    "They say the {display} can be seen from far away, but no path leads to it.",
    "Every stone in the {display} was placed by hand, long before anyone lived here.",
    "When the wind moves through the {display}, it sounds like a name you almost recognize.",
    "There is a well in the {display} that no one has ever reached the bottom of.",
    "The {display} appears in the dreams of those who have never seen it.",
    "There is a bell in the {display} that rings only when no one is listening.",
    "The {display} has a scent that cannot be described, only remembered.",
    "Every path through the {display} leads to the same clearing, no matter where you start.",
    "The {display} was built by no one, for no purpose, and yet it endures.",
]

ADVERBS = [
    "softly", "endlessly", "gently", "relentlessly",
    "patiently", "eternally", "silently", "slowly",
    "constantly", "subtly", "quietly", "ceaselessly",
]

COLORS = [
    "vivid", "murky", "burnished", "stark",
    "lurid", "mottled", "bleached", "veined",
    "iridescent", "fluorescent", "scintillating", "coruscating",
]

TIME_WORDS = [
    "already", "still", "yet", "now", "once", "always",
]

TIMES_OF_DAY = [
    "Dawn breaks over the landscape",
    "The dead of night holds the land in darkness",
    "A blazing noon sun beats down without mercy",
    "Dusk settles over the landscape",
    "Early morning light bathes the land in pale gold",
    "Midnight beneath a crescent moon covers all in silver",
    "Twilight fades to darkness as night takes hold",
    "The golden hour before sunset paints everything amber",
    "The first light of morning touches the land",
    "A starless night presses down in absolute blackness",
    "Late afternoon stretches long shadows across the landscape",
    "A storm-heavy sky presses down upon the landscape",
    "The blue hour casts a deep indigo glow across the landscape",
    "The witching hour settles over the landscape in absolute stillness",
    "Morning mist clings to the landscape like a half-remembered dream",
]

SEASONS = [
    "It is early spring — the first buds push through the thawing earth",
    "High summer holds the land in a haze of heat and droning insects",
    "Autumn has turned the landscape into a study in gold and decay",
    "Deep winter wraps the landscape in silence and frost",
    "The tender green of late spring covers everything in new growth",
    "Midsummer's lush fullness spills across the landscape in every direction",
    "A sharp autumn chill tinges the air with the scent of falling leaves",
    "The first snow of winter has fallen, muffling the world in white",
    "Late autumn strips the landscape bare, revealing its bones",
    "Spring thunder rolls across a landscape reborn from rain",
    "Late winter's grip loosens as meltwater carves through the ice",
    "The lengthening shadows of late summer stretch across fields heavy with seed",
    "A pale autumn sun hangs low as the landscape prepares for winter's rest",
    "A hard winter freeze transforms the landscape into a palace of crystal and ice",
    "The soft persistent rain of early spring washes winter's last traces away",
]

SOUNDSCAPES = [
    "The {display} hums {adverb} with a tone that seems to come from everywhere at once.",
    "Somewhere in the {display}, something large shifts and settles {adverb}.",
    "The wind through the {display} sounds like {color} glass shattering {adverb}.",
    "A {adj} sound echoes through the {display} — close, though nothing is there.",
    "The {adverb} call of an unknown creature rings out across the {display}.",
    "A rhythm pulses {adverb} from deep within the {display} — slow, patient, {adj}.",
    "The {display} whispers {adverb}, a sound just at the edge of hearing.",
    "You hear the {display} breathing — a slow, {adj} rhythm that shakes the {element}.",
    "A low drone rises and falls {adverb} somewhere deep in the {display}.",
    "The {element} of the {display} crackles {adverb} like distant radio static.",
    "Footsteps echo {adverb} through the {display}, though you are alone.",
    "From the {adj} depths of the {display}, a single {color} note rings out {adverb}.",
    "Water drips {adverb} from the {adj} surfaces of the {display}, each drop a bright {color} note against the {element}.",
    "A {adj} music drifts {adverb} through the {display}, as if the {color} {element} itself has learned to sing.",
    "The wind howls {adverb} through the {adj} reaches of the {display}, a {color} sound that seems to shape the very {element}.",
    "{adj} voices whisper {adverb} in the {display}, a chorus of {color} sounds that never form words.",
    "The {adj} bones of the {display} groan {adverb}, a deep {color} sound that resonates through the {element}.",
]

WILDLIFE = [
    "A herd of {adj} deer picks its way {adverb} through the {display}.",
    "Eyes watch from the shadows of the {display} — patient, unblinking, {adj}.",
    "Small {color} birds flit {adverb} between the {adj} branches of the {display}.",
    "Something large stirs {adverb} in the depths of the {display}, disturbing the {color} {element}.",
    "A lone {adj} figure stands motionless at the edge of the {display}, watching {adverb}.",
    "The {adverb} call of an unseen creature echoes through the {color} {element} of the {display}.",
    "Tracks in the {adj} earth suggest a presence that moves {adverb} just ahead through the {display}.",
    "The {display} teems with quiet, hidden life — {color} wings, {adj} eyes, the {adverb} rustle of unseen things.",
    "A pack of {adj} shapes moves {adverb} through the {display}, visible only as {color} shadows.",
    "Something small and {adj} chitters {adverb} from within the {color} {element} of the {display}.",
    "Fireflies drift {adverb} through the {adj} air of the {display}, each {color} spark a brief luminous trail.",
    "Something hunts {adverb} at the edge of the {display} — patient, {adj}, tasting the {color} {element}.",
    "A {adj} bird of prey circles {adverb} overhead, a dark {color} silhouette against the {element}.",
    "Beneath the {display}, {adj} things build {adverb}, weaving {color} {element} into their hidden structures.",
    "The {adverb} hum of {color} wings rises from the {adj} depths of the {display} like a living {element}.",
]

PERSPECTIVES = [
    "Seen from above, the {display} reveals itself as a {adj} pattern of {color} {element}",
    "At ground level, the {display} towers {adverb}, overwhelming in its {adj} scale",
    "From a distance, the {display} is a {adj} whisper of {color} on the {element} of the horizon",
    "Up close, the {display} breathes {adverb} with {color} textures and hidden {adj} detail",
    "Seen from the heights, the {display} unfolds like a {adj} map of {color} {element} {adverb} arranged",
    "From within, the {display} wraps around you like a {adj} cocoon of {color} {element}",
    "The {display} stretches {adverb} into the distance, a {adj} expanse of {color} {element}",
    "At the edge of the {display}, the world beyond feels {adverb} distant and {adj}",
    "The scale of the {display} is {adverb} apparent — a {adj} world of {color} {element}",
    "Looking back at the {display}, it seems smaller now, a {adj} patch of {color} {element} receding into the distance",
    "Beneath the {display}, unseen {adj} roots of {color} {element} hold the landscape together {adverb} in the dark",
    "Moving {adverb} through the {display}, the {adj} {color} {element} parts and closes around you like a living curtain",
    "Approaching the {display}, its {adj} silhouette of {color} {element} grows {adverb} against the horizon line",
    "Reflected in a {adj} pool of {color} {element}, the {display} appears {adverb} transformed, its secrets floating on the surface",
    "Drifting {adverb} above the {display}, the {adj} expanse of {color} {element} unfolds beneath you like a living map",
]

TRAVELOGUE_PREFIXES = [
    "Journal entry, day {day}. I have reached the {display} at last.",
    "Log entry — {day} days out. The {display} lies before me.",
    "Chronicle of the journey, day {day}: I have come to the {display}.",
    "The {display}. Day {day} of the expedition. I record what I see.",
]

TRAVELOGUE_SUFFIXES = [
    "I will venture deeper into the {display} come morning.",
    "I mark this in my journal and prepare camp for the night.",
    "The {display} has many stories yet to tell. I will listen.",
    "I note the position on my map and turn in for the evening.",
]

WISTFUL = [
    "You wish you could stay longer in the {display}.",
    "Part of you will always remain in the {display}.",
    "The {display} calls to you even as you turn away.",
    "You carry a piece of the {display} with you now.",
    "Someday you will return to the {display}.",
    "The {display} lingers in your thoughts like a half-remembered dream.",
    "You will never be the same after visiting the {display}.",
    "There is nowhere else in the world like the {display}, and you have been lucky enough to see it.",
    "The {display} feels more like a memory of a place you have always known than a place you have just discovered.",
    "You will try to tell others about the {display}, but the words will never be enough.",
]

# Weight tiers for word selection — common words appear more often, rare words less so
COMMON_WORDS = {
    "crystal", "shadow", "ancient", "forgotten", "silent",
    "mist", "light", "silence", "darkness",
    "trees", "stones", "ruins", "crystals",
    "whisper", "glow", "shimmer", "drift",
    "a gentle rain falls", "a still calm lingers", "mist curls along the ground", "snow falls in heavy flakes",
    "softly", "gently", "silently", "quietly",
    "vivid", "burnished", "stark", "murky",
}

RARE_WORDS = {
    "brass", "ivory", "glass",
    "fragrance", "radiance",
    "geodes", "fungi", "archways",
    "resonate", "vibrate",
    "ash drifts slowly downward",
    "relentlessly", "patiently", "eternally", "ceaselessly",
    "iridescent", "fluorescent", "scintillating", "coruscating",
}


PRESETS = {
    "nightfall": {
        "mood": ["eerie"],
        "bias": "rare",
        "anomaly_prob": 0.8,
        "anomaly_count": 2,
        "weather_count": 2,
        "weather_prob": 1.0,
        "echo_enabled": True,
        "echo_prob": 0.7,
        "echo_count": 2,
        "legend_enabled": True,
        "legend_count": 2,
        "legend_prob": 0.7,
        "travelogue": True,
        "wistful": True,
        "sound_enabled": True,
        "sound_count": 2,
        "sound_prob": 0.7,
        "wildlife_enabled": True,
        "wildlife_count": 2,
        "wildlife_prob": 0.7,
        "time_of_day_enabled": True,
        "time_count": 2,
        "time_prob": 0.7,
        "season_enabled": True,
        "season_count": 2,
        "season_prob": 0.7,
        "perspective_enabled": True,
        "perspective_count": 2,
        "perspective_prob": 0.7,
    },
    "pastoral": {
        "mood": ["peaceful"],
        "anomaly_prob": 0.0,
        "weather_count": 1,
        "weather_prob": 0.8,
        "echo_enabled": True,
        "echo_prob": 0.5,
        "legend_enabled": True,
        "legend_count": 1,
        "legend_prob": 0.6,
        "travelogue": True,
        "wistful": True,
        "sound_enabled": True,
        "sound_count": 1,
        "sound_prob": 0.5,
        "wildlife_enabled": True,
        "wildlife_count": 1,
        "wildlife_prob": 0.6,
        "time_of_day_enabled": True,
        "time_count": 1,
        "time_prob": 0.6,
        "season_enabled": True,
        "season_count": 1,
        "season_prob": 0.6,
        "perspective_enabled": True,
        "perspective_count": 1,
        "perspective_prob": 0.6,
    },
    "sublime": {
        "mood": ["vibrant", "peaceful"],
        "bias": "common",
        "color_enabled": True,
        "weather_count": 2,
        "weather_prob": 1.0,
        "echo_enabled": True,
        "echo_prob": 1.0,
        "echo_count": 3,
        "legend_enabled": True,
        "legend_count": 2,
        "legend_prob": 0.9,
        "travelogue": True,
        "wistful": True,
        "sound_enabled": True,
        "sound_count": 2,
        "sound_prob": 0.95,
        "wildlife_enabled": True,
        "wildlife_count": 2,
        "wildlife_prob": 0.95,
        "time_of_day_enabled": True,
        "time_count": 2,
        "time_prob": 0.95,
        "season_enabled": True,
        "season_count": 2,
        "season_prob": 0.95,
        "perspective_enabled": True,
        "perspective_count": 2,
        "perspective_prob": 0.95,
    },
    "wasteland": {
        "mood": ["desolate"],
        "color_enabled": False,
        "anomaly_prob": 1.0,
        "anomaly_count": 3,
        "weather_count": 1,
        "weather_prob": 1.0,
        "echo_enabled": True,
        "legend_enabled": True,
        "legend_count": 2,
        "legend_prob": 1.0,
        "travelogue": True,
        "wistful": True,
        "sound_enabled": True,
        "sound_count": 2,
        "sound_prob": 1.0,
        "wildlife_enabled": False,
        "wildlife_count": 1,
        "wildlife_prob": 1.0,
        "time_of_day_enabled": True,
        "time_count": 1,
        "time_prob": 1.0,
        "season_enabled": True,
        "season_count": 1,
        "season_prob": 1.0,
        "perspective_enabled": True,
        "perspective_count": 1,
        "perspective_prob": 1.0,
    },
    "dreamscape": {
        "mood": ["eerie", "vibrant"],
        "bias": "flat",
        "anomaly_prob": 1.0,
        "weather_count": 2,
        "weather_prob": 0.9,
        "echo_enabled": True,
        "echo_prob": 1.0,
        "echo_count": 2,
        "detail": 2,
        "legend_enabled": True,
        "legend_count": 2,
        "legend_prob": 0.85,
        "travelogue": True,
        "wistful": True,
        "sound_enabled": True,
        "sound_count": 2,
        "sound_prob": 0.9,
        "wildlife_enabled": True,
        "wildlife_count": 2,
        "wildlife_prob": 0.85,
        "time_of_day_enabled": True,
        "time_count": 2,
        "time_prob": 0.85,
        "season_enabled": True,
        "season_count": 2,
        "season_prob": 0.85,
        "perspective_enabled": True,
        "perspective_count": 2,
        "perspective_prob": 0.85,
    },
}


BIAS_MODES = {
    "normal":  {"common": 10, "normal": 5, "rare": 1},
    "common":  {"common": 20, "normal": 5, "rare": 1},
    "rare":    {"common": 5,  "normal": 5, "rare": 3},
    "flat":    {"common": 1,  "normal": 1, "rare": 1},
}

MOOD_BOOST = 5

MOOD_WORDS = {
    "peaceful": {
        "adjectives": ["calm", "serene", "gentle", "tranquil", "placid", "lulling", "sleepy", "soft"],
        "elements": ["stillness", "warmth", "soft light", "quiet", "breeze", "lullaby"],
        "nouns": ["glades", "shallows", "meadows", "clearings", "reflections", "coves"],
        "verbs": ["rest", "glide", "settle", "bloom", "ripple", "cradle"],
        "colors": ["pale", "soft", "gentle", "mellow", "warm", "milky"],
        "adverbs": ["gently", "softly", "peacefully", "calmly", "tranquilly", "serenely"],
        "weathers": [
            "a soft breeze carries the scent of flowers",
            "warm sunlight filters through gently",
            "the air is still and comfortable",
            "a light mist settles in the hollows",
        ],
        "anomalies": [
            "Everything seems to hum in harmony.",
            "The world holds its breath.",
            "Colors seem more vivid here.",
            "Time moves like honey here.",
        ],
    },
    "eerie": {
        "adjectives": ["shadow", "silent", "forgotten", "bone", "obsidian", "pale", "deep"],
        "elements": ["echo", "silence", "darkness", "stillness", "cave wind"],
        "nouns": ["ruins", "stones", "crystals", "archways", "spires", "fissures"],
        "verbs": ["whisper", "hum", "vibrate", "resonate", "creak", "echo"],
        "colors": ["murky", "bleached", "stark", "veined", "lurid"],
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
        "colors": ["vivid", "burnished", "iridescent", "fluorescent", "scintillating"],
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
        "colors": ["murky", "bleached", "stark", "lurid", "mottled"],
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

MOOD_ATMOSPHERE = {
    "peaceful": [
        "A gentle stillness settles over the scene like a blessing.",
        "The air is soft and kind, as if the landscape itself wishes you well.",
        "Everything here seems to breathe in a slow, tranquil rhythm.",
        "The world holds its breath, and for a moment, all is well.",
    ],
    "eerie": [
        "There is a wrongness in the air that you cannot name.",
        "The silence here has a texture — thick, watchful, patient.",
        "Something about this place makes the hair on your neck stand up.",
        "The landscape seems to watch you with an attention that feels ancient and cold.",
    ],
    "vibrant": [
        "The world feels borderless and alive, humming with impossible energy.",
        "Colour and light seem to bleed from everything, as if the landscape is too full to contain itself.",
        "Every detail of the landscape pulses with a fierce, joyful intensity.",
        "The air itself seems charged with life, electric and golden.",
    ],
    "desolate": [
        "Hope withered here long ago, leaving only the bones of the world.",
        "The land has given up on itself — nothing grows, nothing waits, nothing remembers.",
        "Desolation hangs in the air like a held breath that will never be released.",
        "This place has been empty for so long that emptiness has become its only identity.",
    ],
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
    "fourth": 3,
    "fifth": 4,
    "sixth": 5,
    "seventh": 6,
}


def _pick_template(slot, template_set, template_overrides=None, rng=None):
    effective = (template_overrides or {}).get(slot, template_set)
    templates = SENTENCE_TEMPLATES[slot]
    if effective == "random":
        return (rng or random).choice(templates)
    idx = min(TEMPLATE_SETS[effective], len(templates) - 1)
    return templates[idx]


# Sentence templates for landscape generation — randomly selected each time for variety
def _format_tmpl(template, **kwargs):
    result = template.format(**kwargs)
    return result.replace("  ", " ").replace(" .", ".").replace(" :", ":").strip()


def describe_biome(biome):
    """Return a string describing the given biome's word bank.
    If biome is 'all', describe all biomes."""
    if biome == "all":
        lines = []
        for b in BIOMES:
            lines.append(describe_biome(b))
        return "\n\n".join(lines)
    words = BIOME_WORDS.get(biome)
    if words is None:
        return f"Unknown biome: {biome!r}"
    lines = [f"=== {biome} ==="]
    for cat in ["adjectives", "elements", "nouns", "verbs", "colors", "adverbs", "weathers", "anomalies"]:
        pool = words.get(cat, [])
        lines.append(f"  {cat}: {', '.join(pool)}")
    return "\n".join(lines)


def describe_mood(mood):
    """Return a string describing the given mood's word bank.
    If mood is 'all', describe all moods."""
    if mood == "all":
        lines = []
        for m in MOOD_WORDS:
            lines.append(describe_mood(m))
        return "\n\n".join(lines)
    words = MOOD_WORDS.get(mood)
    if words is None:
        return f"Unknown mood: {mood!r}"
    lines = [f"=== {mood} ==="]
    for cat in ["adjectives", "elements", "nouns", "verbs", "colors", "adverbs", "weathers", "anomalies"]:
        pool = words.get(cat, [])
        lines.append(f"  {cat}: {', '.join(pool)}")
    return "\n".join(lines)


def describe_global():
    """Return a string describing all global word pools with weight tiers."""
    categories = {
        "adjectives": ADJECTIVES,
        "elements": ELEMENTS,
        "nouns": NOUNS,
        "verbs": VERBS,
        "weathers": WEATHERS,
        "anomalies": ANOMALIES,
        "adverbs": ADVERBS,
        "colors": COLORS,
        "time words": TIME_WORDS,
    }
    lines = ["=== global word pools ==="]
    for cat_name, pool in categories.items():
        common = [w for w in pool if w in COMMON_WORDS]
        rare = [w for w in pool if w in RARE_WORDS]
        normal = [w for w in pool if w not in COMMON_WORDS and w not in RARE_WORDS]
        parts = []
        if common:
            parts.append(f"common: {', '.join(common)}")
        if normal:
            parts.append(f"normal: {', '.join(normal)}")
        if rare:
            parts.append(f"rare: {', '.join(rare)}")
        lines.append(f"  {cat_name} ({', '.join(parts)})")
    return "\n".join(lines)


def describe_templates():
    """Return a string describing all available sentence templates per slot."""
    lines = ["=== templates ==="]
    for slot in ["opening", "middle", "weather", "anomaly"]:
        templates = SENTENCE_TEMPLATES[slot]
        lines.append(f"  {slot} ({len(templates)} templates):")
        for i, tmpl in enumerate(templates):
            lines.append(f"    [{i}] {tmpl}")
    return "\n".join(lines)


def describe_echoes():
    """Return a string describing all available echo phrases."""
    lines = ["=== echo phrases ==="]
    for i, echo in enumerate(ECHOES):
        lines.append(f"  [{i}] {echo}")
    return "\n".join(lines)


def describe_legends():
    """Return a string describing all available legend phrases."""
    lines = ["=== legends ==="]
    for i, legend in enumerate(LEGENDS):
        lines.append(f"  [{i}] {legend}")
    return "\n".join(lines)


def describe_travelogue():
    """Return a string describing all available travelogue prefixes and suffixes."""
    lines = ["=== travelogue prefixes ==="]
    for i, prefix in enumerate(TRAVELOGUE_PREFIXES):
        lines.append(f"  [{i}] {prefix}")
    lines.append("=== travelogue suffixes ===")
    for i, suffix in enumerate(TRAVELOGUE_SUFFIXES):
        lines.append(f"  [{i}] {suffix}")
    return "\n".join(lines)


def describe_wistful():
    """Return a string describing all available wistful phrases."""
    lines = ["=== wistful phrases ==="]
    for i, phrase in enumerate(WISTFUL):
        lines.append(f"  [{i}] {phrase}")
    return "\n".join(lines)


def describe_sounds():
    """Return a string describing all available soundscape phrases."""
    lines = ["=== soundscape phrases ==="]
    for i, phrase in enumerate(SOUNDSCAPES):
        lines.append(f"  [{i}] {phrase}")
    return "\n".join(lines)


def describe_wildlife():
    """Return a string describing all available wildlife phrases."""
    lines = ["=== wildlife phrases ==="]
    for i, phrase in enumerate(WILDLIFE):
        lines.append(f"  [{i}] {phrase}")
    return "\n".join(lines)


def describe_times():
    """Return a string describing all available time-of-day phrases."""
    lines = ["=== time-of-day phrases ==="]
    for i, phrase in enumerate(TIMES_OF_DAY):
        lines.append(f"  [{i}] {phrase}")
    return "\n".join(lines)


def describe_seasons():
    """Return a string describing all available seasonal phrases."""
    lines = ["=== season phrases ==="]
    for i, phrase in enumerate(SEASONS):
        lines.append(f"  [{i}] {phrase}")
    return "\n".join(lines)


def describe_perspectives():
    """Return a string describing all available perspective phrases."""
    lines = ["=== perspective phrases ==="]
    for i, phrase in enumerate(PERSPECTIVES):
        lines.append(f"  [{i}] {phrase}")
    return "\n".join(lines)


def describe_presets():
    """Return a string describing all available presets."""
    lines = ["=== presets ==="]
    for name, params in PRESETS.items():
        parts = [f"{k}={v}" for k, v in params.items()]
        lines.append(f"  {name}: {', '.join(parts)}")
    return "\n".join(lines)


SENTENCE_TEMPLATES = {
    "opening": [
        "A vast {adj} {display} of {color} {element} stretches {adverb} before you {time_word}.",
        "Before you, a {adj} {display} of {color} {element} comes into view {adverb} {time_word}.",
        "The {adj} {display} of {color} {element} lies {adverb} ahead {time_word}.",
        "{Element} — the {adj} {display} of {color} light stretches {adverb} before you {time_word}.",
    ],
    "middle": [
        "{Element} {verb_conjugated} {adverb} between the {color} {adj} {noun}.",
        "Among the {adj} {noun}, {color} {element} {verb_conjugated} {adverb}.",
        "The {adj} {noun} {verb} {adverb} with {color} {element}.",
        "{Element} {verb_conjugated} {adverb} through the {color} {adj} {noun}.",
        "Beneath the {adj} {noun}, {color} {element} {verb_conjugated} {adverb}.",
        "Across the {display}, {color} {element} {verb_conjugated} {adverb}.",
        "The {color} light of {element} {verb_conjugated} {adverb}.",
    ],
    "weather": [
        "{Weather} {adverb} through the {color} {adj} {element} {time_word}.",
        "The air tells its own story: {weather} {adverb} through the {color} {adj} {element} {time_word}.",
        "{Weather}, as if the {adj} {display} itself breathes {color} {element} {adverb} {time_word}.",
        "Through the {color} {adj} {element}, {weather} {adverb} {time_word}.",
        "{Weather} {adverb} in {color} {adj} light {time_word}.",
    ],
    "anomaly": [
        "{anomaly}",
        "Something is not right with the {display} {time_word} — {anomaly}",
        "A strange {color} detail catches your eye {adverb} through the {element}: {anomaly_lower}",
        "There is a quiet wrongness here {adverb} {time_word}: {anomaly_lower}",
        "In the {color} {adj} light of the {display}, {anomaly_lower}",
    ],
}

# Biome-specific word enrichments — blended with global pools for more evocative output
BIOME_WORDS = {
    "forest": {
        "adjectives": ["dappled", "verdant", "whispering", "mossy", "deep", "wildwood", "sun-dappled"],
        "elements": ["birdsong", "leaf rustle", "sap scent", "shade", "pine scent", "moss damp"],
        "nouns": ["canopies", "trunks", "glades", "ferns", "branches", "understory", "clearings"],
        "verbs": ["rustle", "whisper", "breathe", "creak", "shade", "dapple", "sigh"],
        "colors": ["emerald", "deep green", "golden", "dappled", "woodland", "forest green"],
        "adverbs": ["softly", "gently", "peacefully", "wistfully", "invitingly"],
        "weathers": [
            "sunlight filters through the canopy in golden beams",
            "a soft wind stirs the leaves overhead",
            "the undergrowth glistens with morning dew",
            "a light drizzle filters through the canopy like whispered secrets",
            "the forest floor releases the scent of damp earth after rain",
        ],
        "anomalies": [
            "Every leaf faces the same direction.",
            "The rings on every stump glow faintly.",
            "Fungal spores hang in the air like tiny lanterns.",
            "The trees grow in a perfect circle around a patch of sky that never clouds.",
            "Every creature in the forest falls silent at the same moment each day.",
        ],
    },
    "desert": {
        "adjectives": ["scorched", "barren", "windswept", "blazing", "golden", "sere", "sun-scorched"],
        "elements": ["heat shimmer", "sand grain", "dry air", "sun flare", "dust devil", "mirage light"],
        "nouns": ["dunes", "mesas", "canyons", "plateaus", "oases", "wadis", "buttes"],
        "verbs": ["bake", "crack", "drift", "shimmer", "scour", "wither", "glare"],
        "colors": ["amber", "golden", "pale", "crimson", "sand", "terracotta"],
        "adverbs": ["relentlessly", "harshly", "patiently", "mercilessly", "brutally"],
        "weathers": [
            "heat ripples rise from the sand in waves",
            "a hot wind scours the dunes",
            "the sun beats down without mercy",
            "sandstorms gather on the horizon like walls of amber",
            "a rare rain falls, each drop sizzling against the hot stone",
        ],
        "anomalies": [
            "The sand falls upward here.",
            "A second sun hangs low on the horizon.",
            "The dunes form perfect geometric spirals.",
            "Footprints behind you fill with water that has no source.",
            "The stars rearrange themselves into unfamiliar constellations at midnight.",
        ],
    },
    "ocean": {
        "adjectives": ["deep", "abyssal", "endless", "bioluminescent", "saline", "tide-worn", "brine-soaked"],
        "elements": ["salt spray", "current pull", "ocean scent", "pressure", "wave crash", "deep current"],
        "nouns": ["trenches", "currents", "reefs", "abysses", "swells", "gyres", "thermals"],
        "verbs": ["crash", "surge", "drift", "plunge", "churn", "swell", "roar"],
        "colors": ["sapphire", "deep blue", "teal", "silver", "aquamarine", "indigo"],
        "adverbs": ["endlessly", "powerfully", "deeply", "rhythmically", "hypnotically"],
        "weathers": [
            "waves roll in from an unseen horizon",
            "a fine salt mist hangs in the air",
            "the water is eerily still and black",
            "rain falls on the surface like a thousand drummers",
            "a deep fog bank rolls across the water, swallowing the horizon",
        ],
        "anomalies": [
            "The water glows with an inner light.",
            "Fish swim in geometric formation overhead.",
            "The surface is a mirror to a different sky.",
            "Pressure changes in ways that do not correspond to depth.",
            "Whales sing in frequencies that vibrate through bone, though no whales are near.",
        ],
    },
    "tundra": {
        "adjectives": ["frozen", "barren", "windswept", "auroral", "pale", "ice-bound", "permafrost"],
        "elements": ["frost", "aurora light", "wind howl", "hoar", "snow whisper", "ice crystal"],
        "nouns": ["ice fields", "glaciers", "crevasses", "permafrost", "snowdrifts", "moraines", "frost heaves"],
        "verbs": ["freeze", "howl", "crack", "gleam", "drift", "shiver", "blast"],
        "colors": ["pale blue", "silver", "frost-white", "auroral", "permafrost white", "glacier blue"],
        "adverbs": ["silently", "eternally", "coldly", "bitterly", "indifferently"],
        "weathers": [
            "the aurora pulses in silent sheets of green",
            "a biting wind carries ice crystals",
            "snow falls in a world of white and silence",
            "ice crystals hang in the air like frozen diamonds",
            "a strange warmth rises from beneath the permafrost",
        ],
        "anomalies": [
            "The ice sings when the wind blows across it.",
            "Shapes move beneath the frozen surface.",
            "The aurora casts shadows that move on their own.",
            "The snow remembers every footprint ever pressed into it.",
            "A mountain in the distance has not moved, yet it is closer than yesterday.",
        ],
    },
    "mountain range": {
        "adjectives": ["jagged", "towering", "snow-capped", "ancient", "granite", "cloud-wreathed", "steep"],
        "elements": ["stone echo", "thin air", "alpine scent", "cold light", "rockfall echo", "alpine frost"],
        "nouns": ["peaks", "ridges", "cliffs", "valleys", "crags", "coloirs", "cirques"],
        "verbs": ["tower", "loom", "echo", "rise", "cut", "sculpt", "shelter"],
        "colors": ["granite grey", "snow-white", "purple", "slate", "stone grey", "alpine"],
        "adverbs": ["majestically", "patiently", "tirelessly", "steadily", "proudly"],
        "weathers": [
            "wind howls through the narrow passes",
            "clouds cling to the peaks like shawls",
            "thin air carries every sound for miles",
            "snow falls in heavy silence, muffling the world",
            "a warm wind descends from the peaks, carrying the scent of distant valleys",
        ],
        "anomalies": [
            "The peaks rearrange themselves at night.",
            "Echoes return minutes after you speak.",
            "A stone bridge arcs between clouds.",
            "There is a peak that appears only in reflections.",
            "The mountain casts two shadows under a single sun.",
        ],
    },
    "swamp": {
        "adjectives": ["fetid", "murky", "choked", "rotting", "drowned", "brackish", "silt-choked"],
        "elements": ["marsh gas", "decay scent", "still water", "humidity", "swamp gas", "rotting wood"],
        "nouns": ["bayous", "mangroves", "bogs", "quicksand", "thickets", "sloughs", "tupelos"],
        "verbs": ["bubble", "fester", "seep", "creep", "stagnate", "sink", "rot"],
        "colors": ["murky", "green-brown", "dark", "rotting", "khaki", "peat brown"],
        "adverbs": ["thickly", "heavily", "sluggishly", "sullenly", "lazily"],
        "weathers": [
            "fog rolls low over the black water",
            "the air is thick and heavy with moisture",
            "gnats swarm in the stagnant heat",
            "a phosphorescent mist rises from the water at dusk",
            "thunder rolls across the marsh without lightning",
        ],
        "anomalies": [
            "Will-o'-wisps flicker in perfect constellations.",
            "The water reflects a world that no longer exists.",
            "Bubbles rise spelling out words in an old language.",
            "Moss-covered trees whisper conversations from a century past.",
            "Every pair of eyes in the swamp blinks in perfect unison.",
        ],
    },
    "cave system": {
        "adjectives": ["subterranean", "echoing", "pitch-dark", "limestone", "dripping", "deep-earth", "stalactite"],
        "elements": ["drip sound", "stone scent", "darkness", "cave wind", "cavern draft", "mineral drip"],
        "nouns": ["stalactites", "caverns", "tunnels", "chambers", "fissures", "flowstones", "pillars"],
        "verbs": ["drip", "echo", "glimmer", "resonate", "collapse", "carve", "murmur"],
        "colors": ["pitch-black", "phosphorescent", "glimmering", "deep violet", "cave-dark", "mineral blue"],
        "adverbs": ["patiently", "ceaselessly", "endlessly", "remotely", "inexorably"],
        "weathers": [
            "water drips in a slow, endless rhythm",
            "a draft carries the scent of deep earth",
            "the darkness presses in from all sides",
            "a low mist hugs the cave floor, cool and thick",
            "an underground stream sings somewhere in the darkness",
        ],
        "anomalies": [
            "The crystals here glow without a light source.",
            "Passages rearrange when you blink.",
            "The cave breathes — a slow, deep rhythm.",
            "Stalactites and stalagmites grow toward each other at visible speed.",
            "The darkness here has weight — it presses against your back.",
        ],
    },
    "plain": {
        "adjectives": ["endless", "golden", "wide", "wind-scoured", "open", "rolling", "sweeping"],
        "elements": ["grass rustle", "open sky", "distant haze", "earth scent", "distant thunder", "wildflower scent"],
        "nouns": ["grasses", "horizons", "fields", "bluffs", "meadows", "savannas", "swales"],
        "verbs": ["wave", "stretch", "roll", "sway", "bend", "ripple", "gleam"],
        "colors": ["golden", "pale", "amber", "wide", "tawny", "dusty rose"],
        "adverbs": ["endlessly", "freely", "peacefully", "tranquilly", "openly"],
        "weathers": [
            "a warm wind sends ripples across the grass",
            "clouds cast slow-moving shadows on the land",
            "the sky stretches forever, blue and empty",
            "a slow breeze carries the scent of wildflowers from miles away",
            "a bank of fog rolls in from the horizon at dusk",
        ],
        "anomalies": [
            "The grass bends in patterns that spell something.",
            "There is no horizon — land and sky merge as one.",
            "Distant figures never get closer no matter how far you walk.",
            "The grass grows in the shape of a language that predates humanity.",
            "Every footstep you take is echoed by a second set of footsteps that stop when you stop.",
        ],
    },
    "volcanic field": {
        "adjectives": ["scorched", "smoldering", "obsidian", "sulfurous", "cracked", "magmatic", "cinder-strewn"],
        "elements": ["sulfur scent", "heat haze", "lava glow", "ash fall", "pumice dust", "lava crack"],
        "nouns": ["vents", "fissures", "calderas", "magma chambers", "slag heaps", "fumaroles", "tuff cones"],
        "verbs": ["smolder", "hiss", "crack", "erupt", "seethe", "spit", "quake"],
        "colors": ["obsidian black", "crimson", "molten orange", "ash-grey", "scoria red", "pumice grey"],
        "adverbs": ["violently", "harshly", "relentlessly", "fiercely", "explosively"],
        "weathers": [
            "ash falls like gray snow from a black sky",
            "steam vents hiss in ragged chorus",
            "lava illuminates the smoke from below",
            "sulfur fumes drift across the cracked earth in low-lying clouds",
            "a hot rain of ash and cinders falls without warning",
        ],
        "anomalies": [
            "Lava flows uphill without reason.",
            "Obsidian shards show visions of the past.",
            "The heat does not burn — it freezes.",
            "The ground beneath your feet pulses with a heartbeat that is not your own.",
            "Molten rock flows in formations that spell out coordinates to nowhere.",
        ],
    },
    "coral reef": {
        "adjectives": ["luminous", "vibrant", "underwater", "reef-born", "crystalline", "reef-knitted", "polyp-laden"],
        "elements": ["coral scent", "underwater light", "current hum", "salt", "tide pool", "coral spawn"],
        "nouns": ["polyps", "anemones", "lagoon beds", "drop-offs", "groves", "sea fans", "crevices"],
        "verbs": ["pulse", "drift", "glow", "wave", "filter", "spawn", "flicker"],
        "colors": ["coral", "turquoise", "bioluminescent", "vibrant pink", "scarlet", "coral pink"],
        "adverbs": ["gently", "softly", "brilliantly", "vibrantly", "flowingly"],
        "weathers": [
            "sunlight dances on the water in shifting patterns",
            "warm currents drift through the coral canyons",
            "the water is clear and impossibly blue",
            "underwater currents carry a symphony of clicks and pops",
            "the tide pulls in patterns that do not follow the moon",
        ],
        "anomalies": [
            "The coral pulses in unison like a single heart.",
            "Fish leave trails of light as they swim.",
            "Every shell contains a tiny, perfect melody.",
            "The reef glows in wavelengths visible only to something that has been watching.",
            "Time passes differently here — hours feel like minutes, minutes like hours.",
        ],
    },
    "ruined city": {
        "adjectives": ["crumbling", "hollow", "rusted", "fallen", "skeletal", "gutted", "fractured", "ashen", "shattered", "graffitied"],
        "elements": ["distant hum", "dust", "rust scent", "broken light", "stifled echo", "mold scent", "broken glass"],
        "nouns": ["facades", "girders", "husks", "plazas", "overpasses", "broken windows", "skeletons", "rubble piles"],
        "verbs": ["creak", "settle", "sway", "crumble", "groan", "fracture", "whine"],
        "colors": ["grey", "rusted", "ashen", "faded", "pale grey", "verdigris"],
        "adverbs": ["silently", "slowly", "patiently", "hollowly", "wearily"],
        "weathers": [
            "ash drifts through broken windows like snow",
            "a pale sun filters through smog",
            "the wind moans through empty streets",
            "a rust-colored drizzle stains the concrete further",
            "dust devils spin through collapsed intersections",
        ],
        "anomalies": [
            "The street signs point in directions that don't exist.",
            "Every clock reads the same time.",
            "Shadows of people who aren't there move along the walls.",
            "The city gives birth to new streets at night — a map that redraws itself.",
            "All the doors in the city are slightly ajar, as if someone just left.",
        ],
    },
    "fungal grove": {
        "adjectives": ["bioluminescent", "spongy", "spore-filled", "mycelial", "phosphorescent", "thriving", "veined", "delicate", "spore-dusted", "hyphael"],
        "elements": ["spore glow", "fungal scent", "mycelium hum", "rot warmth", "spore cloud", "mycelium network"],
        "nouns": ["caps", "gills", "stalks", "hyphae", "puffballs", "tendrils", "mycelia", "sporocarps"],
        "verbs": ["pulse", "glow", "release", "expand", "spore", "spiral", "weep"],
        "colors": ["phosphorescent", "neon green", "luminous", "deep purple", "mushroom beige", "sporescent"],
        "adverbs": ["gently", "silently", "unceasingly", "organically", "prolifically"],
        "weathers": [
            "spores drift through the air like slow-motion snow",
            "the ground pulses with faint blue light",
            "a warm dampness carries the scent of growth",
            "spore-laden rain falls in curtains of gold and silver",
            "a warm mist carries the sweet scent of fungal bloom",
        ],
        "anomalies": [
            "The mushrooms sing at frequencies only bones can feel.",
            "Spores form faces when they settle.",
            "The entire grove shares one consciousness.",
            "The mycelium network reacts to your thoughts — the glow shifts as you approach.",
            "Fungal growths form temporary sculptures that collapse and reform in endless cycles.",
        ],
    },
    "sky islands": {
        "adjectives": ["floating", "cloud-wreathed", "sun-bleached", "sky-born", "ethereal", "exposed", "high", "wind-bitten", "aerial", "cloud-banked"],
        "elements": ["cloud vapor", "wind shear", "sky-blue light", "thin air", "upper air", "cloud mist"],
        "nouns": ["archipelagos", "peaks", "bridges", "precipices", "cloud banks", "updrafts", "thermals", "wind shears"],
        "verbs": ["float", "drift", "soar", "hover", "ride", "glide", "sail"],
        "colors": ["sky-blue", "cloud-white", "golden", "sunset-tinged", "dawn pink", "storm grey"],
        "adverbs": ["gracefully", "silently", "peacefully", "weightlessly", "distantly"],
        "weathers": [
            "clouds churn far below like a white sea",
            "lightning arcs silently between nearby islands",
            "the wind is constant and unforgiving",
            "rain falls upward from the cloud sea below",
            "a thin mist wraps each island in solitude",
        ],
        "anomalies": [
            "The islands orbit each other in a slow dance.",
            "Waterfalls flow upward into the clouds.",
            "A bell tolls from an island that no one has ever reached.",
            "The islands cast shadows onto the clouds below — shadows that move independently.",
            "Gravity weakens at the center of each island, as if the land itself is trying to float free.",
        ],
    },
}


def _pick(category, biomes, bias="normal", mood=None, mood_weight=MOOD_BOOST, bias_overrides=None, mood_weight_overrides=None, used_words=None, rng=None):
    """Pick a random word from the biome-specific pool(s) blended with the global pool.
    `biomes` is a list of biome names; words from all specified biomes are included.
    Words are weighted per the given bias mode and optionally boosted for mood.
    `bias_overrides` is an optional dict mapping category name -> bias mode,
    allowing per-category bias that takes precedence over the global `bias`.
    `mood_weight_overrides` is an optional dict mapping category name -> float,
    allowing per-category mood-weight that takes precedence over the global `mood_weight`.
    `used_words` is an optional set of words already used in this generation — the
    chosen word is added to it, and already-used words are excluded from selection.
    `rng` is an optional random.Random instance; if None, the global random module is used."""
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
        "colors": COLORS,
    }[category]
    pool = specific + global_pool
    if used_words is not None:
        available = [w for w in pool if w not in used_words]
        if available:
            pool = available
    weights = [_word_weight(w, effective_bias, mood, category, mood_weight, mood_weight_overrides) for w in pool]
    rng = rng or random
    chosen = rng.choices(pool, weights=weights, k=1)[0]
    if used_words is not None:
        used_words.add(chosen)
    return chosen


def generate_landscape(seed=None, biome=None, show_biome=False, fmt="prose", combine=None, detail=1, bias="normal", show_seed=False, mood=None, mood_weight=MOOD_BOOST, template_set="random", bias_overrides=None, mood_weight_overrides=None, template_overrides=None, anomaly_prob=0.3, anomaly_count=1, dedup=True, adverb_enabled=True, biome_weights=None, weather_enabled=True, weather_count=1, weather_prob=1.0, middle_enabled=True, color_enabled=True, element_enabled=True, anomaly_enabled=True, echo_enabled=False, echo_count=1, echo_prob=1.0, time_word_enabled=True, legend_enabled=False, legend_count=1, legend_prob=1.0, travelogue=False, wistful=False, sound_enabled=False, sound_count=1, sound_prob=1.0, time_of_day_enabled=False, time_count=1, time_prob=1.0, season_enabled=False, season_count=1, season_prob=1.0, wildlife_enabled=False, wildlife_count=1, wildlife_prob=1.0, perspective_enabled=False, perspective_count=1, perspective_prob=1.0, mood_atmosphere=False):
    if seed is not None:
        rng = random.Random(seed)
    elif show_seed:
        seed = random.Random().randint(0, 2**31 - 1)
        rng = random.Random(seed)
    else:
        rng = random.Random()

    if biome is not None:
        biomes = [biome.lower()]
        display = biome.lower()
    elif combine is not None:
        biomes = [b.strip().lower() for b in combine.split(",")]
        if len(biomes) == 0:
            biomes = [rng.choice(BIOMES)]
        display = " and ".join(biomes)
    else:
        if biome_weights:
            weights = [biome_weights.get(b, 1) for b in BIOMES]
            if all(w == 0 for w in weights):
                chosen = rng.choice(BIOMES)
            else:
                chosen = rng.choices(BIOMES, weights=weights, k=1)[0]
        else:
            chosen = rng.choice(BIOMES)
        biomes = [chosen]
        display = chosen

    used_words = set() if dedup else None

    time_phrases = []
    if time_of_day_enabled and time_count > 0:
        used_times = set()
        for _ in range(time_count):
            if rng.random() < time_prob:
                pool = [t for t in TIMES_OF_DAY if t not in used_times] or TIMES_OF_DAY
                phrase = rng.choice(pool)
                used_times.add(phrase)
                time_phrases.append(phrase)

    season_phrases = []
    if season_enabled and season_count > 0:
        used_seasons = set()
        for _ in range(season_count):
            if rng.random() < season_prob:
                pool = [s for s in SEASONS if s not in used_seasons] or SEASONS
                phrase = rng.choice(pool)
                used_seasons.add(phrase)
                season_phrases.append(phrase)

    adj = _pick("adjectives", biomes, bias=bias, mood=mood, mood_weight=mood_weight, bias_overrides=bias_overrides, mood_weight_overrides=mood_weight_overrides, used_words=used_words, rng=rng)
    if element_enabled:
        element = _pick("elements", biomes, bias=bias, mood=mood, mood_weight=mood_weight, bias_overrides=bias_overrides, mood_weight_overrides=mood_weight_overrides, used_words=used_words, rng=rng)
    else:
        element = ""
    if adverb_enabled:
        adverb = _pick("adverbs", biomes, bias=bias, mood=mood, mood_weight=mood_weight, bias_overrides=bias_overrides, mood_weight_overrides=mood_weight_overrides, used_words=used_words, rng=rng)
    else:
        adverb = ""
    if color_enabled:
        color = _pick("colors", biomes, bias=bias, mood=mood, mood_weight=mood_weight, bias_overrides=bias_overrides, mood_weight_overrides=mood_weight_overrides, used_words=used_words, rng=rng)
    else:
        color = ""
    if time_word_enabled:
        time_word = rng.choice(TIME_WORDS)
    else:
        time_word = ""
    opening_tmpl = _pick_template("opening", template_set, template_overrides, rng=rng)
    opening = _format_tmpl(opening_tmpl, adj=adj, display=display, adverb=adverb, element=element, Element=element.capitalize(), color=color, time_word=time_word)
    parts = [opening]
    for i, phrase in enumerate(time_phrases):
        parts.insert(i, phrase + ".")
    for i, phrase in enumerate(season_phrases):
        parts.insert(i, phrase + ".")

    perspective_phrases = []
    if perspective_enabled and perspective_count > 0:
        used_perspectives = set()
        for _ in range(perspective_count):
            if rng.random() < perspective_prob:
                pool = [p for p in PERSPECTIVES if p not in used_perspectives] or PERSPECTIVES
                phrase = rng.choice(pool)
                used_perspectives.add(phrase)
                perspective_text = phrase.format(
                    display=display, adverb=adverb, color=color,
                    adj=adj, element=element,
                )
                perspective_phrases.append(perspective_text)

    for i, pphrase in enumerate(perspective_phrases):
        parts.insert(i, pphrase + ".")

    if mood_atmosphere and mood is not None:
        active_moods = mood if isinstance(mood, (list, tuple)) else [mood]
        available = [m for m in active_moods if m in MOOD_ATMOSPHERE]
        if available:
            chosen_mood = rng.choice(available)
            phrase = rng.choice(MOOD_ATMOSPHERE[chosen_mood])
            parts.append(phrase)

    for _ in range(max(detail, 0)):
        if element_enabled:
            element = _pick("elements", biomes, bias=bias, mood=mood, mood_weight=mood_weight, bias_overrides=bias_overrides, mood_weight_overrides=mood_weight_overrides, used_words=used_words, rng=rng)
        else:
            element = ""
        adj = _pick("adjectives", biomes, bias=bias, mood=mood, mood_weight=mood_weight, bias_overrides=bias_overrides, mood_weight_overrides=mood_weight_overrides, used_words=used_words, rng=rng)
        if color_enabled:
            color = _pick("colors", biomes, bias=bias, mood=mood, mood_weight=mood_weight, bias_overrides=bias_overrides, mood_weight_overrides=mood_weight_overrides, used_words=used_words, rng=rng)
        else:
            color = ""
        if middle_enabled:
            noun = _pick("nouns", biomes, bias=bias, mood=mood, mood_weight=mood_weight, bias_overrides=bias_overrides, mood_weight_overrides=mood_weight_overrides, used_words=used_words, rng=rng)
            verb = _pick("verbs", biomes, bias=bias, mood=mood, mood_weight=mood_weight, bias_overrides=bias_overrides, mood_weight_overrides=mood_weight_overrides, used_words=used_words, rng=rng)
            verb_conjugated = _conjugate(verb)
        if adverb_enabled:
            adverb = _pick("adverbs", biomes, bias=bias, mood=mood, mood_weight=mood_weight, bias_overrides=bias_overrides, mood_weight_overrides=mood_weight_overrides, used_words=used_words, rng=rng)
        else:
            adverb = ""
        if middle_enabled:
            middle_tmpl = _pick_template("middle", template_set, template_overrides, rng=rng)
            parts.append(
                _format_tmpl(middle_tmpl, Element=element.capitalize(), element=element, adj=adj, noun=noun, verb=verb, verb_conjugated=verb_conjugated, adverb=adverb, display=display, color=color)
            )

        if weather_enabled and weather_count > 0:
            for _ in range(weather_count):
                if rng.random() < weather_prob:
                    weather = _pick("weathers", biomes, bias=bias, mood=mood, mood_weight=mood_weight, bias_overrides=bias_overrides, mood_weight_overrides=mood_weight_overrides, used_words=used_words, rng=rng)
                    weather_tmpl = _pick_template("weather", template_set, template_overrides, rng=rng)
                    parts.append(
                        _format_tmpl(weather_tmpl, Weather=weather.capitalize(), weather=weather, display=display, adverb=adverb, element=element, color=color, adj=adj, time_word=time_word)
                    )

    if anomaly_enabled and detail >= 1 and anomaly_count > 0:
        for _ in range(anomaly_count):
            if rng.random() < anomaly_prob:
                anomaly_tmpl = _pick_template("anomaly", template_set, template_overrides, rng=rng)
                anomaly_word = _pick("anomalies", biomes, bias=bias, mood=mood, mood_weight=mood_weight, bias_overrides=bias_overrides, mood_weight_overrides=mood_weight_overrides, used_words=used_words, rng=rng)
                anomaly_lower = anomaly_word[0].lower() + anomaly_word[1:]
                parts.append(_format_tmpl(anomaly_tmpl, anomaly=anomaly_word, anomaly_lower=anomaly_lower, adverb=adverb, color=color, element=element, display=display, adj=adj, time_word=time_word))

    if echo_enabled and detail >= 1 and echo_count > 0:
        used_echoes = set()
        for _ in range(echo_count):
            if rng.random() < echo_prob:
                pool = [e for e in ECHOES if e not in used_echoes] or ECHOES
                echo = rng.choice(pool)
                used_echoes.add(echo)
                parts.append(_format_tmpl(echo, display=display, adverb=adverb, element=element, color=color, adj=adj, time_word=time_word))

    if sound_enabled and detail >= 1 and sound_count > 0:
        used_sounds = set()
        for _ in range(sound_count):
            if rng.random() < sound_prob:
                pool = [s for s in SOUNDSCAPES if s not in used_sounds] or SOUNDSCAPES
                sound = rng.choice(pool)
                used_sounds.add(sound)
                parts.append(sound.format(
                    display=display, adverb=adverb, color=color,
                    adj=adj, element=element,
                ))

    if wildlife_enabled and detail >= 1 and wildlife_count > 0:
        used_wildlife = set()
        for _ in range(wildlife_count):
            if rng.random() < wildlife_prob:
                pool = [w for w in WILDLIFE if w not in used_wildlife] or WILDLIFE
                wildlife = rng.choice(pool)
                used_wildlife.add(wildlife)
                parts.append(wildlife.format(
                    display=display, adverb=adverb, color=color,
                    adj=adj, element=element,
                ))

    if legend_enabled and detail >= 1 and legend_count > 0:
        used_legends = set()
        for _ in range(legend_count):
            if rng.random() < legend_prob:
                pool = [l for l in LEGENDS if l not in used_legends] or LEGENDS
                legend = rng.choice(pool)
                used_legends.add(legend)
                parts.append(_format_tmpl(legend, display=display))

    if wistful and detail >= 1:
        parts.append(rng.choice(WISTFUL).format(display=display))

    if travelogue:
        day = rng.randint(1, 365)
        prefix = rng.choice(TRAVELOGUE_PREFIXES).format(display=display, day=day)
        suffix = rng.choice(TRAVELOGUE_SUFFIXES).format(display=display)
        parts.insert(0, prefix)
        parts.append(suffix)

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
        if weather_enabled:
            data["weather_count"] = weather_count
            data["weather_prob"] = weather_prob
        if echo_enabled:
            data["echo_enabled"] = True
            data["echo_prob"] = echo_prob
            data["echo_count"] = echo_count
        if legend_enabled:
            data["legend_enabled"] = True
            data["legend_count"] = legend_count
            data["legend_prob"] = legend_prob
        if travelogue:
            data["travelogue"] = True
        if wistful:
            data["wistful"] = True
        if sound_enabled:
            data["sound_enabled"] = True
            data["sound_count"] = sound_count
            data["sound_prob"] = sound_prob
        if wildlife_enabled:
            data["wildlife_enabled"] = True
            if wildlife_count != 1:
                data["wildlife_count"] = wildlife_count
            if wildlife_prob != 1.0:
                data["wildlife_prob"] = wildlife_prob
        if time_phrases:
            data["time_of_day"] = time_phrases if len(time_phrases) > 1 else time_phrases[0]
            if time_count != 1:
                data["time_count"] = time_count
            if time_prob != 1.0:
                data["time_prob"] = time_prob
        if season_phrases:
            data["season"] = season_phrases if len(season_phrases) > 1 else season_phrases[0]
            if season_count != 1:
                data["season_count"] = season_count
            if season_prob != 1.0:
                data["season_prob"] = season_prob
        if perspective_enabled:
            data["perspective_enabled"] = True
            if perspective_count != 1:
                data["perspective_count"] = perspective_count
            if perspective_prob != 1.0:
                data["perspective_prob"] = perspective_prob
        if bias_overrides:
            data["bias_overrides"] = bias_overrides
        if mood_atmosphere:
            data["mood_atmosphere"] = True
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
        "--describe-biome", type=str, default=None, nargs="?",
        const="all",
        help="Show word bank for a biome (or 'all' for all biomes, default: all)",
    )
    parser.add_argument(
        "--describe-mood", type=str, default=None, nargs="?",
        const="all",
        help="Show word bank for a mood (or 'all' for all moods, default: all)",
    )
    parser.add_argument(
        "--describe-global", action="store_true",
        help="Show all global word pools with weight tiers (common/normal/rare)",
    )
    parser.add_argument(
        "--describe-templates", action="store_true",
        help="Show all sentence templates per slot with their index numbers",
    )
    parser.add_argument(
        "--describe-echoes", action="store_true",
        help="Show all available echo phrases with their index numbers",
    )
    parser.add_argument(
        "--describe-travelogue", action="store_true",
        help="Show all available travelogue prefixes and suffixes",
    )
    parser.add_argument(
        "--describe-sounds", action="store_true",
        help="Show all available soundscape phrases",
    )
    parser.add_argument(
        "--describe-wildlife", action="store_true",
        help="Show all available wildlife phrases",
    )
    parser.add_argument(
        "--describe-wistful", action="store_true",
        help="Show all available wistful phrases",
    )
    parser.add_argument(
        "--describe-times", action="store_true",
        help="Describe all available time-of-day phrases",
    )
    parser.add_argument(
        "--describe-seasons", action="store_true",
        help="Describe all available seasonal phrases",
    )
    parser.add_argument(
        "--describe-presets", action="store_true",
        help="Show all available presets with their settings",
    )
    parser.add_argument(
        "--preset", type=str, default=None, choices=list(PRESETS.keys()),
        help="Apply a named preset configuration (overridable by explicit flags)",
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
    parser.add_argument("--bias-adverb", type=str, default=None, choices=["normal", "common", "rare", "flat"],
        help="Per-category override: bias for adverbs")
    parser.add_argument("--bias-color", type=str, default=None, choices=["normal", "common", "rare", "flat"],
        help="Per-category override: bias for colors")
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
    parser.add_argument("--mood-weight-adverb", type=float, default=None,
        help="Per-category override: mood weight for adverbs")
    parser.add_argument("--mood-weight-color", type=float, default=None,
        help="Per-category override: mood weight for colors")
    parser.add_argument(
        "--mood-atmosphere", action="store_true",
        help="Add mood-specific atmospheric framing phrases that establish the emotional register",
    )
    parser.add_argument(
        "--show-seed", action="store_true",
        help="Display the random seed used for reproducibility",
    )
    parser.add_argument(
        "--template-set", type=str, default="random", choices=list(TEMPLATE_SETS.keys()),
        help="Template selection mode: random (default), first–seventh (fixed index)",
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
        "--no-weather", action="store_true",
        help="Disable weather descriptions in landscape output",
    )
    parser.add_argument(
        "--weather-count", type=int, default=1, choices=[0, 1, 2, 3],
        help="Number of weather descriptions per detail level (0-3, default: 1)",
    )
    parser.add_argument(
        "--weather-prob", type=float, default=1.0,
        help="Probability of a weather description appearing per roll (0.0 to 1.0, default: 1.0)",
    )
    parser.add_argument(
        "--no-middle", action="store_true",
        help="Disable middle sentences in landscape output (opening + weather + anomaly only)",
    )
    parser.add_argument(
        "--no-color", action="store_true",
        help="Disable color words in landscape descriptions",
    )
    parser.add_argument(
        "--no-element", action="store_true",
        help="Disable element words in landscape descriptions",
    )
    parser.add_argument(
        "--no-time-word", action="store_true",
        help="Disable temporal time words in landscape descriptions",
    )
    parser.add_argument(
        "--no-anomaly", action="store_true",
        help="Disable anomaly descriptions in landscape output",
    )
    parser.add_argument(
        "--echo", action="store_true",
        help="Append an atmospheric echo/memory phrase to the landscape",
    )
    parser.add_argument(
        "--echo-count", type=int, default=1, choices=[0, 1, 2, 3],
        help="Number of echo phrases per landscape (0-3, default: 1, requires --echo)",
    )
    parser.add_argument(
        "--echo-prob", type=float, default=1.0,
        help="Probability of an echo appearing per roll (0.0 to 1.0, default: 1.0)",
    )
    parser.add_argument(
        "--no-echo", action="store_true",
        help="Disable echo phrases (overrides preset and --echo)",
    )
    parser.add_argument(
        "--legend", action="store_true",
        help="Append a folkloric legend phrase to the landscape",
    )
    parser.add_argument(
        "--legend-count", type=int, default=1, choices=[0, 1, 2, 3],
        help="Number of legend phrases per landscape (0-3, default: 1, requires --legend)",
    )
    parser.add_argument(
        "--legend-prob", type=float, default=1.0,
        help="Probability of a legend appearing per roll (0.0 to 1.0, default: 1.0)",
    )
    parser.add_argument(
        "--no-legend", action="store_true",
        help="Disable legend phrases (overrides preset and --legend)",
    )
    parser.add_argument(
        "--describe-legends", action="store_true",
        help="Show all available legend phrases with their index numbers",
    )
    parser.add_argument(
        "--travelogue", action="store_true",
        help="Frame the landscape as a travel journal entry",
    )
    parser.add_argument(
        "--sound", action="store_true",
        help="Append a soundscape phrase describing sounds in the landscape",
    )
    parser.add_argument(
        "--no-sound", action="store_true",
        help="Disable soundscape phrases (overrides preset and --sound)",
    )
    parser.add_argument(
        "--sound-count", type=int, default=1, choices=[0, 1, 2, 3],
        help="Number of soundscape phrases per landscape (0-3, default: 1, requires --sound)",
    )
    parser.add_argument(
        "--sound-prob", type=float, default=1.0,
        help="Probability of a soundscape phrase appearing per roll (0.0 to 1.0, default: 1.0)",
    )
    parser.add_argument(
        "--time", action="store_true",
        help="Prepend a time-of-day phrase establishing when the landscape is viewed",
    )
    parser.add_argument(
        "--time-count", type=int, default=1, choices=[0, 1, 2, 3],
        help="Number of time-of-day phrases per landscape (0-3, default: 1, requires --time)",
    )
    parser.add_argument(
        "--time-prob", type=float, default=1.0,
        help="Probability of a time-of-day phrase appearing per roll (0.0 to 1.0, default: 1.0)",
    )
    parser.add_argument(
        "--no-time", action="store_true",
        help="Disable time-of-day phrase (overrides preset and --time)",
    )
    parser.add_argument(
        "--season", action="store_true",
        help="Prepend a seasonal phrase establishing the time of year",
    )
    parser.add_argument(
        "--season-count", type=int, default=1, choices=[0, 1, 2, 3],
        help="Number of seasonal phrases per landscape (0-3, default: 1, requires --season)",
    )
    parser.add_argument(
        "--season-prob", type=float, default=1.0,
        help="Probability of a seasonal phrase appearing per roll (0.0 to 1.0, default: 1.0)",
    )
    parser.add_argument(
        "--no-season", action="store_true",
        help="Disable seasonal phrase (overrides preset and --season)",
    )
    parser.add_argument(
        "--wildlife", action="store_true",
        help="Append a wildlife phrase describing inhabitants or creatures in the landscape",
    )
    parser.add_argument(
        "--wildlife-count", type=int, default=1, choices=[0, 1, 2, 3],
        help="Number of wildlife phrases per landscape (0-3, default: 1)",
    )
    parser.add_argument(
        "--wildlife-prob", type=float, default=1.0,
        help="Probability of a wildlife phrase appearing per roll (0.0 to 1.0, default: 1.0)",
    )
    parser.add_argument(
        "--no-wildlife", action="store_true",
        help="Disable wildlife phrases (overrides preset and --wildlife)",
    )
    parser.add_argument(
        "--perspective", action="store_true",
        help="Prepend a perspective/vantage phrase establishing spatial scale and viewing position",
    )
    parser.add_argument(
        "--no-perspective", action="store_true",
        help="Disable perspective phrase (overrides preset and --perspective)",
    )
    parser.add_argument(
        "--perspective-count", type=int, default=1, choices=[0, 1, 2, 3],
        help="Number of perspective phrases per landscape (0-3, default: 1)",
    )
    parser.add_argument(
        "--perspective-prob", type=float, default=1.0,
        help="Probability of a perspective phrase appearing per roll (0.0 to 1.0, default: 1.0)",
    )
    parser.add_argument(
        "--describe-perspectives", action="store_true",
        help="Show all available perspective phrases with their index numbers",
    )
    parser.add_argument(
        "--wistful", action="store_true",
        help="Append a wistful, yearning closing phrase to the landscape",
    )
    parser.add_argument(
        "--no-travelogue", action="store_true",
        help="Disable travelogue journal framing (overrides preset and --travelogue)",
    )
    parser.add_argument(
        "--no-wistful", action="store_true",
        help="Disable wistful closing phrase (overrides preset and --wistful)",
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
        "bias_adverb": "adverbs",
        "bias_color": "colors",
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
        "mood_weight_adverb": "adverbs",
        "mood_weight_color": "colors",
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

    # Apply preset — only overrides CLI args that have their default values
    if args.preset is not None:
        preset = PRESETS[args.preset]
        if "mood" in preset and args.mood is None:
            args.mood = preset["mood"]
        if "bias" in preset and args.bias == "normal":
            args.bias = preset["bias"]
        if "detail" in preset and args.detail == 1:
            args.detail = preset["detail"]
        if "anomaly_prob" in preset and args.anomaly_prob == 0.3:
            args.anomaly_prob = preset["anomaly_prob"]
        if "anomaly_count" in preset and args.anomaly_count == 1:
            args.anomaly_count = preset["anomaly_count"]
        if "weather_count" in preset and args.weather_count == 1:
            args.weather_count = preset["weather_count"]
        if "weather_prob" in preset and args.weather_prob == 1.0:
            args.weather_prob = preset["weather_prob"]
        if "echo_enabled" in preset and args.echo is False and not args.no_echo:
            args.echo = preset["echo_enabled"]
        if "echo_count" in preset and args.echo_count == 1:
            args.echo_count = preset["echo_count"]
        if "echo_prob" in preset and args.echo_prob == 1.0:
            args.echo_prob = preset["echo_prob"]
        if "legend_enabled" in preset and args.legend is False and not args.no_legend:
            args.legend = preset["legend_enabled"]
        if "legend_count" in preset and args.legend_count == 1:
            args.legend_count = preset["legend_count"]
        if "legend_prob" in preset and args.legend_prob == 1.0:
            args.legend_prob = preset["legend_prob"]
        if "travelogue" in preset and args.travelogue is False and not args.no_travelogue:
            args.travelogue = preset["travelogue"]
        if "wistful" in preset and args.wistful is False and not args.no_wistful:
            args.wistful = preset["wistful"]
        if "sound_enabled" in preset and args.sound is False and not args.no_sound:
            args.sound = preset["sound_enabled"]
        if "sound_count" in preset and args.sound_count == 1:
            args.sound_count = preset["sound_count"]
        if "sound_prob" in preset and args.sound_prob == 1.0:
            args.sound_prob = preset["sound_prob"]
        if "wildlife_enabled" in preset and args.wildlife is False and not args.no_wildlife:
            args.wildlife = preset["wildlife_enabled"]
        if "wildlife_count" in preset and args.wildlife_count == 1:
            args.wildlife_count = preset["wildlife_count"]
        if "wildlife_prob" in preset and args.wildlife_prob == 1.0:
            args.wildlife_prob = preset["wildlife_prob"]
        if "perspective_enabled" in preset and args.perspective is False and not args.no_perspective:
            args.perspective = preset["perspective_enabled"]
        if "perspective_count" in preset and args.perspective_count == 1:
            args.perspective_count = preset["perspective_count"]
        if "perspective_prob" in preset and args.perspective_prob == 1.0:
            args.perspective_prob = preset["perspective_prob"]
        if "time_of_day_enabled" in preset and args.time is False and not args.no_time:
            args.time = preset["time_of_day_enabled"]
        if "time_count" in preset and args.time_count == 1:
            args.time_count = preset["time_count"]
        if "time_prob" in preset and args.time_prob == 1.0:
            args.time_prob = preset["time_prob"]
        if "season_enabled" in preset and args.season is False and not args.no_season:
            args.season = preset["season_enabled"]
        if "season_count" in preset and args.season_count == 1:
            args.season_count = preset["season_count"]
        if "season_prob" in preset and args.season_prob == 1.0:
            args.season_prob = preset["season_prob"]
        if "color_enabled" in preset and args.no_color is False:
            args.no_color = not preset["color_enabled"]

    # --no-* overrides take effect after all preset gating
    if args.no_echo:
        args.echo = False
    if args.no_legend:
        args.legend = False
    if args.no_sound:
        args.sound = False
    if args.no_wildlife:
        args.wildlife = False
    if args.no_perspective:
        args.perspective = False
    if args.no_travelogue:
        args.travelogue = False
    if args.no_time:
        args.time = False
    if args.no_season:
        args.season = False
    if args.no_wistful:
        args.wistful = False

    if args.describe_biome is not None:
        print(describe_biome(args.describe_biome))
        return
    if args.describe_mood is not None:
        print(describe_mood(args.describe_mood))
        return
    if args.describe_global:
        print(describe_global())
        return
    if args.describe_templates:
        print(describe_templates())
        return
    if args.describe_echoes:
        print(describe_echoes())
        return
    if args.describe_legends:
        print(describe_legends())
        return
    if args.describe_travelogue:
        print(describe_travelogue())
        return
    if args.describe_sounds:
        print(describe_sounds())
        return
    if args.describe_wildlife:
        print(describe_wildlife())
        return
    if args.describe_perspectives:
        print(describe_perspectives())
        return
    if args.describe_wistful:
        print(describe_wistful())
        return
    if args.describe_times:
        print(describe_times())
        return
    if args.describe_seasons:
        print(describe_seasons())
        return
    if args.describe_presets:
        print(describe_presets())
        return

    lines = []
    for i in range(args.count):
        effective_seed = args.seed + i if args.seed is not None else None
        lines.append(generate_landscape(seed=effective_seed, biome=args.biome, show_biome=args.show_biome, fmt=args.format, combine=args.combine, detail=args.detail, bias=args.bias, show_seed=args.show_seed, mood=args.mood, mood_weight=args.mood_weight, template_set=args.template_set, anomaly_prob=args.anomaly_prob, anomaly_count=args.anomaly_count, bias_overrides=bias_overrides, mood_weight_overrides=mood_weight_overrides, template_overrides=template_overrides, dedup=not args.no_dedup, adverb_enabled=not args.no_adverb, biome_weights=biome_weights, weather_enabled=not args.no_weather, weather_count=args.weather_count, weather_prob=args.weather_prob, middle_enabled=not args.no_middle, color_enabled=not args.no_color, element_enabled=not args.no_element, anomaly_enabled=not args.no_anomaly, echo_enabled=args.echo, echo_count=args.echo_count, echo_prob=args.echo_prob, time_word_enabled=not args.no_time_word, legend_enabled=args.legend, legend_count=args.legend_count, legend_prob=args.legend_prob, travelogue=args.travelogue, wistful=args.wistful, sound_enabled=args.sound, sound_count=args.sound_count, sound_prob=args.sound_prob, time_of_day_enabled=args.time, time_count=args.time_count, time_prob=args.time_prob, season_enabled=args.season, season_count=args.season_count, season_prob=args.season_prob, wildlife_enabled=args.wildlife, wildlife_count=args.wildlife_count, wildlife_prob=args.wildlife_prob, perspective_enabled=args.perspective, perspective_count=args.perspective_count, perspective_prob=args.perspective_prob, mood_atmosphere=args.mood_atmosphere))
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
