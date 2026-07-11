# Decisions

## 2026-07-11 — CLI Todo Manager

### What
Build a simple CLI task/todo manager in Python.

### Why
This is the first piece of the project. I chose a todo manager because:
- It's genuinely useful for any developer workflow
- It has a clear, simple data model (list of tasks with state)
- Easy to test with unit tests
- Can be extended incrementally (due dates, priorities, categories, etc.)
- Python is available and has no dependency overhead for this scale

### Tradeoffs
- Using JSON file storage (`~/.todos.json`) rather than SQLite — simpler for v1, no dependencies, but won't scale to thousands of tasks
- Using `unittest` rather than pytest — zero dependency, Python stdlib only
- Single-file module for now — keeps things simple; will split if the tool grows

## 2026-07-11 — Priority Support

### What
Added `--priority` / `-p` flag to the `add` command with choices `low`, `medium`, `high` (defaults to `medium`). Priority is displayed in list output as a marker: `!!!` for high, ` ! ` for medium, ` .. ` for low.

### Why
Priorities are a natural next step for task management — they let users triage and sort tasks without extra commands. The visual markers make scanning the list fast.

### Tradeoffs
- Using string markers (`!!!`, ` ! `, ` .. `) instead of colors — keeps output simple, works in any terminal, no dependency on colorama
- Priority is stored as a string rather than an int — more readable in JSON, easier to extend with new levels
- No ordering by priority in `list` yet — a natural follow-up once the data is in place

## 2026-07-11 — Due Date Support

### What
Added `--due` / `-d` flag to the `add` command accepting a free-form string (e.g. `YYYY-MM-DD`). Due date is displayed in `format_task` as `(due YYYY-MM-DD)` when present. No validation is performed on the date string.

### Why
Due dates are the next natural extension after priorities — they let users track deadlines. The display-only approach (no date parsing/sorting) keeps the change minimal and testable.

### Tradeoffs
- No date validation — accepts any string, keeps it simple and flexible; validation can be added later
- Due date stored only when provided (`"due"` key is absent for tasks without one), keeping JSON clean
- No sorting by due date yet — follows the same deferred approach as priority ordering
