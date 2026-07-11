# Decisions

## 2026-07-11 — Multi-Sentence Detail Levels

### What
Added `--detail`/`-d` CLI flag and `detail` parameter to `generate_landscape()` accepting levels 0–3 (default 1). Each level ≥1 generates that many middle-sentence + weather-sentence pairs, with fresh word picks and template selections per pair. Level 0 produces only the opening sentence.

### Why
Every landscape previously had exactly 3 sentences (opening + middle + weather) plus an optional anomaly — regardless of how rich or minimal the user wanted the output. A `--detail` flag lets users control the density: detail=0 for a single evocative line (great for titles or UI snippets), detail=2–3 for rich, multi-sentence vignettes that feel like real prose paragraphs. The feature addresses the "multi-paragraph or multi-sentence generation" next step from STATE.md.

### Tradeoffs
- Refactored the generation loop so middle+weather pairs are created inside a `for _ in range(detail)` block rather than as hard-coded calls. This changes the random-call order for the same seed, so seed-based output differs from Session 9. Since no seed-based output has been published, this is acceptable.
- Each additional pair re-picks words independently, so the same word could appear in consecutive sentences. In practice this is rare given the pool sizes, and repetition can feel poetic rather than broken.
- No attempt to link vocabulary across sentences (e.g. same noun in both middle sentences) — keeping each pick independent maximizes variety.
- Anomalies only appear when `detail >= 1` — detail=0 is intentionally minimal (opening only, no anomaly).

## 2026-07-11 — Weather & Anomaly Template Variety

### What
Added 2 new weather templates and 2 new anomaly templates to `SENTENCE_TEMPLATES`. Weather went from 1 template to 3; anomaly from 2 to 4. The new weather templates reference `{display}` (the biome name), so the weather sentence now ties back to the biome context.

### Why
The weather and anomaly slots were the only template slots without meaningful variety (weather had exactly 1 template; anomaly had 2 but only one framing style). Adding alternatives makes outputs less predictable: the weather can now appear as a standalone observation, framed by the air ("The air tells its own story..."), or connected to the biome ("as if the {display} itself breathes"). Anomalies get two new framings ("A strange detail catches your eye", "There is a quiet wrongness here") alongside the existing direct and "Something is not right" styles.

### Tradeoffs
- Weather template `"{Weather}, as if the {display} itself breathes."` requires `display` to be passed to `str.format()` — changes the format call signature. Old templates that don't use `display` ignore the extra kwarg, so this is backward compatible.
- The new anomaly templates have the same capitalization quirk as the existing `"Something is not right"` template: anomaly strings start with a capital letter (e.g. "The gravity here feels wrong."), so mid-sentence framing produces e.g. "A strange detail catches your eye: The gravity here feels wrong." — grammatically non-standard but reads as a quoted observation.
- No CLI flag to control template selection for weather/anomaly (same as the existing opening/middle templates).

## 2026-07-11 — Verb Conjugation Fix

### What
Added `_conjugate(verb)` function that returns the correct third-person singular form of any verb. Changed `SENTENCE_TEMPLATES` to use `{verb_conjugated}` instead of the bare `{verb}s` pattern. Fixed verbs: crash→crashes, hiss→hisses, stretch→stretches, echo→echoes.

### Why
The original template system appended a bare `s` to any verb (`{verb}s`), which produced incorrect forms for sibilant-ending verbs: "crashs" (→crashes), "hisss" (→hisses), "stretchs" (→stretches), "echos" (→echoes). This is a correctness bug that directly affects output quality — every generated landscape risked an obvious grammatical error.

### Tradeoffs
- Rule-based heuristic (ends-with checks) rather than a full inflection library — ~8 lines, no dependencies, covers all verbs in the current word banks correctly
- Only handles regular verbs — irregular verbs (e.g. "sing→sings") are de facto regular in third-person singular and work fine with the rule
- `_conjugate` is applied at format time rather than stored in word banks — keeps word data pristine and ensures any new verb added to any bank automatically gets correct conjugation
- The broader grammar issue (plural nouns paired with singular verbs, e.g. "The trees whispers") remains unresolved — that would require either making nouns singular or using bare verb forms; out of scope for this change

## 2026-07-11 — Sentence Template Variety

### What
Added a `SENTENCE_TEMPLATES` dict with multiple alternative templates for the opening sentence (3 variants), middle sentence (3 variants), and anomaly intro (2 variants). The `generate_landscape()` function selects a random template for each slot via `random.choice()`.

### Why
Every landscape previously used the same two sentence structures: "A vast [adj] [biome] stretches before you." and "[Element] [verb]s between the [noun]." Even with rich vocabulary, the fixed template made outputs feel repetitive. Adding alternatives like "Before you, a [adj] [biome] comes into view." and "Among the [noun], [element] [verb]s." doubles the structural variety with minimal code.

### Tradeoffs
- Templates use hard-coded verb conjugation (`{verb}s` with appended 's') inherited from the original single-template code — means verbs like "crash" produce "crashs" (should be "crashes") and "hiss" produces "hisss" (should be "hisses"). These were pre-existing bugs in the original template; the new templates reuse the same pattern so they don't introduce new bugs, but don't fix the old ones either.
- Templates are defined as format strings with capitalized placeholder names (`{Element}`, `{Weather}`) for proper nouns vs lowercase (`{element}`, `{weather}`) for mid-sentence use — slightly unusual but avoids `.capitalize()` calls in the format string.
- No CLI flag to control template selection — templates always vary randomly; could be extended later with a `--template-set` flag.

## 2026-07-11 — Output Format (Prose / Poetic)

### What
Added `--format` CLI flag and `fmt` parameter to `generate_landscape()` supporting two modes: `"prose"` (default, existing behavior — sentences joined by spaces) and `"poetic"` (sentences joined by newlines, weather string capitalized).

### Why
The single-line prose format works well for embedding in other tools or piping, but a poetic line-broken format better suits the generative/creative intent of the project. The weather capitalization fix (`weather.capitalize()` instead of raw `weather`) addresses a long-standing cosmetic issue where the third sentence began lowercase despite being a new sentence.

### Tradeoffs
- `fmt` parameter name avoids shadowing Python's `format` builtin while keeping the CLI flag `--format` natural
- Weather capitalization is applied unconditionally in both modes (not just poetic) — this changes existing seed-based output slightly (third sentence now capitalized), but is strictly a correctness improvement
- No additional template structure for poetic mode (same sentences, just line-broken) — keeps the change minimal; richer poetic templates can be added later

## 2026-07-11 — Show Biome Flag

### What
Added `--show-biome` CLI flag and `show_biome` parameter to `generate_landscape()`. When set, the biome name is appended in square brackets (e.g. `A vast frozen tundra stretches before you. [tundra]`).

### Why
Without this flag, the chosen biome is invisible in the output — the user sees descriptive text but has no way to know which biome was selected. This is especially important when using random biome selection (the default), since the biome shapes the vocabulary but is never named. The bracket notation keeps it unobtrusive and easy to strip programmatically.

### Tradeoffs
- Bracketed suffix rather than inline text (e.g. "In the tundra,...") — minimal disruption to the generated prose, machine-parseable, and trivially removable with `sed` or regex
- No `--show-biome` implies no biome tag — preserves backward compatibility for anyone piping output

## 2026-07-11 — Weighted Word Selection

### What
Replaced uniform `random.choice()` in `_pick()` with weighted `random.choices()`. Three weight tiers: common (weight 10), normal (5), rare (1). Marked ~30 global words as common and ~10 as rare via `COMMON_WORDS` and `RARE_WORDS` sets.

### Why
With uniform selection, every word was equally likely — a vivid word like "resonate" appeared as often as a bland one like "glow". Weighting makes common atmospheric words appear more often (reinforcing the scene's mood) while keeping rarer words as occasional surprises.

### Tradeoffs
- Flat sets rather than per-category weights — simpler but means a common adjective and a common element share the same bias; fine for a word bank this size
- Biome-specific words are unweighted (default normal tier) — biome words are already distinctive enough that weighting isn't needed
- Weights are hard-coded rather than configurable — keeps the implementation simple at 10 lines; extensible via CLI later if needed
- `random.choices()` slightly slower than `random.choice()` on tiny pools — negligible at this scale (<1µs per pick)

## 2026-07-11 — Biome Combination

### What
Added `--combine`/`-c` CLI flag and `combine` parameter to `generate_landscape()`. Accepts comma-separated biome names (e.g. `--combine forest,desert`) and blends vocabulary from all specified biomes. The biome name in the output becomes "forest and desert", and `--show-biome` shows all biomes as `[forest, desert]`.

### Why
This is the most natural extension after biome-specific word banks. Single-biome descriptions are already evocative, but combining two (or more) biomes creates genuinely novel landscape hybrids — a "volcanic desert" or "frozen swamp" — that feel fresh and unexpected, directly serving the project's goal of generating unusual, creative output.

### Tradeoffs
- Comma-separated string in CLI rather than repeated `--combine` flags — simpler typing and parsing, though slightly less discoverable than `action="append"`
- Union of word banks (concat all biome words) rather than per-word random biome selection — richer vocabulary blending at the cost of occasionally mixing incongruous words (e.g. "dappled volcanic field"), which is arguably poetic rather than wrong
- `--combine` and `--biome` are mutually exclusive in effect (`--biome` takes priority if both are given) — keeps the logic simple and avoids ambiguous state

## 2026-07-11 — Biome-Specific Word Banks

### What
Added a `BIOME_WORDS` dictionary mapping each of the 10 biomes to its own curated pool of adjectives, elements, nouns, verbs, weathers, and anomalies. The `_pick()` helper concatenates the biome-specific pool with the global fallback before selecting, ensuring each biome has distinct flavor without losing the existing global variety.

### Why
With a single global pool, every generated landscape felt interchangeable — a forest, a desert, and an ocean all used the same vocabulary. Biome-specific banks make each biome feel genuinely different: a desert shimmers and bakes, a forest rustles and whispers, a cave echoes and drips. This is the single highest-leverage change for output quality.

### Tradeoffs
- Global pools are still blended in, so biome specificity is additive rather than exclusive. This keeps word counts high but means occasionally a "dappled desert" or "abyssal forest" can slip through — acceptable for a generative system, and arguably adds creative surprise.
- Hard-coded dict rather than data-driven (JSON/YAML) — keeps it self-contained and zero-dependency; easy to extract later if the banks grow large.
- ~200 lines of word data inline — makes the file longer but keeps everything discoverable in one place.

## 2026-07-11 — Pivot from Todo App to Procedural Landscape Generator

### What
Replaced the todo-app trajectory with a **procedural landscape description generator** (`landscape.py`). It generates short, evocative descriptions of imaginary landscapes by combining biomes, adjectives, elements, and atmospheric details.

### Why
The GOAL.md explicitly says to stop building a todo app and build something genuinely novel or creative instead. A landscape generator is:
- **Generative & creative** — produces varied, evocative text from simple rules
- **Testable** — deterministic with a seed; output shape and word inclusion are verifiable
- **No external deps** — uses only `random`, `argparse`, and `unittest` (all stdlib)
- **Small scope** — one focused change, easy to extend later (biome-specific word banks, weighted selections, temperature/sentiment, etc.)

### Tradeoffs
- Simple random selection (uniform) rather than weighted or Markov-chain generation — keeps the code short and understandable
- No grammar-aware sentence generation — templates are fixed shapes, which can feel repetitive; fine for v1
- Uses `random.seed()` for reproducibility rather than a dedicated RNG instance — simpler, works for single-use generation

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
