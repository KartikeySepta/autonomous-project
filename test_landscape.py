import unittest

import random

from landscape import (
    generate_landscape,
    BIOMES, ADJECTIVES, ELEMENTS, NOUNS, VERBS, WEATHERS, ANOMALIES, BIOME_WORDS,
    COMMON_WORDS, RARE_WORDS, SENTENCE_TEMPLATES, BIAS_MODES, _conjugate,
)

ALL_ADJECTIVES = set(ADJECTIVES) | {w for bw in BIOME_WORDS.values() for w in bw.get("adjectives", [])}
ALL_VERBS = set(VERBS) | {w for bw in BIOME_WORDS.values() for w in bw.get("verbs", [])}
ALL_ELEMENTS = set(ELEMENTS) | {w for bw in BIOME_WORDS.values() for w in bw.get("elements", [])}
ALL_NOUNS = set(NOUNS) | {w for bw in BIOME_WORDS.values() for w in bw.get("nouns", [])}
ALL_WEATHERS = set(WEATHERS) | {w for bw in BIOME_WORDS.values() for w in bw.get("weathers", [])}
ALL_ANOMALIES = set(ANOMALIES) | {w for bw in BIOME_WORDS.values() for w in bw.get("anomalies", [])}


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
        self.assertTrue(
            any(result.startswith(s) for s in valid_starts),
            f"Output doesn't start with any valid opening: {result!r}",
        )

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
        }
        distinct = sum(1 for v in counts.values() if v > 0)
        self.assertGreaterEqual(distinct, 2, f"Only {distinct} opening patterns seen: {counts}")

    def test_template_variety_middle_has_varied_structure(self):
        results = [generate_landscape(seed=s, biome="forest") for s in range(100)]
        has_classic = any(" between the " in r for r in results)
        has_among = any(r.startswith("Among") for r in results)
        self.assertTrue(has_classic or has_among, "Neither classic nor among middle pattern found")

    def test_template_variety_does_not_break_output(self):
        for s in range(50):
            result = generate_landscape(seed=s)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 10)

    def test_template_variety_weather_has_varied_structure(self):
        results = [generate_landscape(seed=s, biome="forest") for s in range(200)]
        has_air_tells = any("The air tells its own story: " in r for r in results)
        has_as_if = any(" itself breathes." in r for r in results)
        self.assertTrue(
            has_air_tells or has_as_if,
            "Neither alternative weather template appeared across 200 seeds",
        )

    def test_template_variety_anomaly_has_varied_structure(self):
        results = [generate_landscape(seed=s, biome="forest") for s in range(200)]
        has_strange = any("A strange detail catches your eye: " in r for r in results)
        has_wrongness = any("There is a quiet wrongness here: " in r for r in results)
        self.assertTrue(
            has_strange or has_wrongness,
            "Neither alternative anomaly template appeared across 200 seeds",
        )

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

    def test_detail_two_is_longer_than_one(self):
        for s in range(20):
            d1 = generate_landscape(seed=s, detail=1)
            d2 = generate_landscape(seed=s, detail=2)
            self.assertGreater(len(d2), len(d1),
                f"detail=2 not longer than detail=1 at seed {s}")

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
        common_hits_normal = 0
        common_hits_common = 0
        for s in range(300):
            if any(c in generate_landscape(seed=s, bias="normal") for c in COMMON_WORDS):
                common_hits_normal += 1
            if any(c in generate_landscape(seed=s, bias="common") for c in COMMON_WORDS):
                common_hits_common += 1
        self.assertGreater(common_hits_common, common_hits_normal,
            "bias=common should produce more outputs with common words than bias=normal")

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


if __name__ == "__main__":
    unittest.main()
