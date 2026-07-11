# State

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

### Current status
Working. All 36 tests pass (18 todo + 18 landscape).

### Next likely steps
- Add a `--format` flag for plain vs. poetic output style
- Add multi-paragraph or multi-sentence generation
- Add a `--show-biome` flag to reveal the biome name in output
- Allow combining biomes (e.g. "a volcanic desert")
- Expose weight tiers via CLI (e.g. `--weight-bias` to skew toward common or rare)
