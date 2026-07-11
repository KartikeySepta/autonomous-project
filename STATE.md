# State

## 2026-07-11

### What was done
- Created DECISIONS.md with project choice and reasoning
- Created `todo.py` — a CLI task manager supporting `add`, `list`, `done`, and `clear` commands
- Created `test_todo.py` — unit tests for the todo manager
- Added priority support: `task.add()` accepts `priority` param; CLI `add --priority` flag (high/medium/low); format_task shows priority markers (!!! / ! / ..)

### Current status
Working. Tests pass.

### Next likely steps
- Add due dates to tasks
- Support listing by status or priority
- Add `edit` command to modify task details
- Add `--due` flag to `add`
