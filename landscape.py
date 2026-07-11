#!/usr/bin/env python3
import argparse
import random

BIOMES = [
    "forest", "desert", "tundra", "ocean", "mountain range",
    "swamp", "cave system", "plain", "volcanic field", "coral reef",
]

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


def generate_landscape(seed=None):
    if seed is not None:
        random.seed(seed)

    biome = random.choice(BIOMES)
    adj = random.choice(ADJECTIVES)
    element = random.choice(ELEMENTS)
    noun = random.choice(NOUNS)
    verb = random.choice(VERBS)
    weather = random.choice(WEATHERS)

    parts = [
        f"A vast {adj} {biome} stretches before you.",
        f"{element.capitalize()} {verb}s between the {noun}.",
        f"{weather}.",
    ]

    if random.random() < 0.3:
        parts.append(random.choice(ANOMALIES))

    return " ".join(parts)


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
    args = parser.parse_args()

    for i in range(args.count):
        print(generate_landscape(seed=args.seed))
        if args.count > 1 and i < args.count - 1:
            print()


if __name__ == "__main__":
    main()
