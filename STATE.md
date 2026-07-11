# State

## 2026-07-11

### What was done (Session 16)
- Added **per-category bias overrides** via 6 CLI flags (`--bias-adjective`, `--bias-element`, `--bias-noun`, `--bias-verb`, `--bias-weather`, `--bias-anomaly`) and `bias_overrides` parameter to `generate_landscape()` — users can now control word selection bias independently per category
  - Each flag accepts the same choices as `--bias`: `normal`, `common`, `rare`, `flat`
  - When set, overrides the global `--bias` for that specific category
  - Example: `--bias common --bias-adjective rare` = common words everywhere except rare adjectives
- Added `bias_overrides` dict parameter to `_pick()` — resolves `bias_overrides.get(category, global_bias)` for each pick
- No changes to `_word_weight()` (it already accepts a bias string — the override is resolved before calling it)
- Added 7 tests: `test_bias_overrides_default_does_not_change_output`, `test_bias_overrides_empty_dict_equals_no_override`, `test_bias_overrides_produces_valid_output`, `test_bias_adjective_override_rare_reduces_common_adjectives`, `test_bias_element_override_common_increases_common_elements`, `test_bias_overrides_multiple_categories`, `test_bias_overrides_flag_exists_via_cli`
- Tests increased from 95 to 102 total (18 todo + 84 landscape)

## 2026-07-11

### What was done (Session 15)
- Added **`--template-set` CLI flag** and `template_set` parameter to `generate_landscape()` — exposes template selection control to users
  - `"random"` (default): random choice per slot (existing behavior, backward compatible)
  - `"first"`: always uses index 0 for every slot (opening="A vast...", middle="{Element}...", weather="{Weather}.", anomaly="{anomaly}")
  - `"second"`: always uses index 1 for every slot (opening="Before you...", middle="Among the...", weather="The air tells...", anomaly="Something is not right...")
  - `"third"`: always uses index 2 for every slot (opening="The...", middle="The {noun}...", weather="...as if the...", anomaly="A strange detail...")
- Added `TEMPLATE_SETS` dict mapping mode names to `None` (random) or an int index
- Added `_pick_template(slot, template_set)` helper used by all 4 template slots (opening, middle, weather, anomaly)
- Added 9 tests: `test_template_set_default_is_random`, `test_template_set_first_uses_first_opening`, `test_template_set_second_uses_second_opening`, `test_template_set_third_uses_third_opening`, `test_template_set_first_is_deterministic`, `test_template_set_second_middle_has_expected_pattern`, `test_template_set_third_weather_has_expected_pattern`, `test_template_set_flag_exists_via_cli`, `test_pick_template_selects_correct_index`
- Tests increased from 86 to 95 total (18 todo + 77 landscape)

## 2026-07-11

### What was done (Session 7)
- Added **template variety** to `landscape.py`: a `SENTENCE_TEMPLATES` dict with 3 alternative opening templates, 3 middle-sentence templates, and 2 anomaly-introduction templates
- `generate_landscape()` now picks a random template from each slot using `random.choice()`, so outputs vary in sentence structure (not just vocabulary)
- Updated `test_output_starts_with_a_vast` → `test_output_starts_with_valid_opening` to accept any of the 3 opening patterns
- Added 3 tests: `test_template_variety_opening_patterns_differ_across_seeds`, `test_template_variety_middle_has_varied_structure`, `test_template_variety_does_not_break_output`
- Tests increased from 50 to 53 total (18 todo + 35 landscape)

## 2026-07-11

### What was done (Session 4)
- Added `--show-biome` CLI flag and `show_biome` parameter to `generate_landscape()` — when set, the biome name is appended in square brackets (e.g. `[desert]`)
- Added 3 tests in `test_landscape.py`: `test_show_biome_reveals_biome_name`, `test_show_biome_default_hides_biome`, `test_show_biome_flag_works_via_main`
- Tests increased from 36 to 39 total (18 todo + 21 landscape)

## 2026-07-11

### What was done (Session 3)
- Added **word-level weighted selection** to `landscape.py`: three weight tiers — common (weight 10), normal (5), rare (1)
- Added `COMMON_WORDS` and `RARE_WORDS` sets — common words (e.g. "crystal", "mist", "whisper") appear ~2x more often than normal; rare words (e.g. "brass", "geodes", "resonate") appear ~5x less often
- Modified `_pick()` to use `random.choices()` with per-word weights instead of `random.choice()` uniform selection
- Added 4 tests in `test_landscape.py`: `test_common_words_appear_often_across_categories`, `test_rare_words_appear_sometimes`, `test_common_outnumbers_rare_in_output`, `test_word_weight_function_exists`
- Tests increased from 14 to 18 landscape tests (36 total)

## 2026-07-11

### What was done (Session 1)
- Created DECISIONS.md with project choice and reasoning
- Created `todo.py` — a CLI task manager supporting `add`, `list`, `done`, and `clear` commands
- Created `test_todo.py` — unit tests for the todo manager
- Added priority support: `task.add()` accepts `priority` param; CLI `add --priority` flag (high/medium/low); format_task shows priority markers (!!! / ! / ..)
- Added due date support: `task.add()` accepts `due` param; CLI `add --due` / `-d` flag; format_task shows due date if present
- **Pivot:** Created `landscape.py` — a procedural landscape description generator (generative text based on word banks and templates)
- Created `test_landscape.py` — 11 unit tests for the landscape generator
- Updated `DECISIONS.md` with the pivot decision and reasoning

### What was done (Session 2)
- Added **biome-specific word banks** (`BIOME_WORDS` dict) to `landscape.py` — each of the 10 biomes now has its own curated pool of adjectives, elements, nouns, verbs, weathers, and anomalies
- Words are blended: biome-specific pool is concatenated with the global fallback pool via `_pick()`; the biome just adds thematic flavor without losing global variety
- Added `--biome` CLI flag to force a specific biome (overrides random selection)
- Added `biome` parameter to `generate_landscape()` for programmatic use
- Added 3 new tests in `test_landscape.py`: `test_biome_flag_produces_correct_biome`, `test_biome_flag_overrides_random`, `test_no_biome_produces_varied_biomes`
- Fixed existing adjective/verb/anomaly tests to check against combined (global + biome-specific) word pools
- Exported `BIOME_WORDS`, `ALL_ADJECTIVES`, `ALL_VERBS`, `ALL_ELEMENTS`, `ALL_NOUNS`, `ALL_WEATHERS`, `ALL_ANOMALIES` from test module for reuse

### What was done (Session 5)
- Added `--format` CLI flag and `fmt` parameter to `generate_landscape()` — accepts `"prose"` (default, existing behavior joined by spaces) or `"poetic"` (lines joined by `\n`, weather string capitalized)
- Weather string is now capitalized in both modes (`weather.capitalize()` instead of raw `weather`) — fixes a long-standing cosmetic issue where the third sentence started lowercase
- Added 5 tests: `test_default_format_is_prose`, `test_format_poetic_has_linebreaks`, `test_format_prose_no_linebreaks`, `test_format_poetic_all_lines_capitalized`, `test_format_flag_works_via_cli`
- Tests increased from 39 to 44 total (18 todo + 26 landscape)

### What was done (Session 6)
- Added **biome combination** via `--combine`/`-c` CLI flag and `combine` parameter to `generate_landscape()` — accepts comma-separated biome names (e.g. `--combine forest,desert`) to create blended landscapes
- Refactored `_pick()` to accept a list of biomes and draw from their union of word banks, so vocabulary from all specified biomes is blended into every generated description
- When combining, the biome name in the template becomes `"forest and desert"`; the `--show-biome` tag shows all biomes as `"[forest, desert]"`
- Single-biome `--combine` produces identical output to `--biome` (backward compatible)
- Added 6 tests: `test_combine_two_biomes_contains_both_names`, `test_combine_three_biomes_contains_all_names`, `test_combine_uses_vocabulary_from_both`, `test_combine_show_biome_shows_all`, `test_combine_single_biome_equals_regular`, `test_combine_flag_exists_via_cli`
- Tests increased from 44 to 50 total (18 todo + 32 landscape)

### What was done (Session 8)
- Fixed **verb conjugation** bug: `_conjugate(verb)` function added to `landscape.py` that correctly handles third-person singular verb forms
  - Regular verbs get `+s` (whisper → whispers, glow → glows)
  - Verbs ending in `s`, `sh`, `ch`, `x`, `z`, `o` get `+es` (crash → crashes, hiss → hisses, stretch → stretches, echo → echoes)
  - Verbs ending in consonant + `y` get `y→ies` (fly → flies)
- Updated `SENTENCE_TEMPLATES` to use `{verb_conjugated}` instead of bare `{verb}s` in all three middle templates
- Added 4 new tests: `test_conjugate_adds_s_for_regular_verbs`, `test_conjugate_adds_es_for_sibilant_endings`, `test_conjugate_handles_y_endings`, `test_conjugate_output_no_bare_s_append_for_es_verbs`
- Tests increased from 53 to 57 total (18 todo + 39 landscape)

### What was done (Session 9)
- Added **template variety for weather and anomaly slots**: weather went from 1 template to 3, anomaly from 2 to 4
  - Weather templates: `"{Weather}."`, `"The air tells its own story: {weather}."`, `"{Weather}, as if the {display} itself breathes."` (the last two tie weather to the biome/noun context)
  - Anomaly templates: `"{anomaly}"`, `"Something is not right — {anomaly}"`, `"A strange detail catches your eye: {anomaly}"`, `"There is a quiet wrongness here: {anomaly}"`
- Updated weather format call to pass `display` parameter (needed by the new `as if the {display}` template)
- Added 2 tests: `test_template_variety_weather_has_varied_structure`, `test_template_variety_anomaly_has_varied_structure`
- Tests increased from 57 to 59 total (18 todo + 41 landscape)

### What was done (Session 10)
- Added **multi-sentence generation** via `--detail`/`-d` CLI flag and `detail` parameter to `generate_landscape()`
  - `detail=1` (default): opening + 1 middle + 1 weather + optional anomaly (backward compatible)
  - `detail=0`: opening sentence only (minimal mode)
  - `detail=2`: opening + 2 middle + 2 weather + optional anomaly
  - `detail=3`: opening + 3 middle + 3 weather + optional anomaly
- Refactored `generate_landscape()` to loop over middle+weather pairs, picking fresh words and templates for each pair
  - Each additional sentence gets its own random word pick and template choice, so sentences within the same landscape vary in vocabulary and structure
- Added 5 tests: `test_detail_default_is_one`, `test_detail_zero_is_shorter_than_one`, `test_detail_two_is_longer_than_one`, `test_detail_three_produces_valid_output`, `test_detail_flag_exists_via_cli`
- Tests increased from 59 to 64 total (18 todo + 46 landscape)

### What was done (Session 11)
- Added **`--bias` CLI flag** and `bias` parameter to `generate_landscape()` exposing the word-weight system for user control
  - Four modes: `normal` (default, common=10 / normal=5 / rare=1), `common` (common=20, further skews toward frequent words), `rare` (rare=3, makes uncommon words appear more often), `flat` (all=1, uniform selection)
  - `BIAS_MODES` dict maps mode names to weight triples
  - `_word_weight()` now accepts a `bias` parameter; `_pick()` threads it through
- Added 6 tests: `test_bias_default_is_normal`, `test_bias_modes_affect_word_weights`, `test_bias_flat_produces_valid_output`, `test_bias_common_increases_common_word_frequency`, `test_bias_rare_increases_rare_word_frequency`, `test_bias_flag_exists_via_cli`
- Tests increased from 64 to 70 total (18 todo + 52 landscape)

### What was done (Session 12)
- Added **`--show-seed` CLI flag** and `show_seed` parameter to `generate_landscape()` — when set, the seed used is appended in square brackets (e.g. `[seed=42]`)
  - If a seed is provided via `--seed`, that seed is shown
  - If no seed is provided, a random seed is auto-generated, the RNG is seeded with it, and that seed is shown — making every output reproducible
- Added 5 tests: `test_show_seed_with_provided_seed_shows_seed`, `test_show_seed_default_hides_seed`, `test_show_seed_without_seed_generates_seed`, `test_show_seed_output_is_reproducible`, `test_show_seed_flag_works_via_cli`
- Tests increased from 70 to 75 total (18 todo + 57 landscape)

### What was done (Session 13)
- Added **mood/emotion overlay** via `--mood` CLI flag and `mood` parameter to `generate_landscape()`
  - Three moods: `eerie`, `vibrant`, `desolate`
  - Each mood defines a curated set of tone-matched words per category (adjectives, elements, nouns, verbs, weathers, anomalies)
- Added `MOOD_WORDS` dict and `MOOD_BOOST = 5` constant
- Updated `_word_weight()` to accept `mood` and `category` params — when a word matches the active mood's category list, its weight is multiplied by `MOOD_BOOST` (5x), making mood-themed words much more likely without excluding other vocabulary
- `mood` parameter threads through `_pick()` → `_word_weight()` for all word selections
- Mood works orthogonally to `--bias`: bias sets the base weight distribution, mood multiplies on top; they compose naturally
- Added 5 tests: `test_mood_does_not_break_output`, `test_mood_word_weight_boosted_for_matched_words`, `test_mood_word_weight_not_boosted_for_unmatched_words`, `test_mood_category_specific_boost`, `test_mood_flag_exists_via_cli`
- Tests increased from 75 to 80 total (18 todo + 62 landscape)

### What was done (Session 14)
- Added **`--mood-weight` CLI flag** and `mood_weight` parameter to `generate_landscape()` — a float multiplier (default: 5) that controls how strongly mood-matched words are boosted
  - `--mood-weight 1` means no mood boost (equivalent to no mood)
  - `--mood-weight 0` suppresses mood words entirely (weight = 0)
  - Higher values (e.g. 10, 20) make mood words dominate the output
  - `--mood-weight` replaces the hard-coded `MOOD_BOOST = 5` constant, threading through `_word_weight()` → `_pick()` → `generate_landscape()` → CLI
- `MOOD_BOOST` kept as module-level constant (default value), so existing code that imports it still works
- Added 6 tests: `test_mood_weight_one_equals_no_boost`, `test_mood_weight_zero_suppresses_mood_words`, `test_mood_weight_high_magnifies_boost`, `test_mood_weight_default_matches_mood_boost`, `test_mood_weight_produces_valid_output`, `test_mood_weight_flag_exists_via_cli`
- Tests increased from 80 to 86 total (18 todo + 68 landscape)

## 2026-07-11

### What was done (Session 17)
- Added **per-category mood-weight overrides** via 6 CLI flags (`--mood-weight-adjective`, `--mood-weight-element`, `--mood-weight-noun`, `--mood-weight-verb`, `--mood-weight-weather`, `--mood-weight-anomaly`) and `mood_weight_overrides` dict parameter to `generate_landscape()` — users can now control mood weight independently per category
  - Each flag accepts a float (same as `--mood-weight`), overriding the global mood weight for that specific category
  - Example: `--mood eerie --mood-weight 5 --mood-weight-adjective 20` = eerie mood with heavy adjective skew but normal boost for everything else
- Added `mood_weight_overrides` dict parameter to `_word_weight()` — resolves `mood_weight_overrides.get(category, mood_weight)` for each mood-boost computation
- Added `mood_weight_overrides` parameter to `_pick()` and `generate_landscape()` — threads through to `_word_weight()` the same way `bias_overrides` threads through to `_pick()`
- Added 7 tests: `test_mood_weight_overrides_default_does_not_change_output`, `test_mood_weight_overrides_empty_dict_equals_no_override`, `test_mood_weight_overrides_produces_valid_output`, `test_mood_weight_adjective_override_high_boosts_mood_adjectives`, `test_mood_weight_element_override_zero_suppresses_mood_elements`, `test_mood_weight_overrides_multiple_categories`, `test_mood_weight_overrides_cli_flags_exist`
- Tests increased from 102 to 109 total (18 todo + 91 landscape)

## 2026-07-11

### What was done (Session 19)
- Added **cross-sentence word dedup**: `_pick()` now accepts an optional `used_words` set — when provided, already-used words are excluded from the selection pool and the newly chosen word is added to the set
- In `generate_landscape()`, a single `used_words = set()` is threaded through all `_pick()` calls, so no word can be selected more than once per landscape (across all categories: adjectives, elements, nouns, verbs, weathers, anomalies)
- If the filtered pool is empty (all words exhausted), falls back to the unfiltered pool — so edge cases with tiny biome word banks don't crash
- Backward compatible: `used_words=None` (default) preserves the existing behavior for tests or direct `_pick()` calls that don't need dedup
- Updated `test_detail_two_is_longer_than_one` to `test_detail_two_has_more_sentences_than_one` (counts periods instead of char length) to avoid a statistical edge case where anomaly text at detail=1 happens to equal the extra sentence pair at detail=2
- Added 5 tests: `test_word_dedup_via_used_words_parameter`, `test_word_dedup_across_multiple_picks_same_category`, `test_word_dedup_across_categories`, `test_word_dedup_without_used_words_still_works`, `test_word_dedup_still_produces_valid_output`, `test_word_dedup_does_not_break_format_modes`
- Tests increased from 116 to 122 total (18 todo + 104 landscape)

## 2026-07-11

### What was done (Session 20)
- Added **configurable anomaly probability** via `--anomaly-prob` CLI flag and `anomaly_prob` parameter to `generate_landscape()` — users can now control how often anomalies appear (0.0 = never, 1.0 = always, default 0.3 preserves existing behavior)
  - Replaced the hardcoded `random.random() < 0.3` with `random.random() < anomaly_prob`
  - This was the last remaining magic number in the generation logic
- Added 5 tests: `test_anomaly_prob_default_works`, `test_anomaly_prob_zero_suppresses_anomalies`, `test_anomaly_prob_one_always_has_anomaly`, `test_anomaly_prob_produces_valid_output`, `test_anomaly_prob_flag_exists_via_cli`
- Tests increased from 122 to 127 total (18 todo + 109 landscape)

## 2026-07-11

### What was done (Session 21)
- Fixed **`--count` + `--seed` interaction**: previously, `--seed 42 --count 3` produced the same output 3 times because every loop iteration passed the same seed. Now the seed auto-increments per iteration (`seed + i`), so each output is unique and individually reproducible
  - `--seed 42 --count 3` is equivalent to running `--seed 42`, `--seed 43`, `--seed 44` separately
  - `--count` without `--seed` (fully random) is unaffected
- One-line change in `main()`: `effective_seed = args.seed + i if args.seed is not None else None`
- Added 4 tests in `TestCountWithSeed` class: `test_count_seed_sequence_produces_unique_outputs`, `test_count_seed_sequence_is_reproducible`, `test_count_seed_sequence_different_from_single_seed`, `test_count_without_seed_produces_varied_outputs`
- Tests increased from 127 to 131 total (18 todo + 113 landscape)

## 2026-07-11

### What was done (Session 22)
- Added **3 new biomes**: `ruined city`, `fungal grove`, and `sky islands` — expanding the landscape generator beyond purely natural environments into weird, unusual settings
  - **ruined city**: post-urban decay vocabulary (crumbling, rusted, skeletal facades and girders)
  - **fungal grove**: bioluminescent mushroom forest (spore glow, mycelial, caps and hyphae)
  - **sky islands**: floating archipelago above the clouds (cloud-wreathed, ethereal, archipelagos and updrafts)
- Added 11 tests in `TestNewBiomes` class: `test_ruined_city_in_biomes_list`, `test_fungal_grove_in_biomes_list`, `test_sky_islands_in_biomes_list`, `test_ruined_city_produces_valid_output`, `test_fungal_grove_produces_valid_output`, `test_sky_islands_produces_valid_output`, `test_ruined_city_uses_specific_vocabulary`, `test_fungal_grove_uses_specific_vocabulary`, `test_sky_islands_uses_specific_vocabulary`, `test_new_biomes_appear_in_random_selection`, `test_combine_with_new_biome_uses_vocabulary`
- Tests increased from 131 to 142 total (18 todo + 124 landscape)

## 2026-07-11

### What was done (Session 23)
- **Fixed noun-verb agreement in middle template 3**: Changed `{verb_conjugated}` to `{verb}` in `SENTENCE_TEMPLATES["middle"][2]` — the third middle template was `"The {noun} {verb_conjugated} with {element}."`, which produced grammatically incorrect outputs like "The trees whispers with light." (plural noun + singular verb). Now produces "The trees whisper with light." (plural noun + bare verb).
  - Templates 1 and 2 are unaffected — their subject (`{Element}` and `{element}`) are singular, so `{verb_conjugated}` is correct there.
- Added 2 tests: `test_middle_third_template_uses_bare_verb` (direct template string assertion) and `test_middle_third_end_to_end_bare_verb` (smoke test with `template_set="third"`).
- Tests increased from 142 to 144 total (18 todo + 126 landscape)

## 2026-07-11

### What was done (Session 24)
- Added **adverb word category** (`ADVERBS`) to `landscape.py` — a new 12-word global adverb pool with weighted tiers (4 common, 4 rare)
  - Common adverbs: softly, gently, silently, quietly
  - Rare adverbs: relentlessly, patiently, eternally, ceaselessly
  - Normal adverbs: endlessly, slowly, constantly, subtly
- Added **mood-specific adverbs** to each mood in `MOOD_WORDS`: eerie gets silent/slow/eternal adverbs, vibrant gets gentle/soft/endless, desolate gets relentless/constant/slow
- Added `"adverbs"` to the global pool dict in `_pick()` — fully integrated with weighted selection, bias, mood boosts, per-category bias/mood-weight overrides, and cross-sentence word dedup
- `generate_landscape()` picks a single adverb per landscape (before the sentence loop), threaded through all format calls as `{adverb}` — templates that don't use it ignore it
- Added **2 new middle templates** with `{adverb}`:
  - `"{Element} {verb_conjugated} {adverb} through the {noun}."` (index 3)
  - `"Beneath the {noun}, {element} {verb_conjugated} {adverb}."` (index 4)
- Existing 3 middle templates are unchanged — `template_set="first/second/third"` and `template_overrides` still work
- Added 6 tests: `test_output_contains_known_adverb`, `test_adverb_appears_in_middle_templates`, `test_adverb_with_mood_does_not_break_output`, `test_adverb_is_deterministic_with_seed`, `test_adverb_with_detail_three_produces_valid_output`, `test_adverb_word_weight_function_works`
- Tests increased from 144 to 150 total (18 todo + 132 landscape)

## 2026-07-11

### What was done (Session 26)
- Added **JSON output format** via `--format json` CLI flag — outputs a structured JSON object with the landscape `text` plus metadata fields (`biome`, `seed`, `mood`, `bias`, `detail`, `template_set`, `anomaly_prob`, and any overrides)
  - When `--combine` is used, includes both `biome` (display string) and `biomes` (list of all combined biomes)
  - When `--mood` is set, includes `mood` as a list (even for a single mood, for consistency)
  - The `text` field contains the clean prose without bracketed biome/seed tags — metadata goes in JSON fields instead
  - All existing `--format` modes (`prose`, `poetic`) are unchanged
- Added `import json` to `landscape.py`
- Added 9 tests: `test_format_json_valid_json`, `test_format_json_contains_text_key`, `test_format_json_contains_biome_key`, `test_format_json_contains_seed_when_provided`, `test_format_json_text_matches_prose`, `test_format_json_with_combine_includes_biomes_list`, `test_format_json_includes_mood_when_set`, `test_format_json_does_not_have_bracketed_tags`, `test_format_json_works_with_all_formats_flag`
- Tests increased from 155 to 164 total (18 todo + 146 landscape)

### What was done (Session 25)
- Added **mood blending**: `--mood` CLI flag now uses `action="append"` and accepts multiple values — users can blend moods by repeating the flag (e.g. `--mood eerie --mood vibrant`) to create hybrid tonal palettes
  - `--mood eerie --mood vibrant` = haunting beauty (eerie's silence + vibrant's light)
  - `--mood eerie --mood desolate` = bleak and unsettling (both lean into darkness/stillness)
  - `--mood vibrant --mood desolate` = beauty amidst decay (vibrant's glow + desolate's barren)
  - `--mood eerie --mood vibrant --mood desolate` = all three (most words from any mood list get boosted)
- Modified `_word_weight()` to accept `mood` as a string (single mood, backward compatible), list, or tuple — when a word matches **any** active mood's category list, the mood-weight boost applies
  - The `break` on first match ensures the boost is applied once (not compounded) even if a word appears in multiple moods' lists
- No changes to `_pick()` or `generate_landscape()` signatures — `mood` threaded through as before, both string and list callers work
- `--mood` CLI changed from `type=str, choices=...` to `action="append", type=str, choices=...` — single usage (`--mood eerie`) produces a 1-element list internally, which `_word_weight()` normalizes the same way as a bare string
- Added 5 tests: `test_mood_combine_does_not_break_output`, `test_mood_combine_uses_words_from_both`, `test_mood_combine_different_from_single_mood`, `test_mood_combine_all_three_still_valid`, `test_mood_combine_cli_flag_accepts_multiple`
- Tests increased from 150 to 155 total (18 todo + 137 landscape)

## 2026-07-11

### What was done (Session 28)
- Added **`{adverb}` to the third opening template** — changed `"The {adj} {display} lies ahead."` to `"The {adj} {display} lies {adverb} ahead."` in `SENTENCE_TEMPLATES["opening"]`. The adverb is already picked per-landscape and passed to all template format calls, but only middle templates used it. Now the opening template can produce lines like "The crystal forest lies silently ahead.", making the opener more expressive.
- No new tests needed — existing template tests (`test_output_starts_with_valid_opening`, `test_template_set_third_uses_third_opening`, `test_template_set_third_weather_has_expected_pattern`) all still pass because the opening start ("The ") and index 2 are unchanged.
- Tests: still 167 (18 todo + 149 landscape)

### What was done (Session 29)
- Added **`--anomaly-count` CLI flag** and `anomaly_count` parameter to `generate_landscape()` — users can now control how many anomaly rolls happen per landscape (default: 1, range 0–3)
  - Each anomaly independently rolls against `anomaly_prob`, so `--anomaly-count 3 --anomaly-prob 0.5` yields ~1–2 anomalies on average
  - `--anomaly-count 0` suppresses anomalies regardless of `anomaly_prob` (alternative to `--anomaly-prob 0`)
  - Replaced the single `if` block with a `for _ in range(anomaly_count)` loop
  - Added `anomaly_count` to JSON metadata output
- Added 6 tests: `test_anomaly_count_default_is_one`, `test_anomaly_count_zero_no_anomalies`, `test_anomaly_count_two_sometimes_has_multiple`, `test_anomaly_count_produces_valid_output`, `test_anomaly_count_flag_exists_via_cli`, `test_anomaly_count_json_includes_field`
- Tests increased from 167 to 173 total (18 todo + 155 landscape)

### What was done (Session 30)
- **Added `{adverb}` to opening templates 0 and 1, and weather template 1** — the adverb is now used in all 3 opening templates (was only in template 2/third) and in the first weather template (was not used by any weather template)
  - Opening 0: `"A vast {adj} {display} stretches {adverb} before you."` (previously no adverb)
  - Opening 1: `"Before you, a {adj} {display} comes into view {adverb}."` (previously no adverb)
  - Weather 1: `"{Weather} {adverb}."` (previously `"{Weather}."`)
  - No code changes needed — `adverb` was already threaded through all format calls
  - No new tests — existing adverb and template tests cover the change
- Tests: still 173 total (18 todo + 155 landscape)

### Current status
Working. All 173 tests pass (18 todo + 155 landscape).
