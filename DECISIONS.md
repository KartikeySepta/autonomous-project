# Decisions

## 2026-07-12 — Biome Frequency Weights (`--biome-weight`)

### What
Added `--biome-weight` CLI flag and `biome_weights` parameter to `generate_landscape()` (default: `None`). Accepts comma-separated `biome=weight` pairs (e.g. `forest=5,desert=1,sky_islands=10`). When set, random biome selection uses `random.choices()` with the given weights instead of `random.choice()`. Biomes not mentioned get weight 1. Weight 0 suppresses a biome entirely.

### Why
With 13 biomes (10 natural + 3 weird), `random.choice(BIOMES)` treats all equally. A user who wants more sky-islands and fewer ruined cities had no way to express that. The `--biome-weight` flag is the biome-distribution equivalent of `--bias` (word frequency) and `--mood-blend` (emotional tone) — it gives users fine-grained control over *which worlds* get generated. It also enables use cases like "exclude biome X" (by setting its weight to 0) without a separate `--exclude` flag.

### Tradeoffs
- Comma-separated `key=value` pairs in a single string rather than repeated `--biome-weight` flags — simpler typing and parsing, consistent with `--combine`'s comma-separated biome list
- Only affects random selection (`--biome` and `--combine` are unchanged) — if the user explicitly names biomes, weights are irrelevant
- If all biomes have weight 0, falls back to equal probability — prevents crashes from degenerate input
- Weight 0 is a natural way to "exclude" a biome without needing a separate `--exclude` flag, following the precedent of `--anomaly-prob 0` for suppressing anomalies
- 6 new tests, 206 total.

## 2026-07-12 — JSON Array Output for `--format json --count N`

### What
Fixed `main()` so that when `fmt="json"` and `count > 1`, the output is wrapped in a JSON array (`[item1,\nitem2,\n...]`) instead of concatenating JSON objects with `\n\n`. Single-landscape JSON output (`--count 1`) is unchanged.

### Why
`--format json --count 3` previously produced three JSON objects separated by blank lines — an invalid JSON document that tools like `jq`, `json.loads()`, and HTTP APIs cannot parse. Each individual object was valid, but the composite was not. This made the JSON output mode unusable for batch generation. The fix makes `--format json --count N` produce a valid JSON array, which is the standard way to represent multiple homogeneous items in JSON.

### Tradeoffs
- Only the CLI `main()` path is affected; `generate_landscape()` still returns individual JSON strings — callers who iterate themselves are unchanged
- Single-landscape JSON output is not wrapped in a single-element array — preserves backward compatibility and avoids breaking existing consumers
- The array uses `",\n"` (comma-newline) separators for readability; output is a single valid JSON document ending with `\n`
- Prose and poetic formats are unaffected — they still use `\n\n` separation
- 4 new tests, 200 total.

## 2026-07-12 — Configurable Adverb Suppression (`--no-adverb`)

### What
Added `--no-adverb` CLI flag and `adverb_enabled` parameter to `generate_landscape()` (default: `True`). When `adverb_enabled=False`, the adverb pick is skipped entirely and an empty string is passed to all template format calls. A `_format_tmpl()` helper post-processes formatted text to collapse double spaces and remove space-before-period artifacts.

### Why
The adverb system (Session 24) was an automatic quality improvement with no off switch. Adverbs generally improve output, but some users may want to suppress them — for shorter/more direct descriptions, to avoid a formal tone, or to match a specific style where adverbs feel intrusive. Making it configurable follows the established pattern (same as `--no-dedup`, `--anomaly-prob`).

### Tradeoffs
- `adverb_enabled=True` is the default, preserving backward compatibility and existing seed-based output
- When disabled, the adverb variable is `""` rather than skipping the template placeholder — all templates continue to receive the kwarg but render it as empty
- The `_format_tmpl` helper is a general-purpose spacing cleanup that applies to all format calls regardless of adverb state — it's a no-op when adverb has a real value
- Flag name `--no-adverb` (negation) follows the same convention as `--no-dedup`
- 8 new tests, 196 total.

## 2026-07-12 — Configurable Word Dedup (`--no-dedup`)

### What
Added `--no-dedup` CLI flag and `dedup` parameter to `generate_landscape()` (default: `True`). When `dedup=False`, the `used_words` set is set to `None` instead of `set()`, bypassing the cross-sentence word deduplication logic in `_pick()` entirely.

### Why
Cross-sentence word dedup (Session 19) was an automatic quality improvement with no off switch. While dedup generally improves output, some users may want repetition — for poetic effect, for very short outputs where the word pool can handle it, or for specific creative purposes where repeating a word feels intentional rather than broken. Making dedup configurable follows the established pattern of exposing automatic behavior as user-facing controls (same pattern as `--anomaly-prob` for the hardcoded 0.3 magic number).

### Tradeoffs
- `dedup=True` is the default, preserving backward compatibility and existing seed-based output
- No change to `_pick()` — the existing `used_words=None` default already means "no dedup"; the change is only in `generate_landscape()` where the set is created
- The flag name `--no-dedup` (negation) rather than `--dedup` follows the convention of flags that disable features (like `git --no-verify`), making the default behavior (dedup on) unstated and the deviation explicit
- 6 new tests, 188 total.

## 2026-07-11 — File Output Flag (`--output` / `-o`)

### What
Added `--output` / `-o` CLI flag to `landscape.py` that writes generated output to a file instead of printing to stdout. Refactored `main()` to collect all generated landscape strings (including multi-landscape `--count` output) into a list, then either writes them to the specified file or prints to stdout.

### Why
The landscape generator is useful for creative writing prompts, worldbuilding, and procedural content generation — all use cases where saving output to a file is more practical than piping from stdout. A user generating 10 landscapes with `--count 10 --seed 42` wants to keep those as a file for later review or editing, not just see them flash by in the terminal. This is the most basic quality-of-life feature that was missing: the ability to capture output persistently.

### Tradeoffs
- Output file is overwritten (`"w"` mode) rather than appended — avoids surprise accumulation and matches the standard CLI tool convention (`grep -o outfile`, `curl -o outfile`). Append mode could be added later with a `--append` flag if users need it.
- The refactoring from per-iteration `print()` to collecting a `lines` list + single output write is a minor internal change but zero behavioral change for the default stdout path.
- `--count` output is separated by `\n\n` (blank line) matching the previous stdout behavior exactly — files look the same as what was printed.
- No `--quiet` flag needed: when `--output` is set, nothing is printed to stdout. This is the expected convention — output goes exclusively to the file.
- 5 new tests, 182 total.

## 2026-07-11 — Anomaly Lowercase in Colon Templates; Plain Biome Verb Fix

### What
Changed `SENTENCE_TEMPLATES["anomaly"][2]` and `[3]` from `{anomaly}` to `{anomaly_lower}`, so anomaly text starts with a lowercase letter when introduced by a colon (templates: "A strange detail catches your eye:" and "There is a quiet wrongness here:"). In `generate_landscape()`, the anomaly word is now stored in a variable so both `{anomaly}` (capitalized) and `{anomaly_lower}` (lowercased first letter) can be passed to the format call.

Also fixed a duplicate `"stretch"` verb in the `plain` biome word bank — the list contained `"stretch"` twice, giving it an unintentional 2x selection weight vs other plain verbs.

### Why
The colon-style anomaly templates have been producing grammatically non-standard output since Session 9 — `"A strange detail catches your eye: The gravity here feels wrong."` reads as awkward because the colon introduces what looks like a new sentence rather than a continuation. Lowercasing the first letter of the anomaly after a colon makes the sentence read naturally as a continuation. The em-dash template ("Something is not right — The gravity...") is fine with a capital because an em-dash separates independent clauses.

The duplicate `"stretch"` was a data bug that went unnoticed since Session 2 (when the plain biome was created). It only affected the plain biome and only at the verb-selection level, making `"stretch"` twice as likely as the other 4 plain verbs.

### Tradeoffs
- `{anomaly_lower}` is computed inline rather than stored in the word bank — keeps anomaly data pristine (full sentences with capitals) and avoids needing a separate lowercase word list.
- The standalone template 0 and em-dash template 1 keep `{anomaly}` (capitalized) because in those positions a capital letter is grammatically correct. The choice of which template uses which form is per-slot in `SENTENCE_TEMPLATES`, not an automatic rule — a future template that also embeds the anomaly mid-sentence would need to use `{anomaly_lower}` explicitly.
- No new tests added beyond the 4 anomaly-lowercase tests and one test fix — the template string assertions and output-matching tests provide adequate coverage.
- 159 tests total (18 todo + 141 landscape).

## 2026-07-11 — `{adverb}` in More Templates (Openings 0/1, Weather 1)

### What
Added `{adverb}` to two opening templates (0 and 1) and weather template 1 in `SENTENCE_TEMPLATES`. The adverb is now used in all 3 opening templates (was only in template 2) and for the first time in a weather template. No code changes — the `adverb` kwarg was already passed to all format calls.

### Why
The adverb system (Session 24) picked a single adverb per landscape and threaded it through all template format calls, but only 1 of 3 opening templates and 2 of 5 middle templates actually used it. Weather and anomaly templates didn't use it at all. This meant the adverb was invisible in most outputs — the word was picked, consumed a dedup slot, but never appeared. Adding `{adverb}` to the remaining opening templates and the simplest weather template makes the adverb useful in nearly every output regardless of which templates are randomly selected.

### Tradeoffs
- Opening template 0 now reads `"... stretches softly before you."` — the adverb sits before "before you" which reads naturally; "stretches silently before you" is more evocative than "stretches before you".
- Opening template 1 reads `"... comes into view silently."` — end-of-sentence adverb placement is slightly formal but grammatically natural.
- Weather template 1 reads `"A gentle rain falls silently."` — some weather strings already imply a manner ("ash drifts slowly downward" + "gently" = "ash drifts slowly downward gently"), but the dedup prevents exact word repetition and the combination reads as atmospheric layering rather than a bug.
- The adverb is now used in 6 of 12 templates (opening: 3/3, middle: 2/5, weather: 1/3, anomaly: 0/4) — up from 3 of 12. Anomaly templates remain adverb-free because `{anomaly}` includes a complete sentence with a period, making adverb attachment grammatically awkward.
- No new tests — existing tests (`test_output_contains_known_adverb`, `test_adverb_appears_in_middle_templates`, template set tests) already cover adverb appearance in output.
- 173 tests total (unchanged).

## 2026-07-11 — Multiple Anomalies (`--anomaly-count`)

### What
Added `--anomaly-count` CLI flag and `anomaly_count` parameter to `generate_landscape()` (default: 1, range 0–3). Instead of a single anomaly probability check per landscape, the generator now loops over `anomaly_count` iterations, each independently rolling against `anomaly_prob`. Each anomaly gets its own word pick (subject to cross-sentence dedup) and its own template selection.

### Why
At high detail levels (`--detail 3`), a rich landscape paragraph with only one potential anomaly felt under-explored — the most surreal element of the description was limited to a single appearance. Allowing multiple anomaly rolls lets users create landscapes with layered strangeness: multiple anomalies building on each other, especially useful for scenario generation or writing prompts where the uncanny accumulates.

### Tradeoffs
- `--anomaly-count 0` is an alternative suppression mechanism to `--anomaly-prob 0.0`: the former skips the loop entirely, the latter keeps the loop but never triggers. Both are valid; `anomaly_count=0` is slightly more explicit about intent.
- Each anomaly independently rolls probability and picks its own word/template, meaning a user could get 0, 1, 2, or 3 anomalies even at `--anomaly-count 3 --anomaly-prob 0.5`. This is intentional — the randomness of which anomalies appear is part of the generative appeal.
- Cross-sentence word dedup applies across all anomaly picks, so the same anomaly text won't appear twice in one landscape.
- 6 new tests, 173 total.

## 2026-07-11 — `mood_weight` in JSON Output

### What
Added `mood_weight` to the JSON output data. Previously, the `--mood-weight` parameter was silently omitted from JSON output even though every other major generation parameter (`bias`, `detail`, `template_set`, `anomaly_prob`) was included. Now `mood_weight` is always present in JSON output at its current value.

### Why
Omission from Session 26 (JSON format). The `mood_weight` parameter affects the generated text when mood is active, so consumers need it to understand how the output was produced. Without it, JSON consumers would see `mood` in the metadata but have no way to know how strongly it influenced word selection.

3 new tests, 167 total.

## 2026-07-11 — JSON Output Format

### What
Added `"json"` as a third option for `--format` (alongside `prose` and `poetic`). When `fmt="json"`, `generate_landscape()` returns a JSON string with a `text` field (the clean prose output) and metadata fields: `biome`, `seed` (if known), `mood` (if set), `bias`, `detail`, `template_set`, `anomaly_prob`, and any overrides (`bias_overrides`, `mood_weight_overrides`, `template_overrides`). When `--combine` is used, the JSON also includes a `biomes` list.

### Why
After 25 sessions of adding creative controls (biomes, moods, biases, template-sets, overrides, etc.), the tool could generate rich landscapes but only output text. A machine-readable JSON format unlocks programmatic consumption: piping into other tools, embedding in web apps, saving structured generation data for analysis, or using as training data. The format is backward compatible — `prose` and `poetic` are unchanged.

### Tradeoffs
- JSON mode sets `show_biome` and `show_seed` semantics differently: bracketed suffixes are never appended to `text` — biome and seed data goes into JSON fields instead. This is cleaner for consumers who would otherwise have to parse brackets out of the text.
- All generation parameters that the user might want to reference later are included in the JSON output (seed for reproducibility, bias/mood/overrides for understanding what produced the text). This is comprehensive but adds some redundancy — a consumer could reconstruct some of these from the `text` alone.
- The `text` field in JSON always uses prose-style space-joined formatting (not poetic line breaks) — JSON is primarily for machine consumption, and a single text string is easier to work with than multiline content.
- 9 new tests (164 total, 18 todo + 146 landscape).

## 2026-07-11 — Mood Blending

### What
Changed `--mood` from a single-choice flag to an `action="append"` flag that accepts multiple moods (e.g. `--mood eerie --mood vibrant`). In `_word_weight()`, the `mood` parameter now accepts a string (single mood, backward compatible) or list/tuple of strings — a word gets the mood-weight boost if it matches **any** active mood's category list.

### Why
After adding mood weight and per-category mood-weight overrides (Sessions 13–17), the mood system was flexible but users were locked into exactly one emotional palette per landscape. A forest with eerie mood always felt silent and shadowed; a vibrant mood always felt bright and luminous. Mood blending unlocks genuinely new tones that don't exist as single presets: "eerie + vibrant" creates a haunted-but-beautiful atmosphere (bioluminescent shadows, silent radiance), while "eerie + desolate" doubles down on bleak wrongness. This is the mood equivalent of `--combine` for biomes (Session 6) — combining existing data to create something new.

### Tradeoffs
- `action="append"` internally produces a list even for a single `--mood eerie` (becomes `["eerie"]`), but `_word_weight()` handles both strings and lists transparently via `isinstance` normalization. All existing callers that pass a bare string still work.
- The mood-weight boost applies only once per word, even if it appears in multiple moods' lists — `break` on first match prevents compounding. This keeps the boost binary (on/off) rather than additive, which is simpler and avoids needing to think about "how many moods does this word match."
- The `choices` constraint is preserved, so argparse still validates each mood value independently — `--mood eerie --mood nonexistent` is rejected.
- No change to mood weight or mood-weight overrides — blending composes with all existing mood controls. `--mood eerie --mood vibrant --mood-weight 10` boosts words in either mood by 10x.
- 5 new tests (155 total, 18 todo + 137 landscape).

## 2026-07-11 — Adverb Word Category

### What
Added a new `ADVERBS` word category to the landscape generator: 12 global adverbs with weighted tiers (4 common, 4 rare, 4 normal), mood-specific adverb lists, and 2 new middle templates that use `{adverb}`. The adverb is picked once per landscape and threaded through all format calls as an ignored-optional kwarg.

### Why
After 23 sessions of adding biomes, moods, biases, templates, and overrides, the generated descriptions still lacked one key dimension of descriptive language: *how* things happen. "Mist drifts between the trees" is descriptive; "Mist drifts slowly between the trees" is evocative. Adverbs add texture to existing sentences with minimal data — 12 words and 2 templates — while fitting naturally into the existing weighted-selection, mood-boost, and dedup systems.

### Tradeoffs
- Single adverb per landscape (not per sentence) — avoids overusing adverbs while ensuring every sentence can potentially use it. A per-sentence adverb would add more variety but could make the output feel cluttered ("softly... gently... quietly...") across detail=3 outputs.
- Only middle templates use `{adverb}` — opening and anomaly templates don't get adverb variants. Mid-sentence adverbs feel most natural in descriptive action ("shimmers softly through", "whispers gently beneath"), while opening templates are more static ("stretches before you") and anomalies are about surreal wrongness ("Time seems to flow backward").
- `{adverb}` is passed to all format calls as an extra kwarg that is silently ignored by templates that don't use it. This is identical to how `display` is already passed to templates that may or may not use it — no new plumbing needed.
- No biome-specific adverbs — the global pool is generic enough that biome-specific adverbs would add little value. But mood-specific adverbs were worth adding (3 lists of 4-5 words each) since mood already controls tonal palette and adverbs like "relentlessly" vs "gently" carry strong mood signals.
- No CLI flag to control adverb selection — like word dedup, this is an automatic quality improvement, not a user-facing control. Adverbs are always active; users who want to suppress them can't, but the impact is mild (one extra word in ~50-80% of middle sentences depending on which template is selected).
- 6 new tests (150 total, 18 todo + 132 landscape).

## 2026-07-11 — Noun-Verb Agreement Fix in Middle Template 3

### What
Changed `{verb_conjugated}` → `{verb}` in `SENTENCE_TEMPLATES["middle"][2]`. The template was `"The {noun} {verb_conjugated} with {element}."` and is now `"The {noun} {verb} with {element}."`.

### Why
All nouns in the word banks are plural ("trees", "stones", "ruins", etc.), so using third-person singular verb conjugation ("whispers", "glows") produced a grammatical error: "The trees whispers with light." Using the bare verb form ("whisper") fixes the agreement: "The trees whisper with light." This was explicitly called out as a known tradeoff in the Session 8 decision entry.

### Tradeoffs
- Templates 1 and 2 use `{Element}`/`{element}` (singular concepts like "Mist", "Light") as the subject, so `{verb_conjugated}` is correct there — only template 3 was wrong
- The bare verb is already passed to `str.format()` as the `verb` kwarg — no new data or parameters needed
- 2 new tests, 144 total

## 2026-07-11 — Three New Biomes (Ruined City, Fungal Grove, Sky Islands)

### What
Added 3 new biomes to `BIOMES` and `BIOME_WORDS`: `ruined city`, `fungal grove`, and `sky islands`. Each has 8 adjectives, 4-5 elements, 6 nouns, 5 verbs, 3 weathers, and 3 anomalies — expanding the total biome count from 10 to 13.

### Why
The existing 10 biomes are all natural environments (forest, desert, ocean, etc.). Adding weird, non-natural biomes directly serves the project's creative goal: "originality matters more than 'usefulness'." A ruined city evokes post-apocalyptic wonder, a fungal grove is surreal and alien, and sky islands are dreamlike. These biomes add genuinely new flavor to the output — a landscape can now describe an urban ruin or a floating archipelago, not just another forest or desert.

### Tradeoffs
- 3 biomes rather than 1 — the data is compact (~60 lines total) and the impact per line is high; adding them all at once avoids 3 separate sessions of the same mechanical change
- Some biome words overlap with mood words (e.g. fungal grove's "bioluminescent" overlaps with vibrant mood's "bioluminescent") — this is fine because the mood boost is orthogonal to biome; the word appears in both pools independently
- "ruined city" and "fungal grove" share some desolate/eerie vocabulary with existing mood words — cross-pollination between biomes and moods is a feature, not a bug; a ruined city with eerie mood will feel doubly eerie
- New biomes are not added to `COMMON_WORDS` or `RARE_WORDS` — their words default to normal weight (weight 5), which is appropriate since they're already distinctive
- 11 new tests (142 total, 18 todo + 124 landscape)

## 2026-07-11 — Per-Category Mood-Weight Override (`--mood-weight-adjective`, etc.)

### What
Added 6 CLI flags (`--mood-weight-adjective`, `--mood-weight-element`, `--mood-weight-noun`, `--mood-weight-verb`, `--mood-weight-weather`, `--mood-weight-anomaly`) and a `mood_weight_overrides` dict parameter to `_word_weight()`, `_pick()`, and `generate_landscape()`. Each flag accepts a float and overrides the global `--mood-weight` for that word category.

### Why
The global `--mood-weight` flag (Session 14) applies the same multiplier to all 6 word categories. A user who wants strongly mood-biased adjectives (every adjective should feel eerie) but neutral weather (weather shouldn't be pushed toward any mood) had no way to express that. Per-category mood-weight overrides unlock fine-grained emotional control: "make adjectives heavily eerie but keep weather neutral and elements only slightly eerie."

### Tradeoffs
- Dict parameter rather than 6 individual kwargs — same pattern as `bias_overrides`, keeps the `generate_landscape()` signature from growing, easy to extend with new categories
- Resolution happens in `_word_weight()` (one line: `effective_mw = (mood_weight_overrides or {}).get(category, mood_weight)`) — clean separation, same pattern as `bias_overrides`
- Overrides compose with bias the same way global mood weight does: bias sets base weight, (possibly overridden) mood weight multiplies on top
- This was the first suggested "next likely step" from Session 16's STATE.md — natural follow-up
- Per-category mood-weight overrides make `mood_weight_overrides` the fourth dict parameter alongside `bias_overrides`, keeping the pattern consistent

## 2026-07-11 — Auto-Increment Seed for `--count` with `--seed`

### What
Fixed `main()` so that when `--count > 1` and `--seed` is given, each iteration uses `seed + i` instead of the same seed. `--seed 42 --count 3` now produces 3 different outputs, equivalent to running `--seed 42`, `--seed 43`, `--seed 44` separately.

### Why
`--seed 42 --count 3` previously printed the same landscape 3 times — a usability bug that made `--count` pointless when combined with `--seed`. The fix makes `--count` genuinely useful for batch-producing N different reproducible landscapes.

### Tradeoffs
- Simple additive offset (`seed + i`) rather than any fancy hashing — preserves determinism and makes it obvious which seed produced which output
- The change is in `main()` only; `generate_landscape()` is untouched
- A caller who somehow wants N copies of the same output can still call `generate_landscape()` directly; the CLI no longer supports that degenerate case
- 4 new tests, 131 total

## 2026-07-11 — Configurable Anomaly Probability (`--anomaly-prob`)

### What
Added `--anomaly-prob` CLI flag and `anomaly_prob` parameter to `generate_landscape()` — a float from 0.0 to 1.0 that controls the probability of an anomaly appearing in the output (default: 0.3, preserving existing behavior).

### Why
The anomaly chance was the last hardcoded magic number in the generation logic. Unlike every other creative control (bias, mood, mood-weight, template-set, detail), there was no way to control whether anomalies appeared frequently, rarely, or never. This gap was especially noticeable when using `--detail 3` for rich vignettes — anomalies felt too rare or too frequent depending on the use case. Making it configurable follows the project's established pattern of turning constants into user-facing parameters.

### Tradeoffs
- Single global probability rather than per-detail-level probabilities — keeps the API simple; a user who wants anomalies only at high detail levels can compose with `--detail` themselves
- No per-category override for anomaly probability (unlike bias/mood-weight overrides) — anomaly is a single binary event per landscape, not a per-category concept, so overrides don't apply
- The default 0.3 matches the previous hardcoded value exactly, so all existing seed-based output is preserved

## 2026-07-11 — Cross-Sentence Word Dedup

### What
Added an optional `used_words` set parameter to `_pick()`. When provided, already-used words are excluded from the selection pool, and the newly chosen word is added to the set. `generate_landscape()` creates a single `used_words` set and threads it through all `_pick()` calls, so no word can be selected more than once per landscape.

### Why
After 18 sessions of adding parameters, knobs, and overrides, the project needed a core output-quality improvement. The most obvious quality gap was that the same word could appear twice in one landscape — "crystal" as both adjective and element, or "shimmer" as verb appearing in both the middle sentence and weather phrase. This made the output feel repetitive and less polished. Dedup is invisible to the user (no CLI flag needed) but meaningfully improves every generated landscape.

### Tradeoffs
- `used_words=None` by default preserves backward compatibility for direct `_pick()` callers (not used in production, but keeps tests clean)
- Global cross-category dedup (not per-category) — a single set shared across adjectives, elements, nouns, verbs, weathers, and anomalies. This is intentional: the goal is to prevent any word from appearing twice in a single description, regardless of grammatical role. A word like "echo" appearing in both elements and verbs would feel repetitive even though it's grammatically valid in both slots.
- When the filtered pool is empty (all words for a category have been used), falls back to the unfiltered pool. This is a safety net for edge cases with tiny biome word banks at high detail levels — the description might repeat a word rather than crash.
- Morphological variants (e.g. "crystal" vs "crystals", "shimmer" vs "shimmers") are NOT deduped — they're different strings. Full lemmatization would add complexity and a dependency; in practice, these variants read as natural repetition rather than a bug.
- This is the first feature in the project that doesn't add a CLI flag — it's an automatic quality improvement, not a user-facing control. This sets a precedent: not every change needs a knob.
- The `test_detail_two_is_longer_than_one` test was changed to count sentences instead of character length, because anomaly text at detail=1 may be as long as an extra sentence pair at detail=2. Counting periods is more robust.
- 6 new tests added (122 total, 18 todo + 104 landscape).

## 2026-07-11 — Per-Category Bias Override (`--bias-adjective`, etc.)

### What
Added 6 CLI flags (`--bias-adjective`, `--bias-element`, `--bias-noun`, `--bias-verb`, `--bias-weather`, `--bias-anomaly`) and a `bias_overrides` dict parameter to `generate_landscape()` and `_pick()`. Each flag accepts the same choices as `--bias` and overrides the global bias for that word category. The dict is built in `main()` from whichever flags the user set.

### Why
The global `--bias` flag (Session 11) applies the same weight distribution to all 6 word categories — adjectives, elements, nouns, verbs, weathers, anomalies. A user who wants rare, unusual adjectives but common, familiar nouns had no way to express that. Per-category overrides unlock fine-grained creative control: "use rare adjectives so descriptions feel surprising, but keep common weather patterns so the atmosphere stays recognizable."

### Tradeoffs
- Dict parameter rather than individual kwargs — keeps the `generate_landscape()` signature from growing by 6 more arguments and is easy to extend with new categories
- CLI flag names use singular form (`--bias-adjective` not `--bias-adjectives`) — reads more naturally and the mapping to plural internal names is handled in `main()` via a small lookup dict
- Resolution happens in `_pick()` (one line: `effective_bias = (bias_overrides or {}).get(category, bias)`) — clean separation: `_word_weight()` doesn't need to know about overrides at all
- No per-category bias for mood weight yet — that would be a natural follow-up (`--mood-weight-adjective`, etc.)
- Overrides compose with mood the same way global bias does: mood weight is a multiplier on top of the (potentially overridden) base weight

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
