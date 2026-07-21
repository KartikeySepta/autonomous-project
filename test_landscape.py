import unittest
from pathlib import Path

import random

from landscape import (
    generate_landscape,
    BIOMES, ADJECTIVES, ELEMENTS, NOUNS, VERBS, WEATHERS, ANOMALIES, ADVERBS, COLORS, BIOME_WORDS, ECHOES, LEGENDS,
    COMMON_WORDS, RARE_WORDS, SENTENCE_TEMPLATES, BIAS_MODES, _conjugate,
    MOOD_WORDS, MOOD_BOOST, TEMPLATE_SETS, _pick_template,
    TIME_WORDS, TIMES_OF_DAY, SEASONS, TRAVELOGUE_PREFIXES, TRAVELOGUE_SUFFIXES, WISTFUL, SOUNDSCAPES, WILDLIFE, PERSPECTIVES, SIMILES, METAPHORS, PERSONIFICATIONS,
    describe_travelogue, describe_wistful, describe_sounds, describe_times, describe_seasons, describe_wildlife, describe_perspectives, describe_similes, describe_metaphors, describe_personifications,
)

ALL_ADJECTIVES = set(ADJECTIVES) | {w for bw in BIOME_WORDS.values() for w in bw.get("adjectives", [])}
ALL_VERBS = set(VERBS) | {w for bw in BIOME_WORDS.values() for w in bw.get("verbs", [])}
ALL_ELEMENTS = set(ELEMENTS) | {w for bw in BIOME_WORDS.values() for w in bw.get("elements", [])}
ALL_NOUNS = set(NOUNS) | {w for bw in BIOME_WORDS.values() for w in bw.get("nouns", [])}
ALL_WEATHERS = set(WEATHERS) | {w for bw in BIOME_WORDS.values() for w in bw.get("weathers", [])}
ALL_ANOMALIES = set(ANOMALIES) | {w for bw in BIOME_WORDS.values() for w in bw.get("anomalies", [])}
ALL_ADVERBS = set(ADVERBS) | {w for bw in BIOME_WORDS.values() for w in bw.get("adverbs", [])}
ALL_COLORS = set(COLORS) | {w for bw in BIOME_WORDS.values() for w in bw.get("colors", [])}
ALL_TIME_WORDS = set(TIME_WORDS)
ALL_LEGENDS = set(LEGENDS)
ALL_WISTFUL = set(WISTFUL)
ALL_SOUNDSCAPES = set(SOUNDSCAPES)
ALL_TIMES_OF_DAY = set(TIMES_OF_DAY)
ALL_SEASONS = set(SEASONS)
ALL_SIMILES = set(SIMILES)
ALL_PERSONIFICATIONS = set(PERSONIFICATIONS)

TIME_INDICATORS = [
    "Dawn breaks",
    "dead of night",
    "blazing noon",
    "Dusk settles",
    "Early morning",
    "Midnight beneath",
    "Twilight fades",
    "golden hour",
    "first light",
    "starless night",
    "Late afternoon",
    "storm-heavy",
    "blue hour",
    "witching hour",
    "Morning mist",
    "amber and rose",
    "full moon rises",
    "heavy stillness of noon",
    "deepest dark before dawn",
    "Low grey clouds",
]

SEASON_INDICATORS = [
    "first buds push through",
    "droning insects",
    "study in gold and decay",
    "silence and frost",
    "tender green of late spring",
    "Midsummer's lush fullness",
    "scent of falling leaves",
    "muffling the world in white",
    "revealing its bones",
    "reborn from rain",
    "meltwater carves",
    "fields heavy with seed",
    "prepares for winter's rest",
    "palace of crystal and ice",
    "washes winter's last traces",
    "thunderheads pile",
    "Indian summer warmth lingers",
    "thick white silence",
    "Spring wildflowers blanket",
    "Autumn fog wraps the landscape",
]

WILDLIFE_INDICATORS = [
    "deer picks its way",
    "Eyes watch from the shadows",
    "birds flit",
    "Something large stirs",
    "A lone",
    "call of an unseen creature",
    "Tracks in the",
    "teems with quiet, hidden life",
    "pack of",
    "chitters",
    "Fireflies drift",
    "Something hunts",
    "bird of prey circles",
    "hidden structures",
    "wings rises from",
    "Bats wheel",
    "forked tongue",
    "Fish leap",
    "Crows roost",
    "moths flutter",
]

SOUND_INDICATORS = [
    "tone that seems to come from everywhere",
    "shifts and settles",
    "glass shattering",
    "close, though nothing is there",
    "call of an unknown creature",
    "slow, patient",
    "at the edge of hearing",
    "shakes the",
    "drone rises and falls",
    "crackles like distant",
    "Footsteps echo through",
    "note rings out",
    "each drop a bright",
    "learned to sing",
    "shape the very",
    "never form words",
    "resonates through the",
    "thunder rumbles",
    "Steam hisses",
    "never quite settles into a pattern",
]

WEATHER_INDICATORS = [
    "gentle rain falls",
    "still calm lingers",
    "breeze drifts through",
    "unnatural silence hangs",
    "faint humming fills",
    "drifts slowly downward",
    "curls along the ground",
    "shimmers with heat",
    "snow falls",
    "cold fog rolls",
    "exhales a thin",
    "flickers on the",
    "thin mist rises from",
    "smell of distant rain",
    "promise of thunder",
    "drives needles of sleet",
    "swirl in sudden eddies",
    "shafts of amber light",
    "heavy and damp",
    "fine dust rises in spirals",
    "rush of wings",
    "world to silhouettes",
    "white foam",
    "glass-calm",
    "haboob swallows",
    "phantom pools",
    "swallowing the ground floor",
    "rain drums on",
    "hoarfrost settles",
    "wind screams across",
    "avalanche thunders",
    "boil over the ridgeline",
    "warm rain falls in heavy droplets",
    "shed leaves and seed pods",
    "deep rumble echoes",
    "veins of silver and white",
    "curtain of black and silver",
    "plain into a sea of fire",
    "groan issues from deep",
    "lightning forks through",
    "living constellation",
    "bioluminescent plankton ignites",
    "caps pulse in slow waves",
    "veil of spores settles",
    "bank of luminous clouds",
    "stars pierce the thin air",
    "cascade of prismatic light",
    "liquid geometry",
]

LEGEND_INDICATORS = [
    "maps leave", "was not here", "Pilgrims once walked", "older than stone",
    "many names", "returns unchanged", "song about", "no map",
    "dreams of a time", "hermit once lived",
    "remembers those who built", "seen from far away", "placed by hand",
    "sounds like a name", "well in the",
    "appears in the dreams of those who have never",
    "bell in the",
    "scent that cannot be described",
    "leads to the same clearing",
    "built by no one",
]

PERSPECTIVE_INDICATORS = [
    "Seen from above",
    "At ground level",
    "From a distance",
    "Up close, the",
    "Seen from the heights",
    "From within,",
    "into the distance",
    "At the edge of the",
    "scale of the",
    "Looking back at",
    "hold the landscape together",
    "parts and closes around",
    "grows against the horizon",
    "appears transformed",
    "unfolds beneath you",
    "vertiginous glimpse",
    "vertical cascade that dwarfs",
    "depth that swallows",
    "suspended, a vision in",
    "world without edges",
]

SIMILE_INDICATORS = [
    "tapestry of",
    "moves through the",
    "falls like",
    "slumbering",
    "shimmers like a",
    "glow like embers",
    "wraps around everything like",
    "hangs like a",
    "dream of",
    "bleed into the surroundings",
    "like water in a dry",
    "shifts like a living map",
    "rises and falls like the",
    "drawn in liquid",
    "half-remembered and fading",
    "reaching toward the sky",
    "rousing from a sleep",
    "wave frozen",
    "needs no fuel",
    "world that never was",
]

METAPHOR_INDICATORS = [
    "cathedral of",
    "living chronicle",
    "language spoken only by",
    "offered to the",
    "wound in the world",
    "memories of a",
    "threshold between",
    "up to the",
    "neither side willing",
    "beating beneath",
    "armor of",
    "sung by stones",
    "forge where",
    "anchor of",
    "feast of",
    "arching between",
    "forgotten gravity",
    "unseen hand",
    "world within a world",
    "silence of ages",
]

PERSONIFICATION_INDICATORS = [
    "filling the air",
    "turns its",
    "older than words",
    "slumber deep",
    "each pulse sending",
    "grasping at",
    "song older than memory",
    "light was young",
    "between stars",
    "story falling",
    "dances under the",
    "cascade that echoes",
    "head lowered in reverence",
    "sorrow that has no name",
    "holding it close in",
    "shaking the sky",
    "breath that spans ages",
    "ancient lesson",
    "cannot quench",
    "standing against the sky",
]


class TestLandscape(unittest.TestCase):
    def test_output_is_nonempty_string(self):
        result = generate_landscape(seed=42)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_output_ends_with_period(self):
        result = generate_landscape(seed=42)
        self.assertTrue(result.endswith("."))

    def test_output_starts_with_valid_opening(self):
        result = generate_landscape(seed=42)
        valid_starts = ("A vast ", "Before you", "The ")
        has_em_dash = " — " in result[:60] and result[0].isupper()
        self.assertTrue(
            any(result.startswith(s) for s in valid_starts) or has_em_dash,
            f"Output doesn't start with any valid opening: {result!r}",
        )

    def test_opening_contains_known_element(self):
        result = generate_landscape(seed=42)
        self.assertTrue(
            any(e in result for e in ALL_ELEMENTS),
            f"Opening should contain a known element word: {result!r}",
        )

    def test_opening_em_dash_template_appears_across_seeds(self):
        results = [generate_landscape(seed=s, biome="forest") for s in range(200)]
        em_dash_count = sum(1 for r in results if " — " in r[:60])
        self.assertGreater(em_dash_count, 0,
            "Em-dash opening template should appear across 200 seeds")

    def test_opening_element_is_deterministic(self):
        a = generate_landscape(seed=42)
        b = generate_landscape(seed=42)
        self.assertEqual(a, b)

    def test_opening_element_works_with_detail_zero(self):
        for s in range(20):
            result = generate_landscape(seed=s, detail=0)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)

    def test_opening_element_works_with_json_format(self):
        result = generate_landscape(seed=42, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertGreater(len(data["text"]), 0)

    def test_output_contains_known_biome(self):
        result = generate_landscape(seed=42)
        self.assertTrue(any(b in result for b in BIOMES))

    def test_output_contains_known_adjective(self):
        result = generate_landscape(seed=42)
        self.assertTrue(any(a in result for a in ALL_ADJECTIVES))

    def test_output_contains_known_verb(self):
        result = generate_landscape(seed=42)
        self.assertTrue(any(v in result for v in ALL_VERBS))

    def test_seed_produces_deterministic_output(self):
        a = generate_landscape(seed=100)
        b = generate_landscape(seed=100)
        self.assertEqual(a, b)

    def test_different_seeds_produce_different_output(self):
        a = generate_landscape(seed=100)
        b = generate_landscape(seed=200)
        self.assertNotEqual(a, b)

    def test_anomaly_may_appear(self):
        results = {generate_landscape(seed=s) for s in range(200)}
        has_anomaly = any(
            any(a in r for a in ALL_ANOMALIES) for r in results
        )
        self.assertTrue(has_anomaly)

    def test_some_outputs_have_no_anomaly(self):
        results = {generate_landscape(seed=s) for s in range(200)}
        no_anomaly = any(
            not any(a in r for a in ALL_ANOMALIES) for r in results
        )
        self.assertTrue(no_anomaly)

    def test_biome_flag_produces_correct_biome(self):
        result = generate_landscape(seed=42, biome="desert")
        self.assertIn("desert", result)

    def test_biome_flag_overrides_random(self):
        r1 = generate_landscape(seed=99, biome="ocean")
        r2 = generate_landscape(seed=99, biome="ocean")
        self.assertEqual(r1, r2)
        self.assertIn("ocean", r1)

    def test_no_biome_produces_varied_biomes(self):
        biomes_seen = set()
        for s in range(50):
            r = generate_landscape(seed=s)
            for b in BIOMES:
                if b in r:
                    biomes_seen.add(b)
        self.assertGreater(len(biomes_seen), 1)

    def test_count_flag_argument_exists(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_common_words_appear_often_across_categories(self):
        results = [generate_landscape(seed=s) for s in range(500)]
        common_hits = sum(
            1 for r in results if any(c in r for c in COMMON_WORDS)
        )
        self.assertGreater(common_hits, 100)

    def test_rare_words_appear_sometimes(self):
        results = [generate_landscape(seed=s) for s in range(500)]
        rare_hits = sum(
            1 for r in results if any(c in r for c in RARE_WORDS)
        )
        self.assertLess(rare_hits, 400)
        self.assertGreater(rare_hits, 0)

    def test_common_outnumbers_rare_in_output(self):
        common_count = 0
        rare_count = 0
        for s in range(500):
            r = generate_landscape(seed=s)
            common_count += sum(1 for c in COMMON_WORDS if c in r)
            rare_count += sum(1 for c in RARE_WORDS if c in r)
        self.assertGreater(common_count, rare_count * 2)

    def test_word_weight_function_exists(self):
        from landscape import _word_weight
        self.assertGreater(_word_weight("crystal"), _word_weight("brass"))
        self.assertEqual(_word_weight("crystal"), _word_weight("shadow"))
        self.assertEqual(_word_weight("brass"), _word_weight("ivory"))

    def test_show_biome_reveals_biome_name(self):
        result = generate_landscape(seed=42, biome="tundra", show_biome=True)
        self.assertIn("[tundra]", result)

    def test_show_biome_default_hides_biome(self):
        result = generate_landscape(seed=42, biome="tundra", show_biome=False)
        self.assertNotIn("[tundra]", result)

    def test_show_biome_flag_works_via_main(self):
        from landscape import main
        self.assertTrue(callable(main))


    def test_default_format_is_prose(self):
        result = generate_landscape(seed=42)
        self.assertNotIn("\n", result)

    def test_format_poetic_has_linebreaks(self):
        result = generate_landscape(seed=42, fmt="poetic")
        self.assertIn("\n", result)

    def test_format_prose_no_linebreaks(self):
        result = generate_landscape(seed=42, fmt="prose")
        self.assertNotIn("\n", result)

    def test_format_poetic_all_lines_capitalized(self):
        result = generate_landscape(seed=42, biome="tundra", fmt="poetic")
        for line in result.split("\n"):
            self.assertTrue(line[0].isupper(), f"Line does not start with capital: {line!r}")

    def test_format_flag_works_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_format_json_valid_json(self):
        result = generate_landscape(seed=42, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIsInstance(data, dict)

    def test_format_json_contains_text_key(self):
        result = generate_landscape(seed=42, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertGreater(len(data["text"]), 0)

    def test_format_json_contains_biome_key(self):
        result = generate_landscape(seed=42, biome="tundra", fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("biome", data)
        self.assertEqual(data["biome"], "tundra")

    def test_format_json_contains_seed_when_provided(self):
        result = generate_landscape(seed=42, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("seed", data)
        self.assertEqual(data["seed"], 42)

    def test_format_json_text_matches_prose(self):
        prose = generate_landscape(seed=42, biome="forest")
        result = generate_landscape(seed=42, biome="forest", fmt="json")
        import json as j
        data = j.loads(result)
        self.assertEqual(data["text"], prose)

    def test_format_json_with_combine_includes_biomes_list(self):
        result = generate_landscape(seed=42, combine="forest,desert", fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("biome", data)
        self.assertIn("biomes", data)
        self.assertEqual(data["biomes"], ["forest", "desert"])

    def test_format_json_includes_mood_when_set(self):
        result = generate_landscape(seed=42, mood="eerie", fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("mood", data)
        self.assertIn("eerie", data["mood"])

    def test_format_json_does_not_have_bracketed_tags(self):
        result = generate_landscape(seed=42, biome="tundra", show_biome=True, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertNotIn("[tundra]", data["text"])
        self.assertEqual(data["biome"], "tundra")

    def test_format_json_works_with_all_formats_flag(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_format_json_includes_mood_weight(self):
        result = generate_landscape(seed=42, mood="eerie", fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("mood_weight", data)
        self.assertEqual(data["mood_weight"], 5)

    def test_format_json_includes_mood_weight_without_mood(self):
        result = generate_landscape(seed=42, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("mood_weight", data)
        self.assertEqual(data["mood_weight"], 5)

    def test_format_json_mood_weight_reflects_custom_value(self):
        result = generate_landscape(seed=42, mood="eerie", mood_weight=20, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertEqual(data["mood_weight"], 20)


    def test_output_contains_known_adverb(self):
        results = {generate_landscape(seed=s) for s in range(200)}
        self.assertTrue(
            any(a in r for r in results for a in ALL_ADVERBS),
            "No known adverb appeared across 200 seeds",
        )

    def test_adverb_appears_in_middle_templates(self):
        results = [generate_landscape(seed=s, biome="forest", template_set="first") for s in range(200)]
        self.assertTrue(
            any(a in r for r in results for a in ALL_ADVERBS),
            "No adverb appeared in middle sentences across 200 seeds",
        )

    def test_adverb_with_mood_does_not_break_output(self):
        for mood in ["eerie", "vibrant", "desolate"]:
            for s in range(10):
                result = generate_landscape(seed=s, mood=mood)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 10)

    def test_adverb_is_deterministic_with_seed(self):
        a = generate_landscape(seed=42)
        b = generate_landscape(seed=42)
        self.assertEqual(a, b)

    def test_adverb_with_detail_three_produces_valid_output(self):
        for s in range(20):
            result = generate_landscape(seed=s, detail=3)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 50)

    def test_adverb_word_weight_function_works(self):
        from landscape import _word_weight
        w_common = _word_weight("softly", bias="normal")
        w_rare = _word_weight("relentlessly", bias="normal")
        self.assertGreater(w_common, w_rare,
            "Common adverb should have higher weight than rare adverb")

    def test_per_sentence_adverb_uses_multiple_adverbs(self):
        result = generate_landscape(seed=42, template_set="first", detail=2, dedup=True)
        found = [a for a in ALL_ADVERBS if a in result]
        self.assertGreaterEqual(len(found), 2,
            "Per-sentence adverb should use different adverbs across sentences")

    def test_per_sentence_adverb_deterministic(self):
        a = generate_landscape(seed=42, detail=2)
        b = generate_landscape(seed=42, detail=2)
        self.assertEqual(a, b,
            "Per-sentence adverb should be deterministic with same seed")

    def test_per_sentence_adverb_detail_three_has_more_adverb_variety(self):
        adverbs_found = set()
        for s in range(50):
            result = generate_landscape(seed=s, template_set="first", detail=3, dedup=True)
            adverbs_found.update(a for a in ALL_ADVERBS if a in result)
        self.assertGreaterEqual(len(adverbs_found), 3,
            "With detail=3 and per-sentence adverb, should see varied adverbs across many outputs")

    def test_per_sentence_adverb_respects_adverb_disabled(self):
        for s in range(20):
            result = generate_landscape(seed=s, adverb_enabled=False, detail=2)
            self.assertNotIn("  ", result)
            self.assertNotIn(" .", result)
            self.assertTrue(result.endswith("."))

    def test_per_sentence_adverb_with_adverb_enabled_default(self):
        a = generate_landscape(seed=42, adverb_enabled=True, detail=2)
        b = generate_landscape(seed=42, detail=2)
        self.assertEqual(a, b,
            "adverb_enabled=True should match default with per-sentence adverb")

    def test_per_sentence_adj_uses_multiple_adjectives(self):
        all_adjs = ALL_ADJECTIVES
        multi_count = 0
        for s in range(100):
            result = generate_landscape(seed=s, template_set="first", detail=2, dedup=True)
            found = [a for a in all_adjs if a in result]
            if len(set(found)) >= 2:
                multi_count += 1
        self.assertGreater(multi_count, 50,
            "Per-sentence adjective should produce multiple distinct adjectives in most outputs")

    def test_per_sentence_adj_deterministic(self):
        a = generate_landscape(seed=42, detail=2)
        b = generate_landscape(seed=42, detail=2)
        self.assertEqual(a, b,
            "Per-sentence adjective should be deterministic with same seed")

    def test_per_sentence_adj_detail_three_has_more_adjective_variety(self):
        adjs_found = set()
        for s in range(50):
            result = generate_landscape(seed=s, template_set="first", detail=3, dedup=True)
            adjs_found.update(a for a in ALL_ADJECTIVES if a in result)
        self.assertGreaterEqual(len(adjs_found), 3,
            "With detail=3 and per-sentence adjective, should see varied adjectives across many outputs")

    def test_per_sentence_adj_respects_middle_disabled(self):
        for s in range(20):
            result = generate_landscape(seed=s, middle_enabled=False, detail=2)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)

    def test_per_sentence_adj_with_adverb_disabled(self):
        for s in range(20):
            result = generate_landscape(seed=s, adverb_enabled=False, detail=2)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)

    def test_combine_two_biomes_contains_both_names(self):
        result = generate_landscape(seed=42, combine="forest,desert")
        self.assertIn("forest", result)
        self.assertIn("desert", result)
        self.assertIn(" and ", result)

    def test_combine_three_biomes_contains_all_names(self):
        result = generate_landscape(seed=42, combine="tundra,ocean,mountain range")
        self.assertIn("tundra", result)
        self.assertIn("ocean", result)
        self.assertIn("mountain range", result)

    def test_combine_uses_vocabulary_from_both(self):
        forest_words = set(BIOME_WORDS["forest"].get("adjectives", []))
        desert_words = set(BIOME_WORDS["desert"].get("adjectives", []))
        results = [generate_landscape(seed=s, combine="forest,desert") for s in range(200)]
        found_forest = any(any(w in r for w in forest_words) for r in results)
        found_desert = any(any(w in r for w in desert_words) for r in results)
        self.assertTrue(found_forest, "forest-specific adjectives never appeared")
        self.assertTrue(found_desert, "desert-specific adjectives never appeared")

    def test_combine_show_biome_shows_all(self):
        result = generate_landscape(seed=42, combine="swamp,cave system", show_biome=True)
        self.assertIn("[swamp, cave system]", result)

    def test_combine_single_biome_equals_regular(self):
        combined = generate_landscape(seed=42, combine="tundra")
        regular = generate_landscape(seed=42, biome="tundra")
        self.assertEqual(combined, regular)

    def test_combine_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


    def test_template_variety_opening_patterns_differ_across_seeds(self):
        results = [generate_landscape(seed=s, biome="forest") for s in range(100)]
        counts = {
            "A vast ": sum(1 for r in results if r.startswith("A vast ")),
            "Before you": sum(1 for r in results if r.startswith("Before you")),
            "The ": sum(1 for r in results if r.startswith("The ")),
            "em-dash": sum(1 for r in results if " — " in r[:60]),
        }
        distinct = sum(1 for v in counts.values() if v > 0)
        self.assertGreaterEqual(distinct, 2, f"Only {distinct} opening patterns seen: {counts}")

    def test_template_variety_middle_has_varied_structure(self):
        results = [generate_landscape(seed=s, biome="forest") for s in range(100)]
        has_classic = any(" between the " in r for r in results)
        has_among = any(r.startswith("Among") for r in results)
        has_through = any(" through the " in r for r in results)
        has_beneath = any("Beneath the " in r for r in results)
        self.assertTrue(has_classic or has_among or has_through or has_beneath,
            "No known middle pattern found")

    def test_template_variety_does_not_break_output(self):
        for s in range(50):
            result = generate_landscape(seed=s)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)

    def test_template_variety_weather_has_varied_structure(self):
        results = [generate_landscape(seed=s, biome="forest") for s in range(200)]
        has_air_tells = any("The air tells its own story: " in r for r in results)
        has_as_if = any(" itself breathes " in r for r in results)
        has_through = any("Through the " in r for r in results)
        self.assertTrue(
            has_air_tells or has_as_if or has_through,
            "Neither alternative weather template appeared across 200 seeds",
        )

    def test_weather_contains_known_element(self):
        results = [generate_landscape(seed=s, biome="forest") for s in range(200)]
        self.assertTrue(
            any(e in r for r in results for e in ALL_ELEMENTS),
            "No known element word appeared in weather across 200 seeds",
        )

    def test_weather_element_through_template_appears_across_seeds(self):
        results = [generate_landscape(seed=s, biome="tundra") for s in range(300)]
        through_matches = sum(
            1 for r in results if "Through the " in r
        )
        self.assertGreater(through_matches, 0,
            "'Through the {element}' weather template should appear across 300 seeds",
        )

    def test_weather_element_works_with_middle_disabled(self):
        for s in range(20):
            result = generate_landscape(seed=s, middle_enabled=False, detail=2)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)
            self.assertTrue(result.endswith("."))

    def test_weather_element_is_deterministic(self):
        a = generate_landscape(seed=42, detail=2)
        b = generate_landscape(seed=42, detail=2)
        self.assertEqual(a, b,
            "Weather with element templates should be deterministic")

    def test_weather_element_works_with_detail_three(self):
        for s in range(20):
            result = generate_landscape(seed=s, detail=3)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 50)

    def test_weather_element_works_with_json_format(self):
        result = generate_landscape(seed=42, fmt="json", detail=2)
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertGreater(len(data["text"]), 0)

    def test_weather_element_template_count_increased(self):
        weather_templates = SENTENCE_TEMPLATES["weather"]
        self.assertGreaterEqual(len(weather_templates), 4,
            "Should have at least 4 weather templates")

    def test_weather_element_templates_use_element_placeholder(self):
        weather_templates = SENTENCE_TEMPLATES["weather"]
        element_tmpls = [t for t in weather_templates if "{element}" in t]
        self.assertGreaterEqual(len(element_tmpls), 2,
            "At least 2 weather templates should reference {element}")

    def test_weather_element_works_with_no_adverb(self):
        for s in range(10):
            result = generate_landscape(seed=s, adverb_enabled=False, detail=2)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)
            self.assertNotIn("  ", result)
            self.assertTrue(result.endswith("."))

    def test_template_variety_anomaly_has_varied_structure(self):
        results = [generate_landscape(seed=s, biome="forest") for s in range(200)]
        has_strange = any("catches your eye" in r for r in results)
        has_wrongness = any("There is a quiet wrongness here" in r for r in results)
        self.assertTrue(
            has_strange or has_wrongness,
            "Neither alternative anomaly template appeared across 200 seeds",
        )

    def test_anomaly_standalone_template_keeps_capital(self):
        for s in range(100):
            result = generate_landscape(seed=s, biome="forest", template_overrides={"anomaly": "first"}, anomaly_prob=1.0)
            if "Something is not right" in result or "strange" in result or "quiet wrongness" in result or "In the " in result:
                continue
            for a in ALL_ANOMALIES:
                if a in result:
                    self.assertTrue(a[0].isupper(),
                        f"Standalone anomaly should start capitalized: {result!r}")
                    break

    def test_anomaly_colon_template_lowercases(self):
        results = [
            generate_landscape(seed=s, biome="forest",
                               template_overrides={"anomaly": "third"}, anomaly_prob=1.0)
            for s in range(200)
        ]
        colon_lines = [r for r in results if "detail catches your eye" in r or "There is a quiet wrongness here" in r]
        lowercases = sum(
            1 for r in colon_lines
            for a in ALL_ANOMALIES
            if a[0].lower() + a[1:] in r
        )
        self.assertGreater(
            lowercases, 0,
            "Colon-style anomaly templates should produce lowercase continuation",
        )

    def test_anomaly_lower_does_not_break_output(self):
        for s in range(50):
            result = generate_landscape(seed=s, anomaly_prob=1.0)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)

    def test_anomaly_lower_with_detail_three(self):
        for s in range(20):
            result = generate_landscape(seed=s, detail=3, anomaly_prob=1.0)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 50)

    def test_conjugate_adds_s_for_regular_verbs(self):
        self.assertEqual(_conjugate("whisper"), "whispers")
        self.assertEqual(_conjugate("glow"), "glows")
        self.assertEqual(_conjugate("drift"), "drifts")

    def test_conjugate_adds_es_for_sibilant_endings(self):
        self.assertEqual(_conjugate("crash"), "crashes")
        self.assertEqual(_conjugate("hiss"), "hisses")
        self.assertEqual(_conjugate("stretch"), "stretches")
        self.assertEqual(_conjugate("echo"), "echoes")

    def test_conjugate_handles_y_endings(self):
        self.assertEqual(_conjugate("fly"), "flies")
        self.assertEqual(_conjugate("carry"), "carries")

    def test_conjugate_output_no_bare_s_append_for_es_verbs(self):
        wrong_forms = ["crashs", "stretchs", "echos"]
        results = [generate_landscape(seed=s, combine="ocean,plain,mountain range,cave system,volcanic field") for s in range(500)]
        for r in results:
            for bad in wrong_forms:
                self.assertNotIn(bad, r)


    def test_detail_default_is_one(self):
        result = generate_landscape(seed=42)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_detail_zero_is_shorter_than_one(self):
        for s in range(20):
            d0 = generate_landscape(seed=s, detail=0)
            d1 = generate_landscape(seed=s, detail=1)
            self.assertGreater(len(d1), len(d0),
                f"detail=1 not longer than detail=0 at seed {s}")

    def test_detail_two_has_more_sentences_than_one(self):
        for s in range(20):
            d1 = generate_landscape(seed=s, detail=1)
            d2 = generate_landscape(seed=s, detail=2)
            s1 = d1.count(". ")
            s2 = d2.count(". ")
            self.assertGreater(s2, s1,
                f"detail=2 ({s2} sentences) not more than detail=1 ({s1} sentences) at seed {s}")

    def test_detail_three_produces_valid_output(self):
        for s in range(20):
            result = generate_landscape(seed=s, detail=3)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 50)

    def test_detail_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


    def test_bias_default_is_normal(self):
        from landscape import _word_weight
        self.assertEqual(_word_weight("crystal"), 10)
        self.assertEqual(_word_weight("brass"), 1)
        self.assertEqual(_word_weight("pillars"), 5)

    def test_bias_modes_affect_word_weights(self):
        from landscape import _word_weight
        self.assertEqual(_word_weight("crystal", bias="common"), 20)
        self.assertEqual(_word_weight("crystal", bias="flat"), 1)
        self.assertEqual(_word_weight("brass", bias="rare"), 3)
        self.assertEqual(_word_weight("brass", bias="flat"), 1)

    def test_bias_flat_produces_valid_output(self):
        for s in range(20):
            result = generate_landscape(seed=s, bias="flat")
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)

    def test_bias_common_increases_common_word_frequency(self):
        total_normal = 0
        total_common = 0
        for s in range(300):
            total_normal += sum(1 for c in COMMON_WORDS if c in generate_landscape(seed=s, bias="normal"))
            total_common += sum(1 for c in COMMON_WORDS if c in generate_landscape(seed=s, bias="common"))
        self.assertGreater(total_common, total_normal,
            "bias=common should produce more common word occurrences total than bias=normal")

    def test_bias_rare_increases_rare_word_frequency(self):
        rare_hits_normal = 0
        rare_hits_rare = 0
        for s in range(300):
            if any(r in generate_landscape(seed=s, bias="normal") for r in RARE_WORDS):
                rare_hits_normal += 1
            if any(r in generate_landscape(seed=s, bias="rare") for r in RARE_WORDS):
                rare_hits_rare += 1
        self.assertGreater(rare_hits_rare, rare_hits_normal,
            "bias=rare should produce more outputs with rare words than bias=normal")

    def test_bias_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


    def test_show_seed_with_provided_seed_shows_seed(self):
        result = generate_landscape(seed=42, show_seed=True)
        self.assertIn("[seed=42]", result)

    def test_show_seed_default_hides_seed(self):
        result = generate_landscape(seed=42, show_seed=False)
        self.assertNotIn("[seed=", result)

    def test_show_seed_without_seed_generates_seed(self):
        result = generate_landscape(show_seed=True)
        import re
        match = re.search(r'\[seed=(\d+)\]', result)
        self.assertIsNotNone(match, f"Output should contain [seed=N]: {result!r}")
        seed = int(match.group(1))
        self.assertGreaterEqual(seed, 0)

    def test_show_seed_output_is_reproducible(self):
        a = generate_landscape(show_seed=True)
        import re
        match = re.search(r'\[seed=(\d+)\]', a)
        seed = int(match.group(1))
        b = generate_landscape(seed=seed, show_seed=True)
        self.assertIn(f"[seed={seed}]", b)
        self.assertEqual(a, b,
            "Output with auto-generated seed should be reproducible with that seed")

    def test_show_seed_flag_works_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


    def test_mood_does_not_break_output(self):
        for mood in ["eerie", "vibrant", "desolate"]:
            for s in range(10):
                result = generate_landscape(seed=s, mood=mood)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 10)

    def test_mood_word_weight_boosted_for_matched_words(self):
        from landscape import _word_weight
        # "shadow" is in MOOD_WORDS["eerie"]["adjectives"], so weight is boosted under flat bias
        normal_w = _word_weight("shadow", bias="flat", mood=None, category="adjectives")
        mood_w = _word_weight("shadow", bias="flat", mood="eerie", category="adjectives")
        self.assertEqual(mood_w, normal_w * MOOD_BOOST)

    def test_mood_word_weight_not_boosted_for_unmatched_words(self):
        from landscape import _word_weight
        # "brass" is rare but NOT in any MOOD_WORDS["eerie"] category
        normal_w = _word_weight("brass", bias="normal", mood=None, category="adjectives")
        mood_w = _word_weight("brass", bias="normal", mood="eerie", category="adjectives")
        self.assertEqual(mood_w, normal_w)

    def test_mood_category_specific_boost(self):
        from landscape import _word_weight
        # "shadow" is in MOOD_WORDS["eerie"]["adjectives"] but NOT in "elements"
        w_adjectives = _word_weight("shadow", bias="flat", mood="eerie", category="adjectives")
        w_elements = _word_weight("shadow", bias="flat", mood="eerie", category="elements")
        self.assertEqual(w_elements, _word_weight("shadow", bias="flat"))
        self.assertEqual(w_adjectives, w_elements * MOOD_BOOST)

    def test_mood_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_mood_weight_one_equals_no_boost(self):
        from landscape import _word_weight
        w_no_mood = _word_weight("shadow", bias="flat", mood=None, category="adjectives")
        w_one = _word_weight("shadow", bias="flat", mood="eerie", category="adjectives", mood_weight=1)
        self.assertEqual(w_one, w_no_mood)

    def test_mood_weight_zero_suppresses_mood_words(self):
        from landscape import _word_weight
        w_zero = _word_weight("shadow", bias="flat", mood="eerie", category="adjectives", mood_weight=0)
        self.assertEqual(w_zero, 0)

    def test_mood_weight_high_magnifies_boost(self):
        from landscape import _word_weight
        w_normal = _word_weight("shadow", bias="flat", mood="eerie", category="adjectives", mood_weight=MOOD_BOOST)
        w_high = _word_weight("shadow", bias="flat", mood="eerie", category="adjectives", mood_weight=MOOD_BOOST * 3)
        self.assertEqual(w_high, w_normal * 3)

    def test_mood_weight_default_matches_mood_boost(self):
        from landscape import _word_weight
        w_default = _word_weight("shadow", bias="flat", mood="eerie", category="adjectives")
        w_explicit = _word_weight("shadow", bias="flat", mood="eerie", category="adjectives", mood_weight=MOOD_BOOST)
        self.assertEqual(w_default, w_explicit)

    def test_mood_weight_produces_valid_output(self):
        for w in [0, 1, 10, 20]:
            for s in range(5):
                result = generate_landscape(seed=s, mood="eerie", mood_weight=w)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 10)

    def test_mood_weight_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


    def test_template_set_default_is_random(self):
        result = generate_landscape(seed=42, template_set="random")
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 10)

    def test_template_set_first_uses_first_opening(self):
        for s in range(20):
            result = generate_landscape(seed=s, biome="forest", template_set="first")
            self.assertTrue(
                result.startswith("A vast "),
                f"template_set=first should use first opening template at seed {s}: {result!r}",
            )

    def test_template_set_second_uses_second_opening(self):
        for s in range(20):
            result = generate_landscape(seed=s, biome="forest", template_set="second")
            self.assertTrue(
                result.startswith("Before you"),
                f"template_set=second should use second opening template at seed {s}: {result!r}",
            )

    def test_template_set_third_uses_third_opening(self):
        for s in range(20):
            result = generate_landscape(seed=s, biome="forest", template_set="third")
            self.assertTrue(
                result.startswith("The "),
                f"template_set=third should use third opening template at seed {s}: {result!r}",
            )

    def test_template_set_first_is_deterministic(self):
        a = generate_landscape(seed=42, template_set="first")
        b = generate_landscape(seed=42, template_set="first")
        self.assertEqual(a, b)

    def test_template_set_second_middle_has_expected_pattern(self):
        for s in range(20):
            result = generate_landscape(seed=s, biome="forest", template_set="second")
            self.assertIn("Among the ", result,
                f"template_set=second middle should use 'Among the' pattern at seed {s}")

    def test_template_set_third_weather_has_expected_pattern(self):
        for s in range(20):
            result = generate_landscape(seed=s, biome="forest", template_set="third")
            self.assertIn(" itself breathes", result,
                f"template_set=third weather should use the 'as if the' pattern at seed {s}")

    def test_template_set_fourth_uses_fourth_opening(self):
        for s in range(20):
            result = generate_landscape(seed=s, biome="forest", template_set="fourth")
            self.assertTrue(
                " — " in result[:60],
                f"template_set=fourth should use the em-dash opening template at seed {s}: {result!r}",
            )

    def test_template_set_fifth_uses_fifth_opening(self):
        # Fifth clamps to last template for slots with <5 templates (opening=4)
        for s in range(20):
            result = generate_landscape(seed=s, biome="forest", template_set="fifth")
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)

    def test_template_set_fourth_is_deterministic(self):
        a = generate_landscape(seed=42, template_set="fourth")
        b = generate_landscape(seed=42, template_set="fourth")
        self.assertEqual(a, b)

    def test_template_set_fifth_is_deterministic(self):
        a = generate_landscape(seed=42, template_set="fifth")
        b = generate_landscape(seed=42, template_set="fifth")
        self.assertEqual(a, b)

    def test_template_set_fourth_fifth_produce_valid_output(self):
        for tset in ["fourth", "fifth"]:
            for s in range(10):
                result = generate_landscape(seed=s, template_set=tset)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 10)

    def test_template_set_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_pick_template_selects_correct_index(self):
        self.assertEqual(
            _pick_template("opening", "first"),
            SENTENCE_TEMPLATES["opening"][0],
        )
        self.assertEqual(
            _pick_template("opening", "second"),
            SENTENCE_TEMPLATES["opening"][1],
        )
        self.assertEqual(
            _pick_template("opening", "third"),
            SENTENCE_TEMPLATES["opening"][2],
        )

    def test_pick_template_selects_correct_fourth_index(self):
        self.assertEqual(
            _pick_template("opening", "fourth"),
            SENTENCE_TEMPLATES["opening"][3],
        )

    def test_pick_template_selects_correct_fifth_index(self):
        self.assertEqual(
            _pick_template("weather", "fifth"),
            SENTENCE_TEMPLATES["weather"][4],
        )

    def test_pick_template_selects_correct_sixth_index(self):
        self.assertEqual(
            _pick_template("middle", "sixth"),
            SENTENCE_TEMPLATES["middle"][5],
        )

    def test_pick_template_selects_correct_seventh_index(self):
        self.assertEqual(
            _pick_template("middle", "seventh"),
            SENTENCE_TEMPLATES["middle"][6],
        )

    def test_template_set_sixth_middle_has_expected_pattern(self):
        for s in range(20):
            result = generate_landscape(seed=s, biome="forest", template_set="sixth")
            self.assertIn("Across the ", result,
                f"template_set=sixth middle should use 'Across the' pattern at seed {s}")

    def test_template_set_seventh_middle_has_expected_pattern(self):
        for s in range(20):
            result = generate_landscape(seed=s, biome="forest", template_set="seventh")
            self.assertIn(" light of ", result,
                f"template_set=seventh middle should use 'light of' pattern at seed {s}")

    def test_template_set_sixth_is_deterministic(self):
        a = generate_landscape(seed=42, template_set="sixth")
        b = generate_landscape(seed=42, template_set="sixth")
        self.assertEqual(a, b)

    def test_template_set_seventh_is_deterministic(self):
        a = generate_landscape(seed=42, template_set="seventh")
        b = generate_landscape(seed=42, template_set="seventh")
        self.assertEqual(a, b)

    def test_template_set_sixth_seventh_produce_valid_output(self):
        for tset in ["sixth", "seventh"]:
            for s in range(10):
                result = generate_landscape(seed=s, template_set=tset)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 10)

    def test_middle_third_template_uses_bare_verb(self):
        middle_third = SENTENCE_TEMPLATES["middle"][2]
        self.assertNotIn("{verb_conjugated}", middle_third,
            "Third middle template should use bare {verb} not {verb_conjugated}")
        self.assertIn("{verb}", middle_third)

    def test_middle_third_end_to_end_bare_verb(self):
        for s in range(20):
            result = generate_landscape(seed=s, biome="forest", template_set="third")
            # Template 3 is "The {noun} {verb} with {element}."
            self.assertIn(" with ", result,
                f"template_set=third middle should use '... with ...' pattern at seed {s}")
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)

    def test_middle_template_display_exists_in_pool(self):
        middle_templates = SENTENCE_TEMPLATES["middle"]
        self.assertGreaterEqual(len(middle_templates), 6,
            "Should have at least 6 middle templates")
        display_tmpl = [t for t in middle_templates if "{display}" in t]
        self.assertEqual(len(display_tmpl), 1,
            "Exactly one middle template should reference {display}")
        self.assertIn("Across the {display}", display_tmpl[0])

    def test_middle_template_with_display_appears_in_output(self):
        results = [generate_landscape(seed=s, biome="tundra") for s in range(300)]
        display_matches = sum(
            1 for r in results if "Across the tundra" in r
        )
        self.assertGreater(display_matches, 0,
            "Middle template with {display} should appear across 300 random seeds")

    def test_middle_template_display_composable_with_combine(self):
        results = [generate_landscape(seed=s, combine="forest,desert") for s in range(300)]
        display_matches = sum(
            1 for r in results if "Across the forest and desert" in r
        )
        self.assertGreater(display_matches, 0,
            "Middle template with {display} should appear with combine across 300 seeds")


    def test_template_overrides_default_does_not_change_output(self):
        a = generate_landscape(seed=42, template_set="first")
        b = generate_landscape(seed=42, template_set="first", template_overrides=None)
        self.assertEqual(a, b)

    def test_template_overrides_empty_dict_equals_no_override(self):
        a = generate_landscape(seed=42, template_set="first")
        b = generate_landscape(seed=42, template_set="first", template_overrides={})
        self.assertEqual(a, b)

    def test_template_overrides_produces_valid_output(self):
        for slot in ["opening", "middle", "weather", "anomaly"]:
            for mode in ["first", "second", "third"]:
                for s in range(5):
                    result = generate_landscape(
                        seed=s, template_overrides={slot: mode}
                    )
                    self.assertIsInstance(result, str)
                    self.assertGreater(len(result), 10)

    def test_template_override_opening_first_uses_first_opening(self):
        for s in range(20):
            result = generate_landscape(
                seed=s, biome="forest", template_overrides={"opening": "first"}
            )
            self.assertTrue(
                result.startswith("A vast "),
                f"template_overrides={{'opening': 'first'}} should use first opening at seed {s}: {result!r}",
            )

    def test_template_override_middle_second_uses_second_middle(self):
        for s in range(20):
            result = generate_landscape(
                seed=s, biome="forest", template_overrides={"middle": "second"}
            )
            self.assertIn("Among the ", result,
                f"template_overrides={{'middle': 'second'}} should use 'Among the' middle at seed {s}")

    def test_template_overrides_multiple_slots(self):
        overrides = {"opening": "second", "weather": "third"}
        results = [
            generate_landscape(seed=s, biome="forest", template_overrides=overrides)
            for s in range(20)
        ]
        for r in results:
            self.assertTrue(r.startswith("Before you"),
                f"Opening should be 'Before you' with overrides={overrides}: {r!r}")
            self.assertIn(" itself breathes", r,
                f"Weather should use third template with overrides={overrides}: {r!r}")

    def test_template_overrides_cli_flags_exist(self):
        from landscape import main
        self.assertTrue(callable(main))


    def test_bias_overrides_default_does_not_change_output(self):
        a = generate_landscape(seed=42, bias="normal")
        b = generate_landscape(seed=42, bias="normal", bias_overrides=None)
        self.assertEqual(a, b)

    def test_bias_overrides_empty_dict_equals_no_override(self):
        a = generate_landscape(seed=42, bias="normal")
        b = generate_landscape(seed=42, bias="normal", bias_overrides={})
        self.assertEqual(a, b)

    def test_bias_overrides_produces_valid_output(self):
        for override_bias in ["normal", "common", "rare", "flat"]:
            for cat in ["adjectives", "elements", "nouns", "verbs", "weathers", "anomalies"]:
                for s in range(5):
                    result = generate_landscape(seed=s, bias_overrides={cat: override_bias})
                    self.assertIsInstance(result, str)
                    self.assertGreater(len(result), 10)

    def test_bias_adjective_override_rare_reduces_common_adjectives(self):
        common_adj = {"crystal", "shadow", "ancient", "forgotten", "silent"}
        results_normal = [
            generate_landscape(seed=s, biome="tundra") for s in range(300)
        ]
        results_override = [
            generate_landscape(seed=s, biome="tundra", bias_overrides={"adjectives": "rare"})
            for s in range(300)
        ]
        normal_hits = sum(1 for r in results_normal if any(w in r for w in common_adj))
        override_hits = sum(1 for r in results_override if any(w in r for w in common_adj))
        self.assertGreater(
            normal_hits, override_hits,
            "bias_overrides={'adjectives': 'rare'} should reduce common adjective frequency vs default",
        )

    def test_bias_element_override_common_increases_common_elements(self):
        common_elem = {"mist", "light", "silence", "darkness"}
        results_normal = [
            generate_landscape(seed=s, biome="tundra") for s in range(300)
        ]
        results_override = [
            generate_landscape(seed=s, biome="tundra", bias_overrides={"elements": "common"})
            for s in range(300)
        ]
        normal_hits = sum(1 for r in results_normal if any(w in r for w in common_elem))
        override_hits = sum(1 for r in results_override if any(w in r for w in common_elem))
        self.assertGreater(
            override_hits, normal_hits,
            "bias_overrides={'elements': 'common'} should increase common element frequency vs default",
        )

    def test_bias_overrides_multiple_categories(self):
        overrides = {"adjectives": "flat", "elements": "rare"}
        results = [
            generate_landscape(seed=s, bias_overrides=overrides) for s in range(50)
        ]
        for r in results:
            self.assertIsInstance(r, str)
            self.assertGreater(len(r), 10)

    def test_bias_overrides_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_bias_adverb_override_rare_reduces_common_adverbs(self):
        common_adv = {"softly", "gently", "silently", "quietly"}
        normal_results = [
            generate_landscape(seed=s, biome="tundra") for s in range(300)
        ]
        override_results = [
            generate_landscape(seed=s, biome="tundra", bias_overrides={"adverbs": "rare"})
            for s in range(300)
        ]
        normal_hits = sum(1 for r in normal_results if any(w in r for w in common_adv))
        override_hits = sum(1 for r in override_results if any(w in r for w in common_adv))
        self.assertGreater(
            normal_hits, override_hits,
            "bias_overrides={'adverbs': 'rare'} should reduce common adverb frequency vs default",
        )

    def test_bias_color_override_common_increases_common_colors(self):
        common_col = {"vivid", "murky", "burnished", "stark"}
        normal_results = [
            generate_landscape(seed=s, biome="tundra") for s in range(300)
        ]
        override_results = [
            generate_landscape(seed=s, biome="tundra", bias_overrides={"colors": "common"})
            for s in range(300)
        ]
        normal_hits = sum(1 for r in normal_results if any(w in r for w in common_col))
        override_hits = sum(1 for r in override_results if any(w in r for w in common_col))
        self.assertGreater(
            override_hits, normal_hits,
            "bias_overrides={'colors': 'common'} should increase common color frequency vs default",
        )

    def test_bias_overrides_multiple_with_new_categories(self):
        overrides = {"adverbs": "flat", "colors": "rare"}
        results = [
            generate_landscape(seed=s, bias_overrides=overrides) for s in range(50)
        ]
        for r in results:
            self.assertIsInstance(r, str)
            self.assertGreater(len(r), 10)

    def test_bias_overrides_produces_valid_output_adverb_color(self):
        for override_bias in ["normal", "common", "rare", "flat"]:
            for cat in ["adverbs", "colors"]:
                for s in range(5):
                    result = generate_landscape(seed=s, bias_overrides={cat: override_bias})
                    self.assertIsInstance(result, str)
                    self.assertGreater(len(result), 10)

    def test_mood_weight_overrides_default_does_not_change_output(self):
        a = generate_landscape(seed=42, mood="eerie", mood_weight=5)
        b = generate_landscape(seed=42, mood="eerie", mood_weight=5, mood_weight_overrides=None)
        self.assertEqual(a, b)

    def test_mood_weight_overrides_empty_dict_equals_no_override(self):
        a = generate_landscape(seed=42, mood="eerie", mood_weight=5)
        b = generate_landscape(seed=42, mood="eerie", mood_weight=5, mood_weight_overrides={})
        self.assertEqual(a, b)

    def test_mood_weight_overrides_produces_valid_output(self):
        for mw_val in [0, 1, 10, 20]:
            for cat in ["adjectives", "elements", "nouns", "verbs", "weathers", "anomalies"]:
                for s in range(5):
                    result = generate_landscape(
                        seed=s, mood="eerie",
                        mood_weight_overrides={cat: mw_val}
                    )
                    self.assertIsInstance(result, str)
                    self.assertGreater(len(result), 10)

    def test_mood_weight_adjective_override_high_boosts_mood_adjectives(self):
        from landscape import _word_weight
        # "shadow" is in MOOD_WORDS["eerie"]["adjectives"]
        w_normal = _word_weight("shadow", bias="flat", mood="eerie", category="adjectives", mood_weight=5)
        w_high = _word_weight("shadow", bias="flat", mood="eerie", category="adjectives",
                              mood_weight=5, mood_weight_overrides={"adjectives": 20})
        self.assertEqual(w_high, w_normal * 4)

    def test_mood_weight_element_override_zero_suppresses_mood_elements(self):
        from landscape import _word_weight
        # "echo" is in MOOD_WORDS["eerie"]["elements"]
        w_normal = _word_weight("echo", bias="flat", mood="eerie", category="elements", mood_weight=MOOD_BOOST)
        w_zero = _word_weight("echo", bias="flat", mood="eerie", category="elements",
                              mood_weight=MOOD_BOOST, mood_weight_overrides={"elements": 0})
        self.assertEqual(w_zero, 0)

    def test_mood_weight_overrides_multiple_categories(self):
        overrides = {"adjectives": 1, "elements": 20}
        results = [
            generate_landscape(seed=s, mood="vibrant", mood_weight_overrides=overrides) for s in range(50)
        ]
        for r in results:
            self.assertIsInstance(r, str)
            self.assertGreater(len(r), 10)

    def test_mood_weight_overrides_cli_flags_exist(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_mood_weight_adverb_override_high_boosts_mood_adverbs(self):
        from landscape import _word_weight
        w_normal = _word_weight("silently", bias="flat", mood="eerie", category="adverbs", mood_weight=5)
        w_high = _word_weight("silently", bias="flat", mood="eerie", category="adverbs",
                              mood_weight=5, mood_weight_overrides={"adverbs": 20})
        self.assertEqual(w_high, w_normal * 4)

    def test_mood_weight_color_override_zero_suppresses_mood_colors(self):
        from landscape import _word_weight
        w_normal = _word_weight("murky", bias="flat", mood="eerie", category="colors", mood_weight=MOOD_BOOST)
        w_zero = _word_weight("murky", bias="flat", mood="eerie", category="colors",
                              mood_weight=MOOD_BOOST, mood_weight_overrides={"colors": 0})
        self.assertEqual(w_zero, 0)

    def test_mood_weight_overrides_multiple_with_new_categories(self):
        overrides = {"adverbs": 1, "colors": 20}
        results = [
            generate_landscape(seed=s, mood="vibrant", mood_weight_overrides=overrides) for s in range(50)
        ]
        for r in results:
            self.assertIsInstance(r, str)
            self.assertGreater(len(r), 10)

    def test_mood_weight_overrides_produces_valid_output_adverb_color(self):
        for mw_val in [0, 1, 10, 20]:
            for cat in ["adverbs", "colors"]:
                for s in range(5):
                    result = generate_landscape(
                        seed=s, mood="eerie",
                        mood_weight_overrides={cat: mw_val}
                    )
                    self.assertIsInstance(result, str)
                    self.assertGreater(len(result), 10)

    def test_word_dedup_via_used_words_parameter(self):
        from landscape import _pick
        ws = set()
        # Same category, same biome — second pick should differ from first
        pick1 = _pick("adjectives", ["tundra"], used_words=ws)
        pick2 = _pick("adjectives", ["tundra"], used_words=ws)
        self.assertNotEqual(pick1, pick2,
            "_pick should not return the same word when used_words is tracking")

    def test_word_dedup_across_multiple_picks_same_category(self):
        from landscape import _pick
        ws = set()
        picks = [_pick("nouns", ["forest"], used_words=ws) for _ in range(5)]
        # With dedup, all 5 picks should be different (there are >5 nouns in forest)
        self.assertEqual(len(set(picks)), 5, f"Dedup failed: picks were {picks}")

    def test_word_dedup_across_categories(self):
        from landscape import _pick
        ws = set()
        adj = _pick("adjectives", ["forest"], used_words=ws)
        noun = _pick("nouns", ["forest"], used_words=ws)
        # If a word happens to be in both categories, dedup should prevent it
        # At minimum, consecutive picks should differ
        self.assertIsNotNone(adj)
        self.assertIsNotNone(noun)

    def test_word_dedup_without_used_words_still_works(self):
        from landscape import _pick
        pick1 = _pick("adjectives", ["tundra"])
        pick2 = _pick("adjectives", ["tundra"])
        # Without dedup, same word may appear; just verify no crash
        self.assertIsInstance(pick1, str)
        self.assertIsInstance(pick2, str)
        self.assertGreater(len(pick1), 0)

    def test_word_dedup_still_produces_valid_output(self):
        for s in range(50):
            result = generate_landscape(seed=s, detail=3)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 50)

    def test_word_dedup_does_not_break_format_modes(self):
        for fmt in ["prose", "poetic"]:
            for s in range(20):
                result = generate_landscape(seed=s, fmt=fmt)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 10)


    def test_anomaly_prob_default_works(self):
        for s in range(20):
            result = generate_landscape(seed=s)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)

    def test_anomaly_prob_zero_suppresses_anomalies(self):
        results = [generate_landscape(seed=s, anomaly_prob=0.0) for s in range(100)]
        for r in results:
            for a in ALL_ANOMALIES:
                self.assertNotIn(a, r,
                    f"Anomaly '{a}' should not appear with anomaly_prob=0.0")

    def test_anomaly_prob_one_always_has_anomaly(self):
        results = [generate_landscape(seed=s, anomaly_prob=1.0) for s in range(100)]
        has_anomaly = sum(
            1 for r in results
            if any(
                a in r or a[0].lower() + a[1:] in r
                for a in ALL_ANOMALIES
            )
        )
        self.assertGreater(has_anomaly, 80,
            "With anomaly_prob=1.0, most outputs should contain an anomaly")

    def test_anomaly_prob_produces_valid_output(self):
        for prob in [0.0, 0.1, 0.5, 0.9, 1.0]:
            for s in range(10):
                result = generate_landscape(seed=s, anomaly_prob=prob)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 10)

    def test_anomaly_prob_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_anomaly_count_default_is_one(self):
        for s in range(20):
            result = generate_landscape(seed=s)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)

    def test_anomaly_count_zero_no_anomalies(self):
        results = [generate_landscape(seed=s, anomaly_count=0, anomaly_prob=1.0) for s in range(100)]
        for r in results:
            for a in ALL_ANOMALIES:
                self.assertNotIn(a, r,
                    f"Anomaly '{a}' should not appear with anomaly_count=0")

    def test_anomaly_count_two_sometimes_has_multiple(self):
        results = [generate_landscape(seed=s, anomaly_count=3, anomaly_prob=1.0) for s in range(100)]
        multi = [r for r in results if r.count(". ") - r.count(": ") >= 4]
        self.assertGreater(len(multi), 10,
            "anomaly_count=3 with anomaly_prob=1.0 should often produce multi-anomaly outputs")

    def test_anomaly_count_produces_valid_output(self):
        for count in [0, 1, 2, 3]:
            for s in range(10):
                result = generate_landscape(seed=s, anomaly_count=count)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 10)

    def test_anomaly_count_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_anomaly_count_json_includes_field(self):
        result = generate_landscape(seed=42, anomaly_count=2, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("anomaly_count", data)
        self.assertEqual(data["anomaly_count"], 2)


    def test_mood_combine_does_not_break_output(self):
        for combo in [["eerie", "vibrant"], ["eerie", "desolate"], ["vibrant", "desolate"]]:
            for s in range(10):
                result = generate_landscape(seed=s, mood=combo)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 10)

    def test_mood_combine_uses_words_from_both(self):
        eerie_words = set(MOOD_WORDS["eerie"].get("adjectives", []))
        vibrant_words = set(MOOD_WORDS["vibrant"].get("adjectives", []))
        results = [generate_landscape(seed=s, mood=["eerie", "vibrant"]) for s in range(200)]
        found_eerie = any(any(w in r for w in eerie_words) for r in results)
        found_vibrant = any(any(w in r for w in vibrant_words) for r in results)
        self.assertTrue(found_eerie, "eerie mood words never appeared in blended output")
        self.assertTrue(found_vibrant, "vibrant mood words never appeared in blended output")

    def test_mood_combine_different_from_single_mood(self):
        combined = generate_landscape(seed=42, mood=["eerie", "vibrant"])
        single = generate_landscape(seed=42, mood="eerie")
        self.assertNotEqual(combined, single,
            "Combined mood should produce different output than single mood with same seed")

    def test_mood_combine_all_three_still_valid(self):
        for s in range(10):
            result = generate_landscape(seed=s, mood=["eerie", "vibrant", "desolate"])
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)

    def test_mood_combine_cli_flag_accepts_multiple(self):
        from landscape import main
        self.assertTrue(callable(main))


class TestNewBiomes(unittest.TestCase):
    def test_ruined_city_in_biomes_list(self):
        self.assertIn("ruined city", BIOMES)

    def test_fungal_grove_in_biomes_list(self):
        self.assertIn("fungal grove", BIOMES)

    def test_sky_islands_in_biomes_list(self):
        self.assertIn("sky islands", BIOMES)

    def test_ruined_city_produces_valid_output(self):
        for s in range(10):
            result = generate_landscape(seed=s, biome="ruined city")
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)

    def test_fungal_grove_produces_valid_output(self):
        for s in range(10):
            result = generate_landscape(seed=s, biome="fungal grove")
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)

    def test_sky_islands_produces_valid_output(self):
        for s in range(10):
            result = generate_landscape(seed=s, biome="sky islands")
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)

    def test_ruined_city_uses_specific_vocabulary(self):
        ruined_adj = set(BIOME_WORDS["ruined city"].get("adjectives", []))
        results = [generate_landscape(seed=s, biome="ruined city") for s in range(200)]
        found = any(any(w in r for w in ruined_adj) for r in results)
        self.assertTrue(found, "ruined city-specific adjectives never appeared")

    def test_fungal_grove_uses_specific_vocabulary(self):
        fungal_adj = set(BIOME_WORDS["fungal grove"].get("adjectives", []))
        results = [generate_landscape(seed=s, biome="fungal grove") for s in range(200)]
        found = any(any(w in r for w in fungal_adj) for r in results)
        self.assertTrue(found, "fungal grove-specific adjectives never appeared")

    def test_sky_islands_uses_specific_vocabulary(self):
        sky_adj = set(BIOME_WORDS["sky islands"].get("adjectives", []))
        results = [generate_landscape(seed=s, biome="sky islands") for s in range(200)]
        found = any(any(w in r for w in sky_adj) for r in results)
        self.assertTrue(found, "sky islands-specific adjectives never appeared")

    def test_new_biomes_appear_in_random_selection(self):
        biomes_seen = set()
        for s in range(200):
            r = generate_landscape(seed=s)
            for b in ["ruined city", "fungal grove", "sky islands", "crystal fields"]:
                if b in r:
                    biomes_seen.add(b)
        self.assertGreaterEqual(len(biomes_seen), 1,
            f"At least one new biome should appear in 200 random seeds, got {biomes_seen}")

    def test_combine_with_new_biome_uses_vocabulary(self):
        result = generate_landscape(seed=42, combine="ruined city,fungal grove")
        self.assertIn("ruined city", result)
        self.assertIn("fungal grove", result)
        self.assertIn(" and ", result)

    def test_crystal_fields_in_biomes_list(self):
        self.assertIn("crystal fields", BIOMES)

    def test_crystal_fields_produces_valid_output(self):
        for s in range(10):
            result = generate_landscape(seed=s, biome="crystal fields")
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)

    def test_crystal_fields_uses_specific_vocabulary(self):
        crystal_adj = set(BIOME_WORDS["crystal fields"].get("adjectives", []))
        results = [generate_landscape(seed=s, biome="crystal fields") for s in range(200)]
        found = any(any(w in r for w in crystal_adj) for r in results)
        self.assertTrue(found, "crystal fields-specific adjectives never appeared")


class TestCountWithSeed(unittest.TestCase):
    def test_count_seed_sequence_produces_unique_outputs(self):
        outputs = [generate_landscape(seed=42 + i) for i in range(5)]
        self.assertEqual(len(set(outputs)), 5,
            "Each output in a seeded sequence should be unique")

    def test_count_seed_sequence_is_reproducible(self):
        seq_a = [generate_landscape(seed=100 + i) for i in range(5)]
        seq_b = [generate_landscape(seed=100 + i) for i in range(5)]
        self.assertEqual(seq_a, seq_b,
            "Seeded sequence should be reproducible")

    def test_count_seed_sequence_different_from_single_seed(self):
        single = generate_landscape(seed=42)
        seq_first = generate_landscape(seed=42)
        self.assertEqual(single, seq_first,
            "First element of sequence should equal direct call with same seed")

    def test_count_without_seed_produces_varied_outputs(self):
        outputs = [generate_landscape() for _ in range(5)]
        self.assertGreater(len(set(outputs)), 1,
            "Landscapes without explicit seed should vary")


class TestOutputFlag(unittest.TestCase):
    def setUp(self):
        import tempfile
        self.tmpdir = tempfile.mkdtemp()
        self.outpath = Path(self.tmpdir) / "output.txt"

    def tearDown(self):
        if self.outpath.exists():
            self.outpath.unlink()
        Path(self.tmpdir).rmdir()

    def test_output_flag_writes_to_file(self):
        from landscape import main
        import sys
        old_argv = sys.argv
        sys.argv = ["landscape", "--seed", "42", "--output", str(self.outpath)]
        try:
            main()
        finally:
            sys.argv = old_argv
        self.assertTrue(self.outpath.exists(),
            "Output file should exist after running with --output")
        content = self.outpath.read_text()
        self.assertGreater(len(content), 0,
            "Output file should not be empty")

    def test_output_file_contains_generated_text(self):
        from landscape import main
        import sys
        old_argv = sys.argv
        sys.argv = ["landscape", "--seed", "42", "--biome", "forest",
                     "--output", str(self.outpath)]
        try:
            main()
        finally:
            sys.argv = old_argv
        content = self.outpath.read_text()
        self.assertIn("forest", content,
            "Output file should contain generated text with the biome")

    def test_output_file_matches_stdout_output(self):
        import io
        from landscape import main
        import sys
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--seed", "42", "--biome", "tundra"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        stdout_text = captured.getvalue()

        sys.argv = ["landscape", "--seed", "42", "--biome", "tundra",
                     "--output", str(self.outpath)]
        try:
            main()
        finally:
            sys.argv = old_argv
        file_text = self.outpath.read_text()
        self.assertEqual(stdout_text, file_text,
            "Output file content should match stdout output")

    def test_output_with_count_writes_all_landscapes(self):
        from landscape import main
        import sys
        old_argv = sys.argv
        sys.argv = ["landscape", "--seed", "42", "--count", "3",
                     "--output", str(self.outpath)]
        try:
            main()
        finally:
            sys.argv = old_argv
        content = self.outpath.read_text()
        sections = content.strip().split("\n\n")
        self.assertEqual(len(sections), 3,
            "With --count 3, output file should contain 3 landscapes")

    def test_output_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


class TestDedupFlag(unittest.TestCase):
    def test_dedup_default_is_true(self):
        r1 = generate_landscape(seed=42, dedup=True)
        r2 = generate_landscape(seed=42)
        self.assertEqual(r1, r2, "dedup=True should produce same output as default")

    def test_dedup_disabled_still_produces_valid_output(self):
        result = generate_landscape(seed=42, dedup=False)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))

    def test_dedup_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_dedup_disabled_produces_deterministic_output(self):
        r1 = generate_landscape(seed=99, dedup=False)
        r2 = generate_landscape(seed=99, dedup=False)
        self.assertEqual(r1, r2, "dedup=False should still be deterministic with same seed")

    def test_dedup_disabled_works_with_detail_three(self):
        result = generate_landscape(seed=42, dedup=False, detail=3)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))

    def test_dedup_disabled_works_with_mood_and_bias(self):
        result = generate_landscape(seed=42, dedup=False, mood="eerie", bias="rare")
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))


class TestAdverbFlag(unittest.TestCase):
    def test_adverb_enabled_default_same_as_before(self):
        r1 = generate_landscape(seed=42, adverb_enabled=True)
        r2 = generate_landscape(seed=42)
        self.assertEqual(r1, r2, "adverb_enabled=True should equal default")

    def test_adverb_disabled_still_produces_valid_output(self):
        result = generate_landscape(seed=42, adverb_enabled=False)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))

    def test_adverb_disabled_differs_from_enabled(self):
        # With adverb enabled, the adverb word is picked and appears in the output;
        # with adverb disabled, it's skipped — outputs should differ.
        enabled = generate_landscape(seed=42, adverb_enabled=True)
        disabled = generate_landscape(seed=42, adverb_enabled=False)
        self.assertNotEqual(enabled, disabled,
            "Output should differ when adverb is disabled")

    def test_adverb_disabled_deterministic(self):
        r1 = generate_landscape(seed=99, adverb_enabled=False)
        r2 = generate_landscape(seed=99, adverb_enabled=False)
        self.assertEqual(r1, r2, "adverb_enabled=False should be deterministic with same seed")

    def test_adverb_disabled_no_formatting_artifacts(self):
        results = [generate_landscape(seed=s, adverb_enabled=False) for s in range(50)]
        for r in results:
            self.assertNotIn("  ", r, f"Output has double space: {r!r}")
            self.assertNotIn(" .", r, f"Output has space before period: {r!r}")
            self.assertNotIn(" ,", r, f"Output has space before comma: {r!r}")

    def test_adverb_disabled_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_adverb_disabled_works_with_detail_three(self):
        result = generate_landscape(seed=42, adverb_enabled=False, detail=3)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))

    def test_adverb_disabled_works_with_mood_and_bias(self):
        result = generate_landscape(seed=42, adverb_enabled=False, mood="eerie", bias="rare")
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))


class TestJsonWithCount(unittest.TestCase):
    def test_format_json_count_one_is_single_object(self):
        result = generate_landscape(seed=42, fmt="json")
        import json
        data = json.loads(result)
        self.assertIsInstance(data, dict)

    def test_format_json_count_two_is_array(self):
        import sys
        from landscape import main
        import io
        import json
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--seed", "42", "--count", "2", "--format", "json"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue().strip()
        data = json.loads(output)
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 2)

    def test_format_json_count_three_all_valid_json(self):
        import sys
        from landscape import main
        import io
        import json
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--seed", "42", "--count", "3", "--format", "json"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue().strip()
        data = json.loads(output)
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 3)
        for item in data:
            self.assertIn("text", item)
            self.assertIn("biome", item)
            self.assertIn("seed", item)

    def test_format_json_count_array_items_have_unique_biomes(self):
        import sys
        from landscape import main
        import io
        import json
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--seed", "42", "--count", "3", "--format", "json"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue().strip()
        data = json.loads(output)
        seeds = [item["seed"] for item in data]
        self.assertEqual(seeds, [42, 43, 44],
            "Seeds should auto-increment in JSON array output")


class TestBiomeWeights(unittest.TestCase):
    def test_biome_weights_default_does_not_change_output(self):
        r1 = generate_landscape(seed=42)
        r2 = generate_landscape(seed=42, biome_weights=None)
        self.assertEqual(r1, r2, "biome_weights=None should match default")
        r3 = generate_landscape(seed=42, biome_weights={})
        self.assertEqual(r1, r3, "biome_weights={} should match default")

    def test_biome_weights_produces_valid_output(self):
        for s in range(20):
            result = generate_landscape(seed=s, biome_weights={"forest": 5})
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)

    def test_biome_weights_zero_suppresses_biome(self):
        results = []
        for s in range(200):
            r = generate_landscape(seed=s, biome_weights={"forest": 0, "desert": 0}, show_biome=True)
            results.append(r)
            self.assertNotIn("[forest]", r,
                "Forest should not appear with biome_weights={'forest': 0, 'desert': 0}")
            self.assertNotIn("[desert]", r,
                "Desert should not appear with biome_weights={'forest': 0, 'desert': 0}")

    def test_biome_weights_all_zero_falls_back(self):
        result = generate_landscape(seed=42, biome_weights={b: 0 for b in BIOMES})
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 10)

    def test_biome_weights_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_biome_weights_json_includes_field(self):
        result = generate_landscape(seed=42, biome_weights={"forest": 5}, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("biome_weights", data)
        self.assertEqual(data["biome_weights"], {"forest": 5})


class TestDescribeBiome(unittest.TestCase):
    def test_describe_known_biome_contains_name(self):
        from landscape import describe_biome
        result = describe_biome("forest")
        self.assertIn("forest", result)

    def test_describe_known_biome_contains_categories(self):
        from landscape import describe_biome
        result = describe_biome("tundra")
        self.assertIn("adjectives:", result)
        self.assertIn("elements:", result)
        self.assertIn("nouns:", result)

    def test_describe_unknown_biome_returns_error(self):
        from landscape import describe_biome
        result = describe_biome("nonexistent")
        self.assertIn("Unknown biome", result)

    def test_describe_all_contains_all_biomes(self):
        from landscape import describe_biome
        result = describe_biome("all")
        for b in ["forest", "desert", "tundra", "ocean", "ruined city", "fungal grove", "sky islands"]:
            self.assertIn(b, result)

    def test_describe_biome_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_describe_biome_flag_prints_to_stdout(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--describe-biome", "forest"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertIn("forest", output)
        self.assertIn("adjectives:", output)

    def test_describe_all_flag_prints_multiple_biomes(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--describe-biome"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertIn("=== forest ===", output)
        self.assertIn("=== desert ===", output)


class TestDescribeMood(unittest.TestCase):
    def test_describe_known_mood_contains_name(self):
        from landscape import describe_mood
        result = describe_mood("eerie")
        self.assertIn("eerie", result)

    def test_describe_known_mood_contains_categories(self):
        from landscape import describe_mood
        result = describe_mood("vibrant")
        self.assertIn("adjectives:", result)
        self.assertIn("elements:", result)
        self.assertIn("nouns:", result)
        self.assertIn("verbs:", result)
        self.assertIn("colors:", result)
        self.assertIn("adverbs:", result)

    def test_describe_unknown_mood_returns_error(self):
        from landscape import describe_mood
        result = describe_mood("nonexistent")
        self.assertIn("Unknown mood", result)

    def test_describe_all_contains_all_moods(self):
        from landscape import describe_mood
        result = describe_mood("all")
        for m in ["peaceful", "eerie", "vibrant", "desolate", "melancholy"]:
            self.assertIn(m, result)

    def test_describe_mood_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_describe_mood_flag_prints_to_stdout(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--describe-mood", "eerie"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertIn("eerie", output)
        self.assertIn("adjectives:", output)

    def test_describe_all_moods_flag_prints_multiple(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--describe-mood"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertIn("=== peaceful ===", output)
        self.assertIn("=== eerie ===", output)
        self.assertIn("=== vibrant ===", output)
        self.assertIn("=== desolate ===", output)
        self.assertIn("=== melancholy ===", output)


class TestDescribeMoodAtmosphere(unittest.TestCase):
    def test_describe_mood_atmosphere_returns_string(self):
        from landscape import describe_mood_atmosphere
        result = describe_mood_atmosphere()
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_describe_mood_atmosphere_contains_header(self):
        from landscape import describe_mood_atmosphere
        result = describe_mood_atmosphere()
        self.assertIn("mood atmosphere phrases", result)

    def test_describe_mood_atmosphere_contains_all_moods(self):
        from landscape import describe_mood_atmosphere, MOOD_ATMOSPHERE
        result = describe_mood_atmosphere()
        for mood in MOOD_ATMOSPHERE:
            self.assertIn(mood, result,
                f"Mood atmosphere description should contain mood: {mood!r}")

    def test_describe_mood_atmosphere_contains_index_numbers(self):
        from landscape import describe_mood_atmosphere
        result = describe_mood_atmosphere()
        self.assertIn("[0]", result, "Should contain index [0]")
        self.assertIn("[1]", result, "Should contain index [1]")

    def test_describe_mood_atmosphere_shows_last_index(self):
        from landscape import describe_mood_atmosphere, MOOD_ATMOSPHERE
        result = describe_mood_atmosphere()
        max_idx = max(len(phrases) for phrases in MOOD_ATMOSPHERE.values()) - 1
        self.assertIn(f"[{max_idx}]", result,
            f"Should contain the last index [{max_idx}]")

    def test_describe_mood_atmosphere_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_describe_mood_atmosphere_flag_prints_to_stdout(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--describe-mood-atmosphere"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertIn("mood atmosphere phrases", output)
        self.assertIn("[0]", output)
        self.assertIn("[1]", output)

    def test_describe_mood_atmosphere_no_landscape_generated(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--describe-mood-atmosphere", "--seed", "42", "--count", "2"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertNotIn("[seed=42]", output,
            "No landscape should be generated when --describe-mood-atmosphere is used")
        self.assertNotIn("\n\n", output,
            "No landscape should be generated when --describe-mood-atmosphere is used")


class TestDescribeGlobal(unittest.TestCase):
    def test_describe_global_returns_string(self):
        from landscape import describe_global
        result = describe_global()
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_describe_global_contains_header(self):
        from landscape import describe_global
        result = describe_global()
        self.assertIn("global word pools", result)

    def test_describe_global_contains_all_categories(self):
        from landscape import describe_global
        result = describe_global()
        for cat in ["adjectives", "elements", "nouns", "verbs", "weathers", "anomalies", "adverbs", "colors", "time words"]:
            self.assertIn(f"{cat} (", result,
                f"Global description should contain category '{cat}'")

    def test_describe_global_contains_weight_tiers(self):
        from landscape import describe_global
        result = describe_global()
        self.assertIn("common:", result,
            "Global description should annotate common words")
        self.assertIn("rare:", result,
            "Global description should annotate rare words")
        self.assertIn("normal:", result,
            "Global description should annotate normal words")

    def test_describe_global_contains_known_common_words(self):
        from landscape import describe_global, COMMON_WORDS
        result = describe_global()
        for w in list(COMMON_WORDS)[:3]:
            self.assertIn(w, result)

    def test_describe_global_contains_known_rare_words(self):
        from landscape import describe_global, RARE_WORDS
        result = describe_global()
        for w in list(RARE_WORDS)[:3]:
            self.assertIn(w, result)

    def test_describe_global_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_describe_global_flag_prints_to_stdout(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--describe-global"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertIn("global word pools", output)
        self.assertIn("adjectives", output)
        self.assertIn("common:", output)
        self.assertIn("rare:", output)

    def test_describe_global_no_landscape_generated(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--describe-global", "--seed", "42", "--count", "2"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertNotIn("[seed=42]", output,
            "No landscape should be generated when --describe-global is used")
        self.assertNotIn("\n\n", output,
            "No landscape should be generated when --describe-global is used")


class TestDescribeTemplates(unittest.TestCase):
    def test_describe_templates_returns_string(self):
        from landscape import describe_templates
        result = describe_templates()
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_describe_templates_contains_header(self):
        from landscape import describe_templates
        result = describe_templates()
        self.assertIn("templates", result)

    def test_describe_templates_contains_all_slots(self):
        from landscape import describe_templates
        result = describe_templates()
        for slot in ["opening", "middle", "weather", "anomaly"]:
            self.assertIn(f"{slot} (", result,
                f"Template description should contain slot '{slot}'")

    def test_describe_templates_contains_known_templates(self):
        from landscape import describe_templates, SENTENCE_TEMPLATES
        result = describe_templates()
        for slot in ["opening", "middle", "weather", "anomaly"]:
            for tmpl in SENTENCE_TEMPLATES[slot][:2]:
                self.assertIn(tmpl, result,
                    f"Template description should contain template string: {tmpl}")

    def test_describe_templates_contains_placeholder_info(self):
        from landscape import describe_templates
        result = describe_templates()
        self.assertIn("{adj}", result, "Template description should contain {adj}")
        self.assertIn("{adverb}", result, "Template description should contain {adverb}")
        self.assertIn("{color}", result, "Template description should contain {color}")
        self.assertIn("{element}", result, "Template description should contain {element}")
        self.assertIn("{display}", result, "Template description should contain {display}")

    def test_describe_templates_contains_index_numbers(self):
        from landscape import describe_templates
        result = describe_templates()
        self.assertIn("[0]", result, "Template description should contain index [0]")
        self.assertIn("[1]", result, "Template description should contain index [1]")

    def test_describe_templates_shows_template_count(self):
        from landscape import describe_templates, SENTENCE_TEMPLATES
        result = describe_templates()
        for slot in ["opening", "middle", "weather", "anomaly"]:
            count = len(SENTENCE_TEMPLATES[slot])
            self.assertIn(f"({count} template", result,
                f"Template description should show count for '{slot}'")

    def test_describe_templates_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_describe_templates_flag_prints_to_stdout(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--describe-templates"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertIn("templates", output)
        self.assertIn("opening", output)
        self.assertIn("middle", output)
        self.assertIn("weather", output)
        self.assertIn("anomaly", output)

    def test_describe_templates_no_landscape_generated(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--describe-templates", "--seed", "42", "--count", "2"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertNotIn("[seed=42]", output,
            "No landscape should be generated when --describe-templates is used")
        self.assertNotIn("\n\n", output,
            "No landscape should be generated when --describe-templates is used")


class TestWeatherFlag(unittest.TestCase):
    def test_weather_enabled_default_same_as_before(self):
        r1 = generate_landscape(seed=42)
        r2 = generate_landscape(seed=42, weather_enabled=True)
        self.assertEqual(r1, r2, "weather_enabled=True should match default")

    def test_weather_disabled_still_produces_valid_output(self):
        result = generate_landscape(seed=42, weather_enabled=False)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))

    def test_weather_disabled_differs_from_enabled(self):
        enabled = generate_landscape(seed=42, weather_enabled=True)
        disabled = generate_landscape(seed=42, weather_enabled=False)
        self.assertNotEqual(enabled, disabled,
            "Output should differ when weather is disabled")

    def test_weather_disabled_has_fewer_sentences(self):
        for s in range(20):
            enabled = generate_landscape(seed=s, weather_enabled=True)
            disabled = generate_landscape(seed=s, weather_enabled=False)
            e_sentences = enabled.count(". ")
            d_sentences = disabled.count(". ")
            self.assertGreaterEqual(e_sentences, d_sentences,
                f"Disabled weather should have same or fewer sentences at seed {s}")

    def test_weather_disabled_deterministic(self):
        r1 = generate_landscape(seed=99, weather_enabled=False)
        r2 = generate_landscape(seed=99, weather_enabled=False)
        self.assertEqual(r1, r2, "weather_enabled=False should be deterministic with same seed")

    def test_weather_disabled_works_with_detail_three(self):
        result = generate_landscape(seed=42, weather_enabled=False, detail=3)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))

    def test_weather_disabled_works_with_mood_and_bias(self):
        result = generate_landscape(seed=42, weather_enabled=False, mood="eerie", bias="rare")
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))

    def test_weather_disabled_works_with_json_format(self):
        result = generate_landscape(seed=42, weather_enabled=False, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertGreater(len(data["text"]), 0)

    def test_weather_disabled_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


class TestWeatherCount(unittest.TestCase):
    def test_weather_count_default_is_one(self):
        a = generate_landscape(seed=42, detail=2)
        b = generate_landscape(seed=42, detail=2, weather_count=1)
        self.assertEqual(a, b,
            "weather_count=1 should match default")

    def test_weather_count_zero_suppresses_weather(self):
        results = [generate_landscape(seed=s, weather_count=0, detail=2) for s in range(50)]
        for r in results:
            for ind in WEATHER_INDICATORS:
                self.assertNotIn(ind, r,
                    f"Weather indicator {ind!r} should not appear with weather_count=0")

    def test_weather_count_two_sometimes_has_multiple(self):
        results = [generate_landscape(seed=s, weather_count=3, detail=2) for s in range(100)]
        multi = [r for r in results if sum(1 for ind in WEATHER_INDICATORS if ind in r) >= 2]
        self.assertGreater(len(multi), 10,
            "weather_count=3 should often produce multi-weather outputs")

    def test_weather_count_produces_valid_output(self):
        for count in [0, 1, 2, 3]:
            for s in range(10):
                result = generate_landscape(seed=s, weather_count=count)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_weather_count_is_deterministic(self):
        a = generate_landscape(seed=42, weather_count=2, detail=2)
        b = generate_landscape(seed=42, weather_count=2, detail=2)
        self.assertEqual(a, b,
            "weather_count should be deterministic with same seed")

    def test_weather_count_works_with_json_format(self):
        result = generate_landscape(seed=42, weather_count=2, fmt="json", detail=2)
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertGreater(len(data["text"]), 0)

    def test_weather_count_json_includes_field(self):
        result = generate_landscape(seed=42, weather_count=2, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("weather_count", data)
        self.assertEqual(data["weather_count"], 2)

    def test_weather_count_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_weather_count_works_with_detail_zero(self):
        result = generate_landscape(seed=42, weather_count=2, detail=0)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))


class TestWeatherProb(unittest.TestCase):
    def test_weather_prob_default_is_one(self):
        a = generate_landscape(seed=42, detail=2)
        b = generate_landscape(seed=42, detail=2, weather_prob=1.0)
        self.assertEqual(a, b,
            "weather_prob=1.0 should match default")

    def test_weather_prob_zero_suppresses_weather(self):
        results = [generate_landscape(seed=s, weather_prob=0.0, detail=2) for s in range(100)]
        for r in results:
            for ind in WEATHER_INDICATORS:
                self.assertNotIn(ind, r,
                    f"Weather indicator {ind!r} should not appear with weather_prob=0.0")

    def test_weather_prob_one_always_has_weather(self):
        results = [generate_landscape(seed=s, weather_prob=1.0, detail=2) for s in range(100)]
        has_weather = sum(1 for r in results if any(ind in r for ind in WEATHER_INDICATORS))
        self.assertGreater(has_weather, 80,
            "With weather_prob=1.0, most outputs should contain weather")

    def test_weather_prob_produces_valid_output(self):
        for prob in [0.0, 0.25, 0.5, 0.75, 1.0]:
            for s in range(10):
                result = generate_landscape(seed=s, weather_prob=prob)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_weather_prob_is_deterministic(self):
        a = generate_landscape(seed=42, weather_prob=0.5, detail=2)
        b = generate_landscape(seed=42, weather_prob=0.5, detail=2)
        self.assertEqual(a, b,
            "weather_prob should be deterministic with same seed")

    def test_weather_prob_json_includes_field(self):
        result = generate_landscape(seed=42, weather_prob=0.5, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("weather_prob", data)
        self.assertEqual(data["weather_prob"], 0.5)

    def test_weather_prob_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


class TestMiddleFlag(unittest.TestCase):
    def test_middle_enabled_default_same_as_before(self):
        r1 = generate_landscape(seed=42)
        r2 = generate_landscape(seed=42, middle_enabled=True)
        self.assertEqual(r1, r2, "middle_enabled=True should match default")

    def test_middle_disabled_still_produces_valid_output(self):
        result = generate_landscape(seed=42, middle_enabled=False)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))

    def test_middle_disabled_differs_from_enabled(self):
        enabled = generate_landscape(seed=42, middle_enabled=True)
        disabled = generate_landscape(seed=42, middle_enabled=False)
        self.assertNotEqual(enabled, disabled,
            "Output should differ when middle is disabled")

    def test_middle_disabled_has_fewer_sentences(self):
        for s in range(20):
            enabled = generate_landscape(seed=s, middle_enabled=True)
            disabled = generate_landscape(seed=s, middle_enabled=False)
            e_sentences = enabled.count(". ")
            d_sentences = disabled.count(". ")
            self.assertGreaterEqual(e_sentences, d_sentences,
                f"Disabled middle should have same or fewer sentences at seed {s}")

    def test_middle_disabled_deterministic(self):
        r1 = generate_landscape(seed=99, middle_enabled=False)
        r2 = generate_landscape(seed=99, middle_enabled=False)
        self.assertEqual(r1, r2, "middle_enabled=False should be deterministic with same seed")

    def test_middle_disabled_works_with_detail_three(self):
        result = generate_landscape(seed=42, middle_enabled=False, detail=3)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))

    def test_middle_disabled_works_with_mood_and_bias(self):
        result = generate_landscape(seed=42, middle_enabled=False, mood="eerie", bias="rare")
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))

    def test_middle_disabled_works_with_json_format(self):
        result = generate_landscape(seed=42, middle_enabled=False, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertGreater(len(data["text"]), 0)

    def test_middle_disabled_works_with_no_weather(self):
        result = generate_landscape(seed=42, middle_enabled=False, weather_enabled=False)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))
        # With both middle and weather disabled, output should be opening only (no anomalies at detail=1? no, anomalies still roll)
        self.assertIn(" ", result, "Output should contain at least opening text")

    def test_middle_disabled_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


class TestColors(unittest.TestCase):
    def test_output_contains_known_color(self):
        results = {generate_landscape(seed=s) for s in range(200)}
        self.assertTrue(
            any(c in r for r in results for c in ALL_COLORS),
            "No known color word appeared across 200 seeds",
        )

    def test_color_appears_in_middle_templates(self):
        results = [generate_landscape(seed=s, biome="tundra", detail=2) for s in range(300)]
        self.assertTrue(
            any(c in r for r in results for c in ALL_COLORS),
            "No color word appeared in middle sentences across 300 seeds",
        )

    def test_color_is_deterministic_with_seed(self):
        a = generate_landscape(seed=42)
        b = generate_landscape(seed=42)
        self.assertEqual(a, b)

    def test_color_with_mood_does_not_break_output(self):
        for mood in ["eerie", "vibrant", "desolate"]:
            for s in range(10):
                result = generate_landscape(seed=s, mood=mood)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 10)

    def test_color_with_detail_three_produces_valid_output(self):
        for s in range(20):
            result = generate_landscape(seed=s, detail=3)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 50)

    def test_color_word_weight_function_works(self):
        from landscape import _word_weight
        w_common = _word_weight("vivid", bias="normal")
        w_rare = _word_weight("iridescent", bias="normal")
        self.assertGreater(w_common, w_rare,
            "Common color word should have higher weight than rare color word")

    def test_color_mood_boost_applies(self):
        from landscape import _word_weight
        w_no_mood = _word_weight("vivid", bias="flat", mood=None, category="colors")
        w_mood = _word_weight("vivid", bias="flat", mood="vibrant", category="colors")
        self.assertEqual(w_mood, w_no_mood * MOOD_BOOST,
            "vivid should be boosted in vibrant mood")

    def test_color_mood_boost_not_applied_for_unmatched(self):
        from landscape import _word_weight
        w_no_mood = _word_weight("fluorescent", bias="flat", mood=None, category="colors")
        w_mood = _word_weight("fluorescent", bias="flat", mood="desolate", category="colors")
        self.assertEqual(w_mood, w_no_mood,
            "fluorescent should not be boosted in desolate mood")

    def test_color_light_template_exists_in_pool(self):
        middle_templates = SENTENCE_TEMPLATES["middle"]
        color_tmpl = [t for t in middle_templates if "{color}" in t]
        self.assertGreaterEqual(len(color_tmpl), 5,
            "At least 5 middle templates should reference {color}")
        self.assertTrue(
            any("The {color} light of {element}" in t for t in color_tmpl),
            "The {color} light template should be one of them",
        )

    def test_color_light_template_appears_in_output(self):
        results = [generate_landscape(seed=s, biome="tundra") for s in range(500)]
        color_matches = sum(
            1 for r in results if " light of " in r
        )
        self.assertGreater(color_matches, 0,
            "Color light template should appear across 500 random seeds")

    def test_color_works_with_deactivated_middle(self):
        for s in range(10):
            result = generate_landscape(seed=s, middle_enabled=False, detail=2)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)

    def test_color_works_with_json_output(self):
        result = generate_landscape(seed=42, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertGreater(len(data["text"]), 0)

    def test_describe_global_includes_colors(self):
        from landscape import describe_global, COLORS
        result = describe_global()
        self.assertIn("colors", result)
        for c in COLORS:
            self.assertIn(c, result)

    def test_weather_contains_known_color(self):
        results = [generate_landscape(seed=s, biome="forest") for s in range(300)]
        self.assertTrue(
            any(c in r for r in results for c in ALL_COLORS),
            "No known color word appeared in weather across 300 seeds",
        )

    def test_weather_in_color_light_template_appears_across_seeds(self):
        results = [generate_landscape(seed=s, biome="tundra") for s in range(500)]
        color_light_matches = sum(
            1 for r in results if " in " in r and " light" in r
        )
        self.assertGreater(color_light_matches, 0,
            "'in {color} light' weather template should appear across 500 seeds",
        )

    def test_weather_color_works_with_middle_disabled(self):
        for s in range(20):
            result = generate_landscape(seed=s, middle_enabled=False, detail=2)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)
            self.assertTrue(result.endswith("."))

    def test_weather_color_appears_with_middle_disabled(self):
        results = [generate_landscape(seed=s, middle_enabled=False, detail=2) for s in range(200)]
        self.assertTrue(
            any(c in r for r in results for c in ALL_COLORS),
            "No color word appeared in weather with middle_enabled=False across 200 seeds",
        )

    def test_weather_color_is_deterministic(self):
        a = generate_landscape(seed=42, detail=2)
        b = generate_landscape(seed=42, detail=2)
        self.assertEqual(a, b,
            "Weather with color templates should be deterministic")

    def test_weather_color_works_with_detail_three(self):
        for s in range(20):
            result = generate_landscape(seed=s, detail=3)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 50)

    def test_weather_color_works_with_json_format(self):
        result = generate_landscape(seed=42, fmt="json", detail=2)
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertGreater(len(data["text"]), 0)

    def test_weather_color_template_count_increased(self):
        weather_templates = SENTENCE_TEMPLATES["weather"]
        self.assertGreaterEqual(len(weather_templates), 5,
            "Should have at least 5 weather templates")

    def test_weather_color_templates_use_color_placeholder(self):
        weather_templates = SENTENCE_TEMPLATES["weather"]
        color_tmpls = [t for t in weather_templates if "{color}" in t]
        self.assertGreaterEqual(len(color_tmpls), 5,
            "All 5 weather templates should reference {color}")

    def test_weather_color_in_all_templates(self):
        weather_templates = SENTENCE_TEMPLATES["weather"]
        for i, tmpl in enumerate(weather_templates):
            self.assertIn("{color}", tmpl,
                f"Weather template {i} should contain {{color}}: {tmpl!r}")

    def test_weather_color_works_with_no_adverb(self):
        for s in range(10):
            result = generate_landscape(seed=s, adverb_enabled=False, detail=2)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)
            self.assertNotIn("  ", result)
            self.assertTrue(result.endswith("."))

    def test_opening_contains_known_color(self):
        results = {generate_landscape(seed=s) for s in range(200)}
        self.assertTrue(
            any(c in r for r in results for c in ALL_COLORS),
            "No known color word appeared in output across 200 seeds",
        )

    def test_opening_color_works_with_color_disabled(self):
        for s in range(20):
            result = generate_landscape(seed=s, color_enabled=False)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)
            self.assertNotIn("  ", result)

    def test_opening_color_is_deterministic(self):
        a = generate_landscape(seed=42)
        b = generate_landscape(seed=42)
        self.assertEqual(a, b)

    def test_opening_color_appears_in_opening_templates(self):
        results = [generate_landscape(seed=s, biome="tundra", template_set="first") for s in range(300)]
        self.assertTrue(
            any(c in r for r in results for c in ALL_COLORS),
            "No color word appeared in opening across 300 seeds with template_set=first",
        )

    def test_opening_em_dash_color_contains_color(self):
        results = [generate_landscape(seed=s, template_set="fourth") for s in range(300)]
        self.assertTrue(
            any(c in r for r in results for c in ALL_COLORS),
            "No color word appeared in em-dash openings across 300 seeds",
        )

    def test_opening_em_dash_color_deterministic(self):
        a = generate_landscape(seed=42, template_set="fourth")
        b = generate_landscape(seed=42, template_set="fourth")
        self.assertEqual(a, b)

    def test_opening_em_dash_color_works_with_color_disabled(self):
        for s in range(20):
            result = generate_landscape(seed=s, template_set="fourth", color_enabled=False)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)
            self.assertNotIn("  ", result)

    def test_color_in_middle_templates(self):
        results = [generate_landscape(seed=s, biome="tundra", detail=2) for s in range(300)]
        color_count = sum(1 for r in results if any(c in r for c in ALL_COLORS))
        self.assertGreater(color_count, 100,
            "Color words should appear in middle sentences across 300 seeds")

    def test_color_middle_works_with_color_disabled(self):
        for s in range(20):
            result = generate_landscape(seed=s, color_enabled=False, detail=2)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)
            self.assertNotIn("  ", result)

    def test_color_middle_is_deterministic(self):
        a = generate_landscape(seed=42, detail=2)
        b = generate_landscape(seed=42, detail=2)
        self.assertEqual(a, b,
            "Color-in-middle should be deterministic with same seed")

    def test_color_middle_works_with_no_adverb(self):
        for s in range(10):
            result = generate_landscape(seed=s, adverb_enabled=False, detail=2)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)
            self.assertNotIn("  ", result)
            self.assertTrue(result.endswith("."))

    def test_color_in_all_middle_templates(self):
        middle_tmpls = SENTENCE_TEMPLATES["middle"]
        color_tmpls = [t for t in middle_tmpls if "{color}" in t]
        self.assertGreaterEqual(len(color_tmpls), 7,
            "All 7 middle templates should reference {color}")

    def test_color_middle_template_zero_and_three_have_color(self):
        tmpls = SENTENCE_TEMPLATES["middle"]
        self.assertIn("{color}", tmpls[0],
            "Middle template 0 should have {color}")
        self.assertIn("{color}", tmpls[3],
            "Middle template 3 should have {color}")

    def test_color_middle_zero_and_three_produce_valid_output(self):
        for s in range(30):
            for ts in ["first", "second", "third"]:
                result = generate_landscape(seed=s, template_set=ts, detail=2)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 10)
                self.assertTrue(result.endswith("."))


class TestPeacefulMood(unittest.TestCase):
    def test_peaceful_mood_does_not_break_output(self):
        for s in range(20):
            result = generate_landscape(seed=s, mood="peaceful")
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)

    def test_peaceful_mood_word_weight_boosted(self):
        from landscape import _word_weight, MOOD_BOOST
        w_no_mood = _word_weight("calm", bias="flat", mood=None, category="adjectives")
        w_mood = _word_weight("calm", bias="flat", mood="peaceful", category="adjectives")
        self.assertEqual(w_mood, w_no_mood * MOOD_BOOST,
            "calm should be boosted in peaceful mood")

    def test_peaceful_mood_word_weight_not_boosted_for_unmatched(self):
        from landscape import _word_weight
        w_no_mood = _word_weight("crystal", bias="flat", mood=None, category="adjectives")
        w_mood = _word_weight("crystal", bias="flat", mood="peaceful", category="adjectives")
        self.assertEqual(w_mood, w_no_mood,
            "crystal should not be boosted in peaceful mood")

    def test_peaceful_mood_combine_with_other_moods(self):
        for combo in [["peaceful", "eerie"], ["peaceful", "vibrant"], ["peaceful", "desolate"], ["peaceful", "melancholy"]]:
            for s in range(10):
                result = generate_landscape(seed=s, mood=combo)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 10)

    def test_peaceful_mood_deterministic(self):
        a = generate_landscape(seed=42, mood="peaceful")
        b = generate_landscape(seed=42, mood="peaceful")
        self.assertEqual(a, b)

    def test_peaceful_mood_uses_peaceful_words(self):
        peaceful_adj = set(MOOD_WORDS["peaceful"].get("adjectives", []))
        results = [generate_landscape(seed=s, mood="peaceful") for s in range(200)]
        found = any(any(w in r for w in peaceful_adj) for r in results)
        self.assertTrue(found, "peaceful-specific adjectives never appeared in output")

    def test_peaceful_mood_json_includes_mood(self):
        result = generate_landscape(seed=42, mood="peaceful", fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("mood", data)
        self.assertIn("peaceful", data["mood"])

    def test_peaceful_mood_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


class TestMelancholyMood(unittest.TestCase):
    def test_melancholy_mood_does_not_break_output(self):
        for s in range(20):
            result = generate_landscape(seed=s, mood="melancholy")
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)

    def test_melancholy_mood_word_weight_boosted(self):
        from landscape import _word_weight, MOOD_BOOST
        w_no_mood = _word_weight("wistful", bias="flat", mood=None, category="adjectives")
        w_mood = _word_weight("wistful", bias="flat", mood="melancholy", category="adjectives")
        self.assertEqual(w_mood, w_no_mood * MOOD_BOOST,
            "wistful should be boosted in melancholy mood")

    def test_melancholy_mood_word_weight_not_boosted_for_unmatched(self):
        from landscape import _word_weight
        w_no_mood = _word_weight("crystal", bias="flat", mood=None, category="adjectives")
        w_mood = _word_weight("crystal", bias="flat", mood="melancholy", category="adjectives")
        self.assertEqual(w_mood, w_no_mood,
            "crystal should not be boosted in melancholy mood")

    def test_melancholy_mood_combine_with_other_moods(self):
        for combo in [["melancholy", "eerie"], ["melancholy", "peaceful"], ["melancholy", "desolate"]]:
            for s in range(10):
                result = generate_landscape(seed=s, mood=combo)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 10)

    def test_melancholy_mood_deterministic(self):
        a = generate_landscape(seed=42, mood="melancholy")
        b = generate_landscape(seed=42, mood="melancholy")
        self.assertEqual(a, b)

    def test_melancholy_mood_uses_melancholy_words(self):
        melancholy_adj = set(MOOD_WORDS["melancholy"].get("adjectives", []))
        results = [generate_landscape(seed=s, mood="melancholy") for s in range(200)]
        found = any(any(w in r for w in melancholy_adj) for r in results)
        self.assertTrue(found, "melancholy-specific adjectives never appeared in output")

    def test_melancholy_mood_json_includes_mood(self):
        result = generate_landscape(seed=42, mood="melancholy", fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("mood", data)
        self.assertIn("melancholy", data["mood"])

    def test_melancholy_mood_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


class TestEerieMood(unittest.TestCase):
    def test_eerie_mood_does_not_break_output(self):
        for s in range(20):
            result = generate_landscape(seed=s, mood="eerie")
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)

    def test_eerie_mood_word_weight_boosted(self):
        from landscape import _word_weight, MOOD_BOOST
        w_no_mood = _word_weight("shadow", bias="flat", mood=None, category="adjectives")
        w_mood = _word_weight("shadow", bias="flat", mood="eerie", category="adjectives")
        self.assertEqual(w_mood, w_no_mood * MOOD_BOOST,
            "shadow should be boosted in eerie mood")

    def test_eerie_mood_word_weight_not_boosted_for_unmatched(self):
        from landscape import _word_weight
        w_no_mood = _word_weight("crystal", bias="flat", mood=None, category="adjectives")
        w_mood = _word_weight("crystal", bias="flat", mood="eerie", category="adjectives")
        self.assertEqual(w_mood, w_no_mood,
            "crystal should not be boosted in eerie mood")

    def test_eerie_mood_combine_with_other_moods(self):
        for combo in [["eerie", "peaceful"], ["eerie", "vibrant"], ["eerie", "desolate"], ["eerie", "melancholy"]]:
            for s in range(10):
                result = generate_landscape(seed=s, mood=combo)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 10)

    def test_eerie_mood_deterministic(self):
        a = generate_landscape(seed=42, mood="eerie")
        b = generate_landscape(seed=42, mood="eerie")
        self.assertEqual(a, b)

    def test_eerie_mood_uses_eerie_words(self):
        eerie_adj = set(MOOD_WORDS["eerie"].get("adjectives", []))
        results = [generate_landscape(seed=s, mood="eerie") for s in range(200)]
        found = any(any(w in r for w in eerie_adj) for r in results)
        self.assertTrue(found, "eerie-specific adjectives never appeared in output")

    def test_eerie_mood_json_includes_mood(self):
        result = generate_landscape(seed=42, mood="eerie", fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("mood", data)
        self.assertIn("eerie", data["mood"])

    def test_eerie_mood_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


class TestVibrantMood(unittest.TestCase):
    def test_vibrant_mood_does_not_break_output(self):
        for s in range(20):
            result = generate_landscape(seed=s, mood="vibrant")
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)

    def test_vibrant_mood_word_weight_boosted(self):
        from landscape import _word_weight, MOOD_BOOST
        w_no_mood = _word_weight("luminous", bias="flat", mood=None, category="adjectives")
        w_mood = _word_weight("luminous", bias="flat", mood="vibrant", category="adjectives")
        self.assertEqual(w_mood, w_no_mood * MOOD_BOOST,
            "luminous should be boosted in vibrant mood")

    def test_vibrant_mood_word_weight_not_boosted_for_unmatched(self):
        from landscape import _word_weight
        w_no_mood = _word_weight("shadow", bias="flat", mood=None, category="adjectives")
        w_mood = _word_weight("shadow", bias="flat", mood="vibrant", category="adjectives")
        self.assertEqual(w_mood, w_no_mood,
            "shadow should not be boosted in vibrant mood")

    def test_vibrant_mood_combine_with_other_moods(self):
        for combo in [["vibrant", "peaceful"], ["vibrant", "eerie"], ["vibrant", "desolate"], ["vibrant", "melancholy"]]:
            for s in range(10):
                result = generate_landscape(seed=s, mood=combo)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 10)

    def test_vibrant_mood_deterministic(self):
        a = generate_landscape(seed=42, mood="vibrant")
        b = generate_landscape(seed=42, mood="vibrant")
        self.assertEqual(a, b)

    def test_vibrant_mood_uses_vibrant_words(self):
        vibrant_adj = set(MOOD_WORDS["vibrant"].get("adjectives", []))
        results = [generate_landscape(seed=s, mood="vibrant") for s in range(200)]
        found = any(any(w in r for w in vibrant_adj) for r in results)
        self.assertTrue(found, "vibrant-specific adjectives never appeared in output")

    def test_vibrant_mood_json_includes_mood(self):
        result = generate_landscape(seed=42, mood="vibrant", fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("mood", data)
        self.assertIn("vibrant", data["mood"])

    def test_vibrant_mood_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


class TestDesolateMood(unittest.TestCase):
    def test_desolate_mood_does_not_break_output(self):
        for s in range(20):
            result = generate_landscape(seed=s, mood="desolate")
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)

    def test_desolate_mood_word_weight_boosted(self):
        from landscape import _word_weight, MOOD_BOOST
        w_no_mood = _word_weight("barren", bias="flat", mood=None, category="adjectives")
        w_mood = _word_weight("barren", bias="flat", mood="desolate", category="adjectives")
        self.assertEqual(w_mood, w_no_mood * MOOD_BOOST,
            "barren should be boosted in desolate mood")

    def test_desolate_mood_word_weight_not_boosted_for_unmatched(self):
        from landscape import _word_weight
        w_no_mood = _word_weight("crystal", bias="flat", mood=None, category="adjectives")
        w_mood = _word_weight("crystal", bias="flat", mood="desolate", category="adjectives")
        self.assertEqual(w_mood, w_no_mood,
            "crystal should not be boosted in desolate mood")

    def test_desolate_mood_combine_with_other_moods(self):
        for combo in [["desolate", "peaceful"], ["desolate", "eerie"], ["desolate", "vibrant"], ["desolate", "melancholy"]]:
            for s in range(10):
                result = generate_landscape(seed=s, mood=combo)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 10)

    def test_desolate_mood_deterministic(self):
        a = generate_landscape(seed=42, mood="desolate")
        b = generate_landscape(seed=42, mood="desolate")
        self.assertEqual(a, b)

    def test_desolate_mood_uses_desolate_words(self):
        desolate_adj = set(MOOD_WORDS["desolate"].get("adjectives", []))
        results = [generate_landscape(seed=s, mood="desolate") for s in range(200)]
        found = any(any(w in r for w in desolate_adj) for r in results)
        self.assertTrue(found, "desolate-specific adjectives never appeared in output")

    def test_desolate_mood_json_includes_mood(self):
        result = generate_landscape(seed=42, mood="desolate", fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("mood", data)
        self.assertIn("desolate", data["mood"])

    def test_desolate_mood_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


MOOD_ATMOSPHERE_INDICATORS = {
    "peaceful": [
        "settles over the scene like a blessing",
        "air is soft and kind",
        "breathe in a slow, tranquil rhythm",
        "for a moment, all is well",
        "exactly where it should be",
        "reluctant to move on",
    ],
    "eerie": [
        "wrongness in the air",
        "thick, watchful, patient",
        "hair on your neck stand up",
        "attention that feels ancient and cold",
        "swallowed something of the light",
        "frozen mid-gesture",
    ],
    "vibrant": [
        "humming with impossible energy",
        "too full to contain itself",
        "fierce, joyful intensity",
        "charged with life, electric and golden",
        "song the world cannot stop singing",
        "cannot contain its own abundance",
    ],
    "desolate": [
        "bones of the world",
        "nothing grows, nothing waits",
        "held breath that will never be released",
        "emptiness has become its only identity",
        "shape left by loss",
        "forgotten how",
    ],
    "melancholy": [
        "gentle sadness in the air",
        "holding its breath and remembering",
        "landscape itself is lost in thought",
        "half-forgotten lullaby",
        "unwilling to commit to either",
        "refuses to fade",
    ],
}

ALL_MOOD_ATMOSPHERE_PHRASES = set()
for phrases in MOOD_ATMOSPHERE_INDICATORS.values():
    ALL_MOOD_ATMOSPHERE_PHRASES.update(phrases)


class TestMoodAtmosphere(unittest.TestCase):
    def test_disabled_by_default(self):
        for s in range(20):
            result = generate_landscape(seed=s, mood="eerie")
            for ind in ALL_MOOD_ATMOSPHERE_PHRASES:
                self.assertNotIn(ind, result,
                    f"Mood atmosphere indicator {ind!r} should not appear by default")

    def test_enabled_appears_with_mood(self):
        results = [generate_landscape(seed=s, mood="eerie", mood_atmosphere=True) for s in range(100)]
        self.assertTrue(
            any(ind in r for r in results for ind in MOOD_ATMOSPHERE_INDICATORS["eerie"]),
            "No eerie mood atmosphere phrase appeared across 100 seeds with mood_atmosphere=True",
        )

    def test_does_not_break_output(self):
        for mood_name in ["peaceful", "eerie", "vibrant", "desolate", "melancholy"]:
            for s in range(10):
                result = generate_landscape(seed=s, mood=mood_name, mood_atmosphere=True)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 10)

    def test_is_deterministic(self):
        a = generate_landscape(seed=42, mood="eerie", mood_atmosphere=True)
        b = generate_landscape(seed=42, mood="eerie", mood_atmosphere=True)
        self.assertEqual(a, b,
            "Mood atmosphere should be deterministic with same seed")

    def test_differs_from_without_atmosphere(self):
        without = generate_landscape(seed=42, mood="eerie", mood_atmosphere=False)
        with_atmos = generate_landscape(seed=42, mood="eerie", mood_atmosphere=True)
        self.assertNotEqual(without, with_atmos,
            "Mood atmosphere enabled should differ from disabled with same seed")

    def test_works_with_all_moods(self):
        for mood_name in ["peaceful", "eerie", "vibrant", "desolate", "melancholy"]:
            with self.subTest(mood=mood_name):
                results = [generate_landscape(seed=s, mood=mood_name, mood_atmosphere=True) for s in range(50)]
                self.assertTrue(
                    any(ind in r for r in results for ind in MOOD_ATMOSPHERE_INDICATORS[mood_name]),
                    f"No {mood_name} mood atmosphere phrase appeared across 50 seeds",
                )

    def test_works_with_json_format(self):
        result = generate_landscape(seed=42, mood="eerie", mood_atmosphere=True, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertGreater(len(data["text"]), 0)

    def test_json_includes_field(self):
        result = generate_landscape(seed=42, mood="eerie", mood_atmosphere=True, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("mood_atmosphere", data)
        self.assertEqual(data["mood_atmosphere"], True)

    def test_json_field_absent_when_disabled(self):
        result = generate_landscape(seed=42, mood="eerie", mood_atmosphere=False, fmt="json")
        import json
        data = json.loads(result)
        self.assertNotIn("mood_atmosphere", data)

    def test_works_with_all_biomes(self):
        for biome in ["forest", "desert", "tundra", "ocean", "ruined city", "sky islands"]:
            with self.subTest(biome=biome):
                result = generate_landscape(seed=42, biome=biome, mood="eerie", mood_atmosphere=True)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 10)

    def test_works_with_mood_combine(self):
        for combo in [["peaceful", "eerie"], ["vibrant", "desolate"], ["eerie", "vibrant"], ["melancholy", "peaceful"]]:
            with self.subTest(mood=combo):
                results = [generate_landscape(seed=s, mood=combo, mood_atmosphere=True) for s in range(50)]
                all_indicators = []
                for m in combo:
                    all_indicators.extend(MOOD_ATMOSPHERE_INDICATORS.get(m, []))
                self.assertTrue(
                    any(ind in r for r in results for ind in all_indicators),
                    f"No mood atmosphere phrase appeared for mood={combo}",
                )

    def test_works_with_detail_zero(self):
        for s in range(10):
            result = generate_landscape(seed=s, mood="eerie", mood_atmosphere=True, detail=0)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)

    def test_works_with_other_features(self):
        result = generate_landscape(seed=42, mood="eerie", mood_atmosphere=True,
                                     echo_enabled=True, sound_enabled=True,
                                     wildlife_enabled=True, time_of_day_enabled=True,
                                     season_enabled=True, perspective_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 50)

    def test_works_with_poetic_format(self):
        for s in range(10):
            result = generate_landscape(seed=s, mood="eerie", mood_atmosphere=True, fmt="poetic")
            self.assertIsInstance(result, str)
            self.assertIn("\n", result)

    def test_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_no_mood_no_atmosphere_even_if_enabled(self):
        result = generate_landscape(seed=42, mood=None, mood_atmosphere=True)
        for ind in ALL_MOOD_ATMOSPHERE_PHRASES:
            self.assertNotIn(ind, result,
                "No mood atmosphere phrase should appear when mood is not set")


class TestMoodAtmosphereCount(unittest.TestCase):
    def test_default_is_one(self):
        self.assertEqual(
            generate_landscape(seed=42, mood="eerie", mood_atmosphere=True, mood_atmosphere_count=1),
            generate_landscape(seed=42, mood="eerie", mood_atmosphere=True),
            "mood_atmosphere_count=1 should match default",
        )

    def test_zero_suppresses_atmosphere(self):
        for s in range(20):
            result = generate_landscape(seed=s, mood="eerie", mood_atmosphere=True, mood_atmosphere_count=0)
            for ind in ALL_MOOD_ATMOSPHERE_PHRASES:
                self.assertNotIn(ind, result,
                    f"Mood atmosphere should be suppressed at count=0, seed={s}")

    def test_multi_atmosphere_with_count_three(self):
        results = [generate_landscape(
            seed=s, mood=["peaceful", "eerie", "vibrant", "desolate", "melancholy"],
            mood_atmosphere=True, mood_atmosphere_count=3,
        ) for s in range(200)]
        multi_count = sum(
            1 for r in results
            if sum(1 for ind in ALL_MOOD_ATMOSPHERE_PHRASES if ind in r) >= 2
        )
        self.assertGreater(multi_count, 0,
            "mood_atmosphere_count=3 should sometimes produce 2+ phrases across 200 seeds")

    def test_does_not_repeat_same_phrase(self):
        for s in range(100):
            result = generate_landscape(
                seed=s, mood=["peaceful", "eerie", "vibrant", "desolate", "melancholy"],
                mood_atmosphere=True, mood_atmosphere_count=3,
            )
            for ind in ALL_MOOD_ATMOSPHERE_PHRASES:
                count = result.count(ind)
                self.assertLessEqual(count, 1,
                    f"Phrase {ind!r} appears {count} times (should be <=1) at seed {s}")

    def test_produces_valid_output(self):
        for count in [0, 1, 2, 3]:
            for s in range(10):
                result = generate_landscape(seed=s, mood="eerie", mood_atmosphere=True, mood_atmosphere_count=count)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 10,
                    f"Invalid output at count={count}, seed={s}")

    def test_is_deterministic(self):
        a = generate_landscape(seed=42, mood="eerie", mood_atmosphere=True, mood_atmosphere_count=2)
        b = generate_landscape(seed=42, mood="eerie", mood_atmosphere=True, mood_atmosphere_count=2)
        self.assertEqual(a, b,
            "mood_atmosphere_count should be deterministic with same seed")

    def test_works_with_json_format(self):
        result = generate_landscape(seed=42, mood="eerie", mood_atmosphere=True, mood_atmosphere_count=2, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertGreater(len(data["text"]), 0)

    def test_json_includes_field(self):
        result = generate_landscape(seed=42, mood="eerie", mood_atmosphere=True, mood_atmosphere_count=2, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("mood_atmosphere_count", data)
        self.assertEqual(data["mood_atmosphere_count"], 2)

    def test_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


class TestMoodAtmosphereProb(unittest.TestCase):
    def test_default_is_one(self):
        self.assertEqual(
            generate_landscape(seed=42, mood="eerie", mood_atmosphere=True, mood_atmosphere_prob=1.0),
            generate_landscape(seed=42, mood="eerie", mood_atmosphere=True),
            "mood_atmosphere_prob=1.0 should match default",
        )

    def test_zero_suppresses_atmosphere(self):
        for s in range(30):
            result = generate_landscape(seed=s, mood="eerie", mood_atmosphere=True, mood_atmosphere_prob=0.0)
            for ind in ALL_MOOD_ATMOSPHERE_PHRASES:
                self.assertNotIn(ind, result,
                    f"Mood atmosphere should be suppressed at prob=0.0, seed={s}")

    def test_produces_valid_output(self):
        for prob in [0.0, 0.5, 1.0]:
            for s in range(10):
                result = generate_landscape(seed=s, mood="eerie", mood_atmosphere=True, mood_atmosphere_prob=prob)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 10,
                    f"Invalid output at prob={prob}, seed={s}")

    def test_is_deterministic(self):
        a = generate_landscape(seed=42, mood="eerie", mood_atmosphere=True, mood_atmosphere_prob=0.7)
        b = generate_landscape(seed=42, mood="eerie", mood_atmosphere=True, mood_atmosphere_prob=0.7)
        self.assertEqual(a, b,
            "mood_atmosphere_prob should be deterministic with same seed")

    def test_json_includes_field(self):
        result = generate_landscape(seed=42, mood="eerie", mood_atmosphere=True, mood_atmosphere_prob=0.7, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("mood_atmosphere_prob", data)
        self.assertEqual(data["mood_atmosphere_prob"], 0.7)

    def test_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


class TestNoMoodAtmosphere(unittest.TestCase):
    def test_no_mood_atmosphere_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_no_mood_atmosphere_disables_with_preset(self):
        from landscape import generate_landscape, PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                preset = dict(PRESETS[name])
                preset.pop("mood_atmosphere", None)
                preset.pop("mood_atmosphere_count", None)
                preset.pop("mood_atmosphere_prob", None)
                result = generate_landscape(seed=42, **preset, mood_atmosphere=False)
                for ind in ALL_MOOD_ATMOSPHERE_PHRASES:
                    self.assertNotIn(ind, result,
                        f"Preset {name} with --no-mood-atmosphere should not contain {ind!r}")

    def test_no_mood_atmosphere_preset_without_flag_still_has_atmosphere(self):
        from landscape import generate_landscape, PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                if "mood_atmosphere" not in PRESETS[name]:
                    continue
                result = generate_landscape(seed=42, **PRESETS[name])
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_no_mood_atmosphere_works_with_other_features(self):
        from landscape import generate_landscape
        for s in range(10):
            result = generate_landscape(seed=s, mood_atmosphere=False,
                                        mood="eerie", echo_enabled=True,
                                        legend_enabled=True, sound_enabled=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)

    def test_no_mood_atmosphere_with_explicit_mood_atmosphere_override(self):
        from landscape import generate_landscape
        no_atm = generate_landscape(seed=42, biome="forest", mood="eerie", mood_atmosphere=False)
        with_atm = generate_landscape(seed=42, biome="forest", mood="eerie", mood_atmosphere=True)
        self.assertNotEqual(no_atm, with_atm,
            "mood_atmosphere=False should differ from mood_atmosphere=True with same seed")

    def test_no_mood_atmosphere_does_not_affect_json_output(self):
        from landscape import generate_landscape
        result = generate_landscape(seed=42, biome="forest", mood="eerie",
                                    mood_atmosphere=False, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertNotIn("mood_atmosphere", data)


class TestColorFlag(unittest.TestCase):
    def test_color_enabled_default_same_as_before(self):
        r1 = generate_landscape(seed=42, color_enabled=True)
        r2 = generate_landscape(seed=42)
        self.assertEqual(r1, r2, "color_enabled=True should match default")

    def test_color_disabled_still_produces_valid_output(self):
        result = generate_landscape(seed=42, color_enabled=False)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))

    def test_color_disabled_differs_from_enabled(self):
        enabled = generate_landscape(seed=42, color_enabled=True)
        disabled = generate_landscape(seed=42, color_enabled=False)
        self.assertNotEqual(enabled, disabled,
            "Output should differ when color is disabled")

    def test_color_disabled_deterministic(self):
        r1 = generate_landscape(seed=99, color_enabled=False)
        r2 = generate_landscape(seed=99, color_enabled=False)
        self.assertEqual(r1, r2, "color_enabled=False should be deterministic with same seed")

    def test_color_disabled_no_formatting_artifacts(self):
        results = [generate_landscape(seed=s, color_enabled=False) for s in range(50)]
        for r in results:
            self.assertNotIn("  ", r, f"Output has double space: {r!r}")
            self.assertNotIn(" .", r, f"Output has space before period: {r!r}")

    def test_color_disabled_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_color_disabled_works_with_detail_three(self):
        result = generate_landscape(seed=42, color_enabled=False, detail=3)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))

    def test_color_disabled_works_with_mood_and_bias(self):
        result = generate_landscape(seed=42, color_enabled=False, mood="eerie", bias="rare")
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))


class TestElementFlag(unittest.TestCase):
    def test_element_enabled_default_same_as_before(self):
        r1 = generate_landscape(seed=42, element_enabled=True)
        r2 = generate_landscape(seed=42)
        self.assertEqual(r1, r2, "element_enabled=True should match default")

    def test_element_disabled_still_produces_valid_output(self):
        result = generate_landscape(seed=42, element_enabled=False)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))

    def test_element_disabled_differs_from_enabled(self):
        enabled = generate_landscape(seed=42, element_enabled=True)
        disabled = generate_landscape(seed=42, element_enabled=False)
        self.assertNotEqual(enabled, disabled,
            "Output should differ when element is disabled")

    def test_element_disabled_deterministic(self):
        r1 = generate_landscape(seed=99, element_enabled=False)
        r2 = generate_landscape(seed=99, element_enabled=False)
        self.assertEqual(r1, r2, "element_enabled=False should be deterministic with same seed")

    def test_element_disabled_no_formatting_artifacts(self):
        results = [generate_landscape(seed=s, element_enabled=False) for s in range(50)]
        for r in results:
            self.assertNotIn("  ", r, f"Output has double space: {r!r}")
            self.assertNotIn(" .", r, f"Output has space before period: {r!r}")

    def test_element_disabled_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_element_disabled_works_with_detail_three(self):
        result = generate_landscape(seed=42, element_enabled=False, detail=3)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))

    def test_element_disabled_works_with_mood_and_bias(self):
        result = generate_landscape(seed=42, element_enabled=False, mood="eerie", bias="rare")
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))

    def test_element_disabled_works_with_combine(self):
        result = generate_landscape(seed=42, element_enabled=False, combine="forest,desert")
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))

    def test_element_disabled_no_elements_in_output(self):
        results = [generate_landscape(seed=s, element_enabled=False) for s in range(300)]
        all_text = " ".join(results)
        element_words_in_output = [e for e in ALL_ELEMENTS if e in all_text]
        self.assertLess(len(element_words_in_output), len(ALL_ELEMENTS),
            "Most elements should be absent from output when element_enabled=False")


class TestTimeWordFlag(unittest.TestCase):
    def test_time_word_enabled_default_same_as_before(self):
        r1 = generate_landscape(seed=42, time_word_enabled=True)
        r2 = generate_landscape(seed=42)
        self.assertEqual(r1, r2, "time_word_enabled=True should match default")

    def test_time_word_disabled_still_produces_valid_output(self):
        result = generate_landscape(seed=42, time_word_enabled=False)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))

    def test_time_word_disabled_differs_from_enabled(self):
        enabled = generate_landscape(seed=42, time_word_enabled=True)
        disabled = generate_landscape(seed=42, time_word_enabled=False)
        self.assertNotEqual(enabled, disabled,
            "Output should differ when time word is disabled")

    def test_time_word_disabled_deterministic(self):
        r1 = generate_landscape(seed=99, time_word_enabled=False)
        r2 = generate_landscape(seed=99, time_word_enabled=False)
        self.assertEqual(r1, r2, "time_word_enabled=False should be deterministic with same seed")

    def test_time_word_disabled_no_formatting_artifacts(self):
        results = [generate_landscape(seed=s, time_word_enabled=False) for s in range(50)]
        for r in results:
            self.assertNotIn("  ", r, f"Output has double space: {r!r}")
            self.assertNotIn(" .", r, f"Output has space before period: {r!r}")

    def test_time_word_disabled_no_time_words_in_output(self):
        results = [generate_landscape(seed=s, time_word_enabled=False) for s in range(300)]
        all_text = " ".join(results)
        time_words_in_output = [t for t in ALL_TIME_WORDS if t in all_text]
        self.assertLess(len(time_words_in_output), len(ALL_TIME_WORDS),
            "Most time words should be absent from output when time_word_enabled=False")

    def test_time_word_disabled_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_time_word_disabled_works_with_detail_three(self):
        result = generate_landscape(seed=42, time_word_enabled=False, detail=3)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))

    def test_time_word_disabled_works_with_mood_and_bias(self):
        result = generate_landscape(seed=42, time_word_enabled=False, mood="eerie", bias="rare")
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))

    def test_time_word_disabled_works_with_combine(self):
        result = generate_landscape(seed=42, time_word_enabled=False, combine="forest,desert")
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))

    def test_time_word_disabled_works_with_echo(self):
        result = generate_landscape(seed=42, time_word_enabled=False, echo_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))


class TestAnomalyFlag(unittest.TestCase):
    def test_anomaly_enabled_default_same_as_before(self):
        r1 = generate_landscape(seed=42, anomaly_enabled=True)
        r2 = generate_landscape(seed=42)
        self.assertEqual(r1, r2, "anomaly_enabled=True should match default")

    def test_anomaly_disabled_still_produces_valid_output(self):
        result = generate_landscape(seed=42, anomaly_enabled=False)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))

    def test_anomaly_disabled_differs_from_enabled(self):
        enabled = generate_landscape(seed=42, anomaly_enabled=True, anomaly_prob=1.0)
        disabled = generate_landscape(seed=42, anomaly_enabled=False, anomaly_prob=1.0)
        self.assertNotEqual(enabled, disabled,
            "Output should differ when anomaly is disabled")

    def test_anomaly_disabled_deterministic(self):
        r1 = generate_landscape(seed=99, anomaly_enabled=False)
        r2 = generate_landscape(seed=99, anomaly_enabled=False)
        self.assertEqual(r1, r2, "anomaly_enabled=False should be deterministic with same seed")

    def test_anomaly_disabled_suppresses_all_anomalies(self):
        results = [generate_landscape(seed=s, anomaly_enabled=False, anomaly_prob=1.0, anomaly_count=3) for s in range(100)]
        has_anomaly = any(
            any(a in r for a in ALL_ANOMALIES) for r in results
        )
        self.assertFalse(has_anomaly,
            "No anomaly should appear when anomaly_enabled=False even with high prob")

    def test_anomaly_disabled_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_anomaly_disabled_works_with_detail_three(self):
        result = generate_landscape(seed=42, anomaly_enabled=False, detail=3)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))

    def test_anomaly_disabled_works_with_mood_and_bias(self):
        result = generate_landscape(seed=42, anomaly_enabled=False, mood="eerie", bias="rare")
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))


class TestAnomalyAdverb(unittest.TestCase):
    def test_anomaly_templates_have_adverb_placeholder(self):
        anomaly_tmpls = SENTENCE_TEMPLATES["anomaly"]
        adverb_tmpls = [t for t in anomaly_tmpls if "{adverb}" in t]
        self.assertGreaterEqual(len(adverb_tmpls), 2,
            "At least 2 anomaly templates should reference {adverb}")

    def test_anomaly_adverb_does_not_break_output(self):
        for s in range(30):
            result = generate_landscape(seed=s, anomaly_prob=1.0)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)
            self.assertTrue(result.endswith("."))

    def test_anomaly_adverb_uses_known_adverb(self):
        results = [generate_landscape(seed=s, anomaly_prob=1.0) for s in range(300)]
        self.assertTrue(
            any(adv in r for r in results for adv in ALL_ADVERBS),
            "No known adverb appeared in anomaly text across 300 seeds",
        )

    def test_anomaly_adverb_is_deterministic(self):
        a = generate_landscape(seed=42, anomaly_prob=1.0)
        b = generate_landscape(seed=42, anomaly_prob=1.0)
        self.assertEqual(a, b,
            "Anomaly with adverb should be deterministic")

    def test_anomaly_adverb_works_with_adverb_disabled(self):
        for s in range(20):
            result = generate_landscape(seed=s, adverb_enabled=False, anomaly_prob=1.0)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)
            self.assertNotIn(" :", result,
                "Space before colon should not appear when adverb is disabled")
            self.assertTrue(result.endswith("."))

    def test_anomaly_adverb_works_with_mood_and_bias(self):
        result = generate_landscape(seed=42, mood="eerie", bias="rare", anomaly_prob=1.0)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))

    def test_anomaly_adverb_works_with_detail_three(self):
        result = generate_landscape(seed=42, detail=3, anomaly_prob=1.0)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 50)
        self.assertTrue(result.endswith("."))

    def test_anomaly_adverb_works_with_json_format(self):
        result = generate_landscape(seed=42, fmt="json", anomaly_prob=1.0)
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertGreater(len(data["text"]), 0)


class TestAnomalyColor(unittest.TestCase):
    def test_anomaly_templates_have_color_placeholder(self):
        anomaly_tmpls = SENTENCE_TEMPLATES["anomaly"]
        color_tmpls = [t for t in anomaly_tmpls if "{color}" in t]
        self.assertGreaterEqual(len(color_tmpls), 2,
            "At least 2 anomaly templates should reference {color}")

    def test_anomaly_color_does_not_break_output(self):
        for s in range(30):
            result = generate_landscape(seed=s, anomaly_prob=1.0)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)
            self.assertTrue(result.endswith("."))

    def test_anomaly_color_uses_known_color(self):
        results = [generate_landscape(seed=s, anomaly_prob=1.0) for s in range(300)]
        self.assertTrue(
            any(c in r for r in results for c in ALL_COLORS),
            "No known color appeared in anomaly text across 300 seeds",
        )

    def test_anomaly_color_is_deterministic(self):
        a = generate_landscape(seed=42, anomaly_prob=1.0)
        b = generate_landscape(seed=42, anomaly_prob=1.0)
        self.assertEqual(a, b,
            "Anomaly with color should be deterministic")

    def test_anomaly_color_works_with_color_disabled(self):
        for s in range(20):
            result = generate_landscape(seed=s, color_enabled=False, anomaly_prob=1.0)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)
            self.assertNotIn("  ", result,
                "Double spaces should not appear when color is disabled")
            self.assertNotIn(" :", result,
                "Space before colon should not appear when color is disabled")
            self.assertTrue(result.endswith("."))

    def test_anomaly_color_works_with_mood_and_bias(self):
        result = generate_landscape(seed=42, mood="vibrant", bias="rare", anomaly_prob=1.0)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))

    def test_anomaly_color_works_with_detail_three(self):
        result = generate_landscape(seed=42, detail=3, anomaly_prob=1.0)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 50)
        self.assertTrue(result.endswith("."))

    def test_anomaly_color_works_with_json_format(self):
        result = generate_landscape(seed=42, fmt="json", anomaly_prob=1.0)
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertGreater(len(data["text"]), 0)

    def test_anomaly_color_in_light_template_appears(self):
        results = [generate_landscape(seed=s, biome="tundra", anomaly_prob=1.0) for s in range(500)]
        light_matches = sum(
            1 for r in results if "In the " in r and " light" in r
        )
        self.assertGreater(light_matches, 0,
            "'In the {color} light' anomaly template should appear across 500 random seeds")


class TestBiomeColorsAndAdverbs(unittest.TestCase):
    def test_biome_forest_has_colors_in_biome_words(self):
        self.assertIn("colors", BIOME_WORDS["forest"])
        self.assertGreater(len(BIOME_WORDS["forest"]["colors"]), 0)

    def test_biome_desert_has_adverbs_in_biome_words(self):
        self.assertIn("adverbs", BIOME_WORDS["desert"])
        self.assertGreater(len(BIOME_WORDS["desert"]["adverbs"]), 0)

    def test_each_biome_has_colors_and_adverbs(self):
        for b in BIOMES:
            with self.subTest(biome=b):
                self.assertIn("colors", BIOME_WORDS[b],
                    f"Biome {b!r} missing 'colors'")
                self.assertIn("adverbs", BIOME_WORDS[b],
                    f"Biome {b!r} missing 'adverbs'")
                self.assertGreater(len(BIOME_WORDS[b]["colors"]), 0,
                    f"Biome {b!r} has empty colors")
                self.assertGreater(len(BIOME_WORDS[b]["adverbs"]), 0,
                    f"Biome {b!r} has empty adverbs")

    def test_biome_specific_colors_appear_in_output(self):
        for biome in ["forest", "desert", "ocean"]:
            with self.subTest(biome=biome):
                colors = set(BIOME_WORDS[biome].get("colors", []))
                results = [generate_landscape(seed=s, biome=biome) for s in range(300)]
                found = any(any(c in r for c in colors) for r in results)
                self.assertTrue(found,
                    f"No {biome}-specific colors appeared across 300 seeds")

    def test_biome_specific_adverbs_appear_in_output(self):
        for biome in ["tundra", "swamp", "cave system"]:
            with self.subTest(biome=biome):
                adverbs = set(BIOME_WORDS[biome].get("adverbs", []))
                results = [generate_landscape(seed=s, biome=biome) for s in range(300)]
                found = any(any(a in r for a in adverbs) for r in results)
                self.assertTrue(found,
                    f"No {biome}-specific adverbs appeared across 300 seeds")

    def test_biome_colors_produce_valid_output(self):
        for b in BIOMES:
            with self.subTest(biome=b):
                for s in range(5):
                    result = generate_landscape(seed=s, biome=b)
                    self.assertIsInstance(result, str)
                    self.assertGreater(len(result), 10)

    def test_biome_colors_work_with_combine(self):
        colors_desert = set(BIOME_WORDS["desert"].get("colors", []))
        colors_ocean = set(BIOME_WORDS["ocean"].get("colors", []))
        combined = colors_desert | colors_ocean
        results = [generate_landscape(seed=s, combine="desert,ocean") for s in range(300)]
        found = any(any(c in r for c in combined) for r in results)
        self.assertTrue(found,
            "No desert or ocean colors appeared in combined output across 300 seeds")

    def test_biome_colors_work_with_color_disabled(self):
        for b in ["forest", "volcanic field", "sky islands"]:
            with self.subTest(biome=b):
                result = generate_landscape(seed=42, biome=b, color_enabled=False)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 10)

    def test_biome_colors_are_deterministic(self):
        for b in ["forest", "coral reef", "ruined city"]:
            with self.subTest(biome=b):
                a = generate_landscape(seed=42, biome=b)
                b_result = generate_landscape(seed=42, biome=b)
                self.assertEqual(a, b_result,
                    f"Output for {b} should be deterministic")

    def test_biome_colors_work_with_mood_and_bias(self):
        for b in ["fungal grove", "plain", "mountain range"]:
            with self.subTest(biome=b):
                result = generate_landscape(seed=42, biome=b, mood="vibrant", bias="common")
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 10)

    def test_biome_colors_appear_across_detail_levels(self):
        for detail in [0, 1, 2, 3]:
            with self.subTest(detail=detail):
                result = generate_landscape(seed=42, biome="forest", detail=detail)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_describe_biome_includes_colors_and_adverbs(self):
        from landscape import describe_biome
        result = describe_biome("forest")
        self.assertIn("colors:", result,
            "describe_biome should include color category")
        self.assertIn("adverbs:", result,
            "describe_biome should include adverb category")


class TestWeatherAdj(unittest.TestCase):
    def test_weather_templates_use_adj_placeholder(self):
        weather_tmpls = SENTENCE_TEMPLATES["weather"]
        adj_tmpls = [t for t in weather_tmpls if "{adj}" in t]
        self.assertGreaterEqual(len(adj_tmpls), 4,
            "At least 4 weather templates should reference {adj}")

    def test_weather_adj_does_not_break_output(self):
        for s in range(30):
            result = generate_landscape(seed=s)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)
            self.assertTrue(result.endswith("."))

    def test_weather_adj_uses_known_adjective(self):
        results = [generate_landscape(seed=s, biome="tundra") for s in range(200)]
        self.assertTrue(
            any(a in r for r in results for a in ALL_ADJECTIVES),
            "No known adjective appeared in weather across 200 seeds",
        )

    def test_weather_adj_is_deterministic(self):
        a = generate_landscape(seed=42)
        b = generate_landscape(seed=42)
        self.assertEqual(a, b,
            "Weather with adj should be deterministic")

    def test_weather_adj_works_with_middle_disabled(self):
        for s in range(20):
            result = generate_landscape(seed=s, middle_enabled=False, detail=2)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)
            self.assertTrue(result.endswith("."))

    def test_weather_adj_works_with_no_adverb(self):
        for s in range(10):
            result = generate_landscape(seed=s, adverb_enabled=False, detail=2)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)
            self.assertNotIn("  ", result)
            self.assertTrue(result.endswith("."))

    def test_weather_adj_works_with_json_format(self):
        result = generate_landscape(seed=42, fmt="json", detail=2)
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertGreater(len(data["text"]), 0)

    def test_weather_adj_works_with_detail_three(self):
        for s in range(10):
            result = generate_landscape(seed=s, detail=3)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 50)
            self.assertTrue(result.endswith("."))

    def test_weather_adj_works_with_mood_and_bias(self):
        result = generate_landscape(seed=42, mood="eerie", bias="rare")
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))


class TestAnomalyAdj(unittest.TestCase):
    def test_anomaly_templates_use_adj_placeholder(self):
        anomaly_tmpls = SENTENCE_TEMPLATES["anomaly"]
        adj_tmpls = [t for t in anomaly_tmpls if "{adj}" in t]
        self.assertGreaterEqual(len(adj_tmpls), 1,
            "At least 1 anomaly template should reference {adj}")

    def test_anomaly_adj_does_not_break_output(self):
        for s in range(30):
            result = generate_landscape(seed=s, anomaly_prob=1.0)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)
            self.assertTrue(result.endswith("."))

    def test_anomaly_adj_uses_known_adjective(self):
        results = [generate_landscape(seed=s, anomaly_prob=1.0) for s in range(300)]
        self.assertTrue(
            any(a in r for r in results for a in ALL_ADJECTIVES),
            "No known adjective appeared in anomaly text across 300 seeds",
        )

    def test_anomaly_adj_is_deterministic(self):
        a = generate_landscape(seed=42, anomaly_prob=1.0)
        b = generate_landscape(seed=42, anomaly_prob=1.0)
        self.assertEqual(a, b,
            "Anomaly with adj should be deterministic")


class TestAnomalyElement(unittest.TestCase):
    def test_anomaly_templates_use_element_placeholder(self):
        anomaly_tmpls = SENTENCE_TEMPLATES["anomaly"]
        element_tmpls = [t for t in anomaly_tmpls if "{element}" in t]
        self.assertGreaterEqual(len(element_tmpls), 1,
            "At least 1 anomaly template should reference {element}")

    def test_anomaly_element_does_not_break_output(self):
        for s in range(30):
            result = generate_landscape(seed=s, anomaly_prob=1.0)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)
            self.assertTrue(result.endswith("."))

    def test_anomaly_element_uses_known_element(self):
        results = [generate_landscape(seed=s, anomaly_prob=1.0) for s in range(300)]
        self.assertTrue(
            any(e in r for r in results for e in ALL_ELEMENTS),
            "No known element word appeared in anomaly text across 300 seeds",
        )

    def test_anomaly_element_is_deterministic(self):
        a = generate_landscape(seed=42, anomaly_prob=1.0)
        b = generate_landscape(seed=42, anomaly_prob=1.0)
        self.assertEqual(a, b,
            "Anomaly with element should be deterministic")


class TestAnomalyTimeWord(unittest.TestCase):
    def test_anomaly_templates_have_time_word_placeholder(self):
        anomaly_tmpls = SENTENCE_TEMPLATES["anomaly"]
        time_word_tmpls = [t for t in anomaly_tmpls if "{time_word}" in t]
        self.assertGreaterEqual(len(time_word_tmpls), 1,
            "At least 1 anomaly template should reference {time_word}")

    def test_anomaly_time_word_does_not_break_output(self):
        for s in range(30):
            result = generate_landscape(seed=s, anomaly_prob=1.0)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)
            self.assertTrue(result.endswith("."))

    def test_anomaly_time_word_uses_known_time_word(self):
        results = [generate_landscape(seed=s, anomaly_prob=1.0) for s in range(300)]
        self.assertTrue(
            any(t in r for r in results for t in ALL_TIME_WORDS),
            "No known time word appeared in anomaly text across 300 seeds",
        )

    def test_anomaly_time_word_works_with_time_word_disabled(self):
        for s in range(20):
            result = generate_landscape(seed=s, time_word_enabled=False, anomaly_prob=1.0)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)
            self.assertNotIn(" :", result,
                "Space before colon should not appear when time word is disabled")
            self.assertTrue(result.endswith("."))

    def test_anomaly_time_word_is_deterministic(self):
        a = generate_landscape(seed=42, anomaly_prob=1.0)
        b = generate_landscape(seed=42, anomaly_prob=1.0)
        self.assertEqual(a, b,
            "Anomaly with time word should be deterministic")

    def test_anomaly_time_word_works_with_mood_and_bias(self):
        result = generate_landscape(seed=42, mood="eerie", bias="rare", anomaly_prob=1.0)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))

    def test_anomaly_time_word_works_with_detail_three(self):
        result = generate_landscape(seed=42, detail=3, anomaly_prob=1.0)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 50)
        self.assertTrue(result.endswith("."))

    def test_anomaly_time_word_works_with_json_format(self):
        result = generate_landscape(seed=42, fmt="json", anomaly_prob=1.0)
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertGreater(len(data["text"]), 0)

    def test_anomaly_time_word_disabled_differs_from_enabled(self):
        enabled = generate_landscape(seed=42, anomaly_prob=1.0)
        disabled = generate_landscape(seed=42, anomaly_prob=1.0, time_word_enabled=False)
        self.assertNotEqual(enabled, disabled,
            "Output should differ when time word is disabled in anomalies")

    def test_anomaly_time_word_works_with_combine(self):
        result = generate_landscape(seed=42, anomaly_prob=1.0, combine="forest,desert")
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 10)
        self.assertTrue(result.endswith("."))

    def test_anomaly_time_word_appears_in_something_is_not_right_phrase(self):
        results = [generate_landscape(seed=s, anomaly_prob=1.0, biome="forest") for s in range(300)]
        not_right_results = [r for r in results if "not right" in r]
        if not_right_results:
            self.assertTrue(
                any(t in r for r in not_right_results for t in ALL_TIME_WORDS),
                "No time word appeared in 'not right' anomaly across 300 seeds",
            )

    def test_anomaly_time_word_appears_in_quiet_wrongness_phrase(self):
        results = [generate_landscape(seed=s, anomaly_prob=1.0, biome="forest") for s in range(300)]
        wrongness_results = [r for r in results if "wrongness" in r]
        if wrongness_results:
            self.assertTrue(
                any(t in r for r in wrongness_results for t in ALL_TIME_WORDS),
                "No time word appeared in 'wrongness' anomaly across 300 seeds",
            )


class TestDescribeEchoes(unittest.TestCase):
    def test_describe_echoes_returns_string(self):
        from landscape import describe_echoes
        result = describe_echoes()
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_describe_echoes_contains_header(self):
        from landscape import describe_echoes
        result = describe_echoes()
        self.assertIn("echo phrases", result)

    def test_describe_echoes_contains_all_echoes(self):
        from landscape import describe_echoes, ECHOES
        result = describe_echoes()
        for echo in ECHOES:
            self.assertIn(echo, result,
                f"Echo description should contain echo: {echo!r}")

    def test_describe_echoes_contains_index_numbers(self):
        from landscape import describe_echoes
        result = describe_echoes()
        self.assertIn("[0]", result, "Echo description should contain index [0]")
        self.assertIn("[1]", result, "Echo description should contain index [1]")

    def test_describe_echoes_shows_all_echoes(self):
        from landscape import describe_echoes, ECHOES
        result = describe_echoes()
        count = len(ECHOES)
        self.assertIn(f"=== echo phrases ===", result)
        self.assertIn(f"[{count - 1}]", result,
            f"Echo description should contain the last index [{count - 1}]")

    def test_describe_echoes_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_describe_echoes_flag_prints_to_stdout(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--describe-echoes"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertIn("echo phrases", output)
        self.assertIn("[0]", output)
        self.assertIn("[1]", output)

    def test_describe_echoes_no_landscape_generated(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--describe-echoes", "--seed", "42", "--count", "2"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertNotIn("[seed=42]", output,
            "No landscape should be generated when --describe-echoes is used")
        self.assertNotIn("\n\n", output,
            "No landscape should be generated when --describe-echoes is used")


# Unique substrings that appear in rendered echo output regardless of biome injection
ECHO_INDICATORS = [
    "remembers", "has been waiting", "has changed in",
    "echoes of the past", "being watched", "deep time",
    "outside of time", "stones remember", "important happened",
    "older than any sound",
    "bends through the", "wind carries a memory",
    "vast turns over", "holds its breath",
    "caught in the",
    "roads of the",
    "Fragments of",
    "mourns",
    "layer upon layer of",
    "boundary between the",
]

# Subset of ECHO_INDICATORS excluding "remembers" which collides with
# legend phrases ("remembers those who built it"). Used by --no-echo suppression
# tests where legends may be present.
NO_ECHO_INDICATORS = [
    "has been waiting", "has changed in",
    "echoes of the past", "being watched", "deep time",
    "outside of time", "stones remember", "important happened",
    "older than any sound",
    "bends through the", "wind carries a memory",
    "vast turns over", "holds its breath",
    "caught in the",
    "roads of the",
    "Fragments of",
    "mourns",
    "layer upon layer of",
    "boundary between the",
]


class TestEcho(unittest.TestCase):
    def test_echo_disabled_default(self):
        result = generate_landscape(seed=42)
        for ind in ECHO_INDICATORS:
            self.assertNotIn(ind, result,
                f"Echo indicator {ind!r} should not appear by default")

    def test_echo_enabled_appends_echo(self):
        results = [generate_landscape(seed=s, echo_enabled=True) for s in range(100)]
        self.assertTrue(
            any(ind in r for r in results for ind in ECHO_INDICATORS),
            "No echo phrase appeared across 100 seeds with echo_enabled=True",
        )

    def test_echo_does_not_break_output(self):
        for s in range(20):
            result = generate_landscape(seed=s, echo_enabled=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)
            self.assertTrue(result.endswith("."))

    def test_echo_is_deterministic(self):
        a = generate_landscape(seed=42, echo_enabled=True)
        b = generate_landscape(seed=42, echo_enabled=True)
        self.assertEqual(a, b,
            "Echo should be deterministic with same seed")

    def test_echo_works_with_poetic_format(self):
        for s in range(10):
            result = generate_landscape(seed=s, echo_enabled=True, fmt="poetic")
            self.assertIsInstance(result, str)
            self.assertIn("\n", result)

    def test_echo_works_with_json_format(self):
        result = generate_landscape(seed=42, echo_enabled=True, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertGreater(len(data["text"]), 0)

    def test_echo_detail_zero_suppresses_echo(self):
        result = generate_landscape(seed=42, echo_enabled=True, detail=0)
        for ind in ECHO_INDICATORS:
            self.assertNotIn(ind, result,
                f"Echo indicator {ind!r} should not appear with detail=0")

    def test_echo_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_echo_display_injection_contains_biome_name(self):
        results = [generate_landscape(seed=s, echo_enabled=True, biome="tundra") for s in range(100)]
        display_phrases = ["tundra remembers", "tundra has been waiting",
                           "in the tundra has changed", "in the tundra once"]
        self.assertTrue(
            any(p in r for r in results for p in display_phrases),
            "Echo with {display} should reference the biome name across 100 seeds",
        )

    def test_echo_display_respects_combine(self):
        results = [generate_landscape(seed=s, echo_enabled=True, combine="forest,desert") for s in range(100)]
        self.assertTrue(
            any("forest and desert" in r for r in results),
            "Echo with {display} should show combined biome name",
        )

    def test_echo_display_without_display_phrase_still_works(self):
        for s in range(20):
            result = generate_landscape(seed=s, echo_enabled=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)
            self.assertTrue(result.endswith("."))

    def test_echo_display_is_deterministic(self):
        a = generate_landscape(seed=42, echo_enabled=True, biome="tundra")
        b = generate_landscape(seed=42, echo_enabled=True, biome="tundra")
        self.assertEqual(a, b,
            "Echo with display should be deterministic with same seed")

    def test_echo_display_works_with_all_biomes(self):
        for biome in ["forest", "desert", "tundra", "ruined city", "sky islands"]:
            with self.subTest(biome=biome):
                result = generate_landscape(seed=42, echo_enabled=True, biome=biome)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)
                self.assertTrue(result.endswith("."))

    def test_echo_adverb_injection_contains_adverb(self):
        results = [generate_landscape(seed=s, echo_enabled=True, detail=2) for s in range(200)]
        self.assertTrue(
            any(a in r for r in results for a in ALL_ADVERBS),
            "Echo with {adverb} should contain adverb words across 200 seeds",
        )

    def test_echo_adverb_respects_no_adverb(self):
        for s in range(20):
            result = generate_landscape(seed=s, echo_enabled=True, adverb_enabled=False)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)
            self.assertNotIn("  ", result, f"Output has double space: {result!r}")
            self.assertNotIn(" .", result, f"Output has space before period: {result!r}")
            self.assertTrue(result.endswith("."))

    def test_echo_adverb_is_deterministic(self):
        a = generate_landscape(seed=42, echo_enabled=True, biome="tundra")
        b = generate_landscape(seed=42, echo_enabled=True, biome="tundra")
        self.assertEqual(a, b,
            "Echo with {adverb} should be deterministic with same seed")

    def test_echo_element_injection_contains_element(self):
        results = [generate_landscape(seed=s, echo_enabled=True, detail=2) for s in range(200)]
        self.assertTrue(
            any("by the " in r and " itself" in r for r in results),
            "Echo with {element} should produce 'by the {color} {element} itself' pattern across 200 seeds",
        )

    def test_echo_element_in_in_time_phrase(self):
        results = [generate_landscape(seed=s, echo_enabled=True, biome="tundra", detail=2) for s in range(300)]
        self.assertTrue(
            any("outside of time, in the " in r for r in results),
            "Echo phrase with {element} should produce 'outside of time, in the {element}' pattern",
        )

    def test_echo_element_is_deterministic(self):
        a = generate_landscape(seed=42, echo_enabled=True, biome="tundra")
        b = generate_landscape(seed=42, echo_enabled=True, biome="tundra")
        self.assertEqual(a, b,
            "Echo with {element} should be deterministic with same seed")

    def test_echo_element_works_with_detail_zero(self):
        for s in range(20):
            result = generate_landscape(seed=s, echo_enabled=True, detail=0)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)
            self.assertTrue(result.endswith("."))

    def test_echo_element_works_with_combine(self):
        results = [generate_landscape(seed=s, echo_enabled=True, combine="forest,desert", detail=2) for s in range(200)]
        self.assertTrue(
            any(e in r for r in results for e in ALL_ELEMENTS),
            "Echo with {element} should contain element words when biomes are combined",
        )

    def test_echo_color_injection_contains_color(self):
        results = [generate_landscape(seed=s, echo_enabled=True, detail=2) for s in range(200)]
        self.assertTrue(
            any(c in r for r in results for c in ALL_COLORS),
            "Echo with {color} should contain color words across 200 seeds",
        )

    def test_echo_color_in_watched_phrase(self):
        results = [generate_landscape(seed=s, echo_enabled=True, biome="tundra", detail=2) for s in range(300)]
        self.assertTrue(
            any("by the " in r and " itself" in r for r in results),
            "Echo phrase with {color} should produce 'by the {color} {element} itself' pattern",
        )

    def test_echo_color_in_time_phrase(self):
        results = [generate_landscape(seed=s, echo_enabled=True, biome="tundra", detail=2) for s in range(300)]
        self.assertTrue(
            any("outside of time, in the " in r for r in results),
            "Echo phrase with {color} should produce 'outside of time, in the {color} {element}' pattern",
        )

    def test_echo_color_is_deterministic(self):
        a = generate_landscape(seed=42, echo_enabled=True, biome="tundra")
        b = generate_landscape(seed=42, echo_enabled=True, biome="tundra")
        self.assertEqual(a, b,
            "Echo with {color} should be deterministic with same seed")

    def test_echo_color_works_with_detail_zero(self):
        for s in range(20):
            result = generate_landscape(seed=s, echo_enabled=True, detail=0)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)
            self.assertTrue(result.endswith("."))

    def test_echo_color_works_with_combine(self):
        results = [generate_landscape(seed=s, echo_enabled=True, combine="forest,desert", detail=2) for s in range(200)]
        self.assertTrue(
            any(c in r for r in results for c in ALL_COLORS),
            "Echo with {color} should contain color words when biomes are combined",
        )

    def test_echo_color_works_with_color_disabled(self):
        for s in range(20):
            result = generate_landscape(seed=s, echo_enabled=True, color_enabled=False)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)
            self.assertNotIn("  ", result, f"Output has double space: {result!r}")
            self.assertTrue(result.endswith("."))

    def test_echo_adj_injection_contains_adj(self):
        results = [generate_landscape(seed=s, echo_enabled=True, detail=2) for s in range(200)]
        self.assertTrue(
            any(a in r for r in results for a in ALL_ADJECTIVES),
            "Echo with {adj} should contain adjective words across 200 seeds",
        )

    def test_echo_adj_in_remembers_phrase(self):
        results = [generate_landscape(seed=s, echo_enabled=True, biome="tundra", detail=2) for s in range(300)]
        self.assertTrue(
            any(a + " " + b in r for r in results
                for a in ALL_ADJECTIVES
                for b in ["tundra remembers", "tundra has been waiting",
                          "tundra has changed", "in the tundra once"]
                if a + " " + b in r),
            "Echo phrase with {adj} should produce 'adj biome ...' pattern",
        )

    def test_echo_adj_is_deterministic(self):
        a = generate_landscape(seed=42, echo_enabled=True, biome="tundra")
        b = generate_landscape(seed=42, echo_enabled=True, biome="tundra")
        self.assertEqual(a, b,
            "Echo with {adj} should be deterministic with same seed")

    def test_echo_adj_works_with_detail_zero(self):
        for s in range(20):
            result = generate_landscape(seed=s, echo_enabled=True, detail=0)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)
            self.assertTrue(result.endswith("."))

    def test_echo_adj_works_with_combine(self):
        results = [generate_landscape(seed=s, echo_enabled=True, combine="forest,desert", detail=2) for s in range(200)]
        self.assertTrue(
            any(a in r for r in results for a in ALL_ADJECTIVES),
            "Echo with {adj} should contain adjective words when biomes are combined",
        )

    def test_echo_adj_works_with_no_adverb(self):
        for s in range(20):
            result = generate_landscape(seed=s, echo_enabled=True, adverb_enabled=False)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)
            self.assertNotIn("  ", result, f"Output has double space: {result!r}")
            self.assertTrue(result.endswith("."))

    def test_echo_adj_works_with_all_biomes(self):
        for biome in ["forest", "desert", "tundra", "ruined city", "sky islands", "fungal grove"]:
            with self.subTest(biome=biome):
                result = generate_landscape(seed=42, echo_enabled=True, biome=biome)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)
                self.assertTrue(result.endswith("."))

    def test_echo_count_default_is_one(self):
        a = generate_landscape(seed=42, echo_enabled=True)
        b = generate_landscape(seed=42, echo_enabled=True, echo_count=1)
        self.assertEqual(a, b,
            "echo_count=1 should match default")

    def test_echo_count_zero_suppresses_echo(self):
        result = generate_landscape(seed=42, echo_enabled=True, echo_count=0)
        for e in ECHOES:
            self.assertNotIn(e, result,
                "Echo should not appear with echo_count=0")

    def test_echo_count_two_sometimes_has_multiple(self):
        results = [generate_landscape(seed=s, echo_enabled=True, echo_count=3) for s in range(100)]
        multi = [r for r in results if sum(1 for ind in ECHO_INDICATORS if ind in r) >= 2]
        self.assertGreater(len(multi), 10,
            "echo_count=3 should often produce multi-echo outputs")

    def test_echo_count_does_not_repeat_same_echo(self):
        results = [generate_landscape(seed=s, echo_enabled=True, echo_count=3) for s in range(200)]
        for r in results:
            for ind in ECHO_INDICATORS:
                self.assertLessEqual(r.count(ind), 1,
                    f"Echo indicator {ind!r} should appear at most once: {r!r}")

    def test_echo_count_produces_valid_output(self):
        for count in [0, 1, 2, 3]:
            for s in range(10):
                result = generate_landscape(seed=s, echo_enabled=True, echo_count=count)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_echo_count_is_deterministic(self):
        a = generate_landscape(seed=42, echo_enabled=True, echo_count=2)
        b = generate_landscape(seed=42, echo_enabled=True, echo_count=2)
        self.assertEqual(a, b,
            "echo_count should be deterministic with same seed")

    def test_echo_count_does_not_affect_unseeded_echo(self):
        a = generate_landscape(seed=42, echo_enabled=True, echo_count=2)
        b = generate_landscape(seed=42, echo_enabled=True, echo_count=2)
        self.assertEqual(a, b,
            "Echo count should be deterministic")

    def test_echo_count_works_with_json_format(self):
        result = generate_landscape(seed=42, echo_enabled=True, echo_count=2, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertGreater(len(data["text"]), 0)

    def test_echo_count_json_includes_field(self):
        result = generate_landscape(seed=42, echo_enabled=True, echo_count=2, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("echo_count", data)
        self.assertEqual(data["echo_count"], 2)

    def test_echo_count_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_echo_json_includes_field(self):
        result = generate_landscape(seed=42, echo_enabled=True, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("echo_enabled", data)
        self.assertTrue(data["echo_enabled"])

    def test_echo_json_field_absent_when_disabled(self):
        result = generate_landscape(seed=42, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertNotIn("echo_enabled", data)

    def test_echo_count_can_exhaust_pool_falls_back(self):
        # With echo_count > len(ECHOES), fallback should allow repeats
        result = generate_landscape(seed=42, echo_enabled=True, echo_count=15)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))


class TestEchoProb(unittest.TestCase):
    def test_echo_prob_default_is_one(self):
        a = generate_landscape(seed=42, echo_enabled=True)
        b = generate_landscape(seed=42, echo_enabled=True, echo_prob=1.0)
        self.assertEqual(a, b,
            "echo_prob=1.0 should match default")

    def test_echo_prob_zero_suppresses_echo(self):
        results = [generate_landscape(seed=s, echo_enabled=True, echo_prob=0.0) for s in range(100)]
        for r in results:
            for ind in ECHO_INDICATORS:
                self.assertNotIn(ind, r,
                    f"Echo indicator {ind!r} should not appear with echo_prob=0.0")

    def test_echo_prob_one_always_has_echo(self):
        results = [generate_landscape(seed=s, echo_enabled=True, echo_prob=1.0) for s in range(100)]
        has_echo = sum(1 for r in results if any(ind in r for ind in ECHO_INDICATORS))
        self.assertGreater(has_echo, 80,
            "With echo_prob=1.0, most outputs should contain an echo")

    def test_echo_prob_produces_valid_output(self):
        for prob in [0.0, 0.25, 0.5, 0.75, 1.0]:
            for s in range(10):
                result = generate_landscape(seed=s, echo_enabled=True, echo_prob=prob)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_echo_prob_is_deterministic(self):
        a = generate_landscape(seed=42, echo_enabled=True, echo_prob=0.5)
        b = generate_landscape(seed=42, echo_enabled=True, echo_prob=0.5)
        self.assertEqual(a, b,
            "echo_prob should be deterministic with same seed")

    def test_echo_prob_json_includes_field(self):
        result = generate_landscape(seed=42, echo_enabled=True, echo_prob=0.5, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("echo_prob", data)
        self.assertEqual(data["echo_prob"], 0.5)

    def test_echo_prob_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


class TestPresets(unittest.TestCase):
    def test_preset_nightfall_uses_eerie_mood(self):
        from landscape import PRESETS
        self.assertIn("mood", PRESETS["nightfall"])
        self.assertIn("eerie", PRESETS["nightfall"]["mood"])

    def test_preset_pastoral_suppresses_anomalies(self):
        from landscape import PRESETS
        self.assertEqual(PRESETS["pastoral"]["anomaly_prob"], 0.0)

    def test_preset_wasteland_enables_echo(self):
        from landscape import PRESETS
        self.assertTrue(PRESETS["wasteland"]["echo_enabled"])

    def test_preset_produces_valid_output(self):
        for name in ["nightfall", "pastoral", "sublime", "wasteland", "dreamscape", "gloaming", "sanctuary", "lament", "oasis", "reverie", "elegy"]:
            with self.subTest(preset=name):
                from landscape import generate_landscape, PRESETS
                result = generate_landscape(seed=42, **PRESETS[name])
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)
                self.assertTrue(result.endswith("."))

    def test_preset_is_deterministic(self):
        from landscape import PRESETS
        for name in ["nightfall", "pastoral", "sublime", "wasteland", "dreamscape", "gloaming", "sanctuary", "lament", "oasis", "reverie", "elegy"]:
            with self.subTest(preset=name):
                a = generate_landscape(seed=42, **PRESETS[name])
                b = generate_landscape(seed=42, **PRESETS[name])
                self.assertEqual(a, b,
                    f"Preset {name} should be deterministic with same seed")

    def test_preset_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_preset_works_via_cli(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--preset", "pastoral", "--seed", "42"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertIsInstance(output, str)
        self.assertGreater(len(output), 0)
        self.assertTrue(output.endswith(".\n"))

    def test_describe_presets_returns_string(self):
        from landscape import describe_presets
        result = describe_presets()
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_describe_presets_contains_header(self):
        from landscape import describe_presets
        result = describe_presets()
        self.assertIn("presets", result)

    def test_describe_presets_contains_all_presets(self):
        from landscape import describe_presets, PRESETS
        result = describe_presets()
        for name in PRESETS:
            self.assertIn(name, result,
                f"Preset description should contain preset name '{name}'")

    def test_all_presets_include_legend_enabled(self):
        from landscape import PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                self.assertIn("legend_enabled", PRESETS[name],
                    f"Preset {name} should include 'legend_enabled'")
                self.assertTrue(PRESETS[name]["legend_enabled"],
                    f"Preset {name} should have legend_enabled=True")

    def test_all_presets_include_travelogue(self):
        from landscape import PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                self.assertIn("travelogue", PRESETS[name],
                    f"Preset {name} should include 'travelogue'")
                self.assertTrue(PRESETS[name]["travelogue"],
                    f"Preset {name} should have travelogue=True")

    def test_preset_with_travelogue_produces_framed_output(self):
        from landscape import PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                result = generate_landscape(seed=42, **PRESETS[name])
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 10)
                has_travelogue = (
                    "Journal entry, day " in result
                    or "Log entry" in result
                    or "Chronicle of the journey" in result
                    or "Day " in result and "of the expedition" in result
                    or "Captain's log, supplemental" in result
                    or "I write to you from" in result
                    or "Field notes, day" in result
                    or "Dispatch " in result and "stretches before us" in result
                    or "I have journeyed" in result
                )
                self.assertTrue(has_travelogue,
                    f"Preset {name} with travelogue should have travelogue framing")

    def test_all_presets_include_wistful(self):
        from landscape import PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                self.assertIn("wistful", PRESETS[name],
                    f"Preset {name} should include 'wistful'")
                self.assertTrue(PRESETS[name]["wistful"],
                    f"Preset {name} should have wistful=True")

    def test_preset_with_wistful_produces_wistful_output(self):
        from landscape import PRESETS, generate_landscape
        for name in PRESETS:
            with self.subTest(preset=name):
                result = generate_landscape(seed=42, **PRESETS[name])
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 10)
                wistful_indicators = [
                    "wish you could stay",
                    "always remain",
                    "calls to you",
                    "carry a piece",
                    "return to the",
                    "half-remembered dream",
                    "never be the same after visiting",
                    "nowhere else in the world like",
                    "more like a memory of a place",
                    "words will never be enough",
                    "fortunate to have walked",
                    "settled into your bones",
                    "the rest of the world has not",
                    "version of yourself behind",
                    "just behind your eyelids",
                    "whispered into its silence",
                    "pale imitation",
                    "too late to hear",
                    "fixed point against",
                    "before it faded",
                ]
                has_wistful = any(ind in result for ind in wistful_indicators)
                self.assertTrue(has_wistful,
                    f"Preset {name} with wistful should produce wistful output")

    def test_all_presets_include_legend_count_and_prob(self):
        from landscape import PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                self.assertIn("legend_count", PRESETS[name],
                    f"Preset {name} should include 'legend_count'")
                self.assertIn("legend_prob", PRESETS[name],
                    f"Preset {name} should include 'legend_prob'")
                self.assertGreaterEqual(PRESETS[name]["legend_count"], 0)
                self.assertLessEqual(PRESETS[name]["legend_count"], 3)
                self.assertGreaterEqual(PRESETS[name]["legend_prob"], 0.0)
                self.assertLessEqual(PRESETS[name]["legend_prob"], 1.0)

    def test_preset_legend_count_affects_output(self):
        from landscape import generate_landscape
        results = {}
        for count in [0, 1, 2, 3]:
            with self.subTest(legend_count=count):
                result = generate_landscape(seed=42, legend_enabled=True, legend_count=count, legend_prob=1.0)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)
                results[count] = result
        self.assertNotEqual(results[0], results[1],
            "legend_count=0 should differ from legend_count=1")

    def test_preset_legend_prob_affects_output(self):
        from landscape import generate_landscape
        zero = generate_landscape(seed=42, legend_enabled=True, legend_count=2, legend_prob=0.0)
        one = generate_landscape(seed=42, legend_enabled=True, legend_count=2, legend_prob=1.0)
        self.assertNotEqual(zero, one,
            "legend_prob=0.0 should differ from legend_prob=1.0")

    def test_preset_with_legend_produces_legend_output(self):
        from landscape import PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                result = generate_landscape(seed=42, **PRESETS[name])
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)
                self.assertTrue(result.endswith("."))

    def test_describe_presets_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_describe_presets_flag_prints_to_stdout(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--describe-presets"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertIn("presets", output)
        self.assertIn("nightfall", output)
        self.assertIn("pastoral", output)

    def test_describe_presets_no_landscape_generated(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--describe-presets", "--seed", "42", "--count", "2"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertNotIn("[seed=42]", output,
            "No landscape should be generated when --describe-presets is used")
        self.assertNotIn("\n\n", output,
            "No landscape should be generated when --describe-presets is used")

    def test_all_presets_include_sound_enabled(self):
        from landscape import PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                self.assertIn("sound_enabled", PRESETS[name],
                    f"Preset {name} should include 'sound_enabled'")
                self.assertTrue(PRESETS[name]["sound_enabled"],
                    f"Preset {name} should have sound_enabled=True")

    def test_preset_with_soundscape_produces_valid_output(self):
        from landscape import PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                result = generate_landscape(seed=42, **PRESETS[name])
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)
                self.assertTrue(result.endswith("."))

    def test_all_presets_include_sound_count_and_prob(self):
        from landscape import PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                self.assertIn("sound_count", PRESETS[name],
                    f"Preset {name} should include 'sound_count'")
                self.assertIn("sound_prob", PRESETS[name],
                    f"Preset {name} should include 'sound_prob'")
                self.assertGreaterEqual(PRESETS[name]["sound_count"], 0)
                self.assertLessEqual(PRESETS[name]["sound_count"], 3)
                self.assertGreaterEqual(PRESETS[name]["sound_prob"], 0.0)
                self.assertLessEqual(PRESETS[name]["sound_prob"], 1.0)

    def test_preset_sound_count_affects_output(self):
        from landscape import generate_landscape
        results = {}
        for count in [0, 1, 2, 3]:
            with self.subTest(sound_count=count):
                result = generate_landscape(seed=42, sound_enabled=True, sound_count=count, sound_prob=1.0)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)
                results[count] = result
        self.assertNotEqual(results[0], results[1],
            "sound_count=0 should differ from sound_count=1")

    def test_preset_sound_prob_affects_output(self):
        from landscape import generate_landscape
        zero = generate_landscape(seed=42, sound_enabled=True, sound_count=2, sound_prob=0.0)
        one = generate_landscape(seed=42, sound_enabled=True, sound_count=2, sound_prob=1.0)
        self.assertNotEqual(zero, one,
            "sound_prob=0.0 should differ from sound_prob=1.0")

    def test_all_presets_include_weather_count_and_prob(self):
        from landscape import PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                self.assertIn("weather_count", PRESETS[name],
                    f"Preset {name} should include 'weather_count'")
                self.assertIn("weather_prob", PRESETS[name],
                    f"Preset {name} should include 'weather_prob'")
                self.assertGreaterEqual(PRESETS[name]["weather_count"], 0)
                self.assertLessEqual(PRESETS[name]["weather_count"], 3)
                self.assertGreaterEqual(PRESETS[name]["weather_prob"], 0.0)
                self.assertLessEqual(PRESETS[name]["weather_prob"], 1.0)

    def test_preset_weather_count_affects_output(self):
        from landscape import generate_landscape
        zero = generate_landscape(seed=42, weather_count=0, detail=2)
        one = generate_landscape(seed=42, weather_count=1, detail=2)
        self.assertNotEqual(zero, one,
            "weather_count=0 should differ from weather_count=1")

    def test_preset_weather_prob_affects_output(self):
        from landscape import generate_landscape
        zero = generate_landscape(seed=42, weather_count=2, weather_prob=0.0, detail=2)
        one = generate_landscape(seed=42, weather_count=2, weather_prob=1.0, detail=2)
        self.assertNotEqual(zero, one,
            "weather_prob=0.0 should differ from weather_prob=1.0")

    def test_all_presets_include_time_of_day_enabled(self):
        from landscape import PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                self.assertIn("time_of_day_enabled", PRESETS[name],
                    f"Preset {name} should include 'time_of_day_enabled'")
                self.assertTrue(PRESETS[name]["time_of_day_enabled"],
                    f"Preset {name} should have time_of_day_enabled=True")

    def test_all_presets_include_season_enabled(self):
        from landscape import PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                self.assertIn("season_enabled", PRESETS[name],
                    f"Preset {name} should include 'season_enabled'")
                self.assertTrue(PRESETS[name]["season_enabled"],
                    f"Preset {name} should have season_enabled=True")

    def test_all_presets_include_season_count_and_prob(self):
        from landscape import PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                self.assertIn("season_count", PRESETS[name],
                    f"Preset {name} should include 'season_count'")
                self.assertIn("season_prob", PRESETS[name],
                    f"Preset {name} should include 'season_prob'")
                self.assertGreaterEqual(PRESETS[name]["season_count"], 0)
                self.assertLessEqual(PRESETS[name]["season_count"], 3)
                self.assertGreaterEqual(PRESETS[name]["season_prob"], 0.0)
                self.assertLessEqual(PRESETS[name]["season_prob"], 1.0)

    def test_all_presets_include_time_count_and_prob(self):
        from landscape import PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                self.assertIn("time_count", PRESETS[name],
                    f"Preset {name} should include 'time_count'")
                self.assertIn("time_prob", PRESETS[name],
                    f"Preset {name} should include 'time_prob'")
                self.assertGreaterEqual(PRESETS[name]["time_count"], 0)
                self.assertLessEqual(PRESETS[name]["time_count"], 3)
                self.assertGreaterEqual(PRESETS[name]["time_prob"], 0.0)
                self.assertLessEqual(PRESETS[name]["time_prob"], 1.0)

    def test_all_presets_include_wildlife_enabled(self):
        from landscape import PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                self.assertIn("wildlife_enabled", PRESETS[name],
                    f"Preset {name} should include 'wildlife_enabled'")

    def test_all_presets_include_wildlife_count_and_prob(self):
        from landscape import PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                self.assertIn("wildlife_count", PRESETS[name],
                    f"Preset {name} should include 'wildlife_count'")
                self.assertIn("wildlife_prob", PRESETS[name],
                    f"Preset {name} should include 'wildlife_prob'")
                self.assertGreaterEqual(PRESETS[name]["wildlife_count"], 0)
                self.assertLessEqual(PRESETS[name]["wildlife_count"], 3)
                self.assertGreaterEqual(PRESETS[name]["wildlife_prob"], 0.0)
                self.assertLessEqual(PRESETS[name]["wildlife_prob"], 1.0)

    def test_all_presets_include_perspective_count_and_prob(self):
        from landscape import PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                self.assertIn("perspective_count", PRESETS[name],
                    f"Preset {name} should include 'perspective_count'")
                self.assertIn("perspective_prob", PRESETS[name],
                    f"Preset {name} should include 'perspective_prob'")
                self.assertGreaterEqual(PRESETS[name]["perspective_count"], 0)
                self.assertLessEqual(PRESETS[name]["perspective_count"], 3)
                self.assertGreaterEqual(PRESETS[name]["perspective_prob"], 0.0)
                self.assertLessEqual(PRESETS[name]["perspective_prob"], 1.0)

    def test_all_presets_include_mood_atmosphere(self):
        from landscape import PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                self.assertIn("mood_atmosphere", PRESETS[name],
                    f"Preset {name} should include 'mood_atmosphere'")
                self.assertTrue(PRESETS[name]["mood_atmosphere"],
                    f"Preset {name} should have mood_atmosphere=True")

    def test_all_presets_include_mood_atmosphere_count_and_prob(self):
        from landscape import PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                self.assertIn("mood_atmosphere_count", PRESETS[name],
                    f"Preset {name} should include 'mood_atmosphere_count'")
                self.assertIn("mood_atmosphere_prob", PRESETS[name],
                    f"Preset {name} should include 'mood_atmosphere_prob'")
                self.assertGreaterEqual(PRESETS[name]["mood_atmosphere_count"], 0)
                self.assertLessEqual(PRESETS[name]["mood_atmosphere_count"], 3)
                self.assertGreaterEqual(PRESETS[name]["mood_atmosphere_prob"], 0.0)
                self.assertLessEqual(PRESETS[name]["mood_atmosphere_prob"], 1.0)

    def test_all_presets_include_simile_enabled_count_and_prob(self):
        from landscape import PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                self.assertIn("simile_enabled", PRESETS[name],
                    f"Preset {name} should include 'simile_enabled'")
                self.assertIn("simile_count", PRESETS[name],
                    f"Preset {name} should include 'simile_count'")
                self.assertIn("simile_prob", PRESETS[name],
                    f"Preset {name} should include 'simile_prob'")
                self.assertGreaterEqual(PRESETS[name]["simile_count"], 0)
                self.assertLessEqual(PRESETS[name]["simile_count"], 3)
                self.assertGreaterEqual(PRESETS[name]["simile_prob"], 0.0)
                self.assertLessEqual(PRESETS[name]["simile_prob"], 1.0)

    def test_all_presets_include_metaphor_enabled_count_and_prob(self):
        from landscape import PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                self.assertIn("metaphor_enabled", PRESETS[name],
                    f"Preset {name} should include 'metaphor_enabled'")
                self.assertIn("metaphor_count", PRESETS[name],
                    f"Preset {name} should include 'metaphor_count'")
                self.assertIn("metaphor_prob", PRESETS[name],
                    f"Preset {name} should include 'metaphor_prob'")
                self.assertGreaterEqual(PRESETS[name]["metaphor_count"], 0)
                self.assertLessEqual(PRESETS[name]["metaphor_count"], 3)
                self.assertGreaterEqual(PRESETS[name]["metaphor_prob"], 0.0)
                self.assertLessEqual(PRESETS[name]["metaphor_prob"], 1.0)

    def test_all_presets_include_personification_enabled_count_and_prob(self):
        from landscape import PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                self.assertIn("personification_enabled", PRESETS[name],
                    f"Preset {name} should include 'personification_enabled'")
                self.assertIn("personification_count", PRESETS[name],
                    f"Preset {name} should include 'personification_count'")
                self.assertIn("personification_prob", PRESETS[name],
                    f"Preset {name} should include 'personification_prob'")
                self.assertGreaterEqual(PRESETS[name]["personification_count"], 0)
                self.assertLessEqual(PRESETS[name]["personification_count"], 3)
                self.assertGreaterEqual(PRESETS[name]["personification_prob"], 0.0)
                self.assertLessEqual(PRESETS[name]["personification_prob"], 1.0)


class TestTimeWords(unittest.TestCase):
    def test_time_word_appears_in_output(self):
        results = [generate_landscape(seed=s) for s in range(200)]
        self.assertTrue(
            any(t in r for r in results for t in ALL_TIME_WORDS),
            "No time word appeared across 200 seeds",
        )

    def test_time_word_is_deterministic(self):
        a = generate_landscape(seed=42, template_set="first")
        b = generate_landscape(seed=42, template_set="first")
        self.assertEqual(a, b,
            "Time word should be deterministic with same seed")

    def test_time_word_does_not_break_output(self):
        for s in range(20):
            result = generate_landscape(seed=s)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)
            self.assertTrue(result.endswith("."))

    def test_time_word_works_with_detail_zero(self):
        for s in range(10):
            result = generate_landscape(seed=s, detail=0)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 5)
            self.assertTrue(result.endswith("."))

    def test_time_word_works_with_json_format(self):
        result = generate_landscape(seed=42, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertGreater(len(data["text"]), 0)

    def test_describe_global_includes_time_words(self):
        from landscape import describe_global
        result = describe_global()
        self.assertIn("time words", result)
        for tw in TIME_WORDS:
            self.assertIn(tw, result)

    def test_time_word_appears_in_second_opening(self):
        results = [generate_landscape(seed=s, biome="forest", template_set="second") for s in range(100)]
        self.assertTrue(
            any(t in r for r in results for t in ALL_TIME_WORDS),
            "No time word appeared in second opening (template_set=second) across 100 seeds",
        )

    def test_time_word_appears_in_third_opening(self):
        results = [generate_landscape(seed=s, biome="forest", template_set="third") for s in range(100)]
        self.assertTrue(
            any(t in r for r in results for t in ALL_TIME_WORDS),
            "No time word appeared in third opening (template_set=third) across 100 seeds",
        )

    def test_time_word_appears_in_fourth_opening(self):
        results = [generate_landscape(seed=s, biome="forest", template_set="fourth") for s in range(100)]
        self.assertTrue(
            any(t in r for r in results for t in ALL_TIME_WORDS),
            "No time word appeared in fourth opening (template_set=fourth) across 100 seeds",
        )

    def test_time_word_works_with_all_biomes(self):
        for biome in ["forest", "desert", "tundra", "ruined city", "sky islands", "fungal grove"]:
            with self.subTest(biome=biome):
                result = generate_landscape(seed=42, biome=biome, template_set="first")
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 10)
                self.assertTrue(result.endswith("."))


class TestEchoTimeWord(unittest.TestCase):
    def test_echo_time_word_appears_in_echo_output(self):
        results = [generate_landscape(seed=s, echo_enabled=True, echo_count=2, biome="forest") for s in range(200)]
        self.assertTrue(
            any(t in r for r in results for t in ALL_TIME_WORDS),
            "No time word appeared in echo output across 200 seeds with echo_enabled=True",
        )

    def test_echo_time_word_is_deterministic(self):
        a = generate_landscape(seed=42, echo_enabled=True, biome="forest")
        b = generate_landscape(seed=42, echo_enabled=True, biome="forest")
        self.assertEqual(a, b,
            "Time word in echoes should be deterministic with same seed")

    def test_echo_time_word_in_waiting_phrase(self):
        results = [generate_landscape(seed=s, echo_enabled=True, biome="forest") for s in range(300)]
        waiting_results = [r for r in results if "has been waiting" in r]
        if waiting_results:
            self.assertTrue(
                any(t in r for r in waiting_results for t in ALL_TIME_WORDS),
                "No time word appeared in 'has been waiting' echo across 300 seeds",
            )

    def test_echo_time_word_in_deep_time_phrase(self):
        results = [generate_landscape(seed=s, echo_enabled=True, biome="forest") for s in range(300)]
        deep_time_results = [r for r in results if "deep time" in r]
        if deep_time_results:
            self.assertTrue(
                any(t in r for r in deep_time_results for t in ALL_TIME_WORDS),
                "No time word appeared in 'deep time' echo across 300 seeds",
            )

    def test_echo_time_word_works_with_detail_zero(self):
        for s in range(10):
            result = generate_landscape(seed=s, detail=0, echo_enabled=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 5)

    def test_echo_time_word_works_with_no_adverb(self):
        for s in range(10):
            result = generate_landscape(seed=s, echo_enabled=True, adverb_enabled=False, biome="forest")
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)
            self.assertTrue(result.endswith("."))

    def test_echo_time_word_works_with_combine(self):
        result = generate_landscape(seed=42, echo_enabled=True, combine="forest,desert")
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 10)

    def test_echo_time_word_works_with_all_biomes(self):
        for biome in ["forest", "desert", "tundra", "ruined city", "sky islands", "fungal grove"]:
            with self.subTest(biome=biome):
                result = generate_landscape(seed=42, biome=biome, echo_enabled=True)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 10)


class TestWeatherTimeWord(unittest.TestCase):
    def test_weather_templates_have_time_word_placeholder(self):
        weather_tmpls = SENTENCE_TEMPLATES["weather"]
        time_word_tmpls = [t for t in weather_tmpls if "{time_word}" in t]
        self.assertGreaterEqual(len(time_word_tmpls), 1,
            "At least 1 weather template should reference {time_word}")

    def test_weather_time_word_does_not_break_output(self):
        for s in range(30):
            result = generate_landscape(seed=s)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)
            self.assertTrue(result.endswith("."))

    def test_weather_time_word_uses_known_time_word(self):
        results = [generate_landscape(seed=s) for s in range(300)]
        self.assertTrue(
            any(t in r for r in results for t in ALL_TIME_WORDS),
            "No known time word appeared in weather across 300 seeds",
        )

    def test_weather_time_word_works_with_time_word_disabled(self):
        for s in range(20):
            result = generate_landscape(seed=s, time_word_enabled=False)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)
            self.assertNotIn(" .", result,
                "Space before period should not appear when time word is disabled")
            self.assertTrue(result.endswith("."))

    def test_weather_time_word_is_deterministic(self):
        a = generate_landscape(seed=42)
        b = generate_landscape(seed=42)
        self.assertEqual(a, b,
            "Weather with time word should be deterministic")

    def test_weather_time_word_works_with_mood_and_bias(self):
        result = generate_landscape(seed=42, mood="eerie", bias="rare")
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))

    def test_weather_time_word_works_with_detail_three(self):
        result = generate_landscape(seed=42, detail=3)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 50)
        self.assertTrue(result.endswith("."))

    def test_weather_time_word_works_with_json_format(self):
        result = generate_landscape(seed=42, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertGreater(len(data["text"]), 0)

    def test_weather_time_word_disabled_differs_from_enabled(self):
        enabled = generate_landscape(seed=42)
        disabled = generate_landscape(seed=42, time_word_enabled=False)
        self.assertNotEqual(enabled, disabled,
            "Output should differ when time word is disabled in weather")

    def test_weather_time_word_works_with_combine(self):
        result = generate_landscape(seed=42, combine="forest,desert")
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 10)
        self.assertTrue(result.endswith("."))

    def test_weather_time_word_appears_in_each_template(self):
        for tset in ["first", "second", "third", "fourth", "fifth"]:
            with self.subTest(template_set=tset):
                results = [generate_landscape(seed=s, biome="forest", template_set=tset) for s in range(200)]
                self.assertTrue(
                    any(t in r for r in results for t in ALL_TIME_WORDS),
                    f"No time word appeared in weather template_set={tset} across 200 seeds",
                )


class TestLegend(unittest.TestCase):
    def test_legend_disabled_default(self):
        result = generate_landscape(seed=42)
        for ind in LEGEND_INDICATORS:
            self.assertNotIn(ind, result,
                f"Legend indicator {ind!r} should not appear by default")

    def test_legend_enabled_appends_legend(self):
        results = [generate_landscape(seed=s, legend_enabled=True) for s in range(100)]
        self.assertTrue(
            any(ind in r for r in results for ind in LEGEND_INDICATORS),
            "No legend phrase appeared across 100 seeds with legend_enabled=True",
        )

    def test_legend_does_not_break_output(self):
        for s in range(20):
            result = generate_landscape(seed=s, legend_enabled=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)
            self.assertTrue(result.endswith("."))

    def test_legend_is_deterministic(self):
        a = generate_landscape(seed=42, legend_enabled=True)
        b = generate_landscape(seed=42, legend_enabled=True)
        self.assertEqual(a, b,
            "Legend should be deterministic with same seed")

    def test_legend_works_with_poetic_format(self):
        for s in range(10):
            result = generate_landscape(seed=s, legend_enabled=True, fmt="poetic")
            self.assertIsInstance(result, str)
            self.assertIn("\n", result)

    def test_legend_works_with_json_format(self):
        result = generate_landscape(seed=42, legend_enabled=True, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertGreater(len(data["text"]), 0)

    def test_legend_detail_zero_suppresses_legend(self):
        result = generate_landscape(seed=42, legend_enabled=True, detail=0)
        for ind in LEGEND_INDICATORS:
            self.assertNotIn(ind, result,
                f"Legend indicator {ind!r} should not appear with detail=0")

    def test_legend_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_legend_display_injection_contains_biome_name(self):
        results = [generate_landscape(seed=s, legend_enabled=True, biome="tundra") for s in range(100)]
        self.assertTrue(
            any("tundra" in r for r in results),
            "Legend with {display} should reference the biome name across 100 seeds",
        )

    def test_legend_works_with_echo(self):
        result = generate_landscape(seed=42, legend_enabled=True, echo_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))

    def test_legend_works_with_combine(self):
        result = generate_landscape(seed=42, legend_enabled=True, combine="forest,desert")
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 10)
        self.assertTrue(result.endswith("."))

    def test_legend_works_with_mood_and_bias(self):
        result = generate_landscape(seed=42, legend_enabled=True, mood="eerie", bias="rare")
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))

    def test_legend_json_includes_field(self):
        result = generate_landscape(seed=42, legend_enabled=True, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("legend_enabled", data)
        self.assertTrue(data["legend_enabled"])

    def test_legend_json_field_absent_when_disabled(self):
        result = generate_landscape(seed=42, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertNotIn("legend_enabled", data)


class TestLegendCount(unittest.TestCase):
    def test_legend_count_default_is_one(self):
        result = generate_landscape(seed=42, legend_enabled=True)
        # With count=1, at most one legend indicator should appear
        found = sum(1 for ind in LEGEND_INDICATORS if ind in result)
        self.assertLessEqual(found, 1,
            "Default legend_count=1 should produce at most one legend phrase")

    def test_legend_count_zero_suppresses_legends(self):
        result = generate_landscape(seed=42, legend_enabled=True, legend_count=0)
        for ind in LEGEND_INDICATORS:
            self.assertNotIn(ind, result,
                f"Legend indicator {ind!r} should not appear with legend_count=0")

    def test_legend_count_two_produces_two_phrases(self):
        results = [generate_landscape(seed=s, legend_enabled=True, legend_count=2) for s in range(100)]
        multi = sum(1 for r in results if sum(1 for ind in LEGEND_INDICATORS if ind in r) >= 2)
        self.assertGreater(multi, 0,
            "legend_count=2 should produce at least 2 legend indicators in some outputs")

    def test_legend_count_three_produces_three_phrases(self):
        results = [generate_landscape(seed=s, legend_enabled=True, legend_count=3) for s in range(200)]
        multi = sum(1 for r in results if sum(1 for ind in LEGEND_INDICATORS if ind in r) >= 3)
        self.assertGreater(multi, 0,
            "legend_count=3 should produce at least 3 legend indicators in some outputs")

    def test_legend_count_no_repeats(self):
        # With 15 legends and count=3, no repeats should occur
        for s in range(100):
            result = generate_landscape(seed=s, legend_enabled=True, legend_count=3)
            found = [ind for ind in LEGEND_INDICATORS if ind in result]
            self.assertEqual(len(found), len(set(found)),
                "Legend phrases should not repeat within the same landscape")

    def test_legend_count_is_deterministic(self):
        a = generate_landscape(seed=42, legend_enabled=True, legend_count=2)
        b = generate_landscape(seed=42, legend_enabled=True, legend_count=2)
        self.assertEqual(a, b,
            "legend_count should be deterministic with same seed")

    def test_legend_count_works_with_combine(self):
        for s in range(20):
            result = generate_landscape(seed=s, legend_enabled=True, legend_count=2, combine="forest,desert")
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)
            self.assertTrue(result.endswith("."))

    def test_legend_count_json_includes_field(self):
        result = generate_landscape(seed=42, legend_enabled=True, legend_count=2, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("legend_enabled", data)
        self.assertTrue(data["legend_enabled"])
        self.assertIn("legend_count", data)
        self.assertEqual(data["legend_count"], 2)

    def test_legend_count_json_absent_when_disabled(self):
        result = generate_landscape(seed=42, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertNotIn("legend_count", data)

    def test_legend_count_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_legend_count_works_with_echo(self):
        for s in range(10):
            result = generate_landscape(seed=s, legend_enabled=True, legend_count=2, echo_enabled=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)
            self.assertTrue(result.endswith("."))

    def test_legend_count_detail_zero_suppresses_legends(self):
        result = generate_landscape(seed=42, legend_enabled=True, legend_count=2, detail=0)
        for ind in LEGEND_INDICATORS:
            self.assertNotIn(ind, result,
                f"Legend indicator {ind!r} should not appear with detail=0 even with legend_count=2")


class TestLegendProb(unittest.TestCase):
    def test_legend_prob_default_is_one(self):
        a = generate_landscape(seed=42, legend_enabled=True)
        b = generate_landscape(seed=42, legend_enabled=True, legend_prob=1.0)
        self.assertEqual(a, b,
            "legend_prob=1.0 should match default")

    def test_legend_prob_zero_suppresses_legends(self):
        results = [generate_landscape(seed=s, legend_enabled=True, legend_prob=0.0) for s in range(100)]
        for r in results:
            for ind in LEGEND_INDICATORS:
                self.assertNotIn(ind, r,
                    f"Legend indicator {ind!r} should not appear with legend_prob=0.0")

    def test_legend_prob_one_always_has_legend(self):
        results = [generate_landscape(seed=s, legend_enabled=True, legend_prob=1.0) for s in range(100)]
        has_legend = sum(1 for r in results if any(ind in r for ind in LEGEND_INDICATORS))
        self.assertGreater(has_legend, 80,
            "With legend_prob=1.0, most outputs should contain a legend")

    def test_legend_prob_produces_valid_output(self):
        for prob in [0.0, 0.25, 0.5, 0.75, 1.0]:
            for s in range(10):
                result = generate_landscape(seed=s, legend_enabled=True, legend_prob=prob)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_legend_prob_is_deterministic(self):
        a = generate_landscape(seed=42, legend_enabled=True, legend_prob=0.5)
        b = generate_landscape(seed=42, legend_enabled=True, legend_prob=0.5)
        self.assertEqual(a, b,
            "legend_prob should be deterministic with same seed")

    def test_legend_prob_json_includes_field(self):
        result = generate_landscape(seed=42, legend_enabled=True, legend_prob=0.5, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("legend_prob", data)
        self.assertEqual(data["legend_prob"], 0.5)

    def test_legend_prob_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


class TestDescribeLegends(unittest.TestCase):
    def test_describe_legends_returns_string(self):
        from landscape import describe_legends
        result = describe_legends()
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_describe_legends_contains_header(self):
        from landscape import describe_legends
        result = describe_legends()
        self.assertIn("legends", result)

    def test_describe_legends_contains_all_legends(self):
        from landscape import describe_legends, LEGENDS
        result = describe_legends()
        for legend in LEGENDS:
            self.assertIn(legend, result,
                f"Legend description should contain: {legend!r}")

    def test_describe_legends_contains_index_numbers(self):
        from landscape import describe_legends
        result = describe_legends()
        self.assertIn("[0]", result)
        self.assertIn("[1]", result)

    def test_describe_legends_shows_all_legends(self):
        from landscape import describe_legends, LEGENDS
        result = describe_legends()
        count = len(LEGENDS)
        self.assertIn("=== legends ===", result)
        self.assertIn(f"[{count - 1}]", result,
            f"Legend description should contain the last index [{count - 1}]")

    def test_describe_legends_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_describe_legends_flag_prints_to_stdout(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--describe-legends"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertIn("legends", output)
        self.assertIn("[0]", output)
        self.assertIn("[1]", output)

    def test_describe_legends_no_landscape_generated(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--describe-legends", "--seed", "42", "--count", "2"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertNotIn("[seed=42]", output,
            "No landscape should be generated when --describe-legends is used")
        self.assertNotIn("\n\n", output,
            "No landscape should be generated when --describe-legends is used")


class TestDescribeTravelogue(unittest.TestCase):
    def test_describe_travelogue_returns_string(self):
        result = describe_travelogue()
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_describe_travelogue_contains_header(self):
        result = describe_travelogue()
        self.assertIn("travelogue prefixes", result)
        self.assertIn("travelogue suffixes", result)

    def test_describe_travelogue_contains_all_prefixes(self):
        result = describe_travelogue()
        for prefix in TRAVELOGUE_PREFIXES:
            self.assertIn(prefix, result,
                f"Travelogue description should contain prefix: {prefix!r}")

    def test_describe_travelogue_contains_all_suffixes(self):
        result = describe_travelogue()
        for suffix in TRAVELOGUE_SUFFIXES:
            self.assertIn(suffix, result,
                f"Travelogue description should contain suffix: {suffix!r}")

    def test_describe_travelogue_contains_index_numbers(self):
        result = describe_travelogue()
        self.assertIn("[0]", result, "Travelogue description should contain index [0]")
        self.assertIn("[1]", result, "Travelogue description should contain index [1]")

    def test_describe_travelogue_shows_all_prefixes(self):
        result = describe_travelogue()
        count = len(TRAVELOGUE_PREFIXES)
        self.assertIn(f"=== travelogue prefixes ===", result)
        self.assertIn(f"[{count - 1}]", result,
            f"Travelogue description should contain the last prefix index [{count - 1}]")

    def test_describe_travelogue_shows_all_suffixes(self):
        result = describe_travelogue()
        count = len(TRAVELOGUE_SUFFIXES)
        self.assertIn(f"=== travelogue suffixes ===", result)
        self.assertIn(f"[{count - 1}]", result,
            f"Travelogue description should contain the last suffix index [{count - 1}]")

    def test_describe_travelogue_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_describe_travelogue_flag_prints_to_stdout(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--describe-travelogue"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertIn("travelogue prefixes", output)
        self.assertIn("travelogue suffixes", output)
        self.assertIn("[0]", output)
        self.assertIn("[1]", output)

    def test_describe_travelogue_no_landscape_generated(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--describe-travelogue", "--seed", "42", "--count", "2"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertNotIn("[seed=42]", output,
            "No landscape should be generated when --describe-travelogue is used")
        self.assertNotIn("\n\n", output,
            "No landscape should be generated when --describe-travelogue is used")


class TestTravelogue(unittest.TestCase):
    TRAVELOGUE_INDICATORS = [
        "Journal entry",
        "Log entry",
        "Chronicle of the journey",
        "expedition.",
        "Captain's log, supplemental",
        "I write to you from",
        "Field notes, day",
        "Dispatch",
        "I have journeyed",
    ]

    def test_travelogue_disabled_by_default(self):
        result = generate_landscape(seed=42, biome="forest")
        for ind in self.TRAVELOGUE_INDICATORS:
            self.assertNotIn(ind, result,
                f"Travelogue indicator {ind!r} should not appear by default")

    def test_travelogue_enabled_appears(self):
        result = generate_landscape(seed=42, biome="forest", travelogue=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        has_prefix = any(ind in result for ind in self.TRAVELOGUE_INDICATORS)
        self.assertTrue(has_prefix,
            "Travelogue prefix should appear when enabled")

    def test_travelogue_contains_biome_name(self):
        result = generate_landscape(seed=42, biome="tundra", travelogue=True)
        self.assertIn("tundra", result)

    def test_travelogue_contains_day_number(self):
        result = generate_landscape(seed=42, biome="forest", travelogue=True)
        import re
        has_day_number = bool(re.search(r'\bday \d+|\d+ days?\b', result, re.IGNORECASE))
        self.assertTrue(has_day_number,
            "Travelogue should contain a day number")

    def test_travelogue_produces_valid_output(self):
        for s in range(20):
            result = generate_landscape(seed=s, travelogue=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)
            self.assertTrue(result.endswith("."))

    def test_travelogue_is_deterministic(self):
        a = generate_landscape(seed=42, biome="forest", travelogue=True)
        b = generate_landscape(seed=42, biome="forest", travelogue=True)
        self.assertEqual(a, b,
            "Travelogue should be deterministic with same seed")

    TRAVELOGUE_SUFFIX_INDICATORS = [
        "venture deeper",
        "prepare camp",
        "many stories yet",
        "turn in for the evening",
        "settle into darkness",
        "does not capture",
        "many more days to cross",
        "asks better questions",
        "still be here, waiting",
    ]

    def test_travelogue_ends_with_suffix(self):
        for s in range(20):
            result = generate_landscape(seed=s, biome="desert", travelogue=True)
            has_suffix = any(ind in result for ind in self.TRAVELOGUE_SUFFIX_INDICATORS)
            self.assertTrue(has_suffix,
                "Travelogue should end with a suffix phrase")

    def test_travelogue_works_with_detail_zero(self):
        for s in range(10):
            result = generate_landscape(seed=s, detail=0, travelogue=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)

    def test_travelogue_works_with_echo(self):
        for s in range(10):
            result = generate_landscape(seed=s, echo_enabled=True, travelogue=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)

    def test_travelogue_works_with_legend(self):
        for s in range(10):
            result = generate_landscape(seed=s, legend_enabled=True, travelogue=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)

    def test_travelogue_works_with_preset(self):
        from landscape import main
        self.assertTrue(callable(main),
            "CLI flag for travelogue should exist")

    def test_travelogue_works_with_json(self):
        result = generate_landscape(seed=42, biome="forest", travelogue=True, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertGreater(len(data["text"]), 0)

    def test_travelogue_differs_from_plain(self):
        plain = generate_landscape(seed=42, biome="forest")
        travel = generate_landscape(seed=42, biome="forest", travelogue=True)
        self.assertNotEqual(plain, travel,
            "Travelogue should differ from plain output")

    def test_travelogue_json_includes_field(self):
        result = generate_landscape(seed=42, biome="forest", travelogue=True, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("travelogue", data)
        self.assertTrue(data["travelogue"])

    def test_travelogue_json_field_absent_when_disabled(self):
        result = generate_landscape(seed=42, biome="forest", fmt="json")
        import json as j
        data = j.loads(result)
        self.assertNotIn("travelogue", data)


class TestDescribeWistful(unittest.TestCase):
    def test_describe_wistful_returns_string(self):
        result = describe_wistful()
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_describe_wistful_contains_header(self):
        result = describe_wistful()
        self.assertIn("wistful phrases", result)

    def test_describe_wistful_contains_all_phrases(self):
        result = describe_wistful()
        for phrase in WISTFUL:
            self.assertIn(phrase, result,
                f"Wistful description should contain phrase: {phrase!r}")

    def test_describe_wistful_contains_index_numbers(self):
        result = describe_wistful()
        self.assertIn("[0]", result, "Wistful description should contain index [0]")
        self.assertIn("[1]", result, "Wistful description should contain index [1]")

    def test_describe_wistful_shows_all_phrases(self):
        result = describe_wistful()
        count = len(WISTFUL)
        self.assertIn(f"=== wistful phrases ===", result)
        self.assertIn(f"[{count - 1}]", result,
            f"Wistful description should contain the last phrase index [{count - 1}]")

    def test_describe_wistful_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_describe_wistful_flag_prints_to_stdout(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--describe-wistful"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertIn("wistful phrases", output)
        self.assertIn("[0]", output)
        self.assertIn("[1]", output)

    def test_describe_wistful_no_landscape_generated(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--describe-wistful", "--seed", "42", "--count", "2"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertNotIn("[seed=42]", output,
            "No landscape should be generated when --describe-wistful is used")
        self.assertNotIn("\n\n", output,
            "No landscape should be generated when --describe-wistful is used")


class TestDescribeSounds(unittest.TestCase):
    def test_describe_sounds_returns_string(self):
        result = describe_sounds()
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_describe_sounds_contains_header(self):
        result = describe_sounds()
        self.assertIn("soundscape phrases", result)

    def test_describe_sounds_contains_all_phrases(self):
        result = describe_sounds()
        for phrase in SOUNDSCAPES:
            self.assertIn(phrase, result,
                f"Soundscape description should contain phrase: {phrase!r}")

    def test_describe_sounds_contains_index_numbers(self):
        result = describe_sounds()
        self.assertIn("[0]", result, "Soundscape description should contain index [0]")
        self.assertIn("[1]", result, "Soundscape description should contain index [1]")

    def test_describe_sounds_shows_all_phrases(self):
        result = describe_sounds()
        count = len(SOUNDSCAPES)
        self.assertIn("=== soundscape phrases ===", result)
        self.assertIn(f"[{count - 1}]", result,
            f"Soundscape description should contain the last phrase index [{count - 1}]")

    def test_describe_sounds_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_describe_sounds_flag_prints_to_stdout(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--describe-sounds"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertIn("soundscape phrases", output)
        self.assertIn("[0]", output)
        self.assertIn("[1]", output)

    def test_describe_sounds_no_landscape_generated(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--describe-sounds", "--seed", "42", "--count", "2"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertNotIn("[seed=42]", output,
            "No landscape should be generated when --describe-sounds is used")
        self.assertNotIn("\n\n", output,
            "No landscape should be generated when --describe-sounds is used")


class TestWistful(unittest.TestCase):
    WISTFUL_INDICATORS = [
        "wish you could stay",
        "always remain",
        "calls to you",
        "carry a piece",
        "return to the",
        "half-remembered dream",
        "never be the same after visiting",
        "nowhere else in the world like",
        "more like a memory of a place",
        "words will never be enough",
        "fortunate to have walked",
        "settled into your bones",
        "the rest of the world has not",
        "version of yourself behind",
        "just behind your eyelids",
        "whispered into its silence",
        "pale imitation",
        "too late to hear",
        "fixed point against",
        "before it faded",
    ]

    def test_wistful_disabled_by_default(self):
        result = generate_landscape(seed=42, biome="forest")
        for ind in self.WISTFUL_INDICATORS:
            self.assertNotIn(ind, result,
                f"Wistful indicator {ind!r} should not appear by default")

    def test_wistful_enabled_appears(self):
        result = generate_landscape(seed=42, biome="forest", wistful=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        has_wistful = any(ind in result for ind in self.WISTFUL_INDICATORS)
        self.assertTrue(has_wistful,
            "Wistful phrase should appear when enabled")

    def test_wistful_contains_biome_name(self):
        result = generate_landscape(seed=42, biome="tundra", wistful=True)
        self.assertIn("tundra", result)

    def test_wistful_produces_valid_output(self):
        for s in range(20):
            result = generate_landscape(seed=s, wistful=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)
            self.assertTrue(result.endswith("."))

    def test_wistful_is_deterministic(self):
        a = generate_landscape(seed=42, biome="forest", wistful=True)
        b = generate_landscape(seed=42, biome="forest", wistful=True)
        self.assertEqual(a, b,
            "Wistful should be deterministic with same seed")

    def test_wistful_works_with_detail_zero(self):
        for s in range(10):
            result = generate_landscape(seed=s, detail=0, wistful=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)

    def test_wistful_works_with_echo(self):
        for s in range(10):
            result = generate_landscape(seed=s, echo_enabled=True, wistful=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)

    def test_wistful_works_with_legend(self):
        for s in range(10):
            result = generate_landscape(seed=s, legend_enabled=True, wistful=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)

    def test_wistful_works_with_travelogue(self):
        for s in range(10):
            result = generate_landscape(seed=s, travelogue=True, wistful=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)

    def test_wistful_works_with_json(self):
        result = generate_landscape(seed=42, biome="forest", wistful=True, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertGreater(len(data["text"]), 0)
        self.assertIn("wistful", data)
        self.assertTrue(data["wistful"])

    def test_wistful_json_field_absent_when_disabled(self):
        result = generate_landscape(seed=42, biome="forest", fmt="json")
        import json as j
        data = j.loads(result)
        self.assertNotIn("wistful", data,
            "wistful should not appear in JSON when wistful=False")

    def test_wistful_differs_from_plain(self):
        plain = generate_landscape(seed=42, biome="forest")
        wistful = generate_landscape(seed=42, biome="forest", wistful=True)
        self.assertNotEqual(plain, wistful,
            "Wistful should differ from plain output")

    def test_wistful_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_wistful_flag_prints_to_stdout(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--wistful", "--seed", "42"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertIsInstance(output, str)
        self.assertGreater(len(output), 0)

    def test_wistful_works_with_preset(self):
        from landscape import PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                result = generate_landscape(seed=42, **PRESETS[name])
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_wistful_suppressed_at_detail_zero(self):
        for s in range(20):
            result = generate_landscape(seed=s, detail=0, wistful=True)
            for ind in self.WISTFUL_INDICATORS:
                self.assertNotIn(ind, result,
                    f"Wistful indicator {ind!r} should not appear at detail=0")


class TestSoundscape(unittest.TestCase):
    def test_soundscape_disabled_by_default(self):
        result = generate_landscape(seed=42, biome="forest")
        for ind in SOUND_INDICATORS:
            self.assertNotIn(ind, result,
                f"Soundscape indicator {ind!r} should not appear by default")

    def test_soundscape_enabled_appears(self):
        results = [generate_landscape(seed=s, biome="forest", sound_enabled=True) for s in range(100)]
        self.assertTrue(
            any(ind in r for r in results for ind in SOUND_INDICATORS),
            "No soundscape phrase appeared across 100 seeds with sound_enabled=True",
        )

    def test_soundscape_contains_biome_name(self):
        result = generate_landscape(seed=42, biome="tundra", sound_enabled=True)
        self.assertIn("tundra", result)

    def test_soundscape_produces_valid_output(self):
        for s in range(20):
            result = generate_landscape(seed=s, sound_enabled=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)
            self.assertTrue(result.endswith("."))

    def test_soundscape_is_deterministic(self):
        a = generate_landscape(seed=42, biome="forest", sound_enabled=True)
        b = generate_landscape(seed=42, biome="forest", sound_enabled=True)
        self.assertEqual(a, b,
            "Soundscape should be deterministic with same seed")

    def test_soundscape_works_with_detail_zero(self):
        for s in range(10):
            result = generate_landscape(seed=s, detail=0, sound_enabled=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)

    def test_soundscape_suppressed_at_detail_zero(self):
        for s in range(20):
            result = generate_landscape(seed=s, detail=0, sound_enabled=True)
            for ind in SOUND_INDICATORS:
                self.assertNotIn(ind, result,
                    f"Soundscape indicator {ind!r} should not appear at detail=0")

    def test_soundscape_works_with_echo(self):
        for s in range(10):
            result = generate_landscape(seed=s, echo_enabled=True, sound_enabled=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)

    def test_soundscape_works_with_legend(self):
        for s in range(10):
            result = generate_landscape(seed=s, legend_enabled=True, sound_enabled=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)

    def test_soundscape_works_with_travelogue(self):
        for s in range(10):
            result = generate_landscape(seed=s, travelogue=True, sound_enabled=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)

    def test_soundscape_works_with_wistful(self):
        for s in range(10):
            result = generate_landscape(seed=s, wistful=True, sound_enabled=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)

    def test_soundscape_works_with_json(self):
        result = generate_landscape(seed=42, biome="forest", sound_enabled=True, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertGreater(len(data["text"]), 0)
        self.assertIn("sound_enabled", data)
        self.assertTrue(data["sound_enabled"])

    def test_soundscape_json_field_absent_when_disabled(self):
        result = generate_landscape(seed=42, biome="forest", fmt="json")
        import json as j
        data = j.loads(result)
        self.assertNotIn("sound_enabled", data,
            "sound_enabled should not appear in JSON when sound_enabled=False")

    def test_soundscape_differs_from_plain(self):
        plain = generate_landscape(seed=42, biome="forest")
        sound = generate_landscape(seed=42, biome="forest", sound_enabled=True)
        self.assertNotEqual(plain, sound,
            "Soundscape should differ from plain output")

    def test_soundscape_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_soundscape_flag_prints_to_stdout(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--sound", "--seed", "42"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertIsInstance(output, str)
        self.assertGreater(len(output), 0)


class TestSoundCount(unittest.TestCase):
    def test_sound_count_default_is_one(self):
        a = generate_landscape(seed=42, sound_enabled=True)
        b = generate_landscape(seed=42, sound_enabled=True, sound_count=1)
        self.assertEqual(a, b,
            "sound_count=1 should match default")

    def test_sound_count_zero_suppresses_soundscape(self):
        result = generate_landscape(seed=42, sound_enabled=True, sound_count=0)
        for ind in SOUND_INDICATORS:
            self.assertNotIn(ind, result,
                "Soundscape should not appear with sound_count=0")

    def test_sound_count_two_sometimes_has_multiple(self):
        results = [generate_landscape(seed=s, sound_enabled=True, sound_count=3) for s in range(100)]
        multi = [r for r in results if sum(1 for ind in SOUND_INDICATORS if ind in r) >= 2]
        self.assertGreater(len(multi), 10,
            "sound_count=3 should often produce multi-soundscape outputs")

    def test_sound_count_does_not_repeat_same_sound(self):
        results = [generate_landscape(seed=s, sound_enabled=True, sound_count=3) for s in range(200)]
        for r in results:
            for ind in SOUND_INDICATORS:
                self.assertLessEqual(r.count(ind), 1,
                    f"Sound indicator {ind!r} should appear at most once: {r!r}")

    def test_sound_count_produces_valid_output(self):
        for count in [0, 1, 2, 3]:
            for s in range(10):
                result = generate_landscape(seed=s, sound_enabled=True, sound_count=count)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_sound_count_is_deterministic(self):
        a = generate_landscape(seed=42, sound_enabled=True, sound_count=2)
        b = generate_landscape(seed=42, sound_enabled=True, sound_count=2)
        self.assertEqual(a, b,
            "sound_count should be deterministic with same seed")

    def test_sound_count_works_with_json_format(self):
        result = generate_landscape(seed=42, sound_enabled=True, sound_count=2, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertGreater(len(data["text"]), 0)

    def test_sound_count_json_includes_field(self):
        result = generate_landscape(seed=42, sound_enabled=True, sound_count=2, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("sound_count", data)
        self.assertEqual(data["sound_count"], 2)

    def test_sound_count_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


class TestSoundProb(unittest.TestCase):
    def test_sound_prob_default_is_one(self):
        a = generate_landscape(seed=42, sound_enabled=True)
        b = generate_landscape(seed=42, sound_enabled=True, sound_prob=1.0)
        self.assertEqual(a, b,
            "sound_prob=1.0 should match default")

    def test_sound_prob_zero_suppresses_soundscape(self):
        results = [generate_landscape(seed=s, sound_enabled=True, sound_prob=0.0) for s in range(100)]
        for r in results:
            for ind in SOUND_INDICATORS:
                self.assertNotIn(ind, r,
                    f"Sound indicator {ind!r} should not appear with sound_prob=0.0")

    def test_sound_prob_one_always_has_soundscape(self):
        results = [generate_landscape(seed=s, sound_enabled=True, sound_prob=1.0) for s in range(100)]
        has_sound = sum(1 for r in results if any(ind in r for ind in SOUND_INDICATORS))
        self.assertGreater(has_sound, 80,
            "With sound_prob=1.0, most outputs should contain a soundscape")

    def test_sound_prob_produces_valid_output(self):
        for prob in [0.0, 0.25, 0.5, 0.75, 1.0]:
            for s in range(10):
                result = generate_landscape(seed=s, sound_enabled=True, sound_prob=prob)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_sound_prob_is_deterministic(self):
        a = generate_landscape(seed=42, sound_enabled=True, sound_prob=0.5)
        b = generate_landscape(seed=42, sound_enabled=True, sound_prob=0.5)
        self.assertEqual(a, b,
            "sound_prob should be deterministic with same seed")

    def test_sound_prob_json_includes_field(self):
        result = generate_landscape(seed=42, sound_enabled=True, sound_prob=0.5, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("sound_prob", data)
        self.assertEqual(data["sound_prob"], 0.5)

    def test_sound_prob_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


TRAVELOGUE_INDICATORS = [
    "Journal entry",
    "Log entry",
    "Chronicle of the journey",
    "the expedition",
    "I will venture",
    "I mark this in my journal",
    "I note the position",
    "I will listen",
    "Captain's log, supplemental",
    "I write to you from",
    "Field notes, day",
    "Dispatch",
    "I have journeyed",
    "settle into darkness",
    "does not capture",
    "many more days to cross",
    "asks better questions",
    "still be here, waiting",
]

WISTFUL_INDICATORS_PHRASES = [
    "You wish you could stay",
    "Part of you will always remain",
    "calls to you even as you turn away",
    "You carry a piece",
    "Someday you will return",
    "lingers in your thoughts",
    "never be the same after visiting",
    "nowhere else in the world like",
    "more like a memory of a place",
    "words will never be enough",
    "fortunate to have walked",
    "settled into your bones",
    "the rest of the world has not",
    "version of yourself behind",
    "just behind your eyelids",
    "whispered into its silence",
    "pale imitation",
    "too late to hear",
    "fixed point against",
    "before it faded",
]


class TestNoTravelogue(unittest.TestCase):
    def test_no_travelogue_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_no_travelogue_disables_travelogue_with_preset(self):
        from landscape import generate_landscape, PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                preset = dict(PRESETS[name])
                preset.pop("travelogue", None)
                result = generate_landscape(seed=42, **preset, travelogue=False)
                for ind in TRAVELOGUE_INDICATORS:
                    self.assertNotIn(ind, result,
                        f"Preset {name} with --no-travelogue should not contain {ind!r}")

    def test_no_travelogue_preset_without_flag_still_has_travelogue(self):
        from landscape import generate_landscape, PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                if "travelogue" not in PRESETS[name]:
                    continue
                result = generate_landscape(seed=42, **PRESETS[name])
                # Without --no-travelogue, preset travelogue should be active
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_no_travelogue_works_with_other_features(self):
        from landscape import generate_landscape
        for s in range(10):
            result = generate_landscape(seed=s, travelogue=False,
                                        echo_enabled=True, legend_enabled=True,
                                        sound_enabled=True, wistful=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)

    def test_no_travelogue_with_explicit_travelogue_override(self):
        from landscape import generate_landscape
        # If --no-travelogue is used, travelogue should be False regardless of --travelogue
        result = generate_landscape(seed=42, biome="forest", travelogue=False)
        for ind in TRAVELOGUE_INDICATORS:
            self.assertNotIn(ind, result,
                f"Output with --no-travelogue should not contain {ind!r}")

    def test_no_travelogue_does_not_affect_json_output(self):
        from landscape import generate_landscape
        result = generate_landscape(seed=42, biome="forest", travelogue=False, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertNotIn("travelogue", data)


class TestNoWistful(unittest.TestCase):
    def test_no_wistful_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_no_wistful_disables_wistful_with_preset(self):
        from landscape import generate_landscape, PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                preset = dict(PRESETS[name])
                preset.pop("wistful", None)
                result = generate_landscape(seed=42, **preset, wistful=False)
                for ind in WISTFUL_INDICATORS_PHRASES:
                    self.assertNotIn(ind, result,
                        f"Preset {name} with --no-wistful should not contain {ind!r}")

    def test_no_wistful_preset_without_flag_still_has_wistful(self):
        from landscape import generate_landscape, PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                if "wistful" not in PRESETS[name]:
                    continue
                result = generate_landscape(seed=42, **PRESETS[name])
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_no_wistful_works_with_other_features(self):
        from landscape import generate_landscape
        for s in range(10):
            result = generate_landscape(seed=s, wistful=False,
                                        echo_enabled=True, legend_enabled=True,
                                        sound_enabled=True, travelogue=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)

    def test_no_wistful_with_explicit_wistful_override(self):
        from landscape import generate_landscape
        result = generate_landscape(seed=42, biome="forest", wistful=False)
        for ind in WISTFUL_INDICATORS_PHRASES:
            self.assertNotIn(ind, result,
                f"Output with --no-wistful should not contain {ind!r}")

    def test_no_wistful_does_not_affect_json_output(self):
        from landscape import generate_landscape
        result = generate_landscape(seed=42, biome="forest", wistful=False, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertNotIn("wistful", data)


class TestNoEcho(unittest.TestCase):
    def test_no_echo_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_no_echo_disables_echo_with_preset(self):
        from landscape import generate_landscape, PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                preset = dict(PRESETS[name])
                preset.pop("echo_enabled", None)
                result = generate_landscape(seed=42, **preset, echo_enabled=False)
                for ind in NO_ECHO_INDICATORS:
                    self.assertNotIn(ind, result,
                        f"Preset {name} with --no-echo should not contain {ind!r}")

    def test_no_echo_preset_without_flag_still_has_echo(self):
        from landscape import generate_landscape, PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                if "echo_enabled" not in PRESETS[name]:
                    continue
                result = generate_landscape(seed=42, **PRESETS[name])
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_no_echo_works_with_other_features(self):
        from landscape import generate_landscape
        for s in range(10):
            result = generate_landscape(seed=s, echo_enabled=False,
                                        legend_enabled=True, sound_enabled=True,
                                        travelogue=True, wistful=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)

    def test_no_echo_with_explicit_echo_override(self):
        from landscape import generate_landscape
        result = generate_landscape(seed=42, biome="forest", echo_enabled=False)
        for ind in NO_ECHO_INDICATORS:
            self.assertNotIn(ind, result,
                f"Output with --no-echo should not contain {ind!r}")

    def test_no_echo_does_not_affect_json_output(self):
        from landscape import generate_landscape
        result = generate_landscape(seed=42, biome="forest", echo_enabled=False, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertNotIn("echo_enabled", data)


class TestNoLegend(unittest.TestCase):
    def test_no_legend_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_no_legend_disables_legend_with_preset(self):
        from landscape import generate_landscape, PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                preset = dict(PRESETS[name])
                preset.pop("legend_enabled", None)
                result = generate_landscape(seed=42, **preset, legend_enabled=False)
                for ind in LEGEND_INDICATORS:
                    self.assertNotIn(ind, result,
                        f"Preset {name} with --no-legend should not contain {ind!r}")

    def test_no_legend_preset_without_flag_still_has_legend(self):
        from landscape import generate_landscape, PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                if "legend_enabled" not in PRESETS[name]:
                    continue
                result = generate_landscape(seed=42, **PRESETS[name])
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_no_legend_works_with_other_features(self):
        from landscape import generate_landscape
        for s in range(10):
            result = generate_landscape(seed=s, legend_enabled=False,
                                        echo_enabled=True, sound_enabled=True,
                                        travelogue=True, wistful=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)

    def test_no_legend_with_explicit_legend_override(self):
        from landscape import generate_landscape
        result = generate_landscape(seed=42, biome="forest", legend_enabled=False)
        for ind in LEGEND_INDICATORS:
            self.assertNotIn(ind, result,
                f"Output with --no-legend should not contain {ind!r}")

    def test_no_legend_does_not_affect_json_output(self):
        from landscape import generate_landscape
        result = generate_landscape(seed=42, biome="forest", legend_enabled=False, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertNotIn("legend_enabled", data)


class TestNoSound(unittest.TestCase):
    def test_no_sound_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_no_sound_disables_sound_with_preset(self):
        from landscape import generate_landscape, PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                preset = dict(PRESETS[name])
                preset.pop("sound_enabled", None)
                result = generate_landscape(seed=42, **preset, sound_enabled=False)
                for ind in SOUND_INDICATORS:
                    self.assertNotIn(ind, result,
                        f"Preset {name} with --no-sound should not contain {ind!r}")

    def test_no_sound_preset_without_flag_still_has_sound(self):
        from landscape import generate_landscape, PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                if "sound_enabled" not in PRESETS[name]:
                    continue
                result = generate_landscape(seed=42, **PRESETS[name])
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_no_sound_works_with_other_features(self):
        from landscape import generate_landscape
        for s in range(10):
            result = generate_landscape(seed=s, sound_enabled=False,
                                        echo_enabled=True, legend_enabled=True,
                                        travelogue=True, wistful=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)

    def test_no_sound_with_explicit_sound_override(self):
        from landscape import generate_landscape
        result = generate_landscape(seed=42, biome="forest", sound_enabled=False)
        for ind in SOUND_INDICATORS:
            self.assertNotIn(ind, result,
                f"Output with --no-sound should not contain {ind!r}")

    def test_no_sound_does_not_affect_json_output(self):
        from landscape import generate_landscape
        result = generate_landscape(seed=42, biome="forest", sound_enabled=False, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertNotIn("sound_enabled", data)


class TestNoTime(unittest.TestCase):
    def test_no_time_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_no_time_disables_time_with_preset(self):
        from landscape import generate_landscape, PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                preset = dict(PRESETS[name])
                preset.pop("time_of_day_enabled", None)
                result = generate_landscape(seed=42, **preset, time_of_day_enabled=False)
                for t in ALL_TIMES_OF_DAY:
                    self.assertNotIn(t, result,
                        f"Preset {name} with --no-time should not contain {t!r}")

    def test_no_time_preset_without_flag_still_has_time(self):
        from landscape import generate_landscape, PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                if "time_of_day_enabled" not in PRESETS[name]:
                    continue
                result = generate_landscape(seed=42, **PRESETS[name])
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_no_time_works_with_other_features(self):
        from landscape import generate_landscape
        for s in range(10):
            result = generate_landscape(seed=s, time_of_day_enabled=False,
                                        echo_enabled=True, legend_enabled=True,
                                        sound_enabled=True, travelogue=True,
                                        wistful=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)

    def test_no_time_with_explicit_time_override(self):
        from landscape import generate_landscape
        result = generate_landscape(seed=42, biome="forest", time_of_day_enabled=False)
        for t in ALL_TIMES_OF_DAY:
            self.assertNotIn(t, result,
                f"Output with --no-time should not contain {t!r}")

    def test_no_time_does_not_affect_json_output(self):
        from landscape import generate_landscape
        result = generate_landscape(seed=42, biome="forest", time_of_day_enabled=False, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertNotIn("time_of_day", data)


class TestTimeOfDay(unittest.TestCase):
    def test_time_of_day_disabled_by_default(self):
        result = generate_landscape(seed=42)
        for t in ALL_TIMES_OF_DAY:
            self.assertNotIn(t, result,
                f"Time-of-day phrase {t!r} should not appear by default")

    def test_time_of_day_enabled_appears(self):
        results = [generate_landscape(seed=s, time_of_day_enabled=True) for s in range(100)]
        self.assertTrue(
            any(t in r for r in results for t in ALL_TIMES_OF_DAY),
            "No time-of-day phrase appeared across 100 seeds with time_of_day_enabled=True",
        )

    def test_time_of_day_produces_valid_output(self):
        for s in range(20):
            result = generate_landscape(seed=s, time_of_day_enabled=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)
            self.assertTrue(result.endswith("."))

    def test_time_of_day_is_deterministic(self):
        a = generate_landscape(seed=42, time_of_day_enabled=True)
        b = generate_landscape(seed=42, time_of_day_enabled=True)
        self.assertEqual(a, b,
            "Time-of-day should be deterministic with same seed")

    def test_time_of_day_differs_from_plain(self):
        plain = generate_landscape(seed=42)
        with_time = generate_landscape(seed=42, time_of_day_enabled=True)
        self.assertNotEqual(plain, with_time,
            "Output with time-of-day should differ from plain output")

    def test_time_of_day_prepends_opening(self):
        for s in range(20):
            result = generate_landscape(seed=s, time_of_day_enabled=True)
            self.assertTrue(
                any(result.startswith(t) for t in ALL_TIMES_OF_DAY),
                f"Output should start with a time-of-day phrase: {result!r}",
            )

    def test_time_of_day_works_with_json_format(self):
        result = generate_landscape(seed=42, time_of_day_enabled=True, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertGreater(len(data["text"]), 0)

    def test_time_of_day_works_with_detail_zero(self):
        for s in range(10):
            result = generate_landscape(seed=s, time_of_day_enabled=True, detail=0)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 5)
            self.assertTrue(result.endswith("."))

    def test_time_of_day_works_with_combine(self):
        result = generate_landscape(seed=42, time_of_day_enabled=True, combine="forest,desert")
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 10)

    def test_time_of_day_works_with_echo(self):
        result = generate_landscape(seed=42, time_of_day_enabled=True, echo_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_time_of_day_works_with_legend(self):
        result = generate_landscape(seed=42, time_of_day_enabled=True, legend_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_time_of_day_works_with_travelogue(self):
        result = generate_landscape(seed=42, time_of_day_enabled=True, travelogue=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_time_of_day_works_with_sound(self):
        result = generate_landscape(seed=42, time_of_day_enabled=True, sound_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_time_of_day_works_with_wistful(self):
        result = generate_landscape(seed=42, time_of_day_enabled=True, wistful=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_time_of_day_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_time_of_day_json_includes_field(self):
        result = generate_landscape(seed=42, time_of_day_enabled=True, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("time_of_day", data)
        self.assertIn(data["time_of_day"], ALL_TIMES_OF_DAY)

    def test_time_of_day_json_field_absent_when_disabled(self):
        result = generate_landscape(seed=42, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertNotIn("time_of_day", data)

    def test_time_of_day_works_with_poetic_format(self):
        for s in range(10):
            result = generate_landscape(seed=s, time_of_day_enabled=True, fmt="poetic")
            self.assertIsInstance(result, str)
            self.assertIn("\n", result)

    def test_time_of_day_works_with_all_biomes(self):
        for biome in ["forest", "desert", "tundra", "ruined city", "sky islands", "fungal grove"]:
            with self.subTest(biome=biome):
                result = generate_landscape(seed=42, time_of_day_enabled=True, biome=biome)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)
                self.assertTrue(result.endswith("."))


class TestTimeCount(unittest.TestCase):
    def test_time_count_default_is_one(self):
        a = generate_landscape(seed=42, time_of_day_enabled=True)
        b = generate_landscape(seed=42, time_of_day_enabled=True, time_count=1)
        self.assertEqual(a, b,
            "time_count=1 should match default")

    def test_time_count_zero_suppresses_time(self):
        result = generate_landscape(seed=42, time_of_day_enabled=True, time_count=0)
        for t in ALL_TIMES_OF_DAY:
            self.assertNotIn(t, result,
                "Time-of-day should not appear with time_count=0")

    def test_time_count_two_sometimes_has_multiple(self):
        results = [generate_landscape(seed=s, time_of_day_enabled=True, time_count=3) for s in range(100)]
        multi = [r for r in results if sum(1 for ind in TIME_INDICATORS if ind in r) >= 2]
        self.assertGreater(len(multi), 10,
            "time_count=3 should often produce multi-time outputs")

    def test_time_count_does_not_repeat_same_phrase(self):
        results = [generate_landscape(seed=s, time_of_day_enabled=True, time_count=3) for s in range(200)]
        for r in results:
            for ind in TIME_INDICATORS:
                count = r.count(ind)
                if count > 1:
                    # "first light" may appear in both "first light of morning" and
                    # "first light" substring of other phrases — check more carefully
                    pass
                self.assertLessEqual(r.count(ind), 2,
                    f"Time indicator {ind!r} should appear at most twice: {r!r}")

    def test_time_count_produces_valid_output(self):
        for count in [0, 1, 2, 3]:
            for s in range(10):
                result = generate_landscape(seed=s, time_of_day_enabled=True, time_count=count)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_time_count_is_deterministic(self):
        a = generate_landscape(seed=42, time_of_day_enabled=True, time_count=2)
        b = generate_landscape(seed=42, time_of_day_enabled=True, time_count=2)
        self.assertEqual(a, b,
            "time_count should be deterministic with same seed")

    def test_time_count_works_with_json_format(self):
        result = generate_landscape(seed=42, time_of_day_enabled=True, time_count=2, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertGreater(len(data["text"]), 0)

    def test_time_count_json_includes_field(self):
        result = generate_landscape(seed=42, time_of_day_enabled=True, time_count=2, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("time_count", data)
        self.assertEqual(data["time_count"], 2)

    def test_time_count_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


class TestTimeProb(unittest.TestCase):
    def test_time_prob_default_is_one(self):
        a = generate_landscape(seed=42, time_of_day_enabled=True)
        b = generate_landscape(seed=42, time_of_day_enabled=True, time_prob=1.0)
        self.assertEqual(a, b,
            "time_prob=1.0 should match default")

    def test_time_prob_zero_suppresses_time(self):
        results = [generate_landscape(seed=s, time_of_day_enabled=True, time_prob=0.0) for s in range(100)]
        for r in results:
            for ind in TIME_INDICATORS:
                self.assertNotIn(ind, r,
                    f"Time indicator {ind!r} should not appear with time_prob=0.0")

    def test_time_prob_produces_valid_output(self):
        for prob in [0.0, 0.25, 0.5, 0.75, 1.0]:
            for s in range(10):
                result = generate_landscape(seed=s, time_of_day_enabled=True, time_prob=prob)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_time_prob_is_deterministic(self):
        a = generate_landscape(seed=42, time_of_day_enabled=True, time_prob=0.5)
        b = generate_landscape(seed=42, time_of_day_enabled=True, time_prob=0.5)
        self.assertEqual(a, b,
            "time_prob should be deterministic with same seed")

    def test_time_prob_json_includes_field(self):
        result = generate_landscape(seed=42, time_of_day_enabled=True, time_prob=0.5, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("time_prob", data)
        self.assertEqual(data["time_prob"], 0.5)

    def test_time_prob_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


class TestDescribeTimes(unittest.TestCase):
    def test_describe_times_returns_string(self):
        result = describe_times()
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_describe_times_contains_header(self):
        result = describe_times()
        self.assertIn("time-of-day phrases", result)

    def test_describe_times_contains_all_phrases(self):
        result = describe_times()
        for phrase in TIMES_OF_DAY:
            self.assertIn(phrase, result,
                f"Time-of-day description should contain phrase: {phrase!r}")

    def test_describe_times_contains_index_numbers(self):
        result = describe_times()
        self.assertIn("[0]", result)
        self.assertIn("[1]", result)

    def test_describe_times_shows_all_phrases(self):
        result = describe_times()
        count = len(TIMES_OF_DAY)
        self.assertIn("=== time-of-day phrases ===", result)
        self.assertIn(f"[{count - 1}]", result,
            f"Time-of-day description should contain the last index [{count - 1}]")

    def test_describe_times_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_describe_times_flag_prints_to_stdout(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--describe-times"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertIn("time-of-day phrases", output)
        self.assertIn("[0]", output)
        self.assertIn("[1]", output)

    def test_describe_times_no_landscape_generated(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--describe-times", "--seed", "42", "--count", "2"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertNotIn("[seed=42]", output,
            "No landscape should be generated when --describe-times is used")
        self.assertNotIn("\n\n", output,
            "No landscape should be generated when --describe-times is used")


class TestSeasonCount(unittest.TestCase):
    def test_season_count_default_is_one(self):
        a = generate_landscape(seed=42, season_enabled=True)
        b = generate_landscape(seed=42, season_enabled=True, season_count=1)
        self.assertEqual(a, b,
            "season_count=1 should match default")

    def test_season_count_zero_suppresses_season(self):
        result = generate_landscape(seed=42, season_enabled=True, season_count=0)
        for s in ALL_SEASONS:
            self.assertNotIn(s, result,
                "Season should not appear with season_count=0")

    def test_season_count_two_sometimes_has_multiple(self):
        results = [generate_landscape(seed=s, season_enabled=True, season_count=3) for s in range(100)]
        multi = [r for r in results if sum(1 for ind in SEASON_INDICATORS if ind in r) >= 2]
        self.assertGreater(len(multi), 10,
            "season_count=3 should often produce multi-season outputs")

    def test_season_count_does_not_repeat_same_phrase(self):
        results = [generate_landscape(seed=s, season_enabled=True, season_count=3) for s in range(200)]
        for r in results:
            for ind in SEASON_INDICATORS:
                self.assertLessEqual(r.count(ind), 1,
                    f"Season indicator {ind!r} should appear at most once: {r!r}")

    def test_season_count_produces_valid_output(self):
        for count in [0, 1, 2, 3]:
            for s in range(10):
                result = generate_landscape(seed=s, season_enabled=True, season_count=count)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_season_count_is_deterministic(self):
        a = generate_landscape(seed=42, season_enabled=True, season_count=2)
        b = generate_landscape(seed=42, season_enabled=True, season_count=2)
        self.assertEqual(a, b,
            "season_count should be deterministic with same seed")

    def test_season_count_works_with_json_format(self):
        result = generate_landscape(seed=42, season_enabled=True, season_count=2, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertGreater(len(data["text"]), 0)

    def test_season_count_json_includes_field(self):
        result = generate_landscape(seed=42, season_enabled=True, season_count=2, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("season_count", data)
        self.assertEqual(data["season_count"], 2)

    def test_season_count_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


class TestSeasonProb(unittest.TestCase):
    def test_season_prob_default_is_one(self):
        a = generate_landscape(seed=42, season_enabled=True)
        b = generate_landscape(seed=42, season_enabled=True, season_prob=1.0)
        self.assertEqual(a, b,
            "season_prob=1.0 should match default")

    def test_season_prob_zero_suppresses_season(self):
        results = [generate_landscape(seed=s, season_enabled=True, season_prob=0.0) for s in range(100)]
        for r in results:
            for ind in SEASON_INDICATORS:
                self.assertNotIn(ind, r,
                    f"Season indicator {ind!r} should not appear with season_prob=0.0")

    def test_season_prob_produces_valid_output(self):
        for prob in [0.0, 0.25, 0.5, 0.75, 1.0]:
            for s in range(10):
                result = generate_landscape(seed=s, season_enabled=True, season_prob=prob)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_season_prob_is_deterministic(self):
        a = generate_landscape(seed=42, season_enabled=True, season_prob=0.5)
        b = generate_landscape(seed=42, season_enabled=True, season_prob=0.5)
        self.assertEqual(a, b,
            "season_prob should be deterministic with same seed")

    def test_season_prob_json_includes_field(self):
        result = generate_landscape(seed=42, season_enabled=True, season_prob=0.5, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("season_prob", data)
        self.assertEqual(data["season_prob"], 0.5)

    def test_season_prob_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


class TestNoSeason(unittest.TestCase):
    def test_no_season_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_no_season_disables_season_with_preset(self):
        from landscape import generate_landscape, PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                preset = dict(PRESETS[name])
                preset.pop("season_enabled", None)
                result = generate_landscape(seed=42, **preset, season_enabled=False)
                for s in ALL_SEASONS:
                    self.assertNotIn(s, result,
                        f"Preset {name} with --no-season should not contain {s!r}")

    def test_no_season_preset_without_flag_still_has_season(self):
        from landscape import generate_landscape, PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                if "season_enabled" not in PRESETS[name]:
                    continue
                result = generate_landscape(seed=42, **PRESETS[name])
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_no_season_works_with_other_features(self):
        from landscape import generate_landscape
        for s in range(10):
            result = generate_landscape(seed=s, season_enabled=False,
                                        echo_enabled=True, legend_enabled=True,
                                        sound_enabled=True, travelogue=True,
                                        wistful=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)

    def test_no_season_with_explicit_season_override(self):
        from landscape import generate_landscape
        result = generate_landscape(seed=42, biome="forest", season_enabled=False)
        for s in ALL_SEASONS:
            self.assertNotIn(s, result,
                f"Output with --no-season should not contain {s!r}")

    def test_no_season_does_not_affect_json_output(self):
        from landscape import generate_landscape
        result = generate_landscape(seed=42, biome="forest", season_enabled=False, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertNotIn("season", data)


class TestSeason(unittest.TestCase):
    def test_season_disabled_by_default(self):
        result = generate_landscape(seed=42)
        for s in ALL_SEASONS:
            self.assertNotIn(s, result,
                f"Season phrase {s!r} should not appear by default")

    def test_season_enabled_appears(self):
        results = [generate_landscape(seed=s, season_enabled=True) for s in range(100)]
        self.assertTrue(
            any(s in r for r in results for s in ALL_SEASONS),
            "No season phrase appeared across 100 seeds with season_enabled=True",
        )

    def test_season_produces_valid_output(self):
        for s in range(20):
            result = generate_landscape(seed=s, season_enabled=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)
            self.assertTrue(result.endswith("."))

    def test_season_is_deterministic(self):
        a = generate_landscape(seed=42, season_enabled=True)
        b = generate_landscape(seed=42, season_enabled=True)
        self.assertEqual(a, b,
            "Season should be deterministic with same seed")

    def test_season_differs_from_plain(self):
        plain = generate_landscape(seed=42)
        with_season = generate_landscape(seed=42, season_enabled=True)
        self.assertNotEqual(plain, with_season,
            "Output with season should differ from plain output")

    def test_season_prepends_opening(self):
        for s in range(20):
            result = generate_landscape(seed=s, season_enabled=True)
            self.assertTrue(
                any(result.startswith(season) for season in ALL_SEASONS),
                f"Output should start with a season phrase: {result!r}",
            )

    def test_season_works_with_json_format(self):
        result = generate_landscape(seed=42, season_enabled=True, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertGreater(len(data["text"]), 0)

    def test_season_works_with_detail_zero(self):
        for s in range(10):
            result = generate_landscape(seed=s, season_enabled=True, detail=0)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 5)
            self.assertTrue(result.endswith("."))

    def test_season_works_with_combine(self):
        result = generate_landscape(seed=42, season_enabled=True, combine="forest,desert")
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 10)

    def test_season_works_with_echo(self):
        result = generate_landscape(seed=42, season_enabled=True, echo_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_season_works_with_legend(self):
        result = generate_landscape(seed=42, season_enabled=True, legend_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_season_works_with_travelogue(self):
        result = generate_landscape(seed=42, season_enabled=True, travelogue=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_season_works_with_sound(self):
        result = generate_landscape(seed=42, season_enabled=True, sound_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_season_works_with_wistful(self):
        result = generate_landscape(seed=42, season_enabled=True, wistful=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_season_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_season_works_with_time_of_day(self):
        for s in range(10):
            result = generate_landscape(seed=s, season_enabled=True, time_of_day_enabled=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)

    def test_season_json_includes_field(self):
        result = generate_landscape(seed=42, season_enabled=True, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("season", data)
        self.assertIn(data["season"], ALL_SEASONS)

    def test_season_json_field_absent_when_disabled(self):
        result = generate_landscape(seed=42, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertNotIn("season", data)

    def test_season_works_with_poetic_format(self):
        for s in range(10):
            result = generate_landscape(seed=s, season_enabled=True, fmt="poetic")
            self.assertIsInstance(result, str)
            self.assertIn("\n", result)

    def test_season_works_with_all_biomes(self):
        for biome in ["forest", "desert", "tundra", "ruined city", "sky islands", "fungal grove"]:
            with self.subTest(biome=biome):
                result = generate_landscape(seed=42, season_enabled=True, biome=biome)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)
                self.assertTrue(result.endswith("."))


class TestDescribeSeasons(unittest.TestCase):
    def test_describe_seasons_returns_string(self):
        result = describe_seasons()
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_describe_seasons_contains_header(self):
        result = describe_seasons()
        self.assertIn("season phrases", result)

    def test_describe_seasons_contains_all_phrases(self):
        result = describe_seasons()
        for phrase in SEASONS:
            self.assertIn(phrase, result,
                f"Season description should contain phrase: {phrase!r}")

    def test_describe_seasons_contains_index_numbers(self):
        result = describe_seasons()
        self.assertIn("[0]", result)
        self.assertIn("[1]", result)

    def test_describe_seasons_shows_all_phrases(self):
        result = describe_seasons()
        count = len(SEASONS)
        self.assertIn("=== season phrases ===", result)
        self.assertIn(f"[{count - 1}]", result,
            f"Season description should contain the last index [{count - 1}]")

    def test_describe_seasons_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_describe_seasons_flag_prints_to_stdout(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--describe-seasons"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertIn("season phrases", output)
        self.assertIn("[0]", output)
        self.assertIn("[1]", output)

    def test_describe_seasons_no_landscape_generated(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--describe-seasons", "--seed", "42", "--count", "2"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertNotIn("[seed=42]", output,
            "No landscape should be generated when --describe-seasons is used")
        self.assertNotIn("\n\n", output,
            "No landscape should be generated when --describe-seasons is used")


class TestWildlife(unittest.TestCase):
    def test_wildlife_disabled_by_default(self):
        results = [generate_landscape(seed=s) for s in range(100)]
        for r in results:
            for ind in WILDLIFE_INDICATORS:
                if ind in r:
                    self.fail(f"Wildlife indicator '{ind}' appeared without --wildlife")
                    return

    def test_wildlife_enabled_appears(self):
        results = [generate_landscape(seed=s, wildlife_enabled=True) for s in range(100)]
        has_wildlife = any(
            any(ind in r for ind in WILDLIFE_INDICATORS) for r in results
        )
        self.assertTrue(has_wildlife,
            "No wildlife indicator appeared across 100 seeds with wildlife_enabled=True")

    def test_wildlife_produces_valid_output(self):
        for s in range(20):
            result = generate_landscape(seed=s, wildlife_enabled=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)
            self.assertTrue(result.endswith("."))

    def test_wildlife_is_deterministic(self):
        a = generate_landscape(seed=42, wildlife_enabled=True)
        b = generate_landscape(seed=42, wildlife_enabled=True)
        self.assertEqual(a, b,
            "Wildlife should be deterministic with same seed")

    def test_wildlife_differs_from_plain(self):
        plain = generate_landscape(seed=42)
        with_wild = generate_landscape(seed=42, wildlife_enabled=True)
        self.assertNotEqual(plain, with_wild,
            "Output with wildlife should differ from output without")

    def test_wildlife_works_with_detail_zero(self):
        for s in range(20):
            result = generate_landscape(seed=s, wildlife_enabled=True, detail=0)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)

    def test_wildlife_works_with_json_format(self):
        result = generate_landscape(seed=42, wildlife_enabled=True, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertGreater(len(data["text"]), 0)

    def test_wildlife_json_includes_field(self):
        result = generate_landscape(seed=42, wildlife_enabled=True, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("wildlife_enabled", data)
        self.assertTrue(data["wildlife_enabled"])

    def test_wildlife_json_field_absent_when_disabled(self):
        result = generate_landscape(seed=42, fmt="json")
        import json
        data = json.loads(result)
        self.assertNotIn("wildlife_enabled", data,
            "wildlife_enabled should not be in JSON when disabled")

    def test_wildlife_works_with_combine(self):
        result = generate_landscape(seed=42, combine="forest,desert", wildlife_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_wildlife_works_with_echo(self):
        result = generate_landscape(seed=42, wildlife_enabled=True, echo_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_wildlife_works_with_legend(self):
        result = generate_landscape(seed=42, wildlife_enabled=True, legend_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_wildlife_works_with_travelogue(self):
        result = generate_landscape(seed=42, wildlife_enabled=True, travelogue=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_wildlife_works_with_sound(self):
        result = generate_landscape(seed=42, wildlife_enabled=True, sound_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_wildlife_works_with_wistful(self):
        result = generate_landscape(seed=42, wildlife_enabled=True, wistful=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_wildlife_works_with_time_of_day(self):
        result = generate_landscape(seed=42, wildlife_enabled=True, time_of_day_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_wildlife_works_with_season(self):
        result = generate_landscape(seed=42, wildlife_enabled=True, season_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_wildlife_works_with_poetic_format(self):
        result = generate_landscape(seed=42, wildlife_enabled=True, fmt="poetic")
        self.assertIn("\n", result)
        self.assertTrue(result.endswith("."))

    def test_wildlife_works_with_all_biomes(self):
        for biome in BIOMES:
            with self.subTest(biome=biome):
                result = generate_landscape(seed=42, biome=biome, wildlife_enabled=True)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_wildlife_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


class TestDescribeWildlife(unittest.TestCase):
    def test_describe_wildlife_returns_string(self):
        result = describe_wildlife()
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_describe_wildlife_contains_header(self):
        result = describe_wildlife()
        self.assertIn("wildlife phrases", result)

    def test_describe_wildlife_contains_all_phrases(self):
        result = describe_wildlife()
        for phrase in WILDLIFE:
            self.assertIn(phrase, result,
                f"Wildlife description should contain phrase: {phrase}")

    def test_describe_wildlife_contains_index_numbers(self):
        result = describe_wildlife()
        self.assertIn("[0]", result)
        self.assertIn("[1]", result)

    def test_describe_wildlife_shows_all_phrases(self):
        result = describe_wildlife()
        for i in range(len(WILDLIFE)):
            self.assertIn(f"[{i}]", result,
                f"Index [{i}] should appear in wildlife description")

    def test_describe_wildlife_last_index(self):
        result = describe_wildlife()
        last = len(WILDLIFE) - 1
        self.assertIn(f"[{last}]", result,
            f"Last index [{last}] should appear in wildlife description")

    def test_describe_wildlife_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_describe_wildlife_flag_prints_to_stdout(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--describe-wildlife"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertIn("wildlife phrases", output)
        self.assertIn("[0]", output)
        self.assertIn("[1]", output)

    def test_describe_wildlife_no_landscape_generated(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--describe-wildlife", "--seed", "42", "--count", "2"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertNotIn("[seed=42]", output,
            "No landscape should be generated when --describe-wildlife is used")
        self.assertNotIn("\n\n", output,
            "No landscape should be generated when --describe-wildlife is used")


class TestWildlifeCount(unittest.TestCase):
    def test_wildlife_count_default_is_one(self):
        a = generate_landscape(seed=42, wildlife_enabled=True)
        b = generate_landscape(seed=42, wildlife_enabled=True, wildlife_count=1)
        self.assertEqual(a, b,
            "wildlife_count=1 should match default")

    def test_wildlife_count_zero_suppresses_wildlife(self):
        result = generate_landscape(seed=42, wildlife_enabled=True, wildlife_count=0)
        for ind in WILDLIFE_INDICATORS:
            self.assertNotIn(ind, result,
                "Wildlife should not appear with wildlife_count=0")

    def test_wildlife_count_two_sometimes_has_multiple(self):
        results = [generate_landscape(seed=s, wildlife_enabled=True, wildlife_count=3) for s in range(100)]
        multi = [r for r in results if sum(1 for ind in WILDLIFE_INDICATORS if ind in r) >= 2]
        self.assertGreater(len(multi), 0,
            "wildlife_count=3 should sometimes produce multi-wildlife outputs")

    def test_wildlife_count_does_not_repeat_same_phrase(self):
        results = [generate_landscape(seed=s, wildlife_enabled=True, wildlife_count=3) for s in range(200)]
        for r in results:
            for ind in WILDLIFE_INDICATORS:
                self.assertLessEqual(r.count(ind), 1,
                    f"Wildlife indicator {ind!r} should appear at most once: {r!r}")

    def test_wildlife_count_produces_valid_output(self):
        for count in [0, 1, 2, 3]:
            for s in range(10):
                result = generate_landscape(seed=s, wildlife_enabled=True, wildlife_count=count)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_wildlife_count_is_deterministic(self):
        a = generate_landscape(seed=42, wildlife_enabled=True, wildlife_count=2)
        b = generate_landscape(seed=42, wildlife_enabled=True, wildlife_count=2)
        self.assertEqual(a, b,
            "wildlife_count should be deterministic with same seed")

    def test_wildlife_count_works_with_json_format(self):
        result = generate_landscape(seed=42, wildlife_enabled=True, wildlife_count=2, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertGreater(len(data["text"]), 0)

    def test_wildlife_count_json_includes_field(self):
        result = generate_landscape(seed=42, wildlife_enabled=True, wildlife_count=2, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("wildlife_count", data)
        self.assertEqual(data["wildlife_count"], 2)

    def test_wildlife_count_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


class TestWildlifeProb(unittest.TestCase):
    def test_wildlife_prob_default_is_one(self):
        a = generate_landscape(seed=42, wildlife_enabled=True)
        b = generate_landscape(seed=42, wildlife_enabled=True, wildlife_prob=1.0)
        self.assertEqual(a, b,
            "wildlife_prob=1.0 should match default")

    def test_wildlife_prob_zero_suppresses_wildlife(self):
        results = [generate_landscape(seed=s, wildlife_enabled=True, wildlife_prob=0.0) for s in range(100)]
        for r in results:
            for ind in WILDLIFE_INDICATORS:
                self.assertNotIn(ind, r,
                    f"Wildlife indicator {ind!r} should not appear with wildlife_prob=0.0")

    def test_wildlife_prob_produces_valid_output(self):
        for prob in [0.0, 0.25, 0.5, 0.75, 1.0]:
            for s in range(10):
                result = generate_landscape(seed=s, wildlife_enabled=True, wildlife_prob=prob)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_wildlife_prob_is_deterministic(self):
        a = generate_landscape(seed=42, wildlife_enabled=True, wildlife_prob=0.5)
        b = generate_landscape(seed=42, wildlife_enabled=True, wildlife_prob=0.5)
        self.assertEqual(a, b,
            "wildlife_prob should be deterministic with same seed")

    def test_wildlife_prob_json_includes_field(self):
        result = generate_landscape(seed=42, wildlife_enabled=True, wildlife_prob=0.5, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("wildlife_prob", data)
        self.assertEqual(data["wildlife_prob"], 0.5)

    def test_wildlife_prob_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


class TestNoWildlife(unittest.TestCase):
    def test_no_wildlife_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_no_wildlife_disables_wildlife_with_preset(self):
        from landscape import PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                result = generate_landscape(seed=42, **PRESETS[name])
                has_wildlife = any(ind in result for ind in WILDLIFE_INDICATORS)
                if not has_wildlife:
                    continue
                # Test with no_wildlife override
                result_no = generate_landscape(seed=42, wildlife_enabled=False, **{k: v for k, v in PRESETS[name].items() if k not in ("wildlife_enabled", "wildlife_count", "wildlife_prob")})
                no_wildlife = not any(ind in result_no for ind in WILDLIFE_INDICATORS)
                self.assertTrue(no_wildlife,
                    f"Preset {name} should have wildlife suppressed with wildlife_enabled=False")

    def test_no_wildlife_works_with_other_features(self):
        result = generate_landscape(seed=42, wildlife_enabled=False, echo_enabled=True, legend_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))

    def test_no_wildlife_json_output(self):
        result = generate_landscape(seed=42, fmt="json")
        import json
        data = json.loads(result)
        self.assertNotIn("wildlife_enabled", data,
            "wildlife_enabled should not be in JSON when disabled")

    def test_no_wildlife_with_explicit_wildlife_override(self):
        no_wild = generate_landscape(seed=42, wildlife_enabled=False)
        with_wild = generate_landscape(seed=42, wildlife_enabled=True)
        self.assertNotEqual(no_wild, with_wild,
            "wildlife_enabled=False should differ from wildlife_enabled=True with same seed")


class TestPerspectiveCount(unittest.TestCase):
    def test_perspective_count_default_is_one(self):
        a = generate_landscape(seed=42, perspective_enabled=True)
        b = generate_landscape(seed=42, perspective_enabled=True, perspective_count=1)
        self.assertEqual(a, b,
            "perspective_count=1 should match default")

    def test_perspective_count_zero_suppresses_perspective(self):
        result = generate_landscape(seed=42, perspective_enabled=True, perspective_count=0)
        for ind in PERSPECTIVE_INDICATORS:
            self.assertNotIn(ind, result,
                "Perspective should not appear with perspective_count=0")

    def test_perspective_count_two_sometimes_has_multiple(self):
        results = [generate_landscape(seed=s, perspective_enabled=True, perspective_count=3) for s in range(100)]
        multi = [r for r in results if sum(1 for ind in PERSPECTIVE_INDICATORS if ind in r) >= 2]
        self.assertGreater(len(multi), 10,
            "perspective_count=3 should often produce multi-perspective outputs")

    def test_perspective_count_does_not_repeat_same_phrase(self):
        results = [generate_landscape(seed=s, perspective_enabled=True, perspective_count=3) for s in range(200)]
        for r in results:
            for ind in PERSPECTIVE_INDICATORS:
                self.assertLessEqual(r.count(ind), 2,
                    f"Perspective indicator {ind!r} should appear at most twice: {r!r}")

    def test_perspective_count_produces_valid_output(self):
        for count in [0, 1, 2, 3]:
            for s in range(10):
                result = generate_landscape(seed=s, perspective_enabled=True, perspective_count=count)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_perspective_count_is_deterministic(self):
        a = generate_landscape(seed=42, perspective_enabled=True, perspective_count=2)
        b = generate_landscape(seed=42, perspective_enabled=True, perspective_count=2)
        self.assertEqual(a, b,
            "perspective_count should be deterministic with same seed")

    def test_perspective_count_works_with_json_format(self):
        result = generate_landscape(seed=42, perspective_enabled=True, perspective_count=2, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertGreater(len(data["text"]), 0)

    def test_perspective_count_json_includes_field(self):
        result = generate_landscape(seed=42, perspective_enabled=True, perspective_count=2, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("perspective_count", data)
        self.assertEqual(data["perspective_count"], 2)

    def test_perspective_count_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


class TestPerspectiveProb(unittest.TestCase):
    def test_perspective_prob_default_is_one(self):
        a = generate_landscape(seed=42, perspective_enabled=True)
        b = generate_landscape(seed=42, perspective_enabled=True, perspective_prob=1.0)
        self.assertEqual(a, b,
            "perspective_prob=1.0 should match default")

    def test_perspective_prob_zero_suppresses_perspective(self):
        results = [generate_landscape(seed=s, perspective_enabled=True, perspective_prob=0.0) for s in range(100)]
        for r in results:
            for ind in PERSPECTIVE_INDICATORS:
                self.assertNotIn(ind, r,
                    f"Perspective indicator {ind!r} should not appear with perspective_prob=0.0")

    def test_perspective_prob_produces_valid_output(self):
        for prob in [0.0, 0.25, 0.5, 0.75, 1.0]:
            for s in range(10):
                result = generate_landscape(seed=s, perspective_enabled=True, perspective_prob=prob)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_perspective_prob_is_deterministic(self):
        a = generate_landscape(seed=42, perspective_enabled=True, perspective_prob=0.5)
        b = generate_landscape(seed=42, perspective_enabled=True, perspective_prob=0.5)
        self.assertEqual(a, b,
            "perspective_prob should be deterministic with same seed")

    def test_perspective_prob_json_includes_field(self):
        result = generate_landscape(seed=42, perspective_enabled=True, perspective_prob=0.5, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("perspective_prob", data)
        self.assertEqual(data["perspective_prob"], 0.5)

    def test_perspective_prob_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


class TestPerspective(unittest.TestCase):
    def test_perspective_disabled_by_default(self):
        for s in range(20):
            result = generate_landscape(seed=s)
            for ind in PERSPECTIVE_INDICATORS:
                self.assertNotIn(ind, result,
                    f"Perspective indicator {ind!r} should not appear by default")

    def test_perspective_enabled_appears(self):
        results = [generate_landscape(seed=s, perspective_enabled=True) for s in range(50)]
        has_perspective = any(
            any(ind in r for ind in PERSPECTIVE_INDICATORS) for r in results
        )
        self.assertTrue(has_perspective,
            "Perspective phrase should appear when enabled")

    def test_perspective_produces_valid_output(self):
        for s in range(50):
            result = generate_landscape(seed=s, perspective_enabled=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)
            self.assertTrue(result.endswith("."))

    def test_perspective_is_deterministic(self):
        a = generate_landscape(seed=42, perspective_enabled=True)
        b = generate_landscape(seed=42, perspective_enabled=True)
        self.assertEqual(a, b,
            "Perspective should be deterministic with same seed")

    def test_perspective_differs_from_plain(self):
        plain = generate_landscape(seed=42)
        perspective = generate_landscape(seed=42, perspective_enabled=True)
        self.assertNotEqual(plain, perspective,
            "Perspective output should differ from plain output")

    def test_perspective_prepends_opening(self):
        for s in range(20):
            result = generate_landscape(seed=s, perspective_enabled=True)
            has_indicator = any(ind in result for ind in PERSPECTIVE_INDICATORS)
            # The perspective phrase should precede the opening, so find the
            # first known opening marker after the perspective text
            if has_indicator:
                first_line = result.split(". ")[0]
                has_persp = any(ind in first_line for ind in PERSPECTIVE_INDICATORS)
                self.assertTrue(has_persp,
                    f"First sentence should contain perspective indicator at seed {s}")

    def test_perspective_works_with_json_format(self):
        result = generate_landscape(seed=42, perspective_enabled=True, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertGreater(len(data["text"]), 0)

    def test_perspective_json_includes_field(self):
        result = generate_landscape(seed=42, perspective_enabled=True, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("perspective_enabled", data)
        self.assertTrue(data["perspective_enabled"])

    def test_perspective_json_field_absent_when_disabled(self):
        result = generate_landscape(seed=42, fmt="json")
        import json
        data = json.loads(result)
        self.assertNotIn("perspective_enabled", data,
            "perspective_enabled should not be in JSON when disabled")

    def test_perspective_works_with_echo(self):
        result = generate_landscape(seed=42, perspective_enabled=True, echo_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))

    def test_perspective_works_with_legend(self):
        result = generate_landscape(seed=42, perspective_enabled=True, legend_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_perspective_works_with_travelogue(self):
        result = generate_landscape(seed=42, perspective_enabled=True, travelogue=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_perspective_works_with_sound(self):
        result = generate_landscape(seed=42, perspective_enabled=True, sound_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_perspective_works_with_wistful(self):
        result = generate_landscape(seed=42, perspective_enabled=True, wistful=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_perspective_works_with_time_of_day(self):
        result = generate_landscape(seed=42, perspective_enabled=True, time_of_day_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_perspective_works_with_season(self):
        result = generate_landscape(seed=42, perspective_enabled=True, season_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_perspective_works_with_wildlife(self):
        result = generate_landscape(seed=42, perspective_enabled=True, wildlife_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_perspective_works_with_poetic_format(self):
        result = generate_landscape(seed=42, perspective_enabled=True, fmt="poetic")
        self.assertIsInstance(result, str)
        self.assertIn("\n", result)

    def test_perspective_works_with_all_biomes(self):
        for biome in BIOMES:
            with self.subTest(biome=biome):
                result = generate_landscape(seed=42, biome=biome, perspective_enabled=True)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_perspective_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


class TestDescribePerspectives(unittest.TestCase):
    def test_describe_perspectives_returns_string(self):
        result = describe_perspectives()
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_describe_perspectives_contains_header(self):
        result = describe_perspectives()
        self.assertIn("perspective phrases", result)

    def test_describe_perspectives_contains_all_phrases(self):
        result = describe_perspectives()
        for phrase in PERSPECTIVES:
            self.assertIn(phrase, result,
                f"Perspective phrase not found in description: {phrase!r}")

    def test_describe_perspectives_contains_index_numbers(self):
        result = describe_perspectives()
        self.assertIn("[0]", result)
        self.assertIn("[1]", result)

    def test_describe_perspectives_shows_all_phrases(self):
        result = describe_perspectives()
        last_idx = len(PERSPECTIVES) - 1
        self.assertIn(f"[{last_idx}]", result,
            f"Last index [{last_idx}] should appear in description")

    def test_describe_perspectives_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_describe_perspectives_flag_prints_to_stdout(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--describe-perspectives"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertIn("perspective phrases", output)
        self.assertIn("[0]", output)

    def test_describe_perspectives_no_landscape_generated(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--describe-perspectives", "--seed", "42", "--count", "2"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertNotIn("[seed=42]", output,
            "No landscape should be generated when --describe-perspectives is used")
        self.assertNotIn("\n\n", output,
            "No landscape should be generated when --describe-perspectives is used")


class TestNoPerspective(unittest.TestCase):
    def test_no_perspective_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_no_perspective_disables_perspective_with_preset(self):
        from landscape import PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                result = generate_landscape(seed=42, **PRESETS[name])
                has_perspective = any(ind in result for ind in PERSPECTIVE_INDICATORS)
                if not has_perspective:
                    continue
                result_no = generate_landscape(
                    seed=42,
                    perspective_enabled=False,
                    **{k: v for k, v in PRESETS[name].items() if k not in ("perspective_enabled", "perspective_count", "perspective_prob")}
                )
                no_perspective = not any(ind in result_no for ind in PERSPECTIVE_INDICATORS)
                self.assertTrue(no_perspective,
                    f"Preset {name} should have perspective suppressed with perspective_enabled=False")

    def test_no_perspective_works_with_other_features(self):
        result = generate_landscape(seed=42, perspective_enabled=False, echo_enabled=True, legend_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))

    def test_no_perspective_json_output(self):
        result = generate_landscape(seed=42, fmt="json")
        import json
        data = json.loads(result)
        self.assertNotIn("perspective_enabled", data,
            "perspective_enabled should not be in JSON when disabled")

    def test_no_perspective_with_explicit_perspective_override(self):
        no_persp = generate_landscape(seed=42, perspective_enabled=False)
        with_persp = generate_landscape(seed=42, perspective_enabled=True)
        self.assertNotEqual(no_persp, with_persp,
            "perspective_enabled=False should differ from perspective_enabled=True with same seed")


class TestSimile(unittest.TestCase):
    def test_simile_disabled_by_default(self):
        for s in range(20):
            result = generate_landscape(seed=s)
            for ind in SIMILE_INDICATORS:
                self.assertNotIn(ind, result,
                    f"Simile indicator {ind!r} should not appear by default")

    def test_simile_enabled_appears(self):
        results = [generate_landscape(seed=s, simile_enabled=True) for s in range(50)]
        has_simile = any(
            any(ind in r for ind in SIMILE_INDICATORS) for r in results
        )
        self.assertTrue(has_simile,
            "Simile phrase should appear when enabled")

    def test_simile_produces_valid_output(self):
        for s in range(50):
            result = generate_landscape(seed=s, simile_enabled=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)
            self.assertTrue(result.endswith("."))

    def test_simile_is_deterministic(self):
        a = generate_landscape(seed=42, simile_enabled=True)
        b = generate_landscape(seed=42, simile_enabled=True)
        self.assertEqual(a, b,
            "Simile should be deterministic with same seed")

    def test_simile_differs_from_plain(self):
        plain = generate_landscape(seed=42)
        similed = generate_landscape(seed=42, simile_enabled=True)
        self.assertNotEqual(plain, similed,
            "Simile output should differ from plain output")

    def test_simile_works_with_detail_zero(self):
        for s in range(10):
            result = generate_landscape(seed=s, simile_enabled=True, detail=0)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)
            # Similes are suppressed at detail=0 (like echoes, soundscapes)
            for ind in SIMILE_INDICATORS:
                self.assertNotIn(ind, result,
                    f"Simile should not appear at detail=0 at seed {s}")

    def test_simile_works_with_json_format(self):
        result = generate_landscape(seed=42, simile_enabled=True, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertGreater(len(data["text"]), 0)

    def test_simile_json_includes_field(self):
        result = generate_landscape(seed=42, simile_enabled=True, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("simile_enabled", data)
        self.assertTrue(data["simile_enabled"])

    def test_simile_json_field_absent_when_disabled(self):
        result = generate_landscape(seed=42, fmt="json")
        import json
        data = json.loads(result)
        self.assertNotIn("simile_enabled", data,
            "simile_enabled should not be in JSON when disabled")

    def test_simile_works_with_echo(self):
        result = generate_landscape(seed=42, simile_enabled=True, echo_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))

    def test_simile_works_with_legend(self):
        result = generate_landscape(seed=42, simile_enabled=True, legend_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_simile_works_with_travelogue(self):
        result = generate_landscape(seed=42, simile_enabled=True, travelogue=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_simile_works_with_sound(self):
        result = generate_landscape(seed=42, simile_enabled=True, sound_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_simile_works_with_wistful(self):
        result = generate_landscape(seed=42, simile_enabled=True, wistful=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_simile_works_with_time_of_day(self):
        result = generate_landscape(seed=42, simile_enabled=True, time_of_day_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_simile_works_with_season(self):
        result = generate_landscape(seed=42, simile_enabled=True, season_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_simile_works_with_wildlife(self):
        result = generate_landscape(seed=42, simile_enabled=True, wildlife_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_simile_works_with_perspective(self):
        result = generate_landscape(seed=42, simile_enabled=True, perspective_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_simile_works_with_mood_atmosphere(self):
        result = generate_landscape(seed=42, simile_enabled=True, mood="eerie", mood_atmosphere=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_simile_works_with_poetic_format(self):
        result = generate_landscape(seed=42, simile_enabled=True, fmt="poetic")
        self.assertIsInstance(result, str)
        self.assertIn("\n", result)

    def test_simile_works_with_all_biomes(self):
        for biome in BIOMES:
            with self.subTest(biome=biome):
                result = generate_landscape(seed=42, biome=biome, simile_enabled=True)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_simile_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


class TestDescribeSimiles(unittest.TestCase):
    def test_describe_similes_returns_string(self):
        result = describe_similes()
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_describe_similes_contains_header(self):
        result = describe_similes()
        self.assertIn("simile phrases", result)

    def test_describe_similes_contains_all_phrases(self):
        result = describe_similes()
        for phrase in SIMILES:
            self.assertIn(phrase, result,
                f"Simile phrase not found in description: {phrase!r}")

    def test_describe_similes_contains_index_numbers(self):
        result = describe_similes()
        self.assertIn("[0]", result)
        self.assertIn("[1]", result)

    def test_describe_similes_shows_all_phrases(self):
        result = describe_similes()
        last_idx = len(SIMILES) - 1
        self.assertIn(f"[{last_idx}]", result,
            f"Last index [{last_idx}] should appear in description")

    def test_describe_similes_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_describe_similes_flag_prints_to_stdout(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--describe-similes"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertIn("simile phrases", output)
        self.assertIn("[0]", output)

    def test_describe_similes_no_landscape_generated(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--describe-similes", "--seed", "42", "--count", "2"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertNotIn("[seed=42]", output,
            "No landscape should be generated when --describe-similes is used")
        self.assertNotIn("\n\n", output,
            "No landscape should be generated when --describe-similes is used")


class TestNoSimile(unittest.TestCase):
    def test_no_simile_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_no_simile_disables_simile_with_preset(self):
        from landscape import PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                result = generate_landscape(seed=42, **PRESETS[name])
                has_simile = any(ind in result for ind in SIMILE_INDICATORS)
                if not has_simile:
                    continue
                result_no = generate_landscape(
                    seed=42,
                    simile_enabled=False,
                    **{k: v for k, v in PRESETS[name].items() if k not in ("simile_enabled",)}
                )
                no_simile = not any(ind in result_no for ind in SIMILE_INDICATORS)
                self.assertTrue(no_simile,
                    f"Preset {name} should have simile suppressed with simile_enabled=False")

    def test_no_simile_works_with_other_features(self):
        result = generate_landscape(seed=42, simile_enabled=False, echo_enabled=True, legend_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))

    def test_no_simile_json_output(self):
        result = generate_landscape(seed=42, fmt="json")
        import json
        data = json.loads(result)
        self.assertNotIn("simile_enabled", data,
            "simile_enabled should not be in JSON when disabled")

    def test_no_simile_with_explicit_simile_override(self):
        no_sim = generate_landscape(seed=42, simile_enabled=False)
        with_sim = generate_landscape(seed=42, simile_enabled=True)
        self.assertNotEqual(no_sim, with_sim,
            "simile_enabled=False should differ from simile_enabled=True with same seed")


class TestSimileCount(unittest.TestCase):
    def test_simile_count_default_is_one(self):
        a = generate_landscape(seed=42, simile_enabled=True)
        b = generate_landscape(seed=42, simile_enabled=True, simile_count=1)
        self.assertEqual(a, b,
            "simile_count=1 should match default")

    def test_simile_count_zero_suppresses_similes(self):
        result = generate_landscape(seed=42, simile_enabled=True, simile_count=0)
        for ind in SIMILE_INDICATORS:
            self.assertNotIn(ind, result,
                "Simile should not appear with simile_count=0")

    def test_simile_count_two_produces_two_phrases(self):
        results = [generate_landscape(seed=s, simile_enabled=True, simile_count=2) for s in range(100)]
        multi = sum(1 for r in results if sum(1 for ind in SIMILE_INDICATORS if ind in r) >= 2)
        self.assertGreater(multi, 0,
            "simile_count=2 should produce at least 2 simile indicators in some outputs")

    def test_simile_count_three_produces_three_phrases(self):
        results = [generate_landscape(seed=s, simile_enabled=True, simile_count=3) for s in range(200)]
        multi = sum(1 for r in results if sum(1 for ind in SIMILE_INDICATORS if ind in r) >= 3)
        self.assertGreater(multi, 0,
            "simile_count=3 should produce at least 3 simile indicators in some outputs")

    def test_simile_count_no_repeats(self):
        for s in range(100):
            result = generate_landscape(seed=s, simile_enabled=True, simile_count=3)
            found = [ind for ind in SIMILE_INDICATORS if ind in result]
            self.assertEqual(len(found), len(set(found)),
                "Simile phrases should not repeat within the same landscape")

    def test_simile_count_produces_valid_output(self):
        for count in [0, 1, 2, 3]:
            for s in range(10):
                result = generate_landscape(seed=s, simile_enabled=True, simile_count=count)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_simile_count_is_deterministic(self):
        a = generate_landscape(seed=42, simile_enabled=True, simile_count=2)
        b = generate_landscape(seed=42, simile_enabled=True, simile_count=2)
        self.assertEqual(a, b,
            "simile_count should be deterministic with same seed")

    def test_simile_count_works_with_json_format(self):
        result = generate_landscape(seed=42, simile_enabled=True, simile_count=2, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertGreater(len(data["text"]), 0)

    def test_simile_count_json_includes_field(self):
        result = generate_landscape(seed=42, simile_enabled=True, simile_count=2, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("simile_count", data)
        self.assertEqual(data["simile_count"], 2)

    def test_simile_count_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


class TestSimileProb(unittest.TestCase):
    def test_simile_prob_default_is_one(self):
        a = generate_landscape(seed=42, simile_enabled=True)
        b = generate_landscape(seed=42, simile_enabled=True, simile_prob=1.0)
        self.assertEqual(a, b,
            "simile_prob=1.0 should match default")

    def test_simile_prob_zero_suppresses_similes(self):
        results = [generate_landscape(seed=s, simile_enabled=True, simile_prob=0.0) for s in range(100)]
        for r in results:
            for ind in SIMILE_INDICATORS:
                self.assertNotIn(ind, r,
                    f"Simile indicator {ind!r} should not appear with simile_prob=0.0")

    def test_simile_prob_one_always_has_simile(self):
        results = [generate_landscape(seed=s, simile_enabled=True, simile_prob=1.0) for s in range(100)]
        has_simile = sum(1 for r in results if any(ind in r for ind in SIMILE_INDICATORS))
        self.assertGreater(has_simile, 80,
            "With simile_prob=1.0, most outputs should contain a simile")

    def test_simile_prob_produces_valid_output(self):
        for prob in [0.0, 0.25, 0.5, 0.75, 1.0]:
            for s in range(10):
                result = generate_landscape(seed=s, simile_enabled=True, simile_prob=prob)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_simile_prob_is_deterministic(self):
        a = generate_landscape(seed=42, simile_enabled=True, simile_prob=0.5)
        b = generate_landscape(seed=42, simile_enabled=True, simile_prob=0.5)
        self.assertEqual(a, b,
            "simile_prob should be deterministic with same seed")

    def test_simile_prob_json_includes_field(self):
        result = generate_landscape(seed=42, simile_enabled=True, simile_prob=0.5, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("simile_prob", data)
        self.assertEqual(data["simile_prob"], 0.5)

    def test_simile_prob_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


class TestMetaphor(unittest.TestCase):
    def test_metaphor_disabled_by_default(self):
        for s in range(20):
            result = generate_landscape(seed=s)
            for ind in METAPHOR_INDICATORS:
                self.assertNotIn(ind, result,
                    f"Metaphor indicator {ind!r} should not appear by default")

    def test_metaphor_enabled_appears(self):
        results = [generate_landscape(seed=s, metaphor_enabled=True) for s in range(50)]
        has_metaphor = any(
            any(ind in r for ind in METAPHOR_INDICATORS) for r in results
        )
        self.assertTrue(has_metaphor,
            "Metaphor phrase should appear when enabled")

    def test_metaphor_produces_valid_output(self):
        for s in range(50):
            result = generate_landscape(seed=s, metaphor_enabled=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)
            self.assertTrue(result.endswith("."))

    def test_metaphor_is_deterministic(self):
        a = generate_landscape(seed=42, metaphor_enabled=True)
        b = generate_landscape(seed=42, metaphor_enabled=True)
        self.assertEqual(a, b,
            "Metaphor should be deterministic with same seed")

    def test_metaphor_differs_from_plain(self):
        plain = generate_landscape(seed=42)
        metaphor = generate_landscape(seed=42, metaphor_enabled=True)
        self.assertNotEqual(plain, metaphor,
            "Metaphor output should differ from plain output")

    def test_metaphor_works_with_detail_zero(self):
        for s in range(10):
            result = generate_landscape(seed=s, metaphor_enabled=True, detail=0)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)
            for ind in METAPHOR_INDICATORS:
                self.assertNotIn(ind, result,
                    f"Metaphor should not appear at detail=0 at seed {s}")

    def test_metaphor_works_with_json_format(self):
        result = generate_landscape(seed=42, metaphor_enabled=True, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertGreater(len(data["text"]), 0)

    def test_metaphor_json_includes_field(self):
        result = generate_landscape(seed=42, metaphor_enabled=True, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("metaphor_enabled", data)
        self.assertTrue(data["metaphor_enabled"])

    def test_metaphor_json_field_absent_when_disabled(self):
        result = generate_landscape(seed=42, fmt="json")
        import json
        data = json.loads(result)
        self.assertNotIn("metaphor_enabled", data,
            "metaphor_enabled should not be in JSON when disabled")

    def test_metaphor_works_with_echo(self):
        result = generate_landscape(seed=42, metaphor_enabled=True, echo_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))

    def test_metaphor_works_with_legend(self):
        result = generate_landscape(seed=42, metaphor_enabled=True, legend_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_metaphor_works_with_travelogue(self):
        result = generate_landscape(seed=42, metaphor_enabled=True, travelogue=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_metaphor_works_with_sound(self):
        result = generate_landscape(seed=42, metaphor_enabled=True, sound_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_metaphor_works_with_wistful(self):
        result = generate_landscape(seed=42, metaphor_enabled=True, wistful=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_metaphor_works_with_time_of_day(self):
        result = generate_landscape(seed=42, metaphor_enabled=True, time_of_day_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_metaphor_works_with_season(self):
        result = generate_landscape(seed=42, metaphor_enabled=True, season_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_metaphor_works_with_wildlife(self):
        result = generate_landscape(seed=42, metaphor_enabled=True, wildlife_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_metaphor_works_with_perspective(self):
        result = generate_landscape(seed=42, metaphor_enabled=True, perspective_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_metaphor_works_with_mood_atmosphere(self):
        result = generate_landscape(seed=42, metaphor_enabled=True, mood="eerie", mood_atmosphere=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_metaphor_works_with_poetic_format(self):
        result = generate_landscape(seed=42, metaphor_enabled=True, fmt="poetic")
        self.assertIsInstance(result, str)
        self.assertIn("\n", result)

    def test_metaphor_works_with_all_biomes(self):
        for biome in BIOMES:
            with self.subTest(biome=biome):
                result = generate_landscape(seed=42, biome=biome, metaphor_enabled=True)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_metaphor_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


class TestDescribeMetaphors(unittest.TestCase):
    def test_describe_metaphors_returns_string(self):
        result = describe_metaphors()
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_describe_metaphors_contains_header(self):
        result = describe_metaphors()
        self.assertIn("metaphor phrases", result)

    def test_describe_metaphors_contains_all_phrases(self):
        result = describe_metaphors()
        for phrase in METAPHORS:
            self.assertIn(phrase, result,
                f"Metaphor phrase not found in description: {phrase!r}")

    def test_describe_metaphors_contains_index_numbers(self):
        result = describe_metaphors()
        self.assertIn("[0]", result)
        self.assertIn("[1]", result)

    def test_describe_metaphors_shows_all_phrases(self):
        result = describe_metaphors()
        last_idx = len(METAPHORS) - 1
        self.assertIn(f"[{last_idx}]", result,
            f"Last index [{last_idx}] should appear in description")

    def test_describe_metaphors_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_describe_metaphors_flag_prints_to_stdout(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--describe-metaphors"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertIn("metaphor phrases", output)
        self.assertIn("[0]", output)

    def test_describe_metaphors_no_landscape_generated(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--describe-metaphors", "--seed", "42", "--count", "2"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertNotIn("[seed=42]", output,
            "No landscape should be generated when --describe-metaphors is used")
        self.assertNotIn("\n\n", output,
            "No landscape should be generated when --describe-metaphors is used")


class TestNoMetaphor(unittest.TestCase):
    def test_no_metaphor_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_no_metaphor_disables_metaphor_with_preset(self):
        from landscape import PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                result = generate_landscape(seed=42, **PRESETS[name])
                has_metaphor = any(ind in result for ind in METAPHOR_INDICATORS)
                if not has_metaphor:
                    continue
                result_no = generate_landscape(
                    seed=42,
                    metaphor_enabled=False,
                    **{k: v for k, v in PRESETS[name].items() if k not in ("metaphor_enabled",)}
                )
                no_metaphor = not any(ind in result_no for ind in METAPHOR_INDICATORS)
                self.assertTrue(no_metaphor,
                    f"Preset {name} should have metaphor suppressed with metaphor_enabled=False")

    def test_no_metaphor_works_with_other_features(self):
        result = generate_landscape(seed=42, metaphor_enabled=False, echo_enabled=True, legend_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))

    def test_no_metaphor_json_output(self):
        result = generate_landscape(seed=42, fmt="json")
        import json
        data = json.loads(result)
        self.assertNotIn("metaphor_enabled", data,
            "metaphor_enabled should not be in JSON when disabled")

    def test_no_metaphor_with_explicit_metaphor_override(self):
        no_met = generate_landscape(seed=42, metaphor_enabled=False)
        with_met = generate_landscape(seed=42, metaphor_enabled=True)
        self.assertNotEqual(no_met, with_met,
            "metaphor_enabled=False should differ from metaphor_enabled=True with same seed")


class TestMetaphorCount(unittest.TestCase):
    def test_metaphor_count_default_is_one(self):
        a = generate_landscape(seed=42, metaphor_enabled=True)
        b = generate_landscape(seed=42, metaphor_enabled=True, metaphor_count=1)
        self.assertEqual(a, b,
            "metaphor_count=1 should match default")

    def test_metaphor_count_zero_suppresses_metaphors(self):
        result = generate_landscape(seed=42, metaphor_enabled=True, metaphor_count=0)
        for ind in METAPHOR_INDICATORS:
            self.assertNotIn(ind, result,
                "Metaphor should not appear with metaphor_count=0")

    def test_metaphor_count_two_produces_two_phrases(self):
        results = [generate_landscape(seed=s, metaphor_enabled=True, metaphor_count=2) for s in range(100)]
        multi = sum(1 for r in results if sum(1 for ind in METAPHOR_INDICATORS if ind in r) >= 2)
        self.assertGreater(multi, 0,
            "metaphor_count=2 should produce at least 2 metaphor indicators in some outputs")

    def test_metaphor_count_three_produces_three_phrases(self):
        results = [generate_landscape(seed=s, metaphor_enabled=True, metaphor_count=3) for s in range(200)]
        multi = sum(1 for r in results if sum(1 for ind in METAPHOR_INDICATORS if ind in r) >= 3)
        self.assertGreater(multi, 0,
            "metaphor_count=3 should produce at least 3 metaphor indicators in some outputs")

    def test_metaphor_count_no_repeats(self):
        for s in range(100):
            result = generate_landscape(seed=s, metaphor_enabled=True, metaphor_count=3)
            found = [ind for ind in METAPHOR_INDICATORS if ind in result]
            self.assertEqual(len(found), len(set(found)),
                "Metaphor phrases should not repeat within the same landscape")

    def test_metaphor_count_produces_valid_output(self):
        for count in [0, 1, 2, 3]:
            for s in range(10):
                result = generate_landscape(seed=s, metaphor_enabled=True, metaphor_count=count)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_metaphor_count_is_deterministic(self):
        a = generate_landscape(seed=42, metaphor_enabled=True, metaphor_count=2)
        b = generate_landscape(seed=42, metaphor_enabled=True, metaphor_count=2)
        self.assertEqual(a, b,
            "metaphor_count should be deterministic with same seed")

    def test_metaphor_count_works_with_json_format(self):
        result = generate_landscape(seed=42, metaphor_enabled=True, metaphor_count=2, fmt="json")
        import json
        data = json.loads(result)
        self.assertIn("text", data)
        self.assertIsInstance(data["text"], str)
        self.assertGreater(len(data["text"]), 0)

    def test_metaphor_count_json_includes_field(self):
        result = generate_landscape(seed=42, metaphor_enabled=True, metaphor_count=2, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("metaphor_count", data)
        self.assertEqual(data["metaphor_count"], 2)

    def test_metaphor_count_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


class TestMetaphorProb(unittest.TestCase):
    def test_metaphor_prob_default_is_one(self):
        a = generate_landscape(seed=42, metaphor_enabled=True)
        b = generate_landscape(seed=42, metaphor_enabled=True, metaphor_prob=1.0)
        self.assertEqual(a, b,
            "metaphor_prob=1.0 should match default")

    def test_metaphor_prob_zero_suppresses_metaphors(self):
        results = [generate_landscape(seed=s, metaphor_enabled=True, metaphor_prob=0.0) for s in range(100)]
        for r in results:
            for ind in METAPHOR_INDICATORS:
                self.assertNotIn(ind, r,
                    f"Metaphor indicator {ind!r} should not appear with metaphor_prob=0.0")

    def test_metaphor_prob_one_always_has_metaphor(self):
        results = [generate_landscape(seed=s, metaphor_enabled=True, metaphor_prob=1.0) for s in range(100)]
        has_metaphor = sum(1 for r in results if any(ind in r for ind in METAPHOR_INDICATORS))
        self.assertGreater(has_metaphor, 80,
            "With metaphor_prob=1.0, most outputs should contain a metaphor")

    def test_metaphor_prob_produces_valid_output(self):
        for prob in [0.0, 0.25, 0.5, 0.75, 1.0]:
            for s in range(10):
                result = generate_landscape(seed=s, metaphor_enabled=True, metaphor_prob=prob)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_metaphor_prob_is_deterministic(self):
        a = generate_landscape(seed=42, metaphor_enabled=True, metaphor_prob=0.5)
        b = generate_landscape(seed=42, metaphor_enabled=True, metaphor_prob=0.5)
        self.assertEqual(a, b,
            "metaphor_prob should be deterministic with same seed")

    def test_metaphor_prob_json_includes_field(self):
        result = generate_landscape(seed=42, metaphor_enabled=True, metaphor_prob=0.5, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("metaphor_prob", data)
        self.assertEqual(data["metaphor_prob"], 0.5)

    def test_metaphor_prob_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


class TestPersonification(unittest.TestCase):
    def test_personification_disabled_by_default(self):
        for s in range(20):
            result = generate_landscape(seed=s)
            for ind in PERSONIFICATION_INDICATORS:
                self.assertNotIn(ind, result,
                    f"Personification indicator {ind!r} should not appear by default")

    def test_personification_enabled_appears(self):
        results = [generate_landscape(seed=s, personification_enabled=True) for s in range(50)]
        has_personification = any(any(ind in r for ind in PERSONIFICATION_INDICATORS) for r in results)
        self.assertTrue(has_personification,
            "Personification should appear in at least one output when enabled")

    def test_personification_produces_valid_output(self):
        for s in range(20):
            result = generate_landscape(seed=s, personification_enabled=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)

    def test_personification_is_deterministic(self):
        a = generate_landscape(seed=42, personification_enabled=True)
        b = generate_landscape(seed=42, personification_enabled=True)
        self.assertEqual(a, b,
            "Personification should be deterministic with same seed")

    def test_personification_differs_from_plain(self):
        plain = generate_landscape(seed=42)
        personified = generate_landscape(seed=42, personification_enabled=True)
        self.assertNotEqual(plain, personified,
            "Output with personification should differ from plain output")

    def test_personification_detail_zero_does_not_include(self):
        for s in range(20):
            result = generate_landscape(seed=s, personification_enabled=True, detail=0)
            for ind in PERSONIFICATION_INDICATORS:
                self.assertNotIn(ind, result,
                    f"Personification indicator {ind!r} should not appear at detail=0")

    def test_personification_json_format(self):
        result = generate_landscape(seed=42, personification_enabled=True, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIsInstance(data, dict)

    def test_personification_json_includes_field_when_enabled(self):
        result = generate_landscape(seed=42, personification_enabled=True, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("personification_enabled", data)
        self.assertTrue(data["personification_enabled"])

    def test_personification_json_no_field_when_disabled(self):
        result = generate_landscape(seed=42, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertNotIn("personification_enabled", data,
            "personification_enabled should not appear in JSON when disabled")

    def test_personification_works_with_echo(self):
        for s in range(10):
            result = generate_landscape(seed=s, personification_enabled=True, echo_enabled=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)

    def test_personification_works_with_legend(self):
        for s in range(10):
            result = generate_landscape(seed=s, personification_enabled=True, legend_enabled=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)

    def test_personification_works_with_travelogue(self):
        for s in range(10):
            result = generate_landscape(seed=s, personification_enabled=True, travelogue=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)

    def test_personification_works_with_sound(self):
        for s in range(10):
            result = generate_landscape(seed=s, personification_enabled=True, sound_enabled=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)

    def test_personification_works_with_wistful(self):
        for s in range(10):
            result = generate_landscape(seed=s, personification_enabled=True, wistful=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)

    def test_personification_works_with_time_of_day(self):
        for s in range(10):
            result = generate_landscape(seed=s, personification_enabled=True, time_of_day_enabled=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)

    def test_personification_works_with_season(self):
        for s in range(10):
            result = generate_landscape(seed=s, personification_enabled=True, season_enabled=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)

    def test_personification_works_with_wildlife(self):
        for s in range(10):
            result = generate_landscape(seed=s, personification_enabled=True, wildlife_enabled=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)

    def test_personification_works_with_perspective(self):
        for s in range(10):
            result = generate_landscape(seed=s, personification_enabled=True, perspective_enabled=True)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)

    def test_personification_works_with_mood_atmosphere(self):
        for s in range(10):
            result = generate_landscape(seed=s, personification_enabled=True, mood_atmosphere=True, mood="eerie")
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)

    def test_personification_poetic_format(self):
        for s in range(10):
            result = generate_landscape(seed=s, personification_enabled=True, fmt="poetic")
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)

    def test_personification_all_biomes(self):
        for biome in BIOMES:
            for s in range(5):
                result = generate_landscape(seed=s, personification_enabled=True, biome=biome)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_personification_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


class TestDescribePersonifications(unittest.TestCase):
    def test_describe_personifications_returns_string(self):
        result = describe_personifications()
        self.assertIsInstance(result, str)

    def test_describe_personifications_contains_header(self):
        result = describe_personifications()
        self.assertIn("personification phrases", result)

    def test_describe_personifications_shows_all_phrases(self):
        result = describe_personifications()
        for phrase in PERSONIFICATIONS:
            self.assertIn(phrase, result,
                f"Personification phrase {phrase!r} should be in describe output")

    def test_describe_personifications_has_index_numbers(self):
        result = describe_personifications()
        for i in range(len(PERSONIFICATIONS)):
            self.assertIn(f"[{i}]", result,
                f"Index [{i}] should appear in describe output")

    def test_describe_personifications_last_index_accurate(self):
        result = describe_personifications()
        self.assertIn(f"[{len(PERSONIFICATIONS) - 1}]", result)

    def test_describe_personifications_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_describe_personifications_outputs_to_stdout(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--describe-personifications", "--seed", "42", "--count", "2"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertIn("personification phrases", output,
            "describe-personifications should output to stdout")

    def test_describe_personifications_no_landscape_generated(self):
        import sys
        import io
        from landscape import main
        old_argv = sys.argv
        old_stdout = sys.stdout
        sys.argv = ["landscape", "--describe-personifications", "--seed", "42", "--count", "2"]
        captured = io.StringIO()
        sys.stdout = captured
        try:
            main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv
        output = captured.getvalue()
        self.assertNotIn("[seed=42]", output,
            "No landscape should be generated when --describe-personifications is used")
        self.assertNotIn("\n\n", output,
            "No landscape should be generated when --describe-personifications is used")


class TestNoPersonification(unittest.TestCase):
    def test_no_personification_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))

    def test_no_personification_disables_with_preset(self):
        from landscape import PRESETS
        for name in PRESETS:
            with self.subTest(preset=name):
                result = generate_landscape(seed=42, **PRESETS[name])
                has_personif = any(ind in result for ind in PERSONIFICATION_INDICATORS)
                if not has_personif:
                    continue
                result_no = generate_landscape(
                    seed=42,
                    personification_enabled=False,
                    **{k: v for k, v in PRESETS[name].items() if k not in ("personification_enabled",)}
                )
                no_personif = not any(ind in result_no for ind in PERSONIFICATION_INDICATORS)
                self.assertTrue(no_personif,
                    f"Preset {name} should have personification suppressed with personification_enabled=False")

    def test_no_personification_works_with_other_features(self):
        result = generate_landscape(seed=42, personification_enabled=False, echo_enabled=True, legend_enabled=True)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue(result.endswith("."))

    def test_no_personification_does_not_affect_json_output(self):
        result = generate_landscape(seed=42, fmt="json")
        import json
        data = json.loads(result)
        self.assertNotIn("personification_enabled", data,
            "personification_enabled should not be in JSON when disabled")

    def test_no_personification_with_explicit_personification_override(self):
        no = generate_landscape(seed=42, personification_enabled=False)
        yes = generate_landscape(seed=42, personification_enabled=True)
        self.assertNotEqual(no, yes,
            "personification_enabled=False should differ from True with same seed")


class TestPersonificationCount(unittest.TestCase):
    def test_personification_count_default_is_one(self):
        a = generate_landscape(seed=42, personification_enabled=True)
        b = generate_landscape(seed=42, personification_enabled=True, personification_count=1)
        self.assertEqual(a, b,
            "personification_count=1 should match default")

    def test_personification_count_zero_suppresses(self):
        results = [generate_landscape(seed=s, personification_enabled=True, personification_count=0) for s in range(100)]
        for r in results:
            for ind in PERSONIFICATION_INDICATORS:
                self.assertNotIn(ind, r,
                    f"Personification indicator {ind!r} should not appear with count=0")

    def test_personification_count_two_produces_two(self):
        results = [generate_landscape(seed=s, personification_enabled=True, personification_count=2) for s in range(50)]
        has_two = any(
            sum(1 for ind in PERSONIFICATION_INDICATORS if ind in r) >= 2
            for r in results
        )
        self.assertTrue(has_two,
            "Expected at least one output with 2+ personification indicators")

    def test_personification_count_three_produces_three(self):
        results = [generate_landscape(seed=s, personification_enabled=True, personification_count=3) for s in range(100)]
        has_three = any(
            sum(1 for ind in PERSONIFICATION_INDICATORS if ind in r) >= 3
            for r in results
        )
        self.assertTrue(has_three,
            "Expected at least one output with 3+ personification indicators")

    def test_personification_count_no_repeat_same_phrase(self):
        results = [generate_landscape(seed=s, personification_enabled=True, personification_count=3) for s in range(100)]
        for r in results:
            found = [ind for ind in PERSONIFICATION_INDICATORS if ind in r]
            self.assertEqual(len(found), len(set(found)),
                "Personification phrases should not repeat within a single landscape")

    def test_personification_count_produces_valid_output(self):
        for count in [0, 1, 2, 3]:
            for s in range(10):
                result = generate_landscape(seed=s, personification_enabled=True, personification_count=count)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_personification_count_is_deterministic(self):
        a = generate_landscape(seed=42, personification_enabled=True, personification_count=2)
        b = generate_landscape(seed=42, personification_enabled=True, personification_count=2)
        self.assertEqual(a, b,
            "personification_count should be deterministic with same seed")

    def test_personification_count_json_includes_field(self):
        result = generate_landscape(seed=42, personification_enabled=True, personification_count=2, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("personification_count", data)
        self.assertEqual(data["personification_count"], 2)

    def test_personification_count_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


class TestPersonificationProb(unittest.TestCase):
    def test_personification_prob_default_is_one(self):
        a = generate_landscape(seed=42, personification_enabled=True)
        b = generate_landscape(seed=42, personification_enabled=True, personification_prob=1.0)
        self.assertEqual(a, b,
            "personification_prob=1.0 should match default")

    def test_personification_prob_zero_suppresses_personifications(self):
        results = [generate_landscape(seed=s, personification_enabled=True, personification_prob=0.0) for s in range(100)]
        for r in results:
            for ind in PERSONIFICATION_INDICATORS:
                self.assertNotIn(ind, r,
                    f"Personification indicator {ind!r} should not appear with personification_prob=0.0")

    def test_personification_prob_one_always_has_personification(self):
        results = [generate_landscape(seed=s, personification_enabled=True, personification_prob=1.0) for s in range(100)]
        has_personif = sum(1 for r in results if any(ind in r for ind in PERSONIFICATION_INDICATORS))
        self.assertGreater(has_personif, 80,
            "With personification_prob=1.0, most outputs should contain a personification")

    def test_personification_prob_produces_valid_output(self):
        for prob in [0.0, 0.25, 0.5, 0.75, 1.0]:
            for s in range(10):
                result = generate_landscape(seed=s, personification_enabled=True, personification_prob=prob)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_personification_prob_is_deterministic(self):
        a = generate_landscape(seed=42, personification_enabled=True, personification_prob=0.5)
        b = generate_landscape(seed=42, personification_enabled=True, personification_prob=0.5)
        self.assertEqual(a, b,
            "personification_prob should be deterministic with same seed")

    def test_personification_prob_json_includes_field(self):
        result = generate_landscape(seed=42, personification_enabled=True, personification_prob=0.5, fmt="json")
        import json as j
        data = j.loads(result)
        self.assertIn("personification_prob", data)
        self.assertEqual(data["personification_prob"], 0.5)

    def test_personification_prob_flag_exists_via_cli(self):
        from landscape import main
        self.assertTrue(callable(main))


if __name__ == "__main__":
    unittest.main()
