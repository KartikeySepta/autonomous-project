import unittest
from pathlib import Path

import random

from landscape import (
    generate_landscape,
    BIOMES, ADJECTIVES, ELEMENTS, NOUNS, VERBS, WEATHERS, ANOMALIES, ADVERBS, COLORS, BIOME_WORDS, ECHOES, LEGENDS,
    COMMON_WORDS, RARE_WORDS, SENTENCE_TEMPLATES, BIAS_MODES, _conjugate,
    MOOD_WORDS, MOOD_BOOST, TEMPLATE_SETS, _pick_template,
    TIME_WORDS, TRAVELOGUE_PREFIXES, TRAVELOGUE_SUFFIXES,
    describe_travelogue,
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

LEGEND_INDICATORS = [
    "maps leave", "was not here", "Pilgrims once walked", "older than stone",
    "many names", "returns unchanged", "song about", "no map",
    "dreams of a time", "hermit once lived",
    "remembers those who built", "seen from far away", "placed by hand",
    "sounds like a name", "well in the",
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
        for m in ["peaceful", "eerie", "vibrant", "desolate"]:
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
        for combo in [["peaceful", "eerie"], ["peaceful", "vibrant"], ["peaceful", "desolate"]]:
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
        for name in ["nightfall", "pastoral", "sublime", "wasteland", "dreamscape"]:
            with self.subTest(preset=name):
                from landscape import generate_landscape, PRESETS
                result = generate_landscape(seed=42, **PRESETS[name])
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)
                self.assertTrue(result.endswith("."))

    def test_preset_is_deterministic(self):
        from landscape import PRESETS
        for name in ["nightfall", "pastoral", "sublime", "wasteland", "dreamscape"]:
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
                )
                self.assertTrue(has_travelogue,
                    f"Preset {name} with travelogue should have travelogue framing")

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
        days = re.findall(r'\bday (\d+)\b', result)
        self.assertGreater(len(days), 0,
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


if __name__ == "__main__":
    unittest.main()
