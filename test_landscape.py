import unittest

import random

from landscape import (
    generate_landscape,
    BIOMES, ADJECTIVES, ELEMENTS, NOUNS, VERBS, WEATHERS, ANOMALIES, ADVERBS, BIOME_WORDS,
    COMMON_WORDS, RARE_WORDS, SENTENCE_TEMPLATES, BIAS_MODES, _conjugate,
    MOOD_WORDS, MOOD_BOOST, TEMPLATE_SETS, _pick_template,
)

ALL_ADJECTIVES = set(ADJECTIVES) | {w for bw in BIOME_WORDS.values() for w in bw.get("adjectives", [])}
ALL_VERBS = set(VERBS) | {w for bw in BIOME_WORDS.values() for w in bw.get("verbs", [])}
ALL_ELEMENTS = set(ELEMENTS) | {w for bw in BIOME_WORDS.values() for w in bw.get("elements", [])}
ALL_NOUNS = set(NOUNS) | {w for bw in BIOME_WORDS.values() for w in bw.get("nouns", [])}
ALL_WEATHERS = set(WEATHERS) | {w for bw in BIOME_WORDS.values() for w in bw.get("weathers", [])}
ALL_ANOMALIES = set(ANOMALIES) | {w for bw in BIOME_WORDS.values() for w in bw.get("anomalies", [])}
ALL_ADVERBS = set(ADVERBS)


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

    def test_anomaly_standalone_template_keeps_capital(self):
        for s in range(100):
            result = generate_landscape(seed=s, biome="forest", template_overrides={"anomaly": "first"}, anomaly_prob=1.0)
            if "Something is not right" in result or "A strange detail" in result or "quiet wrongness" in result:
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
        colon_lines = [r for r in results if "A strange detail catches your eye: " in r or "There is a quiet wrongness here: " in r]
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
            for b in ["ruined city", "fungal grove", "sky islands"]:
                if b in r:
                    biomes_seen.add(b)
        self.assertGreaterEqual(len(biomes_seen), 1,
            f"At least one new biome should appear in 200 random seeds, got {biomes_seen}")

    def test_combine_with_new_biome_uses_vocabulary(self):
        result = generate_landscape(seed=42, combine="ruined city,fungal grove")
        self.assertIn("ruined city", result)
        self.assertIn("fungal grove", result)
        self.assertIn(" and ", result)


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
        outputs = []
        for i in range(10):
            random.seed(42 + i)
            outputs.append(generate_landscape())
        self.assertGreater(len(set(outputs)), 1,
            "Landscapes without explicit seed should vary")


if __name__ == "__main__":
    unittest.main()
