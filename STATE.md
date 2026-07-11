# State

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

### Current status
Working. All 64 tests pass (18 todo + 46 landscape).

### Next likely steps
- Expose weight tiers via CLI (e.g. `--weight-bias` to skew toward common or rare)
- Expose template set choice via CLI flag (e.g. `--template-set`)
- Add a mood/emotion overlay that biases word selection toward a specific tone
