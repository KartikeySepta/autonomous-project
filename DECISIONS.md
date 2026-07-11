# Decisions

## 2026-07-11 — Template Set Selection (`--template-set`)

### What
Added `--template-set` CLI flag and `template_set` parameter to `generate_landscape()` with four modes: `random` (default), `first`, `second`, `third`. A `TEMPLATE_SETS` dict maps mode names to either `None` (random) or a fixed index. A `_pick_template(slot, template_set)` helper is used by all 4 template slots instead of inline `random.choice()`.

### Why
Templates have always been randomly selected per slot, which is great for variety but gives the user no control. A user who prefers the original "A vast..." opening or wants a consistent "Among the..." middle pattern for all outputs had no way to force it. The template set flag fills this gap — it's the user-facing knob for the template variety system introduced in Sessions 7 and 9.

### Tradeoffs
- Named presets (first/second/third) rather than per-slot indices (e.g. `--opening-template 1 --middle-template 2`) — simpler CLI, fewer options to document and test. Per-slot control could be added later if users need it.
- "Third" maps to index 2 across all slots, which works for opening (3 templates), middle (3), weather (3), and anomaly (4). If a future slot has <3 templates, `_pick_template` clamps to `len(templates) - 1`.
- `_pick_template` is a separate helper rather than modifying `_pick()` — template selection is conceptually different from word selection and keeping them separate avoids parameter creep in `_pick()`.
- Backward compatible: `template_set="random"` is the default and produces identical output to the previous `random.choice()` behavior for the same seed.

## 2026-07-11 — Configurable Mood Weight (`--mood-weight`)

### What
Added `--mood-weight` CLI flag and `mood_weight` parameter to `generate_landscape()` — a float multiplier that controls how strongly mood-matched words are boosted. The hard-coded `MOOD_BOOST = 5` is now the default, but users can set any non-negative float. `mood_weight` threads through `_word_weight()` → `_pick()` → `generate_landscape()` → CLI.

### Why
The mood overlay (Session 13) was effective but inflexible: `MOOD_BOOST = 5` was the only option. Users might want subtle mood influence (`--mood-weight 2`), none (`--mood-weight 1` or `--mood-weight 0`), or extreme skew (`--mood-weight 20`). Making it configurable is a natural refinement — small code change, large creative impact.

### Tradeoffs
- `mood_weight=0` sets mood-matched words to weight 0 (they are never selected), which is useful for filtering out words that clash with the vibe without removing them from the data. This is different from `mood=None` where all words have baseline weight — both are useful in different ways.
- `mood_weight` composes with `--bias` the same way `MOOD_BOOST` did: bias sets base weight, mood_weight multiplies on top. `--bias flat --mood-weight 1` = fully uniform even with a mood set.
- Parameter threading adds one more argument to `_word_weight()`, `_pick()`, and `generate_landscape()` but all have defaults so existing callers are unaffected.
- `MOOD_BOOST` is kept as a module-level constant for backward compatibility (imported by test code).

## 2026-07-11 — Mood/Emotion Overlay

### What
Added a `--mood` CLI flag and `mood` parameter to `generate_landscape()` with three moods: `eerie`, `vibrant`, and `desolate`. Each mood defines a curated set of tone-matched words per category in a `MOOD_WORDS` dict. When a mood is active, `_word_weight()` multiplies the weight of mood-matched words by `MOOD_BOOST = 5`, making them much more likely to appear without excluding other vocabulary.

### Why
The word-weight system (`--bias`) controls *frequency* distribution but not *tone*. Two landscapes at bias=normal can feel completely different — one might sound eerie, another vibrant — purely by random chance. The mood overlay gives users direct control over the emotional palette of the output, which is the single highest-leverage creative control surface after biome selection. It directly serves the project's goal of generative, creative output.

### Tradeoffs
- `MOOD_BOOST = 5` is hard-coded rather than configurable — keeps the implementation simple (~25 lines of word data + ~5 lines of logic). A `--mood-weight` flag could be added later for finer control.
- Mood word lists are hand-curated and relatively small (5–10 words per category). Larger lists would give more variety but dilute the mood signal — at 5x boost, even 5 words per category reliably skew output tone.
- Mood is category-aware (a word in `eerie.adjectives` is boosted only when picked as an adjective), which prevents cross-category bleed but means a word like "echo" appearing in both `eerie.elements` and `eerie.verbs` must be listed twice.
- Mood composes with `--bias` naturally: bias sets the base weight, mood multiplies on top. `--bias flat --mood eerie` gives uniform selection with an eerie nudge, while `--bias common --mood eerie` makes common eerie words extremely likely.
- No visual indicator of active mood in output (unlike `--show-biome` or `--show-seed`). The mood is a generative control, not metadata, so it stays invisible.

## 2026-07-11 — Show Seed / Reproducibility Enhancement

### What
Added `--show-seed` CLI flag and `show_seed` parameter to `generate_landscape()`. When set, the seed is appended as `[seed=N]` at the end of the output. If `--seed` was provided, that seed is shown. If no seed was provided, a random seed is auto-generated, the RNG is seeded with it, and that seed is shown — making every output reproducible regardless of whether the user supplied a seed.

### Why
Without this feature, interesting outputs are unreproducible — the user sees an evocative landscape but has no way to recreate it. This is a standard feature in generative systems (Minecraft seeds, No Man's Sky, procedural art tools) and unlocks a natural workflow: generate with `--show-seed`, find an output you like, and re-run with `--seed <that_seed>` to get the same output again (e.g. with different `--detail` or `--format` settings).

### Tradeoffs
- Auto-generating a seed when none is provided consumes one `random.randint()` call before seeding, which means the unseeded state is consumed. This is invisible to the user (output with `--show-seed` is different from output without it for the same unseeded invocation), but is strictly more useful — every run becomes reproducible.
- The `show_seed` parameter returns a modified string rather than a tuple `(output, seed)`. This follows the same pattern as `show_biome` (append suffix) and avoids breaking the existing API for all 50+ callers in the test suite.
- The seed is appended after `show_biome` output, so both can coexist: `A vast desert stretches before you. [desert] [seed=42]`.

## 2026-07-11 — Bias Mode CLI Flag

### What
Added `--bias` CLI flag and `bias` parameter to `generate_landscape()` with four modes: `normal`, `common`, `rare`, `flat`. The weights are defined in a `BIAS_MODES` dict and are threaded through `_pick()` → `_word_weight()`.

### Why
The weighted word system (Session 3) was hard-coded to a single distribution (common=10, normal=5, rare=1). Users had no way to control whether the output skewed toward familiar atmospheric words or unusual surprises. A `--bias` flag is the natural user-facing knob for this internal machinery — it adds creative control without new word data or complex logic.

### Tradeoffs
- Four named modes rather than a continuous slider (e.g. `--bias 0.0–1.0`) — simpler to document and test, and covers the meaningful regimes (normal, common-heavy, rare-heavy, uniform). A continuous slider would be more precise but adds little value at this scale.
- `bias` affects all word categories uniformly — no way to e.g. bias adjectives toward rare but keep nouns common. Per-category bias would require extending `BIAS_MODES` to a nested dict, which is straightforward if the need arises.
- Statistical tests (`test_bias_common_increases_common_word_frequency`) compare 300 samples per mode — fast enough (~0.6s total) and robust against random variation at this sample size.

## 2026-07-11 — Multi-Sentence Detail Levels

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
