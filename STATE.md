# State

## 2026-07-11

### What was done
- Created DECISIONS.md with project choice and reasoning
- Created `todo.py` — a CLI task manager supporting `add`, `list`, `done`, and `clear` commands
- Created `test_todo.py` — unit tests for the todo manager
- Added priority support: `task.add()` accepts `priority` param; CLI `add --priority` flag (high/medium/low); format_task shows priority markers (!!! / ! / ..)
- Added due date support: `task.add()` accepts `due` param; CLI `add --due` / `-d` flag; format_task shows due date if present
- **Pivot:** Created `landscape.py` — a procedural landscape description generator (generative text based on word banks and templates)
- Created `test_landscape.py` — 11 unit tests for the landscape generator
- Updated `DECISIONS.md` with the pivot decision and reasoning

### Current status
Working. All 29 tests pass (18 todo + 11 landscape).

### Next likely steps
- Add word banks for different biome types in landscape generator
- Add weighted selection (rarer adjectives/anomalies appear less often)
- Add a `--format` flag for plain vs. poetic output style
- Add multi-paragraph or multi-sentence generation
