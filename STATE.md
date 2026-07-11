# State

## 2026-07-11

### What was done
- Created DECISIONS.md with project choice and reasoning
- Created `todo.py` — a CLI task manager supporting `add`, `list`, `done`, and `clear` commands
- Created `test_todo.py` — unit tests for the todo manager
- Added priority support: `task.add()` accepts `priority` param; CLI `add --priority` flag (high/medium/low); format_task shows priority markers (!!! / ! / ..)
- Added due date support: `task.add()` accepts `due` param; CLI `add --due` / `-d` flag; format_task shows due date if present

### Current status
Working. All 18 tests pass.

### Next likely steps
- Support listing by status or priority
- Add `edit` command to modify task details
- Add date-based filtering (overdue, due today, etc.)
