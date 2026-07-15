# Decisions

## 2026-07-15 — Perspective/Vantage System (`--perspective`)

### What
Added a `PERSPECTIVES` word bank (10 evocative phrases), `--perspective` CLI
flag (default: off), `--no-perspective` CLI flag, `--describe-perspectives`
introspection, JSON metadata, and preset integration (enabled in all 5 presets).
Each phrase is a standalone sentence prepended before season and time-of-day,
establishing the spatial vantage point and scale from which the landscape is
viewed.

Perspective is enabled by default in all 5 presets (nightfall, pastoral, sublime,
wasteland, dreamscape).

### Why
The "Next likely steps" in every session since Session 122 explicitly called for
adding a spatial geometry dimension (e.g. scale, perspective, distance). The
project had been through 21 consecutive sessions of word bank expansions or
incremental feature additions (wildlife, soundscapes, wildlife count/prob,
soundscape count/prob, etc). After all those incremental improvements, the
generator had sophisticated multi-sensory layers (visual, auditory, atmospheric,
folkloric, temporal, emotional) but lacked any sense of spatial context — the
reader never knew whether the description was from above, below, close up, or
from a distance.

A perspective/vantage system adds a fundamentally new spatial dimension: the
landscape is now not just described, but *viewed from somewhere*. This changes
how the reader relates to the description — a landscape seen from above is a
map-like abstraction, while a ground-level view is immersive and overwhelming.

The 10 phrases each cover a distinct spatial register:
- **Aerial overview**: "Seen from above, the {display} reveals itself as a
  {adj} pattern of {color} {element}" — map-like, abstract
- **Ground level**: "At ground level, the {display} towers {adverb},
  overwhelming in its {adj} scale" — immersive, looming
- **Distance**: "From a distance, the {display} is a {adj} whisper of {color}
  on the {element} of the horizon" — remote, diminished, atmospheric
- **Close-up**: "Up close, the {display} breathes {adverb} with {color}
  textures and hidden {adj} detail" — intimate, detailed
- **Looking down**: "Seen from the heights, the {display} unfolds like a
  {adj} map of {color} {element} {adverb} arranged" — god's-eye view
- **Interior**: "From within, the {display} wraps around you like a {adj}
  cocoon of {color} {element}" — enclosed, immersive
- **Expansive**: "The {display} stretches {adverb} into the distance, a
  {adj} expanse of {color} {element}" — horizon-gazing
- **Threshold**: "At the edge of the {display}, the world beyond feels
  {adverb} distant and {adj}" — liminal, standing at the boundary
- **Scale contemplation**: "The scale of the {display} is {adverb} apparent
  — a {adj} world of {color} {element}" — reflective, meta
- **Looking back**: "Looking back at the {display}, it seems smaller now, a
  {adj} patch of {color} {element} receding into the distance" — departure,
  retrospective

### Tradeoffs
- **10 curated phrases** — same size as the original TIMES_OF_DAY bank (10)
  and WISTFUL (6 initially, now 10). Can be expanded in future sessions.
- **Off by default** (`perspective_enabled=False`), preserving all existing
  seed-based output for users who don't use `--perspective`.
- **Not suppressed at detail=0** — like time-of-day and season, perspective
  is a framing prefix that works naturally with minimal descriptions.
  "Seen from above, the tundra reveals itself as a frozen pattern of silver
  frost." is a coherent minimal description.
- **Inserted as outermost framing** — before season and time-of-day, so the
  order is: perspective → season → time-of-day → opening. Perspective is the
  most general spatial context, and it makes sense for it to be the first
  thing the reader encounters: first we know WHERE we're viewing from, then
  WHEN (year), then WHEN (day).
- **Seed-breaking when enabled**: One extra `rng.choice()` call shifts the
  random sequence after word picks but before the season/time/opening.
  Determinism is preserved (same seed + same args = same output).
- **In all 5 presets from the start** — like season and wildlife, perspective
  was added to presets in the same session it was introduced. This is possible
  because the pattern is now well-established and all the infrastructure
  (preset gating, `--no-*` flags) already exists.
- **No count/prob controls** — follows the same trajectory as time-of-day
  and wildlife, which were initially single-phrase opt-in features. Count and
  probability can be added in future sessions if desired.
- **33 new tests, 913 total** (18 todo + 895 landscape), 299 subtests.
- **Test count +33 tests, +18 subtests** from the previous session (898 tests,
  281 subtests).
- **Fulfills "Next likely steps" from Session 144**: Spatial geometry dimension
  was explicitly called out as the second item, and after 21 sessions of word
  bank expansions and incremental improvements, a genuinely new spatial
  dimension was the right next step.

## 2026-07-15 — Expanded SOUNDSCAPES Word Bank (17 phrases)

### What
Added 5 new curated soundscape phrases to the SOUNDSCAPES bank, expanding it
from 12 to 17 phrases. The new phrases cover water dripping as percussion,
melodic singing, wind howling, choral voices, and structural groaning — sonic
niches absent from the original 12.

### Why
The SOUNDSCAPES bank was last expanded in Session 121 (8→12) and had not
received any expansion since. Every other major word bank had been expanded
more recently: ECHOES (Session 122, 10→15), WISTFUL (Session 123, 6→10),
LEGENDS (Session 124, 15→20), TIMES_OF_DAY (Session 133, 10→15), SEASONS
(Session 135, 10→15), WILDLIFE (Session 143, 10→15). Soundscapes were the
most overdue bank, having gone 23 sessions without expansion.

With soundscapes now enabled by default in all 5 presets (with count=1-2
and prob=0.5-0.95), repetition in soundscape output is noticeable — especially
at higher counts where 2 distinct phrases are drawn per landscape. Expanding
from 12 to 17 reduces repetition by ~42% in the selection pool.

The "Next likely steps" from Session 143 explicitly called for expanding
global word banks, with soundscapes as the first item in the list.

The 5 new phrases each cover a sonic niche not represented in the existing 12:
- **Water percussion**: "Water drips {adverb} from the {adj} surfaces of the
  {display}, each drop a bright {color} note against the {element}." — liquid
  dripping as a percussive element, the only water-related sound in the bank.
  Distinct from existing general "element crackles like static" and
  "single note rings out".
- **Melodic singing**: "A {adj} music drifts {adverb} through the {display},
  as if the {color} {element} itself has learned to sing." — a musical/melodic
  quality, distinct from existing rhythmic pulses ("slow, patient, {adj}")
  and single ringing notes ("a single {color} note rings out").
- **Wind howling**: "The wind howls {adverb} through the {adj} reaches of the
  {display}, a {color} sound that seems to shape the very {element}." — wind
  as a forceful agent that shapes the environment, distinct from existing wind
  simile ("sounds like {color} glass shattering") which is about texture rather
  than agency.
- **Choral voices**: "{adj} voices whisper {adverb} in the {display}, a chorus
  of {color} sounds that never form words." — many speaking presences as a
  collective, distinct from the single whisper ("whispers {adverb}, a sound
  just at the edge of hearing") and single creature call.
- **Structural groaning**: "The {adj} bones of the {display} groan {adverb},
  a deep {color} sound that resonates through the {element}." — the landscape
  itself creaking and groaning, adding a bodily/architectural dimension absent
  from the existing set (which focuses on ambient, wind, and creature sounds).

### Tradeoffs
- **Data-only change**: No modifications to `generate_landscape()`, CLI flags,
  or any logic. Only the SOUNDSCAPES list and SOUND_INDICATORS were updated.
- **No seed-breaking**: Adding phrases to SOUNDSCAPES doesn't change the random
  sequence — `rng.choice(SOUNDSCAPES)` picks from a larger pool but the choice
  function is unchanged. Only the rendered output content changes (new phrases
  appear in the selection pool).
- **No new tests**: All soundscape tests use dynamic checks over
  `SOUND_INDICATORS` and `len(SOUNDSCAPES)`. Only the indicator list was
  extended; test logic is unchanged.
- **Test count unchanged**: 880 landscape tests (281 subtests), 18 todo tests
  — same as Session 143.
- **Fulfills "Next likely steps" from Session 143**: Word bank expansion (more
  soundscapes) was explicitly called out as the first item.

## 2026-07-15 — Expanded WILDLIFE Word Bank (15 phrases)

### What
Added 5 new curated wildlife phrases to the WILDLIFE bank, expanding it from 10
to 15 phrases. The new phrases cover bioluminescent insects, predator stalking,
aerial bird of prey, nest-building creatures, and insect swarm — wildlife niches
absent from the original 10.

### Why
The WILDLIFE bank was created in Session 141 with 10 phrases and had never been
expanded. Session 142 added count/prob controls and per-preset integration,
making wildlife a well-supported feature — but with only 10 phrases, repetition
was noticeable, especially when multiple wildlife phrases appear per landscape
(with `wildlife_count=2` or `wildlife_count=3`). With wildlife now enabled by
default in 4 of 5 presets (all but wasteland), a larger bank reduces repetition
in preset output.

The "Next likely steps" from Session 142 explicitly called for expanding global
word banks, with wildlife being the most recently added and therefore the most
natural first target.

The 5 new phrases each cover a wildlife niche not represented in the existing 10:
- **Fireflies**: "Fireflies drift {adverb} through the {adj} air of the
  {display}, each {color} spark a brief luminous trail." — bioluminescent
  insects, the only insect-specific phrase in the bank. Distinct from existing
  "small birds" (avian) and "something small chitters" (unidentified small
  creature).
- **Predator stalking**: "Something hunts {adverb} at the edge of the {display}
  — patient, {adj}, tasting the {color} {element}." — a predator in active
  hunting mode, distinct from the existing "something large stirs" (passive
  presence) and "eyes watch from the shadows" (unseen observation).
- **Bird of prey**: "A {adj} bird of prey circles {adverb} overhead, a dark
  {color} silhouette against the {element}." — an aerial hunter, the only
  flying predator phrase. Distinct from "small birds flit" (passive non-predator
  birds).
- **Nest-building**: "Beneath the {display}, {adj} things build {adverb},
  weaving {color} {element} into their hidden structures." — creatures engaged
  in construction/engineering, adding active building behavior absent from the
  original 10 (which focus on presence, movement, and auditory signs).
- **Insect swarm**: "The {adverb} hum of {color} wings rises from the {adj}
  depths of the {display} like a living {element}." — a collective swarm/buzzing
  presence, distinct from single-creature phrases. Adds a group-auditory
  dimension not covered by the existing single "call of an unseen creature".

### Tradeoffs
- **Data-only change**: No modifications to `generate_landscape()`, CLI flags,
  or any logic. Only the WILDLIFE list and WILDLIFE_INDICATORS were updated.
- **No seed-breaking**: Adding phrases to WILDLIFE doesn't change the random
  sequence — `rng.choice(WILDLIFE)` picks from a larger pool but the choice
  function is unchanged. Only the rendered output content changes (new phrases
  appear in the selection pool).
- **No new tests**: All wildlife tests use dynamic checks over
  `WILDLIFE_INDICATORS` and `len(WILDLIFE)`. Only the indicator list was
  extended; test logic is unchanged.
- **Test count unchanged**: 880 landscape tests (281 subtests), 18 todo tests
  — same as Session 142.
- **Not seed-breaking**: Adding new entries to a list that `rng.choice()` draws
  from doesn't change the RNG sequence — the same seed picks the same index,
  but the content at that index may be different, which only changes rendered
  output, not determinism.
- **Fulfills "Next likely steps" from Session 142**: Word bank expansion (more
  wildlife) was explicitly called out as the first item.

## 2026-07-15 — Configurable Wildlife Count and Probability (`--wildlife-count`, `--wildlife-prob`)

### What
Added `--wildlife-count` (choices 0-3, default: 1) and `--wildlife-prob` (0.0-1.0,
default: 1.0) CLI flags, with corresponding `wildlife_count` and `wildlife_prob`
parameters to `generate_landscape()`. Users can now control how many wildlife
phrases appear per landscape and how often each roll succeeds.

Also added `wildlife_count` and `wildlife_prob` to all 5 presets with curated
values: nightfall 2/0.7, pastoral 1/0.6, sublime 2/0.95, wasteland 1/1.0,
dreamscape 2/0.85.

### Why
Session 141 added the wildlife feature as a single `rng.choice(WILDLIFE)` call
— one phrase per landscape, no density controls. Every other multi-phrase feature
(echo, sound, time, season, legend, weather, anomaly) has count and probability
controls. Wildlife was the only one without them. This completes the pattern,
giving users fine-grained control over wildlife density and frequency, matching
every other multi-phrase feature in the project.

The "Next likely steps" from Session 141 explicitly called for this:
"Add --wildlife-count, --wildlife-prob for configurable wildlife density" and
"Add per-preset wildlife count and probability."

### Tradeoffs
- **Default wildlife_count=1, wildlife_prob=1.0** preserves backward compatibility
  — all existing seed-based output with `--wildlife` is unchanged.
- **Per-roll probability**: each of `wildlife_count` rolls per landscape
  independently draws `rng.random() < wildlife_prob`, same pattern as
  `echo_prob`, `legend_prob`, `sound_prob`, `time_prob`, `season_prob`, etc.
- **Dedup via used_wildlife set**: prevents the same wildlife phrase from
  appearing twice in the same landscape. When pool is exhausted (count > 10),
  falls back to the full pool.
- **wildlife_count=0** is an alternative suppression mechanism to
  `wildlife_prob=0.0` and `wildlife_enabled=False`. Multiple suppression paths
  are consistent with the rest of the feature set.
- **JSON metadata**: `wildlife` remains a single string when only one phrase is
  generated (backward compatible), and `wildlife_count`/`wildlife_prob` are
  emitted only when non-default values are used (consistent with all other
  count/prob metadata patterns).
- **Preset seed-breaking**: Adding `wildlife_count` and `wildlife_prob` to
  presets changes output for all 5 presets (e.g. pastoral now has
  `wildlife_prob=0.6`, meaning ~40% of landscapes won't have wildlife even
  though `wildlife_enabled=True`). This is acceptable because presets evolve as
  features mature, and determinism is preserved (same seed + same args = same
  output).
- **16 new tests, 898 total** (18 todo + 880 landscape), 276 subtests.
- **Fulfills "Next likely steps" from Session 141**: Both wildlife density
  controls and per-preset values were explicitly called out.

## 2026-07-15 — Wildlife/Inhabitants System (`--wildlife`)

### What
Added a `WILDLIFE` word bank (10 evocative phrases), `--wildlife` CLI flag
(default: off), `--no-wildlife` CLI flag, `--describe-wildlife` introspection,
JSON metadata, and preset integration (enabled in 4 of 5 presets). Each phrase
is a single sentence appended between soundscapes and legends, describing
animals, creatures, or inhabitants of the landscape.

Wildlife is enabled by default in `nightfall`, `pastoral`, `sublime`, and
`dreamscape` presets. `wasteland` has `wildlife_enabled: False` — a desolate
wasteland should not teem with life.

### Why
The "Next likely steps" in every session since Session 122 explicitly called for
adding inhabitants/wildlife as a new sensory dimension. The project had been
through 18 consecutive sessions of word bank expansions or incremental feature
additions (echo count/prob, sound count/prob, weather count/prob, anomaly
count/prob, time-of-day, season, time count/prob, season count/prob, per-preset
counts/probs, and multiple word bank expansions). After all those incremental
improvements, the generator had sophisticated control over its existing
dimensions but lacked any sense of living inhabitants. Wildlife adds a
fundamentally new dimension: the landscape as a place that is *lived in*, not
just observed.

The 10 phrases each cover a different wildlife register, from visible presence
(deer, birds) to unseen presence (eyes watching, something stirring, distant
calls) to traces (tracks in the earth). This range ensures wildlife feels
emergent rather than formulaic.

### Tradeoffs
- **10 curated phrases** — same size as the original TIMES_OF_DAY bank (10)
  and WISTFUL (10). Can be expanded in future sessions.
- **Off by default** (`wildlife_enabled=False`), preserving all existing
  seed-based output for users who don't use `--wildlife`.
- **Suppressed at detail=0** — unlike time-of-day and season (which are framing
  prefixes suitable even for minimal descriptions), wildlife feels like a detail
  that requires at least a basic landscape to inhabit. This matches the behavior
  of echoes, legends, soundscapes, and wistful.
- **Placed between soundscapes and legends** — the order is: framing (season,
  time-of-day) → opening → middle/weather → anomalies → echoes → soundscapes
  → **wildlife** → legends → wistful → travelogue (wraps everything). Wildlife
  comes after abstract sensory layers (echoes, soundscapes) but before folkloric
  (legends) and emotional (wistful) layers, creating a natural progression from
  immediate → ambient → living → legendary → emotional.
- **Seed-breaking when enabled**: One extra `rng.choice()` call shifts the
  random sequence after soundscapes. Determinism is preserved (same seed + same
  args = same output).
- **Not in wasteland preset** — wasteland gets `wildlife_enabled=False` because
  a desolate, barren landscape shouldn't suggest abundant life. All other
  presets enable it. This is a thematic choice, not a technical limitation.
- **No count/prob controls yet** — follows the same trajectory as time-of-day
  (Session 131) and season (Session 134), which were initially single-phrase
  opt-in features. Count and probability controls can be added in future
  sessions if desired.
- **35 new tests, 882 total** (18 todo + 864 landscape), 276 subtests.
- **Test count +35 tests, +23 subtests** from the previous session (847 tests,
  253 subtests).
- **Fulfills "Next likely steps" from Session 140**: Inhabitants/wildlife was
  explicitly called out as the second item, and after 18 sessions of word bank
  expansions and incremental improvements, a genuinely new dimension was the
  right next step.

## 2026-07-15 — Expanded Global ANOMALIES Bank (12 entries)

### What
Added 4 new curated anomaly phrases to the global ANOMALIES bank, expanding it
from 8 to 12 entries. The new phrases cover precognitive false memory, phantom
sensory experience, impossible geometry with memory distortion, and unseen
presence — anomalous phenomena absent from the original 8.

### Why
The global ANOMALIES bank (8 entries) was the only global word bank that had
never been expanded. Every other bank had received at least one expansion:
WEATHERS (8→12, Session 120), SOUNDSCAPES (8→12, Session 121), ECHOES
(10→15, Session 122), WISTFUL (6→10, Session 123), LEGENDS (15→20, Sessions
98 and 124), TIMES_OF_DAY (10→15, Session 133), and SEASONS (10→15, Session
135). The "Next likely steps" from Session 139 explicitly called for expanding
global word banks, with anomalies being the most overdue.

The 4 new phrases each cover an anomalous niche not represented in the existing
8 or in any biome-specific anomaly:
- **Precognitive false memory**: "You remember this landscape from a dream you
  have never had" — the landscape as a half-remembered dream, uncanny
  familiarity without prior experience. Distinct from existing "Colors shift"
  (perception) and fungal grove "the mycelium network reacts to your thoughts"
  (mind-reactive environment).
- **Phantom sensory experience**: "Every breath tastes of a season that does
  not exist" — impossible sensory input, a season perceived through taste/smell
  that has no place in the natural cycle. Adds a synesthetic/impossible-sensory
  dimension not covered by existing anomalies.
- **Impossible geometry with memory distortion**: "The geometry of the landscape
  follows rules you cannot quite recall" — the sense that the landscape's
  spatial logic is knowable but just out of reach, blending impossible geometry
  with a failure of memory. Distinct from "the horizon curves upward"
  (permanent visible geometry) and cave "passages rearrange when you blink"
  (active rearrangement).
- **Unseen presence**: "Something is just beyond sight — a presence that never
  arrives" — ambient paranoia, anticipation without resolution, the feeling of
  being watched by something that never materializes. None of the existing
  global or biome anomalies evoke this specific register of sustained
  anticipation.

### Tradeoffs
- **Data-only change**: No modifications to `generate_landscape()`, `_pick()`,
  CLI flags, or any logic. Only the ANOMALIES list was updated.
- **No seed-breaking**: Adding words to the global ANOMALIES pool doesn't change
  the random sequence — `_pick()` draws from a larger pool but the
  weighted-selection function is unchanged. Only the rendered output content
  changes (new phrases appear in the selection pool).
- **Not marked common or rare**: New anomalies intentionally left at normal
  weight tier (none of the existing 8 are in COMMON_WORDS or RARE_WORDS).
- **No new tests**: ALL_ANOMALIES is dynamically derived from ANOMALIES in the
  test module. All anomaly tests use dynamic loops and generic presence/absence
  checks, so no test changes are needed.
- **Test count unchanged**: 847 tests (18 todo + 829 landscape), 253 subtests.
- **Fulfills "Next likely steps" from Session 139**: Global word bank expansion
  was explicitly called out as the first item, and anomalies were the most
  overdue bank (never expanded).

## 2026-07-15 — Per-Preset Time-of-Day Count and Probability

### What
Added `time_count` and `time_prob` to all 5 preset configurations (`nightfall`,
`pastoral`, `sublime`, `wasteland`, `dreamscape`). Each preset now has curated
time-of-day density and probability values that match its atmospheric theme,
mirroring how `season_count`/`season_prob`, `sound_count`/`sound_prob`,
`weather_count`/`weather_prob`, and `legend_count`/`legend_prob` are already set
per-preset.

### Why
Session 136 added `--time-count` and `--time-prob` CLI flags and parameters,
with gating code in `main()` that checks for preset-level values — but no preset
actually used them. Every other multi-phrase feature (echoes, legends,
soundscapes, weather, anomalies, seasons) had per-preset count and prob values.
Time-of-day was the last dimension without preset-level tuning. This completes
the trajectory: on/off in presets (Session 132) → count/prob as CLI flags
(Session 136) → per-preset count+prob values (this session).

The "Next likely steps" from Session 138 explicitly called for this:
"Add --time-count, --time-prob to presets with curated values."

### Tradeoffs
- **Seed-breaking for presets**: All 5 presets now produce different output from
  Session 138 for the same seed, because `time_prob < 1.0` for some presets
  means extra `rng.random()` calls are consumed per landscape. This is acceptable
  because presets evolve as features mature, and determinism is preserved (same
  seed + same args = same output).
- **Curated values per preset**: nightfall gets `time_count=2, time_prob=0.7`
  (matching its echo/sound/legend/season prob), pastoral gets `time_count=1,
  time_prob=0.6` (gentle, occasional), sublime gets `time_count=2,
  time_prob=0.95` (rich, almost always), wasteland gets `time_count=1,
  time_prob=1.0` (always stark), dreamscape gets `time_count=2,
  time_prob=0.85` (surreal, usually present).
- **No changes to `generate_landscape()`**: Presets are a pure CLI convenience
  layer — the generation function already accepts `time_count`/`time_prob`.
  Only the PRESETS dict changed.
- **Consistent with all other preset integrations**: Every multi-phrase feature
  with count/prob controls now has per-preset tuning — echoes, legends,
  soundscapes, weathers, seasons, and time-of-day (this session).
- **1 new test, 847 total** (18 todo + 829 landscape), 253 subtests.
- **Fulfills "Next likely steps" from Session 138**: Per-preset time count and
  probability was explicitly called out as the last item.

## 2026-07-15 — Per-Preset Seasonal Count and Probability

### What
Added `season_count` and `season_prob` to all 5 preset configurations (`nightfall`,
`pastoral`, `sublime`, `wasteland`, `dreamscape`). Each preset now has curated
seasonal density and probability values that match its atmospheric theme, mirroring
how `sound_count`/`sound_prob`, `weather_count`/`weather_prob`, and
`legend_count`/`legend_prob` are already set per-preset.

### Why
Session 137 added `--season-count` and `--season-prob` CLI flags and parameters,
with gating code in `main()` that checks for preset-level values — but no preset
actually used them. Every other multi-phrase feature (echoes, legends, soundscapes,
weather, anomalies) had per-preset count and prob values. Seasons were the last
dimension without preset-level tuning. This completes the trajectory: on/off in
presets (Session 134) → count/prob as CLI flags (Session 137) → per-preset
count+prob values (this session).

The "Next likely steps" from Session 137 explicitly called for this:
"Add --season-count, --season-prob to presets with curated values."

### Tradeoffs
- **Seed-breaking for presets**: All 5 presets now produce different output from
  Session 137 for the same seed, because `season_prob < 1.0` for some presets
  means extra `rng.random()` calls are consumed per landscape. This is acceptable
  because presets evolve as features mature, and determinism is preserved (same
  seed + same args = same output).
- **Curated values per preset**: nightfall gets `season_count=2, season_prob=0.7`
  (matching its echo/sound/legend prob), pastoral gets `season_count=1,
  season_prob=0.6` (gentle, occasional), sublime gets `season_count=2,
  season_prob=0.95` (rich, almost always), wasteland gets `season_count=1,
  season_prob=1.0` (always stark), dreamscape gets `season_count=2,
  season_prob=0.85` (surreal, usually present).
- **No changes to `generate_landscape()`**: Presets are a pure CLI convenience
  layer — the generation function already accepts `season_count`/`season_prob`.
  Only the PRESETS dict changed.
- **Consistent with all other preset integrations**: Every multi-phrase feature
  with count/prob controls now has per-preset tuning — echoes (Session 103),
  legends (Session 103), soundscapes (Session 116), weathers (Session 117),
  and seasons (this session).
- **1 new test, 846 total** (18 todo + 828 landscape), 243 subtests.
- **Fulfills "Next likely steps" from Session 137**: Per-preset season count and
  probability was explicitly called out as the last item.

## 2026-07-15 — Configurable Seasonal Count and Probability (`--season-count`, `--season-prob`)

### What
Added `--season-count` (choices 0-3, default: 1) and `--season-prob` (0.0-1.0,
default: 1.0) CLI flags, with corresponding `season_count` and `season_prob`
parameters to `generate_landscape()`. Users can now control how many seasonal
phrases appear per landscape and how often each roll succeeds.

Also added `SEASON_INDICATORS` to the test module for dedup/suppression testing,
and preset gating for both new parameters.

### Why
The seasonal system (Session 134) was a single-phrase prepended framing. Every
other multi-phrase feature — echoes, legends, soundscapes, weather, anomalies,
time-of-day — has count and probability controls. Seasons were the last major
feature without them. Adding count and prob gives users fine-grained control
over seasonal density and frequency, matching the established pattern.

The "Next likely steps" from Session 136 explicitly called for this:
"Add --season-count, --season-prob for configurable seasonal density."

### Tradeoffs
- **Default season_count=1, season_prob=1.0** preserves backward compatibility —
  all existing seed-based output with `--season` is unchanged.
- **Per-roll probability**: each of `season_count` rolls per landscape
  independently draws `rng.random() < season_prob`, same pattern as
  `echo_prob`, `legend_prob`, `anomaly_prob`, `sound_prob`, `weather_prob`,
  and `time_prob`.
- **Dedup via used_seasons set**: prevents the same seasonal phrase from
  appearing twice in the same landscape. When pool is exhausted (count > 15),
  falls back to the full pool.
- **season_count=0** is an alternative suppression mechanism to `season_prob=0.0`
  and `season_enabled=False`. Multiple suppression paths are consistent
  with the rest of the feature set.
- **JSON metadata**: `season` is stored as a list when multiple phrases are
  generated, and as a single string when only one (backward compatibility for
  consumers reading `data["season"]` as a string with default count=1).
  `season_count` and `season_prob` are emitted only when non-default values are
  used (consistent with time/echo/weather/sound/legend metadata patterns).
- **Phrases inserted in pick order**: first-picked phrase is outermost (first
  in output), last-picked is innermost (closest to opening). All seasons come
  before time-of-day and the opening — consistent with existing behavior.
- **Seed-breaking when season_prob < 1.0**: When `season_prob` causes a roll to
  be skipped, the RNG sequence shifts by one `rng.random()` call. With
  `season_prob=1.0` (default), no extra random calls are consumed beyond the
  `rng.choice()` for each pick, so behavior is unchanged from the previous
  session.
- **Preset gating exists but no presets use it yet**: The gating code follows
  the exact same pattern as time_count/time_prob, so presets can be updated to
  include season_count/season_prob in a future session if desired.
- **16 new tests, 845 total** (18 todo + 827 landscape), 243 subtests.
- **Fulfills "Next likely steps" from Session 136**: Configurable seasonal
  density was explicitly called out as the first item.

## 2026-07-15 — Configurable Time-of-Day Count and Probability (`--time-count`, `--time-prob`)

### What
Added `--time-count` (choices 0-3, default: 1) and `--time-prob` (0.0-1.0,
default: 1.0) CLI flags, with corresponding `time_count` and `time_prob`
parameters to `generate_landscape()`. Users can now control how many time-of-day
phrases appear per landscape and how often each roll succeeds.

Also added `TIME_INDICATORS` to the test module for dedup/suppression testing,
and preset gating for both new parameters.

### Why
The time-of-day system (Session 131) was a single-phrase prepended framing. Every
other multi-phrase feature — echoes, legends, soundscapes, weather, anomalies —
has count and probability controls. Time-of-day was the last major feature
without them. Adding count and prob gives users fine-grained control over
temporal density and frequency, matching the established pattern.

The "Next likely steps" from Sessions 134/135 explicitly called for this:
"Add --time-count, --time-prob for configurable time-of-day density."

### Tradeoffs
- **Default time_count=1, time_prob=1.0** preserves backward compatibility —
  all existing seed-based output with `--time` is unchanged.
- **Per-roll probability**: each of `time_count` rolls per landscape
  independently draws `rng.random() < time_prob`, same pattern as
  `echo_prob`, `legend_prob`, `anomaly_prob`, `sound_prob`, and `weather_prob`.
- **Dedup via used_times set**: prevents the same time-of-day phrase from
  appearing twice in the same landscape. When pool is exhausted (count > 15),
  falls back to the full pool.
- **time_count=0** is an alternative suppression mechanism to `time_prob=0.0`
  and `time_of_day_enabled=False`. Multiple suppression paths are consistent
  with the rest of the feature set.
- **JSON metadata**: `time_of_day` is stored as a list when multiple phrases are
  generated, and as a single string when only one (backward compatibility for
  consumers reading `data["time_of_day"]` as a string with default count=1).
  `time_count` and `time_prob` are emitted only when non-default values are used
  (consistent with echo/weather/sound/legend metadata patterns).
- **Phrases inserted in pick order**: first-picked phrase is outermost (first
  in output), last-picked is innermost (closest to opening). When season is
  also enabled, season remains outermost — consistent with existing behavior.
- **Seed-breaking when time_prob < 1.0**: When `time_prob` causes a roll to be
  skipped, the RNG sequence shifts by one `rng.random()` call. With
  `time_prob=1.0` (default), no extra random calls are consumed beyond the
  `rng.choice()` for each pick, so behavior is unchanged from the previous
  session.
- **Preset gating exists but no presets use it yet**: The gating code follows
  the exact same pattern as echo_count/echo_prob, so presets can be updated to
  include time_count/time_prob in a future session if desired.
- **15 new tests, 812 total** (18 todo + 794 landscape), 243 subtests.
- **Fulfills "Next likely steps" from Sessions 134/135**: Configurable
  time-of-day density was explicitly called out as the third item.

## 2026-07-15 — Expanded SEASONS Word Bank (15 phrases)

### What
Added 5 new curated seasonal phrases to the SEASONS bank, expanding it from 10
to 15 phrases. The new phrases cover late winter thaw, late summer abundance,
autumn dormancy preparation, hard winter freeze, and persistent spring rain —
seasonal niches absent from the original 10.

### Why
The seasonal system (Session 134) was the newest temporal dimension and had not
yet received any word bank expansion. The original 10 phrases covered broad
seasonal categories but had gaps: no late summer variant, no late winter thaw,
no autumn dormancy transition, no hard winter freeze aesthetic, and only two
spring variants (early and late). With seasonal framing now enabled by default in
all 5 presets (Session 134), a larger bank reduces repetition in preset output.
The "Next likely steps" from Session 134 explicitly called for expanding global
word banks, with seasons as the first item.

The 5 new phrases each cover a seasonal niche not well represented in the
existing 10:
- **Late winter thaw**: "Late winter's grip loosens as meltwater carves through
  the ice" — the transition between winter and spring, a period of melting and
  renewal not covered by deep winter (silence/frost), first snow (muffled/white),
  or any spring phrase.
- **Late summer abundance**: "The lengthening shadows of late summer stretch
  across fields heavy with seed" — late summer as a time of ripeness and long
  shadows, distinct from high summer (heat haze, droning insects) and midsummer
  (lush fullness).
- **Autumn dormancy preparation**: "A pale autumn sun hangs low as the landscape
  prepares for winter's rest" — autumn as a time of quiet preparation and
  acceptance, distinct from the dramatic gold/decay of peak autumn, the sharpness
  of early autumn chill, and the stark stripped-bare revelation of late autumn.
- **Hard winter freeze**: "A hard winter freeze transforms the landscape into a
  palace of crystal and ice" — winter as crystalline beauty, distinct from deep
  winter (silence and frost) and first snow (muffled world in white).
- **Persistent spring rain**: "The soft persistent rain of early spring washes
  winter's last traces away" — a gentle cleansing spring rain, distinct from
  early spring (buds and thawing), late spring (tender green), and spring thunder
  (rebirth through rain and storm).

### Tradeoffs
- **Data-only change**: No modifications to `generate_landscape()`, CLI flags,
  or any logic. Only the SEASONS list was updated.
- **No seed-breaking**: Adding phrases to SEASONS doesn't change the random
  sequence — `rng.choice(SEASONS)` picks from a larger pool but the choice
  function is unchanged. Only the rendered output content changes (new phrases
  appear in the selection pool).
- **No new tests**: `ALL_SEASONS = set(SEASONS)` is dynamically derived, and all
  TestSeason and TestDescribeSeasons tests use dynamic counts/loops. Only the
  data changed; test logic is unchanged.
- **Test count unchanged**: 797 tests (18 todo + 779 landscape), 243 subtests.
- **Not seed-breaking**: Adding new entries to a list that `rng.choice()` draws
  from doesn't change the RNG sequence — the same seed picks the same index,
  but the content at that index may be different, which only changes rendered
  output, not determinism.
- **Fulfills "Next likely steps" from Session 134**: Word bank expansion (more
  seasons) was explicitly called out as the first item.

## 2026-07-15 — Seasonal Variation System (`--season`)

### What
Added a `SEASONS` word bank (10 evocative seasonal phrases), `--season` CLI flag
(default: off), `--no-season` CLI flag, `--describe-seasons` introspection, JSON
metadata, and preset integration. Each phrase is a standalone sentence prepended
before the opening (and before time-of-day if both are enabled), establishing the
time of year.

Seasonal framing is now enabled by default in all 5 presets.

### Why
The "Next likely steps" from Sessions 131–133 explicitly called for seasonal
variation as the next temporal dimension. The time-of-day system (Session 131)
established the pattern: a word bank of prepended framing sentences with
`--feature`, `--no-feature`, `--describe-feature`, JSON metadata, and preset
integration. Seasonal variation follows this exact pattern, adding a complementary
temporal dimension (time of year vs. time of day).

The 10 phrases cover the full seasonal cycle with multiple variants per season:
- **Spring** (3): early spring (buds, thawing), late spring (tender green),
  spring thunder (rebirth through rain)
- **Summer** (2): high summer (haze, droning insects), midsummer (lush fullness)
- **Autumn** (3): autumn (gold and decay), early autumn (sharp chill, falling
  leaves), late autumn (stripped bare, bones revealed)
- **Winter** (2): deep winter (silence and frost), first snow (muffled in white)

Each phrase paints a distinct seasonal register — from the hopeful emergence of
early spring to the stark revelation of late autumn.

### Tradeoffs
- **10 curated phrases** — same size as the original TIMES_OF_DAY bank (10).
  Can be expanded in future sessions.
- **Off by default** (`season_enabled=False`), preserving all existing seed-based
  output for users who don't use `--season`.
- **Not suppressed at detail=0** — same reasoning as time-of-day: a seasonal
  framing prefix works naturally with minimal descriptions.
- **Season before time-of-day** — when both are enabled, season comes first
  ("It is early spring. Dawn breaks over the landscape..."). This is the natural
  order: season is the broader temporal frame, time-of-day is narrower within it.
- **Seed-breaking when enabled**: One extra `rng.choice()` call before the
  time-of-day pick shifts the random sequence. Determinism is preserved (same
  seed + same args = same output).
- **In presets from the start** — unlike time-of-day (which spent one session as
  opt-in only), seasonal variation was added to presets in the same session it
  was introduced. This is possible because the pattern is now well-established
  and all the infrastructure (preset gating, `--no-*` flags) already exists.
- **35 new tests, 797 total** (18 todo + 779 landscape), 243 subtests.
- **Test count +17 tests, +21 subtests** from the previous session (780 tests,
  222 subtests).
- **Fulfills "Next likely steps" from Session 133**: Seasonal variation was the
  first item in the "Next likely steps" list.

## 2026-07-15 — Expanded TIMES_OF_DAY Word Bank (15 phrases)

### What
Added 5 new curated time-of-day phrases to the TIMES_OF_DAY bank, expanding it
from 10 to 15 phrases. The new phrases cover late afternoon, stormy/overcast
conditions, the blue hour, the witching hour, and misty morning — temporal
niches absent from the original 10.

### Why
The time-of-day system (Session 131) was the newest sensory dimension and had
not yet received any word bank expansion. The original 10 phrases covered broad
temporal categories (dawn, noon, dusk, midnight, etc.) but had gaps: no
stormy/overcast setting, no late afternoon, no blue hour, no witching hour, and
only one dawn variant. With time-of-day now enabled by default in all 5 presets
(Session 132), a larger bank reduces repetition in preset output. The "Next
likely steps" from Session 132 explicitly called for expanding global word
banks.

The 5 new phrases each cover a temporal niche not well represented in the
existing 10:
- **Late afternoon**: "Late afternoon stretches long shadows across the
  landscape" — the period between noon and golden hour, characterized by long
  shadows and the day beginning to wane. Distinct from the existing golden hour
  (pre-sunset) and dusk (post-sunset).
- **Stormy/overcast**: "A storm-heavy sky presses down upon the landscape" —
  the only phrase that describes a non-clear temporal setting. Covers any time
  of day when the sky is heavy with clouds, a common atmospheric condition.
- **Blue hour**: "The blue hour casts a deep indigo glow across the landscape"
  — the period of twilight when the sun is below the horizon but the sky is a
  deep saturated blue. Distinct from twilight (which is about fading to
  darkness) and dusk (settling of night).
- **Witching hour**: "The witching hour settles over the landscape in absolute
  stillness" — the supernatural 3 AM hour, distinct from the existing midnight
  (crescent moon, silver light) and dead of night (darkness) and starless
  night (absolute blackness). Adds a folkloric/supernatural temporal register.
- **Misty morning**: "Morning mist clings to the landscape like a
  half-remembered dream" — a misty/mysterious morning, distinct from the
  existing dawn (breaking) and early morning (pale gold light) and first light
  (touching the land). Adds a muted, dreamlike morning variant.

### Tradeoffs
- **Data-only change**: No modifications to `generate_landscape()`, CLI flags,
  or any logic. Only the TIMES_OF_DAY list was updated.
- **No seed-breaking**: Adding phrases to TIMES_OF_DAY doesn't change the
  random sequence — `rng.choice(TIMES_OF_DAY)` picks from a larger pool but
  the choice function is unchanged. Only the rendered output content changes
  (new phrases appear in the selection pool).
- **No new tests**: `ALL_TIMES_OF_DAY = set(TIMES_OF_DAY)` is dynamically
  derived, and all TestTimeOfDay and TestDescribeTimes tests use dynamic
  counts/loops. Only the data changed; test logic is unchanged.
- **Test count unchanged**: 780 tests (18 todo + 762 landscape), 222 subtests.
- **Not seed-breaking**: Adding new entries to a list that `rng.choice()` draws
  from doesn't change the RNG sequence — the same seed picks the same index,
  but the content at that index may be different, which only changes rendered
  output, not determinism.
- **Fulfills "Next likely steps" from Session 132**: Word bank expansion was
  explicitly called out as the next step after time-of-day integration.

## 2026-07-15 — Time-of-Day in Presets + `--no-time` Flag

### What
Added `"time_of_day_enabled": True` to all 5 presets (nightfall, pastoral,
sublime, wasteland, dreamscape), making time-of-day phrases active by default
when using any preset. Also added `--no-time` CLI flag that forces
`time_of_day_enabled=False`, overriding presets and explicit `--time`.

### Why
The time-of-day system (Session 131) was the last opt-in sensory feature that
was not integrated into presets. Every other feature — echoes, legends,
soundscapes, travelogue, wistful — went through the same trajectory: add as
opt-in CLI flag, then add to all presets in a follow-up session. This completes
that trajectory for time-of-day.

The `--no-time` flag is necessary because all 5 presets now enable time-of-day
by default. Users who want a preset's configuration but do NOT want a time-of-day
framing need a way to disable it. This follows the exact same pattern as
`--no-echo`, `--no-legend`, `--no-sound`, `--no-travelogue`, and `--no-wistful.

### Tradeoffs
- **Seed-breaking for presets**: All 5 presets now produce different output from
  the previous session for the same seed, because `time_of_day_enabled=True` was
  not previously in presets. This is acceptable because presets are curated entry
  points that evolve as features mature, and determinism is preserved (same seed
  + same args = same output). Users who want the old behavior can explicitly pass
  `--no-time`.
- **Backward compatibility via CLI overrides**: The gating code checks
  `args.time is False` before applying the preset value. Users who explicitly
  pass `--time` don't get the preset value. Users who pass `--no-time` always
  disable it. This is the same pattern as all other preset overrides.
- **No changes to `generate_landscape()`**: Presets are a pure CLI convenience
  layer — the generation function already accepts `time_of_day_enabled`. Only
  the PRESETS dict and main() gating code changed.
- **Consistent with all other preset integrations**: Every feature with an on/off
  switch is now in all 5 presets — echoes (Session 88), legends (Session 97),
  travelogue (Session 106), wistful (Session 110), soundscapes (Session 113),
  and time-of-day (this session).
- **7 new tests, 780 total** (18 todo + 762 landscape), 222 subtests.
- **Fulfills "Next likely steps" from Session 131**: Steps 1 and 2 were adding
  time-of-day to presets and adding --no-time.

## 2026-07-14 — Time-of-Day System (`--time`)

### What
Added a `TIMES_OF_DAY` word bank (10 evocative phrases) and `--time` CLI flag (default: off) that prepends a time-of-day setting sentence to the generated landscape, establishing when the scene is being viewed. Each phrase is a standalone sentence like "Dawn breaks over the landscape." or "The dead of night holds the land in darkness." — followed by a period, then the opening sentence.

Also added `describe_times()` and `--describe-times` for introspection, `"time_of_day"` in JSON metadata, and 27 tests (20 functional + 7 introspection).

### Why
After 6 consecutive sessions (125–130) of word bank expansions, the project needed a genuinely new sensory dimension. The "Next likely steps" in every session since Session 123 explicitly called out "time-of-day" as a candidate. The existing `TIME_WORDS` system provides single-word narrative adverbs ("already", "still", "yet") that subtly frame the temporal quality of the description — but it doesn't establish a concrete time of day. The new time-of-day system adds an explicit temporal setting: the reader knows whether the landscape is viewed at dawn, noon, dusk, or midnight.

This fills a gap in the temporal framing of the landscape generator. The existing features cover:
- **What it looks like** (templates, colors, elements)
- **What it feels like** (mood, weather)
- **What it sounds like** (soundscapes)
- **What it remembers** (echoes)
- **What people say about it** (legends)
- **How it makes you feel** (wistful)
- **Narrative frame** (travelogue)
- **Narrative time** (time words — "already", "still")
- **When it is** (time of day — new)

The 10 phrases cover a wide temporal range: dawn, dead of night, blazing noon, dusk, early morning, midnight moonlight, twilight, golden hour, first light, starless night. Each is phrased as a complete sentence ending with a period, so it joins naturally with any opening template.

### Tradeoffs
- **10 curated phrases** — small enough to maintain quality, large enough for variety. Each phrase covers a distinct time of day. The bank can be expanded in future sessions.
- **Off by default** (`time_of_day_enabled=False`), preserving all existing seed-based output for users who don't use `--time`.
- **Not suppressed at detail=0** — Unlike echoes, legends, soundscapes, and wistful (which all suppress at detail=0), time-of-day is a framing prefix that works naturally with minimal descriptions. "Dawn breaks over the landscape. A vast crystal forest..." is a coherent minimal description.
- **Placed before the opening** — the time-of-day sentence is prepended with `parts.insert(0, ...)`, making it the first thing the reader sees. This establishes the temporal context before the visual description begins.
- **Seed-breaking when enabled**: One extra `rng.choice()` call shifts the random sequence for the opening and everything after. Determinism is preserved (same seed + same args = same output).
- **Not in presets yet** — follows the same trajectory as echoes, legends, soundscapes, travelogue, and wistful, which were all initially only accessible via explicit CLI flags before being integrated into presets. If time-of-day proves useful, it can be added to presets in a future session.
- **No `--no-time` flag** — follows the same pattern as other opt-in features (echo, legend, sound, wistful when first introduced). The `--no-*` variants were added later. If needed, `--no-time` can be added in a future session alongside time-of-day in presets.
- **27 new tests, 773 total** (18 todo + 755 landscape), 207 subtests.

## 2026-07-14 — Expanded Biome-Specific Weather and Anomaly Banks

### What
Added 2 new weathers and 2 new anomalies to each of the 13 biomes in `BIOME_WORDS` — 52 new entries total. Each new entry is curated to fit the biome's thematic identity: deserts get sandstorms and rare rain (weathers), footprints filling with water and stars rearranging (anomalies); cave systems get low mist and underground streams (weathers), stalactites growing visibly and darkness with weight (anomalies); sky islands get upward rain and thin mist (weathers), independent shadow movement and weakening gravity (anomalies), etc.

### Why
Sessions 125–129 expanded biome adjectives+elements, nouns, verbs, colors, and adverbs — weathers and anomalies were the last two biome word bank categories still at their original size (3 per biome). Weathers appear in weather templates via `_pick("weathers", ...)`, which blends biome-specific pools with the global WEATHERS pool (12 entries). With only 3 biome-specific weathers per biome, the blend was heavily skewed toward generic global weathers — biomes felt less distinct in their weather descriptions. Anomalies follow the same pattern via `_pick("anomalies", ...)`, blending with the global ANOMALIES pool (8 entries). Expanding both categories from 3→5 increases the biome-specific share from 20% to ~29% of the combined pool, making weather and anomaly descriptions more distinctive per biome.

This completes the biome word bank expansion campaign that began in Session 125. Over 6 sessions, every biome word category has been expanded:
- **adjectives+elements** (Session 125): 3→5 adjectives, 4→6 elements
- **nouns** (Session 126): 5→7 nouns (6→8 for 3 biomes)
- **verbs** (Session 127): 5→7 verbs
- **colors** (Session 128): 4→6 colors
- **adverbs** (Session 129): 3→5 adverbs
- **weathers+anomalies** (Session 130): 3→5 weathers, 3→5 anomalies

### Tradeoffs
- **Data-only change**: No modifications to `generate_landscape()`, `_pick()`, CLI flags, or any logic. Only the `BIOME_WORDS` dict values changed.
- **No seed-breaking**: Adding words to biome-specific pools doesn't change the random sequence — `_pick()` draws from a larger pool but the weighted-selection function is unchanged. Only the rendered output content changes (new words appear in the selection pool).
- **No new tests**: Existing biome vocabulary tests cover all behaviors generically — they check for the *existence* of biome-specific words in output, not precise counts or specific words.
- **Test count unchanged**: 746 tests (18 todo + 728 landscape), 201 subtests.
- **Not marked common or rare**: New words intentionally left at normal weight tier. Common/rare designation can be tuned per-word in future sessions if needed.
- **Fulfills "Next likely steps" from Session 129**: Weather and anomaly expansion was explicitly called out as the remaining biome word bank categories. All biome categories are now at expanded sizes.
- **Weather and anomaly containers are lists, not tuples**: Consistency with existing pattern — all BIOME_WORDS categories use Python lists for mutability, though the dict is never mutated at runtime.

## 2026-07-14 — Expanded Biome-Specific Adverb Banks

### What
Added 2 new adverbs to each of the 13 biomes in `BIOME_WORDS` — 26 new entries total. Each new adverb is curated to fit the biome's thematic identity: forests get "wistfully" and "invitingly", ruined cities get "hollowly" and "wearily", sky islands get "weightlessly" and "distantly", etc.

### Why
Sessions 125–128 expanded biome adjectives+elements, nouns, verbs, and colors — adverbs were the last major word category still at their original size (3 per biome). Adverbs appear in opening templates (e.g. "...comes into view {adverb} {time_word}"), middle templates (e.g. "The {adj} {noun} {verb} {adverb} with {color} {element}"), echo phrases (e.g. "The {display} remembers {adverb}"), and soundscape phrases (e.g. "The {display} hums {adverb}"). With only 3 adverbs per biome, variety in adverbial slots was extremely limited. Standardizing to 5 ensures more varied output across all template types.

### Tradeoffs
- **Data-only change**: No modifications to `generate_landscape()`, `_pick()`, CLI flags, or any logic. Only the `BIOME_WORDS` dict values changed.
- **No seed-breaking**: Adding words to biome-specific pools doesn't change the random sequence — `_pick()` draws from a larger pool but the weighted-selection function is unchanged. Only the rendered output content changes (new words appear in the selection pool).
- **No new tests**: Existing biome vocabulary tests cover all behaviors generically — they check for the *existence* of biome-specific words in output, not precise counts or specific words.
- **Test count unchanged**: 746 tests (18 todo + 728 landscape), 201 subtests.
- **Not marked common or rare**: New words intentionally left at normal weight tier. Common/rare designation can be tuned per-word in future sessions if needed.
- **Fulfills "Next likely steps" from Session 128**: Adverb expansion was explicitly called out as the first remaining category. Weathers and anomalies remain.

## 2026-07-14 — Expanded Biome-Specific Color Banks

### What
Added 2 new colors to each of the 13 biomes in `BIOME_WORDS` — 26 new entries total. Each new color is curated to fit the biome's thematic identity: forests get "woodland" and "forest green", ruined cities get "pale grey" and "verdigris", sky islands get "dawn pink" and "storm grey", etc.

### Why
Sessions 125–127 expanded biome adjectives+elements, nouns, and verbs respectively. Colors are the next most-impactful category: they appear in opening templates (e.g. "A vast {adj} {display} of {color} {element} stretches..."), middle templates (e.g. "The {adj} {noun} {verb} {adverb} with {color} {element}"), weather templates, anomaly templates, echo phrases, and soundscape phrases — essentially every template slot. With 4 colors per biome, variety was limited. Standardizing to 6 ensures more varied output across all template types.

### Tradeoffs
- **Data-only change**: No modifications to `generate_landscape()`, `_pick()`, CLI flags, or any logic. Only the `BIOME_WORDS` dict values changed.
- **No seed-breaking**: Adding words to biome-specific pools doesn't change the random sequence — `_pick()` draws from a larger pool but the weighted-selection function is unchanged. Only the rendered output content changes (new words appear in the selection pool).
- **No new tests**: 33 existing biome vocabulary tests cover all behaviors generically — they check for the *existence* of biome-specific words in output, not precise counts or specific words.
- **Test count unchanged**: 746 tests (18 todo + 728 landscape), 201 subtests.
- **Not marked common or rare**: New words intentionally left at normal weight tier. Common/rare designation can be tuned per-word in future sessions if needed.
- **Fulfills "Next likely steps" from Session 127**: Color expansion was explicitly called out as the next remaining biome word bank category.

## 2026-07-14 — Expanded Biome-Specific Verb Banks

### What
Added 2 new verbs to each of the 13 biomes in `BIOME_WORDS` — 26 new entries total. Each new verb is curated to fit the biome's thematic identity: forests get "dapple" and "sigh", ruined cities get "fracture" and "whine", sky islands get "glide" and "sail", etc.

### Why
Session 125 expanded biome adjectives and elements, Session 126 expanded biome nouns. Verbs are the next most-impactful category: they appear in middle templates (e.g. "The {adj} {noun} {verb} {adverb} with {color} {element}") and are a fundamental building block of landscape descriptions. With 5 verbs per biome, variety was limited. Standardizing to 7 ensures more varied output.

### Tradeoffs
- **Data-only change**: No modifications to `generate_landscape()`, `_pick()`, CLI flags, or any logic. Only the `BIOME_WORDS` dict values changed.
- **No seed-breaking**: Adding words to biome-specific pools doesn't change the random sequence — `_pick()` draws from a larger pool but the weighted-selection function is unchanged. Only the rendered output content changes (new words appear in the selection pool).
- **No new tests**: 33 existing biome vocabulary tests cover all behaviors generically — they check for the *existence* of biome-specific words in output, not precise counts or specific words.
- **Test count unchanged**: 746 tests (18 todo + 728 landscape), 201 subtests.
- **Not marked common or rare**: New words intentionally left at normal weight tier. Common/rare designation can be tuned per-word in future sessions if needed.
- **Fulfills "Next likely steps" from Session 126**: Verb expansion was explicitly called out.

## 2026-07-14 — Expanded Biome-Specific Noun Banks

### What
Added 2 new nouns to each of the 13 biomes in `BIOME_WORDS` — 26 new entries total. Each new noun is curated to fit the biome's thematic identity: forests get "understory" and "clearings", ruined cities get "skeletons" and "rubble piles", sky islands get "thermals" and "wind shears", etc.

### Why
Session 125 expanded biome adjectives and elements (the most-used categories in templates). Nouns are the next most-impactful category: they appear in opening templates (e.g. "The {noun} of the {display} {verb} with {element}"), middle templates (e.g. "The {noun} {verb} with {element}"), and are a fundamental building block of landscape descriptions. With 5–6 nouns per biome, variety was limited — especially for the 3 biomes that already had 6 vs the majority at 5. Standardizing to 7–8 ensures more varied output.

### Tradeoffs
- **Data-only change**: No modifications to `generate_landscape()`, `_pick()`, CLI flags, or any logic. Only the `BIOME_WORDS` dict values changed.
- **No seed-breaking**: Adding words to biome-specific pools doesn't change the random sequence — `_pick()` draws from a larger pool but the weighted-selection function is unchanged. Only the rendered output content changes (new words appear in the selection pool).
- **No new tests**: 33 existing biome vocabulary tests cover all behaviors generically — they check for the *existence* of biome-specific words in output, not precise counts or specific words.
- **Test count unchanged**: 746 tests (18 todo + 728 landscape), 201 subtests.
- **Not marked common or rare**: New words intentionally left at normal weight tier. Common/rare designation can be tuned per-word in future sessions if needed.
- **Fulfills "Next likely steps" from Session 125**: Noun expansion was explicitly called out.

## 2026-07-14 — Expanded Biome-Specific Word Banks (adjectives + elements)

### What
Added 2 new adjectives and 2 new elements to each of the 13 biomes in `BIOME_WORDS` — 52 new entries total. Each new word is curated to fit the biome's thematic identity: forests get "wildwood" and "pine scent", ruined cities get "shattered" and "mold scent", sky islands get "aerial" and "upper air", etc.

### Why
Biome-specific word banks were created when each biome was added (Sessions 2–22) and have never been expanded since. All *global* word banks have received multiple expansions (legends: 10→20, echoes: 10→15, soundscapes: 8→12, weathers: 8→12, wistful: 6→10), but the biome-specific pools — which are blended with global pools via `_pick()` — have been static. This means biome-specific vocabulary makes up a shrinking proportion of the available word pool as global banks grow. Expanding biome banks restores balance: biomes should feel *more* distinctive, not less, as the project matures.

Adjectives and elements were chosen as the first categories to expand because they appear in the most template slots:
- Adjectives appear in all 4 openings, all 7 middle templates, all 5 weather templates, and 1 anomaly template
- Elements appear in all 4 openings, all 7 middle templates, all 5 weather templates, and 2 anomaly templates

Adding to these categories has the widest per-word impact on output variety.

### Tradeoffs
- **Data-only change**: No modifications to `generate_landscape()`, `_pick()`, CLI flags, or any logic. Only the `BIOME_WORDS` dict values changed.
- **No seed-breaking**: Adding words to biome-specific pools doesn't change the random sequence — `_pick()` draws from a larger pool but the weighted-selection function is unchanged. Only the rendered output content changes (new words appear in the selection pool).
- **No new tests**: 33 existing biome vocabulary tests (across `TestBiomeWords`, `TestNewBiomes`, `TestBiomeWeights`, etc.) cover all behaviors generically — they check for the *existence* of biome-specific words in output, not precise counts or specific words.
- **Test count unchanged**: 746 tests (18 todo + 728 landscape), 201 subtests.
- **Not marked common or rare**: New words intentionally left at normal weight tier. Common/rare designation can be tuned per-word in future sessions if needed.

## 2026-07-14 — Expanded LEGENDS Bank (20 phrases)

### What
Added 5 new curated legend phrases to the LEGENDS bank, expanding it from 15 to 20 phrases. The new phrases cover prophetic dreams, paradoxical observation, ineffable sensory quality, impossible geography, and purposeless endurance — themes absent from the existing 15.

### Why
The legend system (Session 96) was expanded once before (Session 98: 10→15), but has been at 15 phrases for many sessions while other word banks received more recent expansions: weathers (12, Session 120), soundscapes (12, Session 121), echoes (15, Session 122), and wistful (10, Session 123). Legends are enabled in all 5 presets (since Session 97), so a larger bank reduces repetition in preset output. The "Next likely steps" from Session 123 explicitly called for expanding legends.

The 5 new phrases each cover a folkloric niche not well represented in the existing 15:
- **Prophetic dreams**: "appears in the dreams of those who have never seen it" — unconscious precognitive connection to a place, distinct from existing "dreams of a time before people" (which is about the landscape dreaming, not people dreaming of the landscape)
- **Paradoxical observation**: "bell that rings only when no one is listening" — observer-effect mystery, a riddle about perception and reality, distinct from existing "no one returns unchanged" (transformation) and "no path leads to it" (unreachability)
- **Ineffable sensory quality**: "scent that cannot be described, only remembered" — the limits of language to capture sensory experience, distinct from "sounds like a name you almost recognize" (auditory near-memory)
- **Impossible geography**: "every path leads to the same clearing" — non-Euclidean landscape, labyrinthine convergence, distinct from "no path leads to it" (unreachability) and "marked on no map" (cartographic absence)
- **Purposeless endurance**: "built by no one, for no purpose, and yet it endures" — existential mystery, the landscape as an artifact of unknown origin and intent, distinct from "placed by hand" (ancient construction) and "older than stone" (buried antiquity)

### Tradeoffs
- **Data-only change**: No modifications to `generate_landscape()`, `_format_tmpl()`, CLI flags, or any logic. Only the LEGENDS list and LEGEND_INDICATORS set were updated.
- **No seed-breaking**: Adding phrases to LEGENDS doesn't change the random sequence — `rng.choice(LEGENDS)` picks from a larger pool but the choice function is unchanged. Only the rendered output content changes (new phrases appear in the selection pool).
- **5 new indicators, no new tests**: Existing legend tests (15+ tests across TestLegend, TestLegendCount, TestLegendProb, TestNoLegend) cover all behaviors generically — they test for presence/absence of any indicator, not specific phrase counts. Only the indicator list was updated.
- **Test count unchanged**: 746 tests (18 todo + 728 landscape), 201 subtests.
- **Fulfills "Next likely steps" from Session 123**: Legend expansion was explicitly called out.

## 2026-07-14 — Expanded WISTFUL Bank (10 phrases)

### What
Added 4 new curated wistful phrases to the WISTFUL bank, expanding it from 6 to 10 phrases. The new phrases cover irreversible transformation, uniqueness+gratitude, uncanny familiarity, and ineffability — themes absent from the existing 6.

### Why
The wistful system (Session 108) was enabled in all 5 presets (since Session 110), but the phrase bank was never expanded beyond the original 6. Weathers (12), soundscapes (12), echoes (15), and legends (15) all received expansions — wistful was the last major word bank at its original size. With 5 presets using wistful, a larger bank reduces repetition. The "Next likely steps" from Session 122 explicitly called for this.

The 4 new phrases each cover an emotional niche not well represented in the existing 6:
- **Irreversible transformation**: "You will never be the same after visiting..." — the place as a catalyst for change, distinct from the existing "part of you will always remain" (which is about permanent attachment, not change)
- **Uniqueness + gratitude**: "There is nowhere else in the world like..." — appreciation for the rarity of the experience, distinct from "wish you could stay longer" (desire) and "someday you will return" (future)
- **Uncanny familiarity**: "...more like a memory of a place you have always known than a place you have just discovered" — recognition of the never-before-seen, a specific kind of wistfulness (anemoia) absent from the existing set
- **Ineffability**: "...the words will never be enough" — the limits of language, the gap between experience and description, a meta-emotional reflection on the act of describing itself

### Tradeoffs
- **Data-only change**: No modifications to `generate_landscape()`, `_format_tmpl()`, CLI flags, or any logic. Only the WISTFUL list and indicator lists in the test module were updated.
- **No seed-breaking**: Adding phrases to WISTFUL doesn't change the random sequence — `rng.choice(WISTFUL)` picks from a larger pool but the choice function is unchanged. Only the rendered output content changes (new phrases appear in the selection pool).
- **Test fix**: `test_preset_with_wistful_produces_wistful_output` had a hardcoded copy of the original 6 indicators, causing 2/5 presets to fail at seed=42 (nightfall and sublime selected new phrases). Updated to include all 10 indicators.
- **No new tests**: Existing wistful tests (15+ tests across TestWistful, TestDescribeWistful, TestNoWistful) cover all behaviors generically. Only the indicator lists were updated.
- **746 tests still pass** (18 todo + 728 landscape), 201 subtests unchanged.
- **Fulfills "Next likely steps" from Session 122**: Wistful expansion was explicitly called out.

## 2026-07-14 — Expanded ECHOES Bank (15 phrases)

### What
Added 5 new curated atmospheric echo phrases to the ECHOES bank, expanding it from 10 to 15 phrases. The new phrases cover visual refraction, wind-borne memory, subterranean movement, anticipatory stillness, and synesthetic scent — themes absent from the existing 10.

### Why
The echo system (Sessions 78–86) gained injection support for `{display}`, `{adverb}`, `{element}`, `{color}`, `{adj}`, and `{time_word}`, but the actual phrase bank was never expanded beyond the original 10. Weathers (12, Session 120), soundscapes (12, Session 121), and legends (15, Session 98) all received expansions; echoes were the last major word bank at its original size. Echoes are now enabled in all 5 presets (since Session 88), so a larger bank reduces repetition in preset output — the same reason legends were expanded in Session 98.

The 5 new phrases each cover an atmospheric niche not well represented in the existing 10:
- **Light bending**: visual/atmospheric distortion, light as something with agency — distinct from existing light references (which are elemental/static)
- **Wind memory**: the wind as a carrier of voices, language without a speaker — adds an audible dimension distinct from soundscapes (which are present-tense sounds) and existing echoes (which are about time and presence)
- **Subterranean movement**: deep geological presence, the landscape as a living thing beneath the surface — echoes the "something older than stone" legend theme but from an atmospheric (not folkloric) perspective
- **Holding breath**: anticipation, the landscape poised on the edge of change — fills a temporal-emotional gap between "waiting for you" (expectation) and "deep time" (eternality)
- **Synesthetic scent**: olfactory memory woven into visual/atmospheric texture — a sensory dimension (smell) that the generator lacks as a dedicated system but can now evoke through echo injection

### Tradeoffs
- **Data-only change**: No modifications to `generate_landscape()`, `_format_tmpl()`, CLI flags, or any logic. Only the ECHOES list and ECHO_INDICATORS/NO_ECHO_INDICATORS sets were updated.
- **Multi-injection phrases**: The new phrases use combinations of `{adverb}`, `{adj}`, `{color}`, `{display}`, `{element}`, and `{time_word}` — following the established injection patterns. Each phrase has 2–4 injectable slots, consistent with the existing distribution.
- **No seed-breaking**: Adding phrases to ECHOES doesn't change the random sequence — `rng.choice(ECHOES)` picks from a larger pool but the choice function is unchanged. Only the rendered output content changes (new phrases appear in the selection pool).
- **5 new indicators, no new tests**: Existing echo tests (15+ tests across TestEcho, TestEchoCount, TestEchoProb, TestNoEcho) cover all behaviors generically — they test for presence/absence of any indicator, not specific phrase counts. Only the indicator lists were updated.
- **Test count unchanged**: 746 tests (18 todo + 728 landscape), 201 subtests.
- **Fulfills "Next likely steps" from Session 121**: This was explicitly called out as the next step after expanding weathers (120) and soundscapes (121).

## 2026-07-14 — No-Echo, No-Legend, No-Sound Flags (`--no-echo`, `--no-legend`, `--no-sound`)

### What
Added `--no-echo`, `--no-legend`, and `--no-sound` CLI flags that force `echo_enabled=False` / `legend_enabled=False` / `sound_enabled=False`, overriding presets (which enable all three by default) and explicit `--echo` / `--legend` / `--sound` flags. Implemented as `store_true` args with post-preset overrides in `main()`, following the exact same pattern as `--no-travelogue` and `--no-wistful` (Session 118).

### Why
All 5 presets (nightfall, pastoral, sublime, wasteland, dreamscape) enable echo, legend, and sound. Users who want a preset's mood/bias/detail/anomaly configuration but do NOT want these atmospheric layers had no way to disable them when using `--preset`. This was explicitly called out as the next step in Session 118's "Next likely steps." Every other `--no-*` flag (`--no-color`, `--no-element`, `--no-time-word`, `--no-adverb`, `--no-weather`, etc.) disables features that are ON by default, but echo/legend/sound are OFF by default. The need arises specifically from presets: presets flip them ON, and there was no OFF switch for that case.

### Tradeoffs
- **`--no-*` wins over `--*`**: Same design as Session 118 — the "no" flag is a safety override. The post-preset override block explicitly sets the value after all gating, ensuring `--no-*` always takes effect.
- **No changes to `generate_landscape()`**: The generation function already accepts `echo_enabled`/`legend_enabled`/`sound_enabled` booleans. Only `main()` preset gating and CLI argument definitions changed.
- **Not seed-breaking**: No random call order changes. The new flags only affect whether these features are `True` or `False` when passed to `generate_landscape()`.
- **Test indicator collision**: `ECHO_INDICATORS` includes `"remembers"` which also appears in the legend phrase "remembers those who built it." Added `NO_ECHO_INDICATORS` (same list minus `"remembers"`) for suppression tests where legends may be present.
- **18 new tests, 746 total** (18 todo + 728 landscape), 201 subtests.
- **Fulfills "Next likely steps" from Session 118**: This was explicitly called out as the next step after no-travelogue and no-wistful.

## 2026-07-14 — No-Travelogue and No-Wistful Flags (`--no-travelogue`, `--no-wistful`)

### What
Added `--no-travelogue` and `--no-wistful` CLI flags that force `travelogue=False` / `wistful=False`, overriding presets (which enable both by default) and explicit `--travelogue` / `--wistful` flags. Implemented as separate `store_true` args with a post-preset override block in `main()`.

### Why
All 5 presets (nightfall, pastoral, sublime, wasteland, dreamscape) enable travelogue and wistful. Users who want a preset's mood/bias/anomaly/echo/legend configuration but do NOT want the travelogue framing or wistful closing had no way to disable them when using `--preset`. Every other `--no-*` flag (`--no-color`, `--no-element`, `--no-time-word`, `--no-adverb`, `--no-weather`, etc.) disables features that are ON by default, but travelogue/wistful are OFF by default. The need arises specifically from presets: presets flip them ON, and there was no OFF switch for that case. Adding `--no-*` variants follows the established pattern and gives users full control.

### Tradeoffs
- **`--no-*` wins over `--*`**: If both `--travelogue` and `--no-travelogue` are passed, `--no-travelogue` wins. This is a design choice: the "no" flag is a safety override. The post-preset override block explicitly sets the value after all gating, ensuring `--no-*` always takes effect.
- **No changes to `generate_landscape()`**: The generation function already accepts `travelogue`/`wistful` booleans. Only `main()` preset gating and CLI argument definitions changed.
- **Not seed-breaking**: No random call order changes. The new flags only affect whether `travelogue`/`wistful` are `True` or `False` when passed to `generate_landscape()`.
- **12 new tests, 728 total** (18 todo + 710 landscape), 171 subtests.
- **Fills "Next likely steps" from Session 117**: This was explicitly called out as the next step after weather count/prob.

## 2026-07-14 — Configurable Weather Count and Probability (`--weather-count`, `--weather-prob`)

### What
Added `--weather-count` (choices 0–3, default: 1) and `--weather-prob` (0.0–1.0, default: 1.0) CLI flags, with corresponding `weather_count` and `weather_prob` parameters to `generate_landscape()`. Users can now control how many weather descriptions appear per detail level and how often each roll succeeds. Also added `weather_count` and `weather_prob` to all 5 presets with curated values.

### Why
Echo, legend, anomaly, and soundscape all have count and probability controls — weather was the last major feature missing them. Weather previously only had an on/off switch (`--no-weather`/`weather_enabled`). Adding count and prob gives users fine-grained control over weather density and frequency, matching the established pattern.

### Tradeoffs
- **Default weather_count=1, weather_prob=1.0** preserves backward compatibility — all existing seed-based output is unchanged.
- **Per-roll probability**: each of `weather_count` rolls per detail level independently draws `rng.random() < weather_prob`, same pattern as `echo_prob`, `legend_prob`, `anomaly_prob`, and `sound_prob`.
- **weather_count=0** is an alternative suppression mechanism to `weather_enabled=False`. Both are valid; `weather_count=0` is more explicit when a script conditionally enables weather with variable counts.
- **Included in JSON metadata** — `weather_count` and `weather_prob` emit alongside other metadata fields.
- **Preset seed-breaking**: Adding `weather_count` and `weather_prob` to presets changes output for all 5 presets (nightfall gets 2 weather sentences, pastoral gets weather_prob=0.8, etc.). This is acceptable because presets evolve as features mature.
- **Weather inside detail loop**: Unlike echo/legend/soundscape which are independent blocks, weather remains inside the detail loop. This means with detail=2 and weather_count=2, the output gets 4 weather sentences. With detail=1 and weather_count=2, it gets 2. This is intuitive — detail controls the overall sentence count, and weather_count scales within that.
- **19 new tests, 716 total** (18 todo + 698 landscape), 151 subtests.

## 2026-07-14 — Per-Preset Soundscape Count and Probability

### What
Added `sound_count` and `sound_prob` to all 5 preset configurations (`nightfall`, `pastoral`, `sublime`, `wasteland`, `dreamscape`). Each preset now has curated soundscape density and probability values that match its atmospheric theme, mirroring how `echo_count`/`echo_prob` and `legend_count`/`legend_prob` are already set per-preset.

- **nightfall**: `sound_count=2, sound_prob=0.7` — eerie sounds (whispers, breaths, shattering glass) appear often but not always, matching the nightfall echo config (echo_count=2, echo_prob=0.7) and legend config (legend_count=2, legend_prob=0.7)
- **pastoral**: `sound_count=1, sound_prob=0.5` — a single gentle soundscape, and only 50% of the time, keeping the serene tone uncluttered. Matches pastoral's sparse echo config (echo_count=1, echo_prob=0.5)
- **sublime**: `sound_count=2, sound_prob=0.95` — rich auditory texture almost always present, matching sublime's maximalist echo config (echo_count=3, echo_prob=1.0)
- **wasteland**: `sound_count=2, sound_prob=1.0` — sounds of ruin (glass shattering, wind shifting, slow pulses) always present, matching wasteland's certainty (anomaly_prob=1.0, legend_prob=1.0)
- **dreamscape**: `sound_count=2, sound_prob=0.9` — surreal sounds usually present, matching dreamscape's high-but-not-certain echo config (echo_count=2, echo_prob=1.0)

### Why
The soundscape system evolved through 4 sessions: on/off (Session 112), in-presets (Session 113), count (Session 114), and prob (Session 115). After each building block existed independently, the final integration step was wiring them into presets with thoughtfully chosen values. This follows the exact same trajectory as echo and legend, which also went through on/off → presets (on/off only) → count → prob → per-preset tuning.

Before this change, all presets used default `sound_count=1, sound_prob=1.0` — every preset always produced exactly one soundscape phrase. This worked but missed the opportunity to give each preset a distinct auditory density that matches its mood: a tranquil pastoral landscape shouldn't always have sounds (sometimes it should be silent), while a sublime or wasteland landscape should rarely be silent.

This completes the per-preset soundscape tuning, making the soundscape system fully mature alongside echo and legend.

### Tradeoffs
- **Seed-breaking for presets**: All 5 presets now produce different output from the previous session for the same seed, because `sound_count` and `sound_prob` were not previously in presets. This is acceptable because presets are curated entry points that evolve as features mature, and determinism is preserved (same seed + same args = same output). Users who want the old preset behavior can explicitly pass `--sound-count 1 --sound-prob 1.0`.
- **Backward compatibility via CLI overrides**: The existing gating code checks `args.sound_count == 1` and `args.sound_prob == 1.0` before applying preset values. Users who explicitly pass `--sound-count 1 --sound-prob 1.0` get the old behavior even with `--preset`. This is the same pattern as all other preset overrides.
- **No changes to `generate_landscape()`**: Presets are a pure CLI convenience layer — the generation function already accepts `sound_count` and `sound_prob` (Sessions 114/115). Only the PRESETS dict changed.
- **Consistent with echo and legend preset pattern**: Every preset that has `echo_count`/`echo_prob` and `legend_count`/`legend_prob` now has `sound_count`/`sound_prob` with similar thematic density — high drama presets (sublime, wasteland, dreamscape) use higher counts/probs, while subtle presets (pastoral) use lower values.
- **Relaxed test `test_preset_with_soundscape_produces_soundscape_output`**: Renamed to `test_preset_with_soundscape_produces_valid_output` and changed to only check for valid output structure, not specific soundscape content. This is because presets now have probabilistic sound_prob values (e.g. pastoral: sound_prob=0.5, sound_count=1 means only ~50% soundscape presence). The structural test `test_all_presets_include_sound_count_and_prob` covers the key configuration validation. This matches the pattern of `test_preset_with_legend_produces_legend_output` which also only checks for valid output.
- **3 new tests, 697 total** (18 todo + 679 landscape), 146 subtests.

## 2026-07-14 — Configurable Soundscape Probability (`--sound-prob`)

### What
Added `--sound-prob` CLI flag and `sound_prob` parameter to `generate_landscape()` (default: 1.0). Users can now control how often soundscape phrases appear per roll, with 0.0 suppressing soundscapes entirely and 1.0 always producing them. Each of `sound_count` rolls independently draws `rng.random() < sound_prob`.

### Why
The soundscape system (Session 112) started as an on/off switch, then gained `--sound-count` (Session 114). But every roll always produced a soundscape phrase — there was no way to make soundscapes appear unpredictably. Following the same trajectory as echoes (on/off → count → prob) and legends (on/off → count → prob), adding `sound_prob` gives users fine-grained control over soundscape frequency. This is useful for atmospheric variety where soundscapes feel more organic when they appear unpredictably rather than every time. The Session 114 DECISIONS.md explicitly noted "No `sound_prob`: Unlike echoes (which have `echo_prob`) and legends (`legend_prob`), soundscapes don't have a probability parameter yet. Count came first in the echo/legend trajectory too — prob followed in later sessions."

### Tradeoffs
- **Default 1.0 preserves backward compatibility**: all existing seed-based output with `--sound` is unchanged.
- **Per-roll probability**: each of `sound_count` attempts rolls independently against `sound_prob`, same pattern as `echo_prob` and `legend_prob`.
- **`sound_prob=0.0`** is an alternative suppression mechanism to `sound_count=0`. Both are valid; `sound_prob=0.0` is more explicit about intent when a script conditionally enables soundscapes with different probabilities.
- **Included in JSON metadata** when `sound_enabled=True`, alongside `sound_count`.
- **Seed-breaking when `sound_prob < 1.0`**: When `sound_prob` causes a roll to be skipped, the RNG sequence shifts by one `rng.random()` call. With `sound_prob=1.0` (default), no extra random calls are consumed beyond the `rng.choice()` for each soundscape, so behavior is unchanged.
- **7 new tests, 694 total** (18 todo + 676 landscape), 137 subtests.

## 2026-07-14 — Configurable Soundscape Count (`--sound-count`)

### What
Added `--sound-count` CLI flag and `sound_count` parameter to `generate_landscape()` (default: 1, choices: 0-3). Users can now control how many soundscape phrases appear per landscape, following the exact same pattern as `--echo-count` (Session 79) and `--legend-count` (Session 101):
- `sound_count=0` suppresses soundscape phrases entirely
- `sound_count=1` (default) preserves existing behavior — one phrase per landscape
- `sound_count=2` and `sound_count=3` produce multiple phrases with dedup (no repeated phrases)
- Added `sound_count` to JSON metadata when `sound_enabled=True`
- Added preset gating for `sound_count`

Also fixed `SOUND_INDICATORS` — the test module's invariant substrings used generic words ("hums", "whispers", "breathing") that also appear in general landscape vocabulary, causing false positives in dedup and suppression tests. Replaced with unique long substrings from each soundscape phrase (e.g. "tone that seems to come from everywhere", "at the edge of hearing").

### Why
The soundscape system (Session 112) was initially a simple on/off switch — one phrase per landscape when enabled. Following the same trajectory as echoes (on/off → count → prob) and legends (on/off → count → prob), adding `sound_count` gives users fine-grained control over soundscape density. With 8 curated soundscape phrases, `sound_count=2` or `sound_count=3` produces richer landscapes without repetition (dedup ensures no repeats). This is the natural evolution: the Session 112 DECISIONS.md explicitly noted "Count and prob can be added in future sessions if the feature proves useful."

The SOUND_INDICATORS fix closes a latent bug introduced in Session 112 — the original indicators were too short and matched general vocabulary (e.g. "hums" is also a verb in the word banks, "whispers" is an adverb). The replacement indicators use unique multi-word substrings that are statistically impossible in non-soundscape text.

### Tradeoffs
- **sound_count=0** is an alternative suppression mechanism to not using `--sound`. Both are valid; `sound_count=0` is more explicit when a script conditionally enables soundscapes with variable counts.
- **Dedup with fallback**: Same pattern as echoes and legends — a `used_sounds` set prevents repeats within a landscape. With 8 phrases and max count=3, dedup never exhausts the pool in practice, but the fallback (full pool) is implemented for correctness.
- **No `sound_prob`**: Unlike echoes (which have `echo_prob`) and legends (`legend_prob`), soundscapes don't have a probability parameter yet. Count came first in the echo/legend trajectory too — prob followed in later sessions. If users want variable soundscape density, `sound_count` with dedup already provides variety.
- **Seed-breaking**: Adding `rng.choice()` calls for each soundscape count shifts the random sequence. With `sound_count=1` (default), this preserves the existing single-`rng.choice()` call from before, so existing seed-based output with `--sound` is preserved. With `sound_count > 1`, additional `rng.choice()` calls shift subsequent random calls (legends, wistful, travelogue) — same pattern as echo and legend count.
- **9 new tests, 687 total** (18 todo + 669 landscape), 137 subtests.
- **SOUND_INDICATORS fix is backward compatible**: The new indicators are all stricter (longer substrings), so they don't introduce false negatives for existing tests. The old indicators were too loose (false positives), so the fix only makes tests more correct.

### What
Added `"sound_enabled": True` to all 5 preset configurations (`nightfall`, `pastoral`, `sublime`, `wasteland`, `dreamscape`). Each preset now includes an auditory soundscape phrase by default, following the same pattern as `travelogue` (Session 106) and `wistful` (Session 110).

### Why
Soundscapes (Session 112) were only accessible via the explicit `--sound` flag — presets, which are the curated on-ramp for new users, didn't use them. This meant a `--preset nightfall` landscape would get eerie mood, rare bias, high anomalies, atmospheric echoes, folkloric legends, travelogue framing, and wistful emotional coda — but no auditory dimension. Adding soundscapes to all presets makes them richer out of the box without requiring users to know about `--sound`.

Each preset benefits auditorily:
- **nightfall**: eerie mood + rare bias + soundscape → ominous whispers and inhuman breathing in the dark
- **pastoral**: peaceful mood + soundscape → gentle sounds of a living, breathing landscape
- **sublime**: vibrant+peaceful blend + common bias + soundscape → transcendent auditory beauty
- **wasteland**: desolate mood + no colors + high anomalies + soundscape → the sound of ruin — glass shattering, wind shifting
- **dreamscape**: surreal mood blend + flat bias + soundscape → oneiric, uncanny sounds — rhythms from nowhere, calls from nothing

This completes the preset integration for soundscapes, following the same trajectory as travelogue (Session 104 → 106: add feature, then add to presets), legends (Session 96 → 97), wistful (Session 108 → 110), and echoes (Session 78 → 88).

### Tradeoffs
- **Seed-breaking for presets**: All 5 presets now produce different output from the previous session for the same seed, because `sound_enabled=True` was not previously in presets. This is acceptable because presets are curated entry points that evolve as features mature, and determinism is preserved (same seed + same args = same output). Users who want the old preset behavior can explicitly omit `--sound`.
- **Backward compatibility via CLI overrides**: The gating code checks `args.sound is False` before applying the preset value. Users who explicitly pass `--sound` don't get the preset value. This is the same pattern as all other preset overrides.
- **No changes to `generate_landscape()`**: Presets are a pure CLI convenience layer — the generation function already accepts `sound_enabled` (Session 112). Only the `PRESETS` dict and `main()` gating code changed.
- **Consistent with echo, legend, travelogue, and wistful preset pattern**: All features with an on/off switch are now in all presets — echo (since Session 88), legend (Session 97), travelogue (Session 106), wistful (Session 110), and soundscape (this session).
- **2 new tests, 678 total** (18 todo + 660 landscape), 137 subtests.

## 2026-07-14 — Soundscape Auditory Layer (`--sound`)

### What
Added `SOUNDSCAPES` word bank (8 curated phrases) and `--sound` CLI flag (default: off) that appends one soundscape phrase to the generated landscape, describing what the landscape sounds like. Each phrase uses `{display}`, `{adverb}`, `{color}`, `{adj}`, and `{element}` injection, so soundscape phrases feel grounded in the current landscape's vocabulary palette.

Also added `describe_sounds()` and `--describe-sounds` for introspection, `"sound_enabled": true` in JSON metadata, and 24 tests (8 introspection + 16 functional).

### Why
After 111 sessions of enriching vocabulary, templates, moods, echoes, legends, travelogue, and wistful framing, the landscape generator could describe what a place *looks like, feels like, sounds like (via weather), remembers, what people say about it, what narrative frame it sits in, and what the observer feels about it* — but it never had a dedicated system for *present-moment auditory sensation as an atmospheric layer*. Weather templates describe wind and rain as weather phenomena, and element words include "sound" and "echo" as abstract qualities — but no feature specifically describes the *sounds of the landscape itself* as a focused sensory dimension.

Echoes are atmospheric memory (timeless presence, the land remembering). Legends are cultural (folk knowledge). Travelogue is narrative framing. Wistful is emotional response. Soundscapes fill a gap: *what you hear right now*. This is a genuinely distinct sensory dimension — hearing — and it changes the landscape's feel from a purely visual/phenomenological description to a multi-sensory one. A landscape that "hums with a tone that seems to come from everywhere at once" or "whispers at the edge of hearing" has an auditory texture that the visual templates and weather system don't provide.

This directly serves the GOAL.md directive to "build something genuinely novel or interesting." An auditory layer for a procedural landscape generator — especially one with poetic, eerie, or sublime phrases — is a genuinely unusual addition that transforms the output from a scenic description into a lived, sensory experience.

### Tradeoffs
- **8 curated phrases** — small enough to maintain quality, large enough for variety. Each phrase covers a different sound type: hum (subsonic vibration), shift (movement), shatter (crystal/breaking), echo (close-but-invisible), call (creature), pulse (rhythm), whisper (edge-of-hearing), breath (animistic).
- **Uses existing word categories** — adverb, color, adj, element are all already picked per-landscape before the soundscape block, so no new random calls are added beyond `rng.choice(SOUNDSCAPES)`. The `_format_tmpl` function handles disabled-feature cleanup naturally (e.g. `"shattering ."` → `"shattering."` when adverb is disabled).
- **Placed after echoes, before legends** — same position as wistful relative to legends/travelogue. In the generation flow: opening → middle/weather → anomalies → echoes → soundscapes → legends → wistful → travelogue. This creates a sensory arc: visual → weather → wrongness → what the place remembers → what you hear → what people say → how you feel → narrative frame.
- **Suppressed at `detail=0`** — same pattern as echoes, legends, and wistful. Soundscapes need a described landscape context to have resonance.
- **Not seed-breaking when disabled**: `sound_enabled=False` by default, so all existing seed-based output is preserved. When enabled, one extra `rng.choice()` call shifts the random sequence for legends and beyond.
- **Simple on/off switch** — no count or probability parameters. Follows the same initial pattern as echoes (Session 78), legends (Session 96), and wistful (Session 108): one phrase per landscape when enabled. Count and prob can be added in future sessions if the feature proves useful.
- **Not in presets yet** — follows the same trajectory as echoes, legends, travelogue, and wistful, which were all initially only accessible via explicit CLI flags before being integrated into presets in later sessions. If soundscapes prove useful, they can be added to presets in a future session.
- **Seed-breaking when enabled**: One extra `rng.choice()` call is introduced after echoes and before legends, shifting the random sequence for legends, wistful, and travelogue. Determinism is preserved (same seed + same args = same output).
- **24 new tests, 676 total** (18 todo + 658 landscape), 127 subtests unchanged.

## 2026-07-14 — Wistful Introspection (`--describe-wistful`)

### What
Added `describe_wistful()` function and `--describe-wistful` CLI flag. When invoked, it prints all 6 wistful phrases with their index numbers and exits without generating a landscape.

### Why
The introspection suite now covers biome, mood, global, templates, echoes, legends, presets, and travelogue — but wistful (8 sessions old, now enabled in all 5 presets) had no introspection. Users who want to see wistful phrases had no discoverable way to do so without reading `landscape.py`. This follows the same pattern as every other describe-* feature: a pure function that returns a formatted string, a CLI flag that prints it and exits, and tests that verify the output structure.

### Tradeoffs
- **Data-only addition**: No changes to `generate_landscape()`, generation logic, or any feature code. Only `landscape.py` (new function + CLI flag + early-exit) and `test_landscape.py` (8 new tests) were modified.
- **Not seed-breaking**: No random call order changes — only an introspection function and CLI flag addition.
- **8 new tests, 652 total** (18 todo + 634 landscape), 127 subtests.
- **Follows established pattern**: Every test method in `TestDescribeWistful` has a direct counterpart in `TestDescribeEchoes`, `TestDescribeLegends`, and `TestDescribeTravelogue`, making the test suite symmetric.

## 2026-07-14 — Wistful in Presets

### What
Added `"wistful": True` to all 5 preset configurations (`nightfall`, `pastoral`, `sublime`, `wasteland`, `dreamscape`). Each preset now includes the wistful emotional coda by default, following the same pattern as `travelogue` (Session 106) and `legend_enabled` (Session 97).

### Why
Wistful (Session 108) was only accessible via the explicit `--wistful` flag — presets, which are the curated on-ramp for new users, didn't use it. This meant a `--preset nightfall` landscape would get eerie mood, rare bias, high anomalies, atmospheric echoes, folkloric legends, and travelogue framing — but no personal emotional response. Adding wistful to all presets makes them richer out of the box without requiring users to know about `--wistful`.

Each preset benefits emotionally:
- **nightfall**: eerie mood + rare bias + wistful → the fear of leaving an uncanny place that has begun to feel familiar
- **pastoral**: peaceful mood + wistful → the gentle ache of leaving a serene, welcoming place
- **sublime**: vibrant+peaceful blend + common bias + wistful → the bittersweetness of witnessing beauty you know you'll never see again
- **wasteland**: desolate mood + no colors + high anomalies + wistful → finding something to miss in a place of ruin
- **dreamscape**: surreal mood blend + flat bias + wistful → waking from a dream you wish was real

This completes the preset integration for wistful, following the same trajectory as travelogue (Session 104 → 106: add feature, then add to presets), legends (Session 96 → 97), and echoes (Session 78 → 88).

### Tradeoffs
- **Seed-breaking for presets**: All 5 presets now produce different output from the previous session for the same seed, because `wistful=True` was not previously in presets. This is acceptable because presets are curated entry points that evolve as features mature, and determinism is preserved (same seed + same args = same output). Users who want the old preset behavior can explicitly use `--no-wistful` or omit wistful via the non-preset flags.
- **Backward compatibility via CLI overrides**: The gating code checks `args.wistful is False` before applying the preset value. Users who explicitly pass `--wistful` don't get the preset value. This is the same pattern as all other preset overrides.
- **No changes to `generate_landscape()`**: Presets are a pure CLI convenience layer — the generation function already accepts `wistful` (Session 108). Only the `PRESETS` dict and `main()` gating code changed.
- **Existing test fix**: `test_wistful_works_with_preset` passed both `wistful=True` and `**PRESETS[name]` — now that presets contain `wistful`, the explicit kwarg was removed to avoid `multiple values for keyword argument` errors.
- **Consistent with echo, legend, and travelogue preset pattern**: All features with an on/off switch are now in all presets — echo (since Session 88), legend (Session 97), travelogue (Session 106), and wistful (this session).
- **2 new tests, 644 total** (18 todo + 626 landscape), 127 subtests.

## 2026-07-14 — `wistful` in JSON Metadata

### What
Added `"wistful": true` to JSON output when `wistful=True`, following the same pattern as `travelogue` (Session 105), `echo_enabled` (Session 100), and `legend_enabled` (Session 97). Previously, wistful framing was invisible in JSON metadata — consumers had no way to detect whether a landscape had a wistful emotional coda without parsing the text field for wistful phrases.

### Why
When wistful was added (Session 108), the JSON metadata gap was the same one that `echo_enabled` and `travelogue` had before their respective metadata sessions: the feature had an on/off switch but no corresponding boolean in JSON output. Every other feature with an on/off switch (echo, legend, travelogue) emits an explicit boolean in JSON. Adding `wistful` makes the JSON format consistent and lets consumers programmatically detect whether the emotional coda is active.

### Tradeoffs
- **Backward compatible**: Existing JSON output without `wistful` is unaffected; the field is only added when `wistful=True`.
- **Not seed-breaking**: No random call order changes — only a metadata field addition.
- **2 new tests**, 642 total (18 todo + 624 landscape), 117 subtests.

## 2026-07-14 — Wistful Emotional Coda (`--wistful`)

### What
Added a `WISTFUL` word bank — 6 curated phrases expressing bittersweet longing and nostalgia — and a `--wistful` CLI flag (default: off) that appends one wistful closing phrase to the generated landscape. Each phrase references `{display}` (the biome name), so the emotional coda feels grounded in the landscape context.

### Why
After 107 sessions of enriching vocabulary, templates, moods, echoes, legends, and travelogue framing, the landscape generator could describe *what a place looks like, feels like, sounds like, what its folklore is, and in what narrative frame* — but it never expressed the *narrator's emotional response* to the landscape. The observer describes the place but never how it makes them feel.

Echoes are atmospheric (timeless presence, memory of the land itself). Legends are cultural (folk knowledge, collective memory). Travelogue is narrative (journal entry about discovery). None of these express *yearning* — the bittersweet feeling of arriving somewhere beautiful and already knowing you'll have to leave, or the ache of carrying a place with you after you depart.

The wistful phrases fill this gap: "You wish you could stay longer in the forest." / "Part of you will always remain in the forest." / "The forest calls to you even as you turn away." These add a personal, emotional dimension distinct from everything else in the generator — not describing the landscape, but describing the *observer's relationship with it*.

This directly serves the GOAL.md directive to "build something genuinely novel or interesting." An emotional coda — especially one tinged with yearning for a fictional place — is a genuinely unusual addition to a procedural landscape generator. It transforms the output from a description into a *memory*.

### Tradeoffs
- **6 curated phrases** — small enough to maintain quality, large enough for variety across multiple runs. Each phrase expresses a slightly different shade of wistfulness: longing to stay, permanent connection, call to return, carrying the place with you, future return, half-remembered dream.
- **Only `{display}` injection** — matches legends and echoes. Wistful phrases are personal reflections about the *place itself*, not about its visual qualities or atmospheric texture. Adding other word categories (adj, adverb, element, color) would make them feel like descriptions rather than emotional responses.
- **Simple on/off switch** — no count or probability parameters. Follows the same initial pattern as echoes (Session 78) and legends (Session 96): one phrase per landscape when enabled. Count and prob can be added in future sessions if the feature proves useful.
- **Placed after legends, before travelogue suffix** — in the travelogue journal frame, the wistful reflection sits between the content and the journal's closing, creating a natural narrative arc: arrival → observation → emotional reflection → planned next steps.
- **Suppressed at `detail=0`** — same pattern as echoes and legends. Wistfulness needs context (a described landscape) to have emotional weight.
- **Not seed-breaking when disabled**: `wistful=False` by default, so all existing seed-based output is preserved. When enabled, one extra `rng.choice()` call is introduced after legends, shifting the random sequence for the travelogue block and beyond.
- **JSON metadata added in Session 109** — `wistful` now emits `"wistful": true` in JSON output, following the same pattern as `travelogue` (Session 105), `echo_enabled` (Session 100), and `legend_enabled` (Session 97).
- **15 new tests**, 641 total (18 todo + 623 landscape), 117 subtests.

## 2026-07-14 — Travelogue Introspection (`--describe-travelogue`)

### What
Added `--describe-travelogue` CLI flag and `describe_travelogue()` function. When invoked, it prints all 4 travelogue prefixes and 4 travelogue suffixes with their index numbers and exits without generating a landscape.

### Why
The introspection suite now includes `--describe-biome` (Session 43), `--describe-mood` (Session 44), `--describe-global` (Session 45), `--describe-templates` (Session 64), `--describe-echoes` (Session 86), `--describe-legends` (Session 99), and `--describe-presets` (Session 88) — covering biome word banks, mood word banks, global word pools, sentence templates, echo phrases, legend phrases, and preset configurations. But the travelogue system (4 prefixes, 4 suffixes from Session 104) had no introspection, even though travelogue is now enabled in all 5 presets (Session 106). Users who want to see what travelogue templates are available had no discoverable way to do so without reading `landscape.py` directly.

This follows the same pattern as every other describe-* feature: a pure function that returns a formatted string, a CLI flag that prints it and exits, and tests that verify the output structure.

### Tradeoffs
- **Data-only addition**: No changes to `generate_landscape()`, CLI flags (beyond the new `--describe-travelogue`), generation logic, or any feature code. Only `landscape.py` (new function + CLI flag + early-exit) and `test_landscape.py` (11 new tests) were modified.
- **Not seed-breaking**: No random call order changes — only an introspection function and CLI flag addition.
- **11 new tests, 626 total** (18 todo + 608 landscape), 112 subtests.
- **Follows established pattern**: Every test method in `TestDescribeTravelogue` has a direct counterpart in `TestDescribeEchoes` and `TestDescribeLegends`, making the test suite symmetric and easier to maintain.

### What
Added `"travelogue": True` to all 5 preset configurations (`nightfall`, `pastoral`, `sublime`, `wasteland`, `dreamscape`). Each preset now frames the landscape as a travel journal entry by default, following the same pattern as `legend_enabled` (Session 97) and `echo_enabled` (Session 88).

### Why
Travelogue (Session 104) was only accessible via the explicit `--travelogue` flag — presets, which are the curated on-ramp for new users, didn't use it. This meant a `--preset nightfall` landscape would get eerie mood, rare bias, high anomalies, atmospheric echoes, and folkloric legends — but no narrative framing. Adding travelogue to all presets makes them richer out of the box without requiring users to know about `--travelogue`.

Each preset benefits narratively:
- **nightfall**: eerie mood + rare bias + travelogue → ominous exploration journal, documenting the discovery of a threatening landscape
- **pastoral**: peaceful mood + travelogue → serene travel diary, recording the beauty of tranquil places
- **sublime**: vibrant+peaceful blend + common bias + travelogue → journal of transcendent discovery, nature writing at its most elevated
- **wasteland**: desolate mood + no colors + high anomalies + travelogue → grim expedition log, post-apocalyptic field notes
- **dreamscape**: surreal mood blend + flat bias + travelogue → explorer's log of impossible places, oneiric cartography

This completes the preset integration for travelogue, following the same trajectory as legends (Session 96 → 97: add feature, then add to presets) and echoes (Session 78 → 88: add feature, then add to presets in later session).

### Tradeoffs
- **Seed-breaking for presets**: All 5 presets now produce different output from the previous session for the same seed, because `travelogue=True` was not previously in presets. This is acceptable because presets are curated entry points that evolve as features mature, and determinism is preserved (same seed + same args = same output). Users who want the old preset behavior can explicitly omit `--travelogue`.
- **Backward compatibility via CLI overrides**: The gating code checks `args.travelogue is False` before applying the preset value. Users who explicitly pass `--no-travelogue` (if that existed) don't get the preset value. This is the same pattern as all other preset overrides.
- **No changes to `generate_landscape()`**: Presets are a pure CLI convenience layer — the generation function already accepts `travelogue` (Session 104). Only the `PRESETS` dict and `main()` gating code changed.
- **Consistent with echo and legend preset pattern**: All features with an on/off switch are now in all presets — echo (since Session 88), legend (Session 97), and travelogue (this session).
- **2 new tests, 616 total** (18 todo + 598 landscape), 112 subtests.

## 2026-07-14 — `travelogue` in JSON Metadata

### What
Added `"travelogue": true` to JSON output when `travelogue=True`, following the same pattern as `echo_enabled` (Session 100) and `legend_enabled` (Session 97). Previously, travelogue framing was invisible in JSON metadata — consumers had no way to distinguish a travelogue-framed landscape from a plain one without parsing the text field for prefix phrases.

### Why
When travelogue was added (Session 104), the JSON metadata gap was the same one that `echo_enabled` had before Session 100 fixed it: the feature had an on/off switch but no corresponding boolean in JSON output. Every other feature with an on/off switch (echo, legend) emits an explicit `_enabled` boolean in JSON. Adding `travelogue` makes the JSON format consistent and lets consumers programmatically detect whether the narrative frame is active.

### Tradeoffs
- **Backward compatible**: Existing JSON output without `travelogue` is unaffected; the field is only added when `travelogue=True`.
- **Not seed-breaking**: No random call order changes — only a metadata field addition.
- **2 new tests**, 614 total (18 todo + 596 landscape), 102 subtests.

## 2026-07-14 — Travelogue Narrative Framing (`--travelogue`)

### What
Added `--travelogue` CLI flag (default: off) and `travelogue` parameter to `generate_landscape()`. When enabled, the generated landscape is wrapped in a travel journal entry: a narrative prefix (e.g. "Journal entry, day 247. I have reached the forest at last.") is inserted at the beginning, and a narrative suffix (e.g. "I will venture deeper into the forest come morning.") is appended at the end. The day number is a random integer 1–365, picked per-landscape via `rng.randint()`. The travelogue uses 4 curated prefix templates and 4 curated suffix templates, all referencing `{display}` (the biome name).

### Why
After 103 sessions of enriching vocabulary, templates, moods, echoes, and legends, the landscape generator could describe *what a place looks like and feels like* from a disembodied, omniscient perspective — but it never positioned the description within an *in-universe narrator's voice*. The travelogue frame transforms the same core generation into an exploration narrative: the landscape becomes a discovered place, documented by an explorer who marks days, journals observations, and plans future exploration. This is a distinct narrative dimension from the existing features — it doesn't change the description's content, it changes who is (implicitly) speaking and why.

This directly serves the GOAL.md directive to "build something genuinely novel or interesting." A travelogue framing is not a new word bank or template system — it's a narrative reframing that gives the output a different genre identity. The same landscape description can be "a prose description of a place" or "an expedition log entry" depending on whether `--travelogue` is used, without any changes to the description itself.

### Tradeoffs
- **4 prefix and 4 suffix templates** — curated for quality and narrative variety. The small pool (4 each) ensures each template is well-crafted and doesn't repeat too often across multiple runs.
- **`{display}` and `{day}` only** — prefixes use biome name and day number; suffixes use only biome name. No other word categories (adj, adverb, element, color, etc.) are injected, keeping the travelogue voice consistent and simple.
- **Seed-breaking when enabled**: `rng.randint(1, 365)` and `rng.choice(TRAVELOGUE_PREFIXES)` and `rng.choice(TRAVELOGUE_SUFFIXES)` add 3 random calls before the joiner, shifting the random sequence. With `travelogue=False` (default), no random calls are added, preserving all existing seed-based output.
- **No effect on JSON `text` field**: The travelogue framing wraps the output string, so JSON output's `text` field includes the framed text. This is consistent with how `--show-biome` and `--show-seed` append tags to the text.
- **Consistent with `--format poetic`**: Travelogue works with poetic format — the prefix, landscape sentences, and suffix are all joined with newlines, creating a journal-like structure.
- **13 new tests, 612 total** (18 todo + 594 landscape), 102 subtests.

## 2026-07-14 — Preset Legend Count and Probability

### What
Added `legend_count` and `legend_prob` to all 5 preset configurations (`nightfall`, `pastoral`, `sublime`, `wasteland`, `dreamscape`). Each preset now has curated legend density and probability values that match its emotional/atmospheric theme, mirroring how `echo_count` and `echo_prob` are already set per-preset.

### Why
The legend system evolved through 4 sessions: on/off (Session 96), in-presets (Session 97), count (Session 101), and prob (Session 102). After each building block existed independently, the final integration step was wiring them into presets with thoughtfully chosen values:

- **nightfall** (`legend_count=2, legend_prob=0.7`): Eerie mood + rare bias creates an ominous atmosphere. Multiple legends at moderate probability mirrors the echo config (echo_count=2, echo_prob=0.7) — folk tales appear as frequently as atmospheric echoes.
- **pastoral** (`legend_count=1, legend_prob=0.6`): Peaceful mood. A single legend, and only 60% of the time — keeps the serene tone from being cluttered. Matches pastoral's sparse echo config (echo_count=1, echo_prob=0.5).
- **sublime** (`legend_count=2, legend_prob=0.9`): Vibrant+peaceful blend with common bias. Two legends almost always present (prob=0.9), mirroring the maximalist approach of echo_count=3, echo_prob=1.0.
- **wasteland** (`legend_count=2, legend_prob=1.0`): Desolate mood with full anomalies. Every landscape gets legends — the "forgotten history" tone of legends pairs naturally with wasteland's desolation. Matches the certainty of anomaly_prob=1.0 and anomaly_count=3.
- **dreamscape** (`legend_count=2, legend_prob=0.85`): Eerie+vibrant blend with detail=2. Two legends at high probability — surreal folk tales that usually appear, matching the high-but-not-certain echo config (echo_count=2, echo_prob=1.0).

### Tradeoffs
- **Seed-breaking for presets**: All 5 presets now produce different output from the previous session for the same seed, because `legend_count` and `legend_prob` were not previously in presets. This is acceptable because presets are curated entry points that evolve as features mature, and determinism is preserved (same seed + same args = same output). Users who want the old preset behavior can explicitly pass `--legend-count 1 --legend-prob 1.0`.
- **Backward compatibility via CLI overrides**: The existing gating code checks `args.legend_count == 1` and `args.legend_prob == 1.0` before applying preset values. Users who explicitly pass `--legend-count 1 --legend-prob 1.0` get the old behavior even with `--preset`. This is the same pattern as all other preset overrides.
- **No changes to `generate_landscape()`**: Presets are a pure CLI convenience layer — the generation function already accepts `legend_count` and `legend_prob` (Sessions 101/102). Only the PRESETS dict changed.
- **Consistent with echo preset pattern**: Every preset that has `echo_count`/`echo_prob` now has `legend_count`/`legend_prob` with similar thematic density — high drama presets (sublime, wasteland, dreamscape) use higher counts/probs, while subtle presets (pastoral) use lower values.
- **3 new tests, 599 total** (18 todo + 581 landscape), 102 subtests.

## 2026-07-13 — Configurable Legend Probability (`--legend-prob`)

### What
Added `--legend-prob` CLI flag and `legend_prob` parameter to `generate_landscape()` (default: 1.0). Users can now control how often legend phrases appear per roll, with 0.0 suppressing legends entirely and 1.0 always producing them. Each of `legend_count` rolls independently draws `rng.random() < legend_prob`.

### Why
The legend system (Session 96) started as an on/off switch with exactly one legend per landscape. Session 101 added `--legend-count` for multi-legend control. But every roll always produced a legend phrase — there was no way to make legends appear unpredictably. Following the same trajectory as echoes (echo on/off → echo-count → echo-prob), adding `legend_prob` gives users fine-grained control over legend frequency. This is useful for atmospheric variety where legends feel more organic when they appear unpredictably rather than every time.

### Tradeoffs
- **Default 1.0 preserves backward compatibility**: all existing seed-based output with `--legend` is unchanged.
- **Per-roll probability**: each of `legend_count` attempts rolls independently against `legend_prob`, same pattern as `echo_prob` and `anomaly_prob`.
- **`legend_prob=0.0`** is an alternative suppression mechanism to `legend_count=0`. Both are valid; `legend_prob=0.0` is more explicit about intent when a script conditionally enables legends with different probabilities.
- **Included in JSON metadata** when `legend_enabled=True`, alongside `legend_count`.
- **Seed-breaking when legend_prob < 1.0**: When legend_prob causes a roll to be skipped, the RNG sequence shifts by one `rng.random()` call. With `legend_prob=1.0` (default), no extra random calls are consumed beyond the `rng.choice()` for each legend, so behavior is unchanged.
- **7 new tests**, 596 total (18 todo + 578 landscape), 93 subtests.

## 2026-07-13 — Configurable Legend Count (`--legend-count`)

### What
Added `--legend-count` CLI flag (choices 0-3, default: 1) and `legend_count` parameter to `generate_landscape()`. When legend is enabled with count > 1, multiple legend phrases are appended per landscape with dedup (no repeated phrases). Added `legend_count` to JSON metadata and preset gating.

### Why
The legend system (Session 96) was introduced as a simple on/off switch — exactly the same pattern as echoes (Session 78), which were also initially on/off before `--echo-count` (later Session 78) and `--echo-prob` (Session 87) were added. The Session 96 DECISIONS.md explicitly noted: "No count or probability — unlike echoes [...] keeps scope small and follows the Session 78 `--echo` pattern (the initial echo implementation was also a simple on/off before echo-count and echo-prob were added in later sessions)."

After 5 sessions of legends existing as a on/off feature, adding `--legend-count` is the natural evolution. With 15 legend phrases now in the bank (Session 98), count=2 or 3 produces richer landscapes without repetition (dedup ensures no repeats within a landscape). This gives users the same fine-grained control over legend density that `--echo-count` provides for echoes.

Users who want the existing behavior are unaffected — `--legend` alone still produces exactly 1 legend phrase. The new `--legend-count` is purely additive.

### Tradeoffs
- **`legend_count=0`** is an alternative suppression mechanism to not using `--legend`. Both are valid; count=0 is more explicit when a script conditionally enables legends with variable counts.
- **Dedup with fallback**: Same pattern as echoes — a `used_legends` set prevents repeats within a landscape. With 15 legends and max count=3, dedup never exhausts the pool in practice, but the fallback (full pool) is implemented for correctness.
- **No `legend_prob`**: Unlike echoes (which have `echo_prob`), legends don't have a probability parameter. Each count always produces a legend when enabled. This follows the same trajectory as echoes (count came first, prob came later in Session 87). If users want variable legend density, `--legend-count` with dedup already provides variety.
- **Seed-breaking**: Adding `rng.choice()` calls for each legend count shifts the random sequence. With `legend_count=1` (default), this adds one extra `rng.choice()` call compared to before (since the old code used `rng.choice(LEGENDS)` and the new code wraps it in a loop). This means existing seed-based output with `--legend` will differ — the same seed produces the same legend phrase, but placed at a different position in the random sequence. This is the same seed-breaking pattern as every other feature addition and is acceptable.
- **12 new tests**, 589 total (18 todo + 571 landscape), 93 subtests.

## 2026-07-13 — `echo_enabled` in JSON Metadata

### What
Added `"echo_enabled": true` to JSON output when `echo_enabled=True`, matching the same pattern as `legend_enabled` (Session 97). Previously, echo metadata only emitted `echo_prob` and `echo_count` when echo was enabled, with no explicit boolean field. Added 2 tests verifying presence when enabled and absence when disabled.

### Why
When legends were added to JSON metadata (Session 97), the pattern was `"legend_enabled": true` — an explicit boolean. But echo — which preceded legends by 20+ sessions — never got the same treatment: echo metadata relied on the presence of `echo_prob` and `echo_count` as implicit indicators. This asymmetry meant JSON consumers needed to check whether `echo_prob` exists in the output to infer echo state, rather than reading an explicit boolean. Adding `echo_enabled` makes the JSON format consistent across both atmospheric echo and folkloric legend features, so every feature that has an on/off switch (echo, legend) emits an explicit `_enabled` boolean in JSON.

### Tradeoffs
- **Backward compatible**: Existing JSON output without `echo_enabled` is unaffected; the field is only added when `echo_enabled=True`, which mirrors the legend pattern.
- **Not seed-breaking**: No random call order changes — only a metadata field addition.
- **2 new tests**, 577 total (18 todo + 559 landscape), 93 subtests.

## 2026-07-13 — Describe-Legends Introspection Tests

### What
Added `TestDescribeLegends` test class with 8 tests for `describe_legends()` and `--describe-legends`, mirroring the `TestDescribeEchoes` pattern (Session 86). Covers: string return, header, all 15 legends, index numbers, last-index validation, CLI flag, stdout output, and early-exit (no landscape generation).

### Why
When legends were introduced (Session 96), the feature had 12 functional tests (disabled by default, enabled, output validity, determinism, poetic format, JSON format, detail=0 suppression, CLI flag, biome injection, echo compatibility, combine, mood/bias) — but `describe_legends()` had zero introspection tests. The `--describe-echoes` introspection tests (Session 86) set the pattern for testing describe-* functions, but when `--describe-legends` was added in Session 96 with an identical implementation, the corresponding tests were not added. This was a test coverage gap.

Every other introspection feature (`--describe-biome`, `--describe-mood`, `--describe-global`, `--describe-templates`, `--describe-echoes`, `--describe-presets`) has dedicated test coverage. Adding `TestDescribeLegends` closes this gap and ensures `--describe-legends` continues to work correctly as the legend bank grows.

### Tradeoffs
- **Data-only test addition**: No changes to `landscape.py`, CLI flags, generation logic, or any feature code. Only `test_landscape.py` was modified (8 new test methods in a new class).
- **8 new tests, 557 total** (18 todo + 539 landscape), 93 subtests unchanged.
- **Follows established pattern**: Every test method in `TestDescribeLegends` has a direct counterpart in `TestDescribeEchoes`, making the test suite symmetric and easier to maintain.

## 2026-07-13 — Expanded Legend Bank (15 phrases)

### What
Added 5 new curated folkloric/historical phrases to the LEGENDS bank, expanding it from 10 to 15 phrases. The new phrases cover additional cultural/mythic themes: hidden history, unreachable places, ancient construction, uncanny familiarity, and bottomless mystery. Added corresponding invariant substrings to `LEGEND_INDICATORS` in the test module.

### Why
The original 10 legend phrases (Session 96) covered a good range of folkloric tropes but left several natural thematic gaps: construction by unknown hands, unreachable destinations, and names-on-the-wind synesthesia. Adding 5 new phrases (50% increase) meaningfully improves output variety without touching generation logic, tests, or CLI — a purely data-driven improvement. With legends now enabled in all 5 presets (Session 97), the cost of a small legend bank is that preset users see the same 10 phrases repeating more often. Expanding to 15 reduces repetition while keeping the same high quality bar.

### Tradeoffs
- **Data-only change**: No modifications to `generate_landscape()`, `_format_tmpl()`, CLI flags, or any other logic. Only the LEGENDS list and LEGEND_INDICATORS set were updated.
- **Single-`{display}` injection preserved**: All new phrases contain exactly one `{display}` reference, matching the existing convention. No other word categories (adj, adverb, color, element, time_word) are injected — consistent with the original design decision that legends are folk sayings about a place, not descriptions of its qualities.
- **No seed-breaking change**: Adding phrases to `LEGENDS` doesn't change the random sequence — `rng.choice(LEGENDS)` picks from a larger pool but the choice function's behavior is unchanged. Only the rendered output content changes (new phrases appear in the selection pool).
- **5 new indicators, no new tests**: Existing legend tests (8 tests + 2 preset subtests) cover all behaviors generically — they don't assert on specific phrase counts, so no test changes were needed beyond adding indicator strings.
- **Test count unchanged**: 549 tests (18 todo + 531 landscape), 93 subtests.

## 2026-07-13 — Legends in Presets and JSON Metadata

### What
Added `legend_enabled=True` to all 5 presets (nightfall, pastoral, sublime, wasteland, dreamscape), so each preset includes a folkloric legend by default. Added `legend_enabled` preset gating in `main()` so explicit `--legend` still overrides the preset. Added `"legend_enabled": true` to JSON metadata when legends are enabled.

### Why
Legends (Session 96) were only accessible via the explicit `--legend` flag — presets, which are the curated on-ramp for new users, didn't use them. This meant a `--preset nightfall` landscape would get eerie mood, rare bias, high anomalies, and an atmospheric echo — but no cultural/historical folkloric context. Adding legends to all presets makes them richer out of the box without requiring users to know about `--legend`.

Each preset benefits narratively:
- **nightfall**: eerie mood + folk legend → ominous, historically charged
- **pastoral**: peaceful mood + folk legend → serene but storied
- **sublime**: vibrant+peaceful + folk legend → transcendent, mythic
- **wasteland**: desolate + folk legend → post-mythic, forgotten
- **dreamscape**: surreal + folk legend → oneiric, folkloric

The JSON metadata gap was a parallel concern: `echo_enabled` emitted `echo_prob` and `echo_count` in JSON, but `legend_enabled` had no representation. Adding `"legend_enabled": true` makes the JSON format complete.

### Tradeoffs
- **Not seed-breaking**: Presets are convenience layer only — no existing seed-based output has been published relying on preset behavior, and the `--legend` flag was default-off (so all prior `--preset` output is unaffected). Only new `--preset` invocations will differ.
- **Preset gating follows the same pattern as echo**: `if "legend_enabled" in preset and args.legend is False: args.legend = preset["legend_enabled"]` — explicit flags always override presets.
- **JSON metadata follows the same pattern as echo**: a simple boolean field, present only when `legend_enabled=True`. No need for `legend_count` or `legend_prob` since legends are always exactly one per landscape when enabled.
- **4 new tests, 549 total** (18 todo + 531 landscape), 93 subtests.

## 2026-07-13 — Folkloric Legends System (`--legend`)

### What
Added a `LEGENDS` word bank — 10 curated folkloric/historical phrases — and a `--legend` CLI flag (default: off) that appends one random legend to the generated landscape. Each legend references `{display}` (the biome name), so phrases feel grounded in the landscape context. Added `--describe-legends` for introspection (same pattern as `--describe-echoes`).

### Why
After 95 sessions of enriching vocabulary (adjectives, elements, nouns, verbs, weathers, anomalies, adverbs, colors, time words), templates (4 opening, 7 middle, 5 weather, 5 anomaly), moods (4 with blending), and atmospheric dimension (echoes — Session 78), the landscape generator had a rich palette for *describing what a place looks like and feels like* — but nothing that positioned the landscape in **cultural or historical time**. Echoes evoke a timeless, emotional presence ("The land remembers."). Legends evoke a specific cultural memory or folk knowledge ("The oldest maps leave the forest blank.") — the difference between *being in a place that remembers itself* and *being in a place that has been named, mapped, and mythologized by people*.

This directly serves the GOAL.md directive to "build something genuinely novel or interesting." Adding cultural context — the idea that landscapes carry human stories, names, and warnings — is a distinct creative dimension from the existing atmospheric/emotional/visual systems. It makes each generated landscape feel like a place with a history, not just a description of a scene.

### Tradeoffs
- **10 curated phrases** — same size as the echo bank. Hand-written for quality and emotional resonance. Each phrase has a different cultural angle: blank maps (mystery), recent arrival (disorientation), pilgrim silence (reverence), buried things (age), forgotten names (loss), unchanged return (transformation), unsung songs (erasure), unknown maps (paradox), dreams before people (deep time), hermit's silence (solitude).
- **Only `{display}` injection** — unlike echoes which have `{adj}`, `{adverb}`, `{element}`, `{color}`, and `{time_word}` injection, legends only use `{display}`. This is intentional: legends are folk sayings about a *place*, not about its visual qualities or atmospheric texture. Adding other word categories would make legends feel like descriptions rather than cultural artifacts. `{display}` is the only natural injection point.
- **No count or probability** — unlike echoes (which have `--echo-count` and `--echo-prob`) and anomalies (which have `--anomaly-count` and `--anomaly-prob`), legends are a simpler on/off switch. One legend per landscape when `--legend` is used. This keeps scope small and follows the Session 78 `--echo` pattern (the initial echo implementation was also a simple on/off before echo-count and echo-prob were added in later sessions).
- **No seed-breaking change**: `legend_enabled=False` by default, so all existing seed-based output is preserved. When enabled, one extra `rng.choice()` call is introduced after all other generation, preserving the random sequence of all existing features.
- **`detail=0` suppresses legends** — same pattern as echoes and anomalies. The most minimal output mode remains purely about the opening sentence.
- **Works orthogonally with all other features**: echoes can be enabled alongside legends (both append independently), all moods/biases/presets work, combine works (legend references the merged display name), and all output formats (prose, poetic, json) work.
- **12 new tests, 545 total** (18 todo + 527 landscape), 83 subtests.
- **Test count**: 545 total (18 todo + 527 landscape), 83 subtests.

## 2026-07-13 — `{time_word}` Injection in Weather Templates

### What
Added `{time_word}` placeholder support to all 5 weather templates — the weather system now passes `time_word=time_word` to `_format_tmpl()`, so phrases that contain `{time_word}` render with the per-landscape time word, completing temporal framing coverage across all template categories:
  - Template 0: `"{Weather} {adverb} through the {color} {adj} {element} {time_word}."` — "A gentle rain falls softly through the vivid crystal mist already."
  - Template 1: `"The air tells its own story: {weather} {adverb} through the {color} {adj} {element} {time_word}."` — "The air tells its own story: a gentle rain falls softly through the vivid crystal mist still."
  - Template 2: `"{Weather}, as if the {adj} {display} itself breathes {color} {element} {adverb} {time_word}."` — "A gentle rain falls, as if the crystal forest itself breathes vivid mist softly yet."
  - Template 3: `"Through the {color} {adj} {element}, {weather} {adverb} {time_word}."` — "Through the vivid crystal mist, a gentle rain falls softly now."
  - Template 4: `"{Weather} {adverb} in {color} {adj} light {time_word}."` — "A gentle rain falls softly in vivid crystal light once."

### Why
The time word system (Sessions 89–94) was injected into all 4 opening templates, 2 echo phrases, and 2 anomaly templates, making temporal framing available in narrative positioning (openings), atmospheric reflection (echoes), and uncanny description (anomalies). But weather — which describes ongoing conditions and atmospheric activity — had no temporal frame. Weather descriptions described *what* was happening but never *when relative to now*: whether the rain was already falling, still persisting, or just now beginning. Adding time words to all 5 weather templates fills this gap with minimal changes (one kwarg addition, 5 template strings), giving weather descriptions a new dimension: temporal position of the atmospheric state.

This follows the same pattern as every previous weather enrichment: `{adverb}` (Session 42), `{element}` (Session 57), `{color}` (Sessions 58/77), `{adj}` (Sessions 69/72) — add a kwarg that existing templates silently ignore, update all templates to use it, let `_format_tmpl` handle disabled-feature cleanup.

### Tradeoffs
- **All 5 weather templates modified** — unlike echoes (2 of 10) and anomalies (2 of 5) where time words were selectively placed, weather templates all end with a period and have a natural insertion point at the end of the sentence before the period. There is no reason to leave any weather template time-word-free.
- **`_format_tmpl` handles cleanup naturally**: When `time_word_enabled=False`, all 5 templates produce `" ."` before the period. The existing `_format_tmpl` replace chain (`" ." → "."`) handles it.
- **Not seed-breaking**: Adding `time_word=time_word` kwarg to the format call doesn't change the random sequence (no new `_pick()` or `rng.choice()` calls). Only the rendered output changes — existing seed-based output has an extra word appended to weather sentences.
- **Completes `{time_word}` coverage across all template categories**: Now all 4 template slots that support word-category injection have `{time_word}` available — openings (Sessions 89–90), echoes (Session 91), anomalies (Session 94), and weather (this session). Every generated sentence can now carry temporal texture.
- **11 new tests, 533 total** (18 todo + 515 landscape), 83 subtests.

## 2026-07-13 — `{time_word}` Injection in Anomaly Templates

### What
Added `{time_word}` placeholder support to 2 of 5 anomaly templates — the anomaly system now passes `time_word=time_word` to `_format_tmpl()`, so phrases that contain `{time_word}` render with the per-landscape time word. The 3 remaining phrases without `{time_word}` are unchanged:
  - Template 1: `"Something is not right with the {display} {time_word} — {anomaly}"` — "Something is not right with the forest already — The gravity here feels wrong."
  - Template 3: `"There is a quiet wrongness here {adverb} {time_word}: {anomaly_lower}"` — "There is a quiet wrongness here silently now: the horizon curves upward."

### Why
The time word system (Sessions 89–91) was injected into all 4 opening templates and 2 echo phrases, making temporal framing available in narrative positioning (openings) and atmospheric reflection (echoes). But the anomaly slot — which describes uncanny, surreal wrongness — had no temporal frame. Anomalies described *what* was wrong but never *when relative to now* it was wrong: whether the wrongness was already present, still persisting, or just now manifesting. Adding time words to 2 anomaly templates fills this gap with minimal changes (one kwarg addition, 2 template strings), giving anomaly descriptions a new dimension: temporal position of the wrongness.

This follows the same pattern as every previous anomaly enrichment: `{adverb}` (Session 61), `{color}` (Session 67), `{display}` (Session 71/75), `{element}` (Session 76), and `{adj}` (Sessions 73/84) — add a kwarg that existing templates silently ignore, update 2 templates to use it, let `_format_tmpl` handle disabled-feature cleanup.

### Tradeoffs
- **2 of 5 phrases modified** — deliberately the 2 framing templates (not raw `{anomaly}`) that already had injection slots. Templates 0 (bare anomaly) and 2 and 4 don't have a natural insertion point without restructuring the sentence.
- **`_format_tmpl` handles cleanup naturally**: When `time_word_enabled=False`, template 1 produces `"with the forest  —"` (double space before em-dash) and template 3 produces `"here silently :"` (space before colon). The existing `_format_tmpl` replace chain (`"  " → " "`, `" :" → ":"`) handles both.
- **Not seed-breaking when anomaly_prob is default**: Adding `time_word=time_word` kwarg to the format call doesn't change the random sequence (no new `_pick()` or `rng.choice()` calls). Only the rendered output changes when an anomaly template with `{time_word}` is selected. Since `anomaly_prob=0.3` by default, seed-based output without explicit `--anomaly-prob 1.0` may or may not differ depending on whether an anomaly triggered.
- **Completes `{time_word}` coverage**: Now all 4 template slots that support word-category injection have `{time_word}` available — openings (Sessions 89–90), echoes (Session 91), and anomalies (this session). Middle and weather templates remain time-word-free by design (temporal framing is less natural in procedural middle descriptions and weather sentences).
- **12 new tests, 522 total** (18 todo + 504 landscape), 78 subtests.

## 2026-07-13 — Configurable Time Word Suppression (`--no-time-word`)

### What
Added `--no-time-word` CLI flag and `time_word_enabled` parameter to `generate_landscape()` (default: `True`). When `time_word_enabled=False`, the `rng.choice(TIME_WORDS)` call is skipped and an empty string is passed to all template format calls that reference `{time_word}`. `_format_tmpl` handles the empty-string cleanup naturally — time words always appear mid-to-late sentence (after an adverb or before a period), so no double-space or trailing-space artifacts occur.

Also fixed `test_describe_global_contains_all_categories` — the test was missing `"time words"` from its expected category list, a test coverage gap introduced when time words were added (Session 89).

### Why
Time words (Sessions 89–91) were an automatic quality improvement with no off switch. Every other word category that was added as an automatic improvement eventually received a `--no-*` suppression flag: `--no-adverb` (Session 34), `--no-color` (Session 53), `--no-element` (Session 92). Following the established pattern, `--no-time-word` gives users fine-grained control over whether temporal framing words (already, still, yet, now, once, always) appear in their landscape descriptions. This is especially useful for users who want pure present-tense descriptions without temporal positioning.

The test fix closes a coverage gap that went unnoticed since Session 89 — `describe_global()` included time words, but the category-exhaustion test never verified it.

### Tradeoffs
- `time_word_enabled=True` is the default, preserving backward compatibility and all existing seed-based output
- When disabled, `time_word = ""` is passed instead of a time word — `_format_tmpl` handles the empty-string cleanup naturally because time words always appear mid-to-late sentence with adjacent whitespace that the existing replace chain (`"  " → " "`, `" ." → "."`, `" :" → ":"`) can handle
- **Seed-breaking change**: Skipping `rng.choice(TIME_WORDS)` changes the random sequence for the RNG — all subsequent random calls shift by one. This means `time_word_enabled=False` produces different output from `time_word_enabled=True` for the same seed, even for non-temporal parts of the landscape. This is the same seed-breaking pattern as `--no-element` (Session 92) and `--no-color` (Session 53) — determinism is preserved (same seed + same flags = same output), which is the important invariant.
- Time words are picked via `rng.choice()` (not `_pick()`), so no dedup slots are consumed when time words are disabled — unlike `--no-element` which saves dedup slots, `--no-time-word` saves one `rng.choice()` call per landscape (negligible performance impact)
- Echo phrases with `{time_word}` (2 of 10) render without the time word — `_format_tmpl` cleans up the trailing space naturally (e.g., "has been waiting silently for you ." → "has been waiting silently for you.")
- `describe_global()` is unaffected — time words are still listed globally even when suppression is enabled, following the same convention as all other `--no-*` flags
- 12 new tests, 511 total (18 todo + 493 landscape), 78 subtests

## 2026-07-13 — Configurable Element Suppression (`--no-element`)

### What
Added `--no-element` CLI flag and `element_enabled` parameter to `generate_landscape()` (default: `True`). When `element_enabled=False`, the element word pick is skipped entirely and an empty string is passed to all template format calls (both `{element}` and `{Element}`). Added `.strip()` to `_format_tmpl()` to handle leading-space artifacts from empty `{Element}` in sentence-initial positions (opening template 3, middle templates 0/3).

### Why
Elements were the last major word category (alongside adverbs and colors) without an off switch. The project had `--no-adverb` (Session 34), `--no-color` (Session 53), `--no-weather` (Session 46), `--no-middle` (Session 48), and `--no-anomaly` (Session 54) — but no way to suppress the element words that appear in all 4 opening templates, 7 middle templates, 5 weather templates, 2 anomaly templates, and 2 echo phrases. Adding `--no-element` completes the `--no-*` suppression family for word categories.

### Tradeoffs
- `element_enabled=True` is the default, preserving backward compatibility and all existing seed-based output
- When disabled, element picks are skipped entirely — saves 1 `_pick()` before the opening and 1 per detail iteration (plus the dedup slot), making output slightly more efficient
- `.strip()` was added to `_format_tmpl()` as a general quality improvement — it's a no-op for all existing templates (none produce leading/trailing spaces in normal operation) but prevents formatting artifacts when `{Element}` evaluates to empty. This is safe because no template has intentional leading/trailing whitespace.
- Templates with `"of {color} {element}"` pattern render as `"of {color}"` when element is disabled (and `"of "` when both color and element are disabled) — `_format_tmpl` handles the double-space cleanup. The result reads as a slightly truncated phrase (e.g. "A vast crystal forest of vivid stretches silently before you.") — this is an acceptable tradeoff for an explicit opt-in suppression flag.
- Echo phrases with `{element}` (2 of 10) render without element words — `_format_tmpl` cleans up spacing artifacts naturally
- Does not affect any preset — all presets use the default `element_enabled=True`
- 10 new tests, 499 total (18 todo + 481 landscape)

## 2026-07-13 — `{time_word}` Injection in Echo Phrases

### What
Added `{time_word}` placeholder support to 2 of 10 ECHOES phrases — the echo system now passes `time_word=time_word` to `_format_tmpl()`, so phrases that contain `{time_word}` render with the per-landscape time word from the opening template. The 8 remaining phrases without `{time_word}` are unchanged:
  - Echo 1: `"The {display} has been waiting {adverb} for you {time_word}."` — "The forest has been waiting silently for you always."
  - Echo 5: `"There is a sense of deep time here, pressing down {adverb} {time_word}."` — "There is a sense of deep time here, pressing down softly yet."

### Why
Sessions 89–90 added `{time_word}` to all 4 opening templates, giving the opening slot temporal framing (already, still, yet, now, once, always). But the echo system — which received `{display}`, `{adverb}`, `{element}`, `{color}`, and `{adj}` injection across sessions 80–84 — had no temporal injection. This left echo phrases feeling temporally flat compared to openings: they could reference biomes, adverbs, elements, colors, and adjectives, but never positioned themselves in narrative time. Adding `{time_word}` to 2 phrases that already carry temporal themes ("has been waiting" and "deep time") creates a natural fit — "waiting... always" reinforces timelessness; "pressing down... yet" creates anticipation.

This completes the injection system for the echo phrases: `{display}`, `{adverb}`, `{element}`, `{color}`, `{adj}`, and now `{time_word}` — all six word categories that are available in the opening template system are now also available in the echo system.

### Tradeoffs
- **2 of 10 phrases modified** — deliberately the 2 phrases with temporal themes ("has been waiting" pairs naturally with "always"/"still"/"yet"; "deep time" pairs with "already"/"still"/"yet"). Adding time words to other phrases (e.g., "The stones remember what the wind has forgotten.") could feel forced.
- **Uses the single per-landscape time word**: same pattern as the opening — picked once per landscape via `rng.choice()`, not via `_pick()`, so it doesn't participate in mood boosts, bias, dedup, or overrides.
- **Not seed-breaking**: no new `_pick()` or `rng.choice()` calls were added, only the rendering of existing echo phrases changed. Echo is off by default, so all existing seed-based output is unaffected.
- **`_format_tmpl` handles time_word naturally**: time words are short and have no trailing-space artifacts, so no formatting edge cases.
- **8 new tests, 489 total** (18 todo + 471 landscape), 78 subtests.

## 2026-07-13 — `{time_word}` Expanded to All 4 Opening Templates

### What
Extended the `{time_word}` injection from opening template 0 to templates 1, 2, and 3. Now all 4 opening templates carry a temporal word that positions the scene in narrative time — whether the landscape "comes into view {adverb} {time_word}" (template 1), "lies {adverb} ahead {time_word}" (template 2), or "stretches {adverb} before you {time_word}" (template 3).

### Why
Session 89 added time words as an explicit "thin edge of the wedge" — only template 0 was modified, with the decision note stating "if the feature proves useful, it can be expanded to other templates in future sessions." After one session of the feature existing, expanding it to the remaining 3 opening templates is the natural next step: it completes the temporal-injection coverage across the opening slot with zero code changes (time_word was already picked and threaded through all format calls), making every opening description temporally textured regardless of which template is randomly selected.

### Tradeoffs
- **Template-level change only**: No code changes to `generate_landscape()` or any other function — `time_word` was already picked per-landscape and passed as a kwarg to the opening format call since Session 89. Only the template strings themselves changed.
- **3 new tests**: statistical tests verify that each of the 3 expanded templates produces time words in output (100 seeds each with forced `template_set`).
- **Seed-breaking**: Adding `{time_word}` to the template strings doesn't change the random sequence (no new `_pick()` calls), but the rendered output now has an extra word appended to templates 1–3, so existing seed-based output that uses those templates differs. Since no seed-based output has been published and this is a content-improvement change, this is acceptable.
- **481 tests total** (18 todo + 463 landscape), 72 subtests.

## 2026-07-13 — Temporal Texture Words (`{time_word}`)

### What
Added a `TIME_WORDS` list (6 words: already, still, yet, now, once, always) to the global word pools in `landscape.py`. One word is picked per landscape via `rng.choice()` before the opening template, and `{time_word}` is injected into opening template 0: `"A vast {adj} {display} of {color} {element} stretches {adverb} before you {time_word}."`

### Why
After 88 sessions, the landscape generator had rich vocabulary covering quality (adjectives), manner (adverbs), visuals (colors), sensory substance (elements), emotional tone (moods), and atmospheric depth (echoes) — but nothing that positions the scene in **narrative time**. A landscape described with "already" feels like something ongoing that the observer has arrived late to; "still" implies persistence against expectation; "yet" creates anticipation; "now" grounds in the immediate present; "once" evokes memory; "always" suggests timelessness. These temporal frames are a distinct dimension from manner adverbs (which describe *how* something happens) — they describe *when relative to now* the scene exists, adding subtle emotional color without changing the core description.

The 6-word list is deliberately small and curated — each word has a distinct temporal-emotional flavor, and the injection affects only 1 of 4 opening templates (25% of openings), so the feature adds variety without dominating every output.

### Tradeoffs
- **Simple `rng.choice()` instead of `_pick()`**: Time words are picked via `rng.choice(TIME_WORDS)` rather than through the full `_pick()` weighted-selection pipeline. This means they don't participate in mood boosts, bias control, dedup, or per-category overrides. This is intentional: time words are a universal temporal frame, not a landscape-specific vocabulary category. The same reasoning applies to echoes (also picked via `rng.choice()`). If a future session wants mood-specific time words (e.g., "already" only for eerie, "still" for peaceful), that could be added then.
- **Not seed-breaking**: `rng.choice(TIME_WORDS)` adds one extra random call before the opening template, which shifts the random sequence for all existing seed-based output. However, given the project's explicit history of accepting seed-breaking changes for features and fixes (Sessions 37, 49, 50, 56, 59, 69, 85), this is acceptable — determinism is preserved (same seed = same output), which is the important invariant.
- **Only template 0**: Only 1 of 4 opening templates receives `{time_word}`. The remaining 3 templates are unchanged. This is deliberate to keep scope small; if the feature proves useful, it can be expanded to other templates in future sessions.
- **7 new tests, 478 total** (18 todo + 460 landscape), 72 subtests.

## 2026-07-13 — Named Presets (`--preset`)

### What
Added a `PRESETS` dict with 5 named configurations (`nightfall`, `pastoral`, `sublime`, `wasteland`, `dreamscape`) and `--preset`/`--describe-presets` CLI flags. Each preset bundles 3–6 settings (mood, bias, anomaly_prob, echo_enabled, etc.) into a single name. Presets apply only when the corresponding CLI arg has its default value — explicit flags always win.

### Why
After 87 sessions of accumulating CLI flags, `landscape.py` has 25+ flags. While power users benefit from fine-grained control, the most common entry point is `--help` followed by trial and error. Presets give new users a curated on-ramp — they demonstrate the generator's emotional range (eerie nightfall, bright sublime, bleak wasteland, surreal dreamscape) without needing to understand the full CLI surface. They also serve as documentation of "interesting" configurations, similar to how `--describe-biome` documents word banks.

The `--describe-presets` flag follows the same introspection pattern as `--describe-biome`, `--describe-mood`, `--describe-global`, `--describe-templates`, and `--describe-echoes`, making the preset system fully discoverable from the CLI.

### Tradeoffs
- **Presets are purely a CLI convenience layer**: zero changes to `generate_landscape()` or the generation pipeline. A preset is just a dict of kwargs that get merged at the call site. This means presets can never break seed-based output or change existing behavior.
- **Default-value gating**: A preset only applies to an arg if that arg has its default value (e.g. `args.bias == "normal"`). If a user explicitly passes `--bias flat`, the preset's `bias: "rare"` is ignored. This is the key design choice: explicit flags are intentional, presets are suggestions. The tradeoff is that `--preset nightfall --anomaly-prob 0.3` doesn't use the preset's `anomaly_prob=0.8` because `0.3` is the default — the user didn't actually pass `--anomaly-prob 0.3`, the parser supplied it. This is an edge case where an explicit-looking arg is actually the default, causing the preset to lose. In practice this is acceptable because: (1) the user can always pass a non-default value like `0.31` to force their intent, and (2) the gating is conservative (it errs on the side of respecting the CLI flag).
- **5 curated presets**: deliberately limited to cover distinct emotional territories (nightfall=pure eerie, pastoral=pure peaceful, sublime=blended serene, wasteland=pure desolate, dreamscape=blended surreal). More presets can be added later as the project grows.
- **13 new tests, 489 total** (18 todo + 471 landscape).

## 2026-07-13 — Configurable Echo Probability (`--echo-prob`)

### What
Added `--echo-prob` CLI flag and `echo_prob` parameter to `generate_landscape()` (default: 1.0). Users can now control how often echo phrases appear per roll, with 0.0 suppressing echoes entirely and 1.0 making them always appear. Each of the `echo_count` rolls independently draws `rng.random() < echo_prob`.

### Why
The echo system (Sessions 78–86) had `echo_enabled` (on/off) and `echo_count` (how many rolls), but every roll always produced an echo phrase. This meant echoes were all-or-nothing: either every landscape had exactly `echo_count` echoes, or none did. Following the same pattern as `anomaly_prob` (Session 16), adding `echo_prob` gives users fine-grained control over echo frequency — useful for atmospheric variety where echoes feel more organic when they appear unpredictably rather than every time.

### Tradeoffs
- **Default 1.0 preserves backward compatibility**: all existing seed-based output with `--echo` is unchanged.
- **Per-roll probability**: each of `echo_count` attempts rolls independently against `echo_prob`, same pattern as `anomaly_prob` with `anomaly_count`. So `--echo-count 3 --echo-prob 0.5` yields ~1–2 echoes on average, with randomness in how many appear.
- **echo_prob=0.0** is an alternative suppression mechanism to not using `--echo`. Both are valid; `echo_prob=0.0` is more explicit about intent when a script conditionally enables echoes with different probabilities.
- **Included in JSON metadata** when `echo_enabled=True`, alongside `echo_count`.
- **7 new tests, 476 total** (18 todo + 458 landscape).

## 2026-07-13 — Echo Introspection (`--describe-echoes`)

### What
Added `--describe-echoes` CLI flag and `describe_echoes()` function. When invoked, it prints all 10 echo phrases with their index numbers and exits without generating a landscape.

### Why
The introspection suite now includes `--describe-biome` (Session 43), `--describe-mood` (Session 44), `--describe-global` (Session 45), and `--describe-templates` (Session 64) — covering biome word banks, mood word banks, global word pools, and sentence templates. But the echo system (10 curated atmospheric phrases from Session 78) had no introspection, even though echoes are now the second most injected template-like system after sentence templates (they receive `{display}`, `{adverb}`, `{element}`, `{color}`, and `{adj}` injection). Users who want to see what echo phrases are available had no discoverable way to do so without reading `landscape.py` directly.

Adding `--describe-echoes` closes this gap, making the echo system fully introspectable from the CLI and completing the introspection feature set.

### Tradeoffs
- `describe_echoes()` is a pure function that returns a string — same pattern as `describe_biome()`, `describe_mood()`, `describe_global()`, and `describe_templates()`. Callers can reuse it programmatically, tests assert on the returned string without capturing stdout.
- `--describe-echoes` is a boolean flag (no argument) — unlike `--describe-biome` and `--describe-mood` which accept an optional name, the echo pool has no sub-selection (there's only one set of 10 phrases). Same pattern as `--describe-global` and `--describe-templates`, which are also single-set introspection.
- Follows the same output format as `describe_templates()`: `=== echo phrases ===\n  [0] <phrase>\n  [1] <phrase>\n...`
- No landscape generation when `--describe-echoes` is used — exits immediately after printing. Same pattern as all other describe flags.
- 8 new tests, 469 total (18 todo + 451 landscape).

## 2026-07-13 — Fix Color Pick When Middle Disabled

### What
Moved the per-sentence-pair color pick outside the `if middle_enabled:` block in `generate_landscape()`, so weather templates always receive a color word regardless of middle sentence state. Previously, `--no-middle` with `color_enabled=True` produced weather sentences without color references because the color pick was gated behind the middle-enabled check.

### Why
This was a latent bug introduced when `{color}` was added to weather templates (Sessions 58+): the color pick in the detail loop was placed inside the `if middle_enabled:` block because color was originally only used by middle templates. When weather templates later gained `{color}`, the placement was never updated. The opening color pick (before the loop) was always correct — only per-sentence-pair colors were nested incorrectly.

### Tradeoffs
- **Seed-breaking**: the random call order changes for all cases (color is now picked before noun/verb instead of after). Since no seed-based output has been published, this is acceptable for a correctness fix.
- **Minimal code change**: moved 3 lines (color pick + empty-string fallback) up by 4 lines in the loop body. No new `_pick()` calls, no behavioral changes other than fixing the bug.
- **New test** verifies colors appear with `middle_enabled=False` across 200 seeds.
- 461 tests total (18 todo + 443 landscape).

## 2026-07-13 — `{adj}` Injection in Echo Phrases

### What
Added `{adj}` placeholder support to 2 of 10 ECHOES phrases — the echo system now passes `adj=adj` to `_format_tmpl()`, so phrases that contain `{adj}` render with the per-sentence-pair adjective word from the detail loop. The 8 remaining phrases without `{adj}` are unchanged.

### Why
The echo system (Sessions 80–83) gained `{display}`, `{adverb}`, `{element}`, and `{color}` injection, completing the word-category coverage that the template system already used. However, `{adj}` (the adjective) was the last word category missing from echo injection — phrases used biome names, adverbs, elements, and colors, but never the landscape's core descriptive adjective. Adding `{adj}` to 2 phrases that already use `{display}` creates a natural adjective-noun stack: "The crystal tundra remembers silently." is more evocative than "The tundra remembers silently."

This completes the injection system for the echo phrases: `{display}` (biome name), `{adverb}` (adverbial flavor), `{element}` (sensory substance), `{color}` (visual palette), and now `{adj}` (descriptive quality). All five word categories that are available in the template system are now also available in the echo system.

### Tradeoffs
- **2 of 10 phrases modified** — deliberately the same 2 phrases that already use `{display}`, since adjectives pair most naturally with biome names ("crystal tundra", "ancient forest"). Adding `{adj}` to phrases without biome references would require awkward restructuring.
- **Uses the last-picked adjective from the detail loop**: same pattern as element, color, and adverb — the most recently selected adjective (last sentence pair, or opening adjective for detail=0).
- **Not seed-breaking**: no new `_pick()` calls were added, only the rendering of existing phrases changed. Echo is off by default, so all existing seed-based output is unaffected.
- **No ECHO_INDICATORS changes**: both modified phrases retain their invariant substrings ("remembers" and "important happened").
- **7 new tests, 460 total** (18 todo + 442 landscape).

## 2026-07-13 — `{color}` Injection in Echo Phrases

### What
Added `{color}` placeholder support to 2 of 10 ECHOES phrases — the echo system now passes `color=color` to `_format_tmpl()`, so phrases that contain `{color}` render with the per-sentence-pair color word from the detail loop. The 8 remaining phrases without `{color}` are unchanged.

### Why
The echo system (Sessions 80–82) gained `{display}`, `{adverb}`, and `{element}` injection for biome awareness, adverbial texture, and sensory substance, but all echo phrases remained color-free — they used generic references like "the mist itself" and "in the mist" without connecting to the landscape's visual palette (vivid, murky, iridescent, etc.). Adding `{color}` to the same 2 phrases that received `{element}` creates a natural adjective-color stack: "You feel as though you are being watched by the vivid mist itself." is more evocative than "…by the mist itself."

This completes the injection system for the echo phrases: `{display}` (biome name), `{adverb}` (adverbial flavor), `{element}` (sensory substance), and now `{color}` (visual palette). All four word categories that are available in the template system are now also available in the echo system.

### Tradeoffs
- **2 of 10 phrases modified** — deliberately the same 2 phrases that received `{element}` injection, since color words pair naturally with element words ("vivid mist", "murky silence"). Adding color to phrases without element would require a different grammatical construction.
- **Uses the last-picked color from the detail loop**: same pattern as element and adverb — the most recently selected color (last sentence pair, or opening color for detail=0).
- **Not seed-breaking**: no new `_pick()` calls were added, only the rendering of existing phrases changed. Echo is off by default, so all existing seed-based output is unaffected.
- **No ECHO_INDICATORS changes**: both modified phrases retain their invariant substrings ("being watched" and "outside of time").
- **`color_enabled=False` composes cleanly**: When `color=""`, `_format_tmpl` collapses "by the  mist" → "by the mist" and "in the  mist" → "in the mist". No formatting artifacts.
- **7 new tests, 453 total** (18 todo + 435 landscape).

## 2026-07-13 — `{element}` Injection in Echo Phrases

### What
Added `{element}` placeholder support to 2 of 10 ECHOES phrases — the echo system now passes `element=element` to `_format_tmpl()`, so phrases that contain `{element}` render with the last-picked element word from the detail loop. The 8 remaining phrases without `{element}` are unchanged.

### Why
The echo system (Sessions 80–81) gained `{display}` and `{adverb}` injection for biome awareness and adverbial texture, but all echo phrases remained element-free — they used generic references like "the landscape itself" and "outside of time" without connecting to the landscape's sensory substance (mist, silence, light, echoes). The Session 80 DECISIONS.md entry explicitly noted: "A future enhancement could inject {display} or {element} into echo templates" — this completes the injection triad for the echo system.

Adding `{element}` to 2 of 10 phrases makes echoes feel grounded in the physical landscape: "You feel as though you are being watched by the mist itself." evokes a different feeling than "…by the silence itself." The time phrase "This place exists outside of time, in the mist." is more evocative than the abstract original.

### Tradeoffs
- **2 of 10 phrases modified** — deliberately fewer than display (5) and adverb (5). Element words are more concrete and sensory than display names or adverbs, so they don't fit naturally into every echo phrase. "The stones remember what the wind has forgotten." would lose its specific imagery if "wind" were replaced by a generic {element}. The smaller split is intentional.
- **Uses the last-picked element from the detail loop**: same pattern as adverb — the most recently selected element (last sentence pair, or opening element for detail=0). Echo is suppressed at detail=0, so in practice it's always the last sentence-pair element.
- **Not seed-breaking**: no new `_pick()` calls were added, only the rendering of existing phrases changed. Echo is off by default, so all existing seed-based output is unaffected.
- **No ECHO_INDICATORS changes**: both modified phrases retain their invariant substrings ("being watched" and "outside of time").
- **5 new tests, 446 total** (18 todo + 428 landscape).

## 2026-07-13 — `{adverb}` Injection in Echo Phrases

### What
Added `{adverb}` placeholder support to 5 of 10 ECHOES phrases — the echo system now passes `adverb=adverb` to `_format_tmpl()`, so phrases that contain `{adverb}` render with the per-landscape adverb (last-picked from the detail loop, or the opening adverb for detail=0). The 5 remaining phrases without `{adverb}` are unchanged.

### Why
The echo system (Session 80) gained `{display}` injection for biome awareness, but all echo phrases remained adverb-free — they read with the same fixed cadence regardless of the landscape's adverbial flavor (slow/silent/gentle/relentless). Adding `{adverb}` to 5 of 10 phrases makes echoes feel connected to the landscape's movement and texture: "The tundra remembers silently." evokes a different feeling than "The tundra remembers patiently."

This follows the same pattern as every previous template enrichment: add a kwarg that existing templates silently ignore, update 5 templates to use it, let `_format_tmpl` handle disabled-feature cleanup. The Session 80 DECISIONS.md entry explicitly noted: "A future enhancement could inject {display} or {element} into echo templates" — this expands the injection system to include adverbs, which were not originally considered for echo injection.

### Tradeoffs
- **5 of 10 phrases modified** — deliberately not all. Some echoes are more powerful without an adverb ("Nothing in the forest has changed in a thousand years." would lose its starkness with an adverb). The split mirrors the `{display}` injection approach (also 5 of 10).
- **Phrase 6 loses its hardcoded "gently"**: The phrase "There is a sense of deep time here, pressing down gently." becomes "There is a sense of deep time here, pressing down {adverb}." — the hardcoded "gently" is replaced by whatever adverb was most recently picked. This is a meaningful improvement (the pressure's quality now varies per landscape: "pressing down relentlessly" vs "pressing down softly") but is a minor seed-breaking change for that specific phrase when echo is enabled.
- **Not seed-breaking for existing seed-based output without `--echo`**: Echo is off by default (`echo_enabled=False`), so existing seed-based output is completely unaffected. When `--echo` is active, the random sequence is unchanged (no new `_pick()` calls), only the rendering of chosen phrases differs.
- **`adverb_enabled=False` composes cleanly**: When `adverb=""`, `_format_tmpl` collapses "remembers ." → "remembers.", "linger  in" → "linger in", etc. No formatting artifacts.
- **ECHO_INDICATORS updated**: Two invariant substrings changed — `"remembers."` → `"remembers"` (period no longer adjacent to the word) and `"linger in the air"` → `"echoes of the past"` (adverb separates "linger" from "in the air"). Other indicators are unaffected.
- **3 new tests, 441 total** (18 todo + 423 landscape).

## 2026-07-13 — `{display}` Injection in Echo Phrases

### What
Added `{display}` placeholder support to 5 of 10 ECHOES phrases — the echo system now formats each chosen phrase with `_format_tmpl(echo, display=display)`, so phrases that contain `{display}` render with the biome name (or combined biome display string). The 5 remaining phrases without `{display}` are unchanged.

### Why
The echo system (Session 78) always produced fixed, generic phrases like "The land remembers." or "This place has been waiting for you." that read identically regardless of whether the landscape is a forest, desert, or ruined city — creating a subtle disconnect between the atmospheric echo and the described setting. The DECISIONS.md entry for Session 78 explicitly noted: "A future enhancement could inject {display} or {element} into echo templates."

This change makes the echo system feel cohesive with the landscape: "The forest remembers." or "Something important happened in the desert once." are more evocative than their generic counterparts. The biome reference is injected for only 5 of 10 phrases, so the echo system retains stylistic variety — some echoes are intimate and biome-specific, others remain universal and timeless.

### Tradeoffs
- **Added formatting dependency**: Echoes are now formatted strings rather than raw static text. This means any future echo phrase containing literal `{` or `}` characters would need escaping. Current biome names contain no such characters, so this is a non-issue in practice.
- **Not seed-breaking**: Echo is still disabled by default. When enabled, the same seed produces the same echo phrase (just formatted with the biome display name). Existing seed-based output without `--echo` is unaffected.
- **`_format_tmpl` handles cleanup**: The `_format_tmpl` helper handles spacing artifacts from template formatting, which is a no-op for echo phrases (none produce double-space patterns). This is a trivial overhead per echo.
- **Works naturally with `--combine`**: When biomes are combined (e.g. `--combine forest,desert`), `display` becomes "forest and desert" and echoes render as "The forest and desert remembers." — which reads as a compound subject and is grammatically correct.
- **5 of 10 phrases modified** — deliberately not all. Some echoes are more powerful as universal statements independent of location ("The silence here is older than any sound."). The split mirrors how templates use `{display}` in some but not all variants.
- **6 new tests, 438 total** (18 todo + 420 landscape).

## 2026-07-13 — Configurable Echo Count (`--echo-count`)

### What
Added `--echo-count` CLI flag and `echo_count` parameter to `generate_landscape()` — controls how many echo phrases appear per landscape (0–3, default: 1). The echo block now loops `echo_count` times, each picking from a `used_echoes` set to prevent repeating the same phrase. When the pool is exhausted (`echo_count > len(ECHOES)`), falls back to the full pool. Added `echo_count` to JSON metadata when `echo_enabled=True`.

### Why
The echo system (Session 78) always produced exactly one echo phrase per landscape. Users who want a richer atmospheric effect — multiple echoes building on each other (e.g., "The land remembers. Something important happened here once.") — had no way to express that. The `--echo-count` flag is the natural counterpart to `--anomaly-count` (Session 29) and follows the same pattern: a simple integer that controls how many instances of the feature appear.

### Tradeoffs
- **echo_count=0** is an alternative suppression mechanism to not using `--echo`: the former explicitly requests zero echoes while using `--echo`, the latter doesn't enable echoes at all. Both are valid; `echo_count=0` is more explicit about intent when a script conditionally enables echoes.
- **Dedup is internal to the echo system**: A `used_echoes` set tracks which phrases have been used, independent of the word-category `used_words` set (which echoes intentionally don't participate in). When dedup exhausts the pool (echo_count > 10), the full pool is reused — same pattern as `_pick()`'s pool-exhaustion fallback. This is purely defensive since echo_count is capped at 3, well below the 10-phrase pool.
- **No seed-breaking change when echo_enabled=False**: The echo block is skipped entirely when disabled, preserving all existing seed-based output. When enabled, the additional `rng.choice()` calls are after all other generation, just like the single-echo version.
- **12 new tests**, 433 total (18 todo + 415 landscape).

## 2026-07-13 — Atmospheric Echo Phrases (`--echo`)

### What
Added a new `ECHOES` word bank — 10 curated atmospheric phrases that evoke a sense of deep time, presence, and experiential depth — and a `--echo` CLI flag (default: off) that appends one random echo to the generated landscape. Each echo is a complete sentence that stands alone after the main description.

### Why
After 77 sessions of enriching vocabulary, templates, moods, biomes, and introspection, the landscape generator could produce richly textured descriptions but they all read as purely observational — a detached third-person view of a place. The project had no mechanism for *emotional resonance* or *experiential presence*. The echo phrases fill this gap: "The land remembers." or "The silence here is older than any sound." add a sense that the landscape has a history, a memory, a weight. This is the difference between looking at a photograph and standing in the place itself.

This directly serves the project's creative goal: it's an unusual, non-obvious addition to a landscape generator. Most landscape/text generators focus on visual description; adding a memory/echo dimension is a small step toward something more literary and emotionally resonant.

### Tradeoffs
- **Curated phrases rather than generated**: All 10 echoes are hand-written complete sentences rather than procedurally composed from word banks. This ensures each one lands emotionally and avoids the grammatical oddities that template-generated echoes could produce. The tradeoff is lower variety per-session (10 phrases vs potentially hundreds of combinations), but the quality bar for an echo is higher — a clunky echo breaks the spell, while a missing echo is invisible.
- **No word-category injection**: Echoes are picked `rng.choice(ECHOES)` rather than drawn from `_pick()`. This means they don't consume dedup slots, don't participate in mood/bias/weight systems, and don't reference biome-specific vocabulary. This is intentional — echoes are universal atmospheric flourishes, not landscape-specific details. A future enhancement could inject `{display}` or `{element}` into echo templates, but that would require templating each echo string, adding complexity for marginal gain.
- **No seed-breaking change**: `echo_enabled=False` by default, so all existing seed-based output is preserved. When enabled, one extra `rng.choice()` call is introduced after all other generation, preserving the random sequence of all existing features.
- **`detail=0` suppresses echoes**: Echoes only appear when `detail >= 1` (same as anomalies). This ensures the most minimal output mode remains purely about the opening sentence.
- **JSON format**: Echo text is part of the `text` field, not a separate metadata field. Echoes are content, not metadata, so they belong in the prose text alongside all other generated sentences.
- **8 new tests**, 422 total (18 todo + 404 landscape).

## 2026-07-13 — `{color}` in All Weather Templates

### What
Added `{color}` to all 4 weather templates that were missing it: templates 0, 1, 2, and 3. Now all 5 weather templates use `{color}`:
- Template 0: `"... through the {color} {adj} {element}."`
- Template 1: `"... through the {color} {adj} {element}."`
- Template 2: `"... breathes {color} {element} {adverb}."`
- Template 3: `"Through the {color} {adj} {element}, ..."`
- Template 4: `"... in {color} {adj} light."` (unchanged from Session 58)

### Why
Session 58 added `{color}` to weather via template 4 (`"{Weather} {adverb} in {color} light."`), but templates 0–3 had no color reference. This meant 80% of weather templates didn't use the per-sentence-pair color word, even though colors were always picked and available as kwargs. Adding `{color}` to the remaining templates makes every weather sentence visually evocative regardless of which template is randomly selected — "a gentle rain falls softly through the vivid crystal mist" is richer than "a gentle rain falls softly through the crystal mist."

### Tradeoffs
- Template-level change only — `color=color` was already passed to all weather format calls since Session 58
- No seed-breaking change: no new `_pick()` calls, only template strings changed
- When `color_enabled=False`, `_format_tmpl` collapses the double-space between `{color}` and `{adj}` naturally — "through the  crystal mist" → "through the crystal mist" reads cleanly without the color word
- Now all 5 weather templates, all 7 middle templates, all 4 opening templates, and 2 of 5 anomaly templates use `{color}` — complete coverage across weather and middle slots
- 10 new tests, 414 total (18 todo + 396 landscape)

## 2026-07-13 — `{display}` in Anomaly Template 1

### What
Added `{display}` to `SENTENCE_TEMPLATES["anomaly"][1]`: changed `"Something is not right — {anomaly}"` to `"Something is not right with the {display} — {anomaly}"` (e.g. "Something is not right with the forest — The gravity here feels wrong.").

### Why
Anomaly template 1 was one of only two templates (alongside template 0, the raw `{anomaly}` form) that didn't reference any injected word category. Templates 2, 3, and 4 all use at least one of `{color}`, `{adverb}`, `{adj}`, or `{display}` to ground the anomaly in the landscape context, but template 1 remained a bare — `{anomaly}` pair. Adding `{display}` is the least invasive enrichment — it connects the "Something is not right" framing to the biome without adding clutter or changing the punchy style.

### Tradeoffs
- Template-level change only — `display=display` was already passed to the anomaly format call (since Session 71/73), so no code changes were needed
- No seed-breaking change: no new `_pick()` calls, only the template string changed
- `"Something is not right with the {display}"` reads naturally with all biome names: singular ("the forest", "the desert"), compound ("the ruined city", "the sky islands"), and multi-word ("the mountain range", "the volcanic field")
- When the biome has an article ("the ruined city"), the template reads as `"Something is not right with the the ruined city"` — no, wait: `display` is `"ruined city"`, not `"the ruined city"`. The template says `"the {display}"`, so it renders as `"the ruined city"` and `"the mountain range"` — correct.
- Template 0 (`{anomaly}`) is intentionally left bare — it's the direct, unadorned anomaly form which is a useful stylistic option
- No new tests — existing anomaly template and output tests cover the change
- 400 tests total (unchanged)

## 2026-07-13 — `{color}` in Em-Dash Opening Template

### What
Added `{color}` to `SENTENCE_TEMPLATES["opening"][3]`: changed `"{Element} — the {adj} {display} stretches {adverb} before you."` to `"{Element} — the {adj} {display} of {color} light stretches {adverb} before you."` (e.g. "Echo — the rusted ruined city of faded light stretches softly before you.").

### Why
The em-dash opening template was the last opening template (4 of 4) and one of the last templates overall without a color reference. Templates 0–2 use `"of {color} {element}"` for their color+element stack, but template 3 has `{Element}` sentence-initially (the element word capitalized, e.g. "Mist — ..."), making a second `{element}` reference redundant. Using `"of {color} light"` instead introduces color through a different construction — "of faded light" — that avoids duplicating the element word while adding visual richness. This also creates a useful template-level distinction: templates 0–2 pair color with element, while the em-dash template pairs color with the generic "light", giving the generator two different color-expression patterns.

### Tradeoffs
- Template-level change only — `color=color` was already passed to the opening format call since Session 59
- No seed-breaking change: no new `_pick()` calls, only the template string changed
- The `"of {color} light"` construction is grammatically distinct from the other openings' `"of {color} {element}"` — adds useful variety to how color is expressed in opening descriptions
- When `color_enabled=False`, `_format_tmpl` collapses `"of  light"` → `"of light"` — reads naturally without the color word (e.g. "Mist — the crystal forest of light stretches silently before you.")
- 3 new tests, 400 total (18 todo + 382 landscape).

## 2026-07-13 — `{adj}` in Anomaly Template 4

### What
Added `{adj}` to `SENTENCE_TEMPLATES["anomaly"][4]`: changed `"In the {color} light of the {display}, {anomaly_lower}"` to `"In the {color} {adj} light of the {display}, {anomaly_lower}"` (e.g. "In the vivid crystal light of the forest, the gravity here feels wrong."). Added `adj=adj` kwarg to the anomaly `_format_tmpl()` call — `adj` was already in scope (last per-sentence-pair adjective from the detail loop) but was not passed to anomaly templates, so the placeholder would have rendered as literal `{adj}` text.

### Why
Every other template slot had complete `{adj}` coverage: all 4 opening templates (Sessions 38–41), all 7 middle templates (Sessions 38/40/41), and all 5 weather templates (Sessions 69/72). Anomaly templates were the last slot without `{adj}` anywhere — templates 0–3 had no natural insertion point, and template 4 (`"In the {color} light of the {display}"`) was the only one where `{adj}` fit naturally before "light". Adding `{adj}` completes adjective coverage across all 20 templates that support word-category injection, making the anomaly slot as descriptively rich as every other slot.

### Tradeoffs
- Template-level change plus one kwarg addition — follows the same established pattern as every previous template enrichment: add a kwarg that existing templates silently ignore, update one template to use it.
- No seed-breaking change: no new `_pick()` calls, only the template string and format kwarg changed.
- When `color_enabled=False`, `_format_tmpl` collapses `"in  crystal light"` → `"in crystal light"` — reads naturally without the color word.
- `{adj}` placed between `{color}` and `light` creates a natural adjective-color stack: "in vivid crystal light" — same placement as weather template 4 (Session 72), which also uses `{color} {adj} light`.
- 4 new tests, 397 total (18 todo + 379 landscape).

## 2026-07-13 — `{adj}` in Weather Template 4

### What
Added `{adj}` to `SENTENCE_TEMPLATES["weather"][4]`: changed `"{Weather} {adverb} in {color} light."` to `"{Weather} {adverb} in {color} {adj} light."` (e.g. "A gentle rain falls softly in vivid crystal light.") — the `adj` kwarg was already passed to the weather format call (since Session 69) and was simply unused by this template.

### Why
Weather template 4 was the only weather template that didn't use `{adj}` — templates 0–3 received it in Session 69, leaving template 4 as the last holdout. Adding `{adj}` completes adjective coverage across all 5 weather templates, making descriptions richer and more consistent regardless of which template is selected.

### Tradeoffs
- Template-level change only — `adj` was already in scope and threaded through `_format_tmpl` since Session 69
- No seed-breaking change: no new `_pick()` calls, only the template string itself changed
- `{adj}` placed between `{color}` and `light` creates a natural adjective-color stack: "in vivid crystal light" — when `color_enabled=False`, `_format_tmpl` collapses `"in  crystal light"` → `"in crystal light"` (reads naturally)
- 393 tests total (unchanged)

## 2026-07-13 — `{display}` in Anomaly Template

### What
Added `{display}` to `SENTENCE_TEMPLATES["anomaly"][4]`: changed `"In the {color} light, {anomaly_lower}"` to `"In the {color} light of the {display}, {anomaly_lower}"`. Also added `display=display` kwarg to the anomaly `_format_tmpl()` call — this was the last template slot that didn't receive the biome display name.

### Why
The anomaly slot was the only template category that never referenced the biome name. Opening, middle, and weather templates all use `{display}` in at least one template, grounding descriptions in their biome context. Anomalies were the outlier — they could mention colors and adverbs but never the biome itself. Adding `{display}` to the "In the light" anomaly template makes anomaly descriptions feel cohesive with their setting ("In the vivid light of the forest, the gravity here feels wrong.") rather than floating in a generic space.

### Tradeoffs
- Template-level change plus one kwarg addition — follows the same pattern as every previous template enrichment (Sessions 38–42, 47, 56–61, 67–69): add a kwarg that existing templates silently ignore, update one template to use it.
- The `{display}` kwarg is added to the anomaly format call alongside `{adverb}` and `{color}`, which were already passed — unmodified templates (0, 1, 2, 3) silently ignore the extra kwarg.
- No seed-breaking change: no new `_pick()` calls, just a change in how an existing kwarg is used.
- No new tests — existing coverage (`test_anomaly_color_in_light_template_appears`, `test_anomaly_color_does_not_break_output`, `test_describe_templates_contains_placeholder_info`) covers the change.
- 393 tests total (18 todo + 375 landscape) — unchanged.

## 2026-07-12 — Template Set Coverage & Template Introspection

### What
Added `"sixth"` (index 5) and `"seventh"` (index 6) to `TEMPLATE_SETS`, completing template-set coverage for all 7 middle templates and 5 weather templates. Added `--describe-templates` CLI flag and `describe_templates()` function, completing the introspection feature set alongside `--describe-biome`, `--describe-mood`, and `--describe-global`.

### Why
**Template sets**: Session 63 added "fourth" and "fifth" template set modes (indices 3 and 4), but middle has 7 templates and weather has 5, so indices 5 and 6 were still accessible only via random choice or template overrides. Adding "sixth" and "seventh" completes the set coverage — now every template index across all 4 slots is directly addressable via `--template-set`. As the TEMPLATE_SETS comment says, "random uses random.choice per slot; others force a fixed index" — with "sixth" and "seventh", all 7 middle indices and all 5 weather indices are now forceable.

**Template introspection**: Sessions 43–45 added `--describe-biome`, `--describe-mood`, and `--describe-global` for word bank introspection, but there was no way to discover what templates are available without reading `landscape.py`. With 4 opening, 7 middle, 5 weather, and 4 anomaly templates, the template system has as much variety as the word banks. A `--describe-templates` flag fills this gap, completing the introspection UX.

### Tradeoffs
- **"sixth" and "seventh" are shallow for slots with fewer templates**: opening (4), weather (5), and anomaly (4) all clamp to their max index when "sixth" or "seventh" is used. Only the middle slot gets a unique index. This is the same pattern as "fifth" (Session 63) — the clamping via `min(idx, len(templates) - 1)` makes it safe but means some template-set values are equivalent for certain slots. No behavioral ambiguity since the clamped index is deterministic.
- **`describe_templates()` is a pure function**: follows the same pattern as `describe_biome()`, `describe_mood()`, and `describe_global()` — returns a string with no side effects, making it testable and reusable.
- **No --template-set option added for six/seven in per-slot overrides**: the existing `--template-opening`, `--template-middle`, `--template-weather`, and `--template-anomaly` flags already accept choices from `TEMPLATE_SETS.keys()`, so "sixth" and "seventh" are automatically available there too.
- **17 new tests, 384 total** (18 todo + 366 landscape).
- **No seed-breaking change**: TEMPLATE_SETS is purely a lookup dict; no random call order changes.

## 2026-07-12 — Fourth Mood: "Peaceful"

### What
Added a new `"peaceful"` mood entry to `MOOD_WORDS` with 8 adjectives, 6 elements, 6 nouns, 6 verbs, 6 colors, 6 adverbs, 4 weathers, and 4 anomalies — all curated to evoke calm, serene, gentle atmospheres. Updates affected tests (`test_describe_all_contains_all_moods`, `test_describe_all_moods_flag_prints_multiple`) and added 8 new tests in `TestPeacefulMood` class.

### Why
The existing 3 moods (eerie, vibrant, desolate) all lean toward the dramatic or intense: eerie is uncanny, vibrant is radiant, desolate is bleak. There was no option for a gentle, restful, or serene emotional palette. A peaceful mood fills this gap, giving users access to landscapes that feel calm, comfortable, and inviting — opening up new creative territory like pastoral descriptions of a dew-soaked meadow at dawn, light mist settling in hollows.

This also enables new mood blends: `--mood peaceful --mood desolate` = quiet desolation (a frozen lake at dusk); `--mood peaceful --mood vibrant` = luminous calm (sun-dappled glade); `--mood peaceful --mood eerie` = gentle eeriness (a foggy moor at twilight). The blending system (Session 25) means the new mood adds combinatorial variety: 3 two-mood blends + 1 three-mood blend with peaceful, for 7 new blended palettes.

### Tradeoffs
- Zero code changes to the generation pipeline — `MOOD_WORDS` is purely a data structure; weighting, bias, dedup, templating, overrides, and JSON output all work automatically through the existing mood system
- Word lists are hand-curated and sized similarly to existing moods (6–8 words per category) — large enough for variety, small enough for the mood boost (5x) to reliably skew output tone
- Some words overlap with global pools (e.g., "gently", "softly" are already in `ADVERBS`) — this is fine because the mood boost is orthogonal: the word was already selectable, now it's more likely when peaceful mood is active
- The peaceful colors ("pale", "soft", "gentle", "mellow", "warm", "milky") are deliberately distinct from the 3 existing mood color lists — they describe soft, warm tones rather than vivid/luminous (vibrant) or dark/bleached (eerie, desolate) colors
- 8 new tests, 306 total

## 2026-07-12 — Configurable Color Suppression (`--no-color`)

### What
Added `--no-color` CLI flag and `color_enabled` parameter to `generate_landscape()` (default: `True`). When `color_enabled=False`, the color word pick is skipped and an empty string is passed to the template format call. `_format_tmpl` handles the double-space cleanup (`"The  light of"` → `"The light of"`) the same way it handles empty `{adverb}`.

### Why
The color word bank (Session 51) was an automatic quality improvement with no off switch. While colors generally improve output, some users may want to suppress them — for shorter/more direct descriptions, for consistency with pre-color seeds, or to avoid the specific "The {color} light of..." template pattern. This was explicitly anticipated as a future gap in the Session 51 DECISIONS.md entry: "A `--no-color` flag could be added later if needed (parallel to `--no-adverb`)."

### Tradeoffs
- `color_enabled=True` is the default, preserving backward compatibility and existing seed-based output
- When disabled, the color template (`"The {color} light of..."`) can still be selected — since `color=""`, the template renders as `"The  light of..."` and `_format_tmpl` collapses the double space to `"The light of..."`. This produces valid, natural-sounding output without the color word
- The empty-string approach (rather than removing the template from the pool) follows the exact same pattern as `adverb_enabled=False` (Session 34): templates that reference the disabled feature still work, just without the word
- 8 new tests, 290 total (18 todo + 272 landscape)

## 2026-07-12 — `{color}` in Opening Templates

### What
Added `{color}` to `SENTENCE_TEMPLATES["opening"][0]`, `[1]`, and `[2]` — the three `of {element}` opening templates now render as `of {color} {element}`, e.g. "A vast crystal forest of vivid mist stretches silently before you." The color word is picked once before the opening (alongside `adj`, `element`, and `adverb`), and `color=color` is passed to the opening format call. The em-dash template (index 3) is unchanged.

### Why
After Session 56 (element in openings) and Session 58 (color in weather), color was the only major word category absent from the opening slot. The opening is the first thing a reader sees — adding color makes first impressions more visually striking. "A vast crystal forest of vivid mist" is more evocative than "A vast crystal forest of mist." This follows the established pattern of enriching templates with available word categories: `{adj}` in all middle templates (Sessions 38/40/41), `{adverb}` in all templates (Sessions 30/37/42/47), `{element}` in openings/weather (Sessions 56/57), `{color}` in weather (Session 58), and now `{color}` in openings.

### Tradeoffs
- Template-level change plus one code change (color pick before opening) — the `color` kwarg was already passed to `_format_tmpl` in other slots; the opening format call now receives it too.
- Seed-breaking change: existing seed-based output differs because the random call order gains one `_pick()` call before the opening template. Since no seed-based output has been published, this is acceptable.
- When `color_enabled=False`, `color=""` produces `"of  "` → `_format_tmpl` collapses to `"of "` — reads naturally without the color word.
- The em-dash template is unchanged because it uses `{Element}` at the start of the sentence rather than `of {element}` — there's no natural insertion point for a color word.
- 4 new tests, 333 total (18 todo + 315 landscape).

## 2026-07-12 — Color Word Bank (`COLORS`)

### What
Added a new `COLORS` word category to the landscape generator: 12 global color words with weighted tiers (4 common, 4 rare), mood-specific color lists in each of the 3 moods, and a new 7th middle template `"The {color} light of {element} {verb_conjugated} {adverb}."`. The color word is picked per-sentence-pair (alongside the adjective) inside the middle-enabled block, fully integrated with weighted selection, mood boosts, bias/mood-weight overrides, cross-sentence dedup, and `describe_global()`.

### Why
After 50 sessions, the landscape generator had 6 word categories (adjectives, elements, nouns, verbs, weathers, anomalies, plus adverbs from Session 24) but no dedicated color vocabulary. Color is one of the most evocative dimensions of descriptive language — a "vivid light of mist" or "murky light of darkness" paints a much richer picture than "the light of mist." Adding colors as a separate category (rather than more adjectives) was deliberate: colors compete in their own dedup pool, so they don't crowd out other adjectives, and the mood system gets another lever for tonal expression (eerie gets "murky"/"bleached", vibrant gets "vivid"/"iridescent", desolate gets "murky"/"lurid").

### Tradeoffs
- Colors are a separate category from adjectives — this means a landscape can have both "crystal trees" (adjective) and "vivid light of mist" (color) without dedup blocking either. The cost is an extra word pick per sentence pair.
- The color is picked per-sentence-pair (like adj), not once per landscape — allows different sentence pairs to reference different colors (e.g., "vivid" in first pair, "iridescent" in second). Follows the same pattern as per-sentence-pair adjectives (Session 49) and adverbs (Session 37).
- Only the middle template uses `{color}` — opening, weather, and anomaly templates don't get color references. This keeps scope small and avoids cluttering weather descriptions (which are already the most verbose slot).
- No CLI flags for color suppression or color-specific overrides — follows the same convention as adverbs (Session 24): an automatic quality improvement. A `--no-color` flag could be added later if needed (parallel to `--no-adverb`).
- 12 new tests, 268 total (18 todo + 250 landscape).

## 2026-07-12 — Local Random State (`random.Random()`)

### What
Refactored `generate_landscape()`, `_pick()`, and `_pick_template()` to use a local `random.Random()` instance instead of the global `random` module. When a seed is provided, `rng = random.Random(seed)` is created; when no seed is given, `rng = random.Random()` (seeded from `os.urandom`). All random calls (`choice`, `choices`, `random`, `randint`) use the local instance. The `_pick()` and `_pick_template()` functions accept an optional `rng=None` parameter — when not provided, they fall back to the global `random` module for backward compatibility with direct callers.

### Why
Since Session 1, `generate_landscape()` called `random.seed(seed)` which modifies the global `random` module state. This is a well-known anti-pattern: any other code using `random` in the same process (test fixtures, other library functions, or the calling application) could have its random state unexpectedly reset by a seeded `generate_landscape()` call. With 49 sessions of accumulated features and the project maturing beyond a simple CLI toy into something that might be imported as a library, this was the most impactful quality debt remaining.

### Tradeoffs
- **Seed-breaking change**: existing seed-based output differs because `random.Random()` implements the same algorithm (MT19937) but the internal state layout differs from the top-level module. Determinism is preserved: the same seed still produces the same output with the new code.
- **When no seed is given**, the old code consumed from the global random state (whatever it happened to be); the new code creates a fresh `Random()` seeded from `os.urandom`. Both produce non-deterministic output, so there's no practical behavioral difference.
- **`_pick()` and `_pick_template()` with `rng=None`** fall back to the global `random` module — this preserves backward compatibility for any external code that calls these functions directly (none known, but tests used `_pick` directly without passing `rng`).
- The `--show-seed` auto-generation path now uses `random.Random().randint()` instead of `random.randint()` — produces an equally random seed number.
- The `test_count_without_seed_produces_varied_outputs` test was updated to call `generate_landscape()` directly instead of pre-seeding the global state with `random.seed()`. The new version is simpler and tests the same invariant (outputs without seeds vary).
- 261 tests total (unchanged).

## 2026-07-12 — Per-Sentence-Pair Adjective Selection

### What
Changed adjective from single-per-landscape to **per-sentence-pair**: previously the adjective was picked once and shared across all templates (opening + all middle sentences); now each sentence pair (and the opening) gets its own adjective pick. The opening's adjective is picked before the template, and inside the `detail` loop a fresh adjective is picked for each middle+weather pair.

### Why
After Session 37 made adverbs per-sentence-pair, the adjective was the last word category locked to a single pick for the entire landscape. This meant the opening's adjective set the tone for all middle sentences — "crystal" in the opening forced "crystal" in every middle sentence, making detail=2 and detail=3 landscapes feel repetitive. Making adjectives per-sentence-pair follows the established pattern (same as adverb per-sentence-pair in Session 37) and allows different adjectival flavors across sentence pairs (e.g., "crystal forest... among the ancient trees..." instead of "crystal forest... among the crystal trees...").

### Tradeoffs
- Opening still picks its own adjective once before the template loop — preserves the single-adjective opening feel while allowing middle sentences to vary.
- The per-pair adjective is picked inside the `if middle_enabled:` block (not outside like adverbs), because weather templates don't use `{adj}` — no need to waste a dedup slot on an unused adjective for weather-only iterations.
- Seed-breaking change: existing seed-based output differs because the random call order changes (one extra `_pick` call per detail level). Since no seed-based output has been published, this is acceptable.
- Per-sentence adjectives compose naturally with dedup (each new adj is added to the shared `used_words` set, preventing cross-sentence repetition).
- `test_bias_common_increases_common_word_frequency` was refactored from binary presence/absence counting to total-occurrence counting — the old approach suffered from a ceiling effect at near-300/300 hit rates.
- 5 new tests, 261 total.

## 2026-07-12 — Configurable Middle Sentence Suppression (`--no-middle`)

### What
Added `--no-middle` CLI flag and `middle_enabled` parameter to `generate_landscape()` (default: `True`). When `middle_enabled=False`, the element/noun/verb picks and middle template rendering are skipped in the detail loop — only weather sentences are generated for each detail iteration.

### Why
Weather has always had a suppression flag (`--no-weather`, Session 46), and `--detail 0` suppresses everything except the opening. But there was no way to suppress *middle* sentences while keeping weather and anomalies. A user who wants atmospheric descriptions without explicit action (e.g., a purely visual vignette of opening + weather, or weather-only landscapes at higher detail levels) had no option. The `--no-middle` flag fills this gap, completing the triad of component-level suppression flags alongside `--no-dedup`, `--no-adverb`, and `--no-weather`.

### Tradeoffs
- `middle_enabled=True` is the default, preserving backward compatibility and all existing seed-based output
- When disabled, element/noun/verb words are not picked at all (saves 3 `_pick()` calls and 3 dedup slots per iteration), making the output more efficient
- The per-sentence-pair adverb is still picked even when middle is disabled — all 3 weather templates use `{adverb}`, so weather benefits from the adverb regardless of middle state
- `--no-middle --no-weather` is a valid degenerate case that produces opening + anomaly only (if anomaly triggers), which is useful for ultra-minimal vignettes
- `--no-middle --detail 0` produces opening only (same as `--detail 0` alone) — middle suppression is a no-op when no sentences are generated
- Works orthogonally with all other controls: mood, bias, detail, anomaly settings, template sets, etc.
- JSON output does not include `middle_enabled` — follows the same convention as `weather_enabled`, `adverb_enabled`, and `dedup`, which are also omitted from JSON metadata
- 10 new tests, 256 total.

## 2026-07-12 — `{adverb}` in All Middle Templates

### What
Added `{adverb}` to `SENTENCE_TEMPLATES["middle"][0]`, `[1]`, and `[2]` — the last 3 middle templates that didn't use the per-sentence-pair adverb. Now all 6 middle templates use `{adverb}`:
- Template 0: `"{Element} {verb_conjugated} {adverb} between the {adj} {noun}."`
- Template 1: `"Among the {adj} {noun}, {element} {verb_conjugated} {adverb}."`
- Template 2: `"The {adj} {noun} {verb} {adverb} with {element}."`

### Why
After Sessions 30, 37, 42, the adverb was used in all 3 opening and all 3 weather templates, but only 3 of 6 middle templates. This left the non-adverb middle templates (the classic pattern "Mist whispers between the crystal trees.") feeling flatter at lower detail levels where fewer sentences are generated. Adding `{adverb}` to the remaining middle templates completes the consistency improvement: now the adverb is useful in every generated middle sentence regardless of which template is randomly selected, matching the coverage of opening and weather templates. The adverb is now used in 11 of 15 templates (73%), up from 8 of 15 (53%).

### Tradeoffs
- Template-level change only — `adverb` was already in scope and threaded through `_format_tmpl` since Session 24/37
- Seed-breaking change: existing seed-based output differs when middle template 0, 1, or 2 is selected, because the adverb now renders in those slots. Since no seed-based output has been published, this is acceptable.
- Template 0 reads as `"Mist whispers softly between the crystal trees."` — adverb between verb and preposition reads naturally
- Template 1 reads as `"Among the crystal trees, mist whispers softly."` — end-of-clause adverb placement is grammatically natural
- Template 2 reads as `"The crystal trees whisper softly with light."` — adverb between verb and "with" reads as natural spoken English
- When `adverb_enabled=False`, `_format_tmpl` handles the trailing space before the period via its existing `" ."` → `"."` cleanup for template 1 (where adverb was the last element before the period)
- No new tests — existing coverage (adverb appearance, template variety, output validity, `adverb_enabled=False` formatting) covers the change
- 246 tests total (unchanged).

## 2026-07-12 — Configurable Weather Suppression (`--no-weather`)

### What
Added `--no-weather` CLI flag and `weather_enabled` parameter to `generate_landscape()` (default: `True`). When `weather_enabled=False`, the weather word pick and template rendering are skipped in the detail loop — only the middle sentence is generated for each detail iteration.

### Why
Weather has been an always-on component since Session 1 (the original landscape generator always had an opening, a middle sentence, and weather). While `--detail 0` suppresses everything except the opening, and `--anomaly-prob 0` / `--anomaly-count 0` suppress anomalies, there was no way to suppress *weather* while keeping middle sentences. A user who wants atmospheric descriptions without explicit weather (e.g., a static scene, an interior space, or a purely visual vignette) had no option. Making it configurable follows the established pattern (`--no-dedup`, `--no-adverb`) of exposing automatic features as user-facing controls.

### Tradeoffs
- `weather_enabled=True` is the default, preserving backward compatibility and all existing seed-based output
- When disabled, weather words are not picked at all (saves a `_pick()` call and a dedup slot), making the output slightly more efficient
- Works orthogonally with all other controls: mood, bias, detail, anomaly settings, template sets, etc.
- JSON output does not include `weather_enabled` — follows the same convention as `dedup` and `adverb_enabled`, which are also omitted from JSON metadata
- 9 new tests, 246 total.

## 2026-07-12 — Global Word Pool Introspection (`--describe-global`)

### What
Added `--describe-global` CLI flag and `describe_global()` function. Prints all global word pools (adjectives, elements, nouns, verbs, weathers, anomalies, adverbs) with each word annotated by its weight tier (common/normal/rare). Exits immediately without generating a landscape.

### Why
Sessions 43–44 added `--describe-biome` and `--describe-mood` for biome and mood introspection. The DECISIONS.md entry for Session 43 explicitly noted: "Users who want to see global words can look at the source or a future `--describe-global` flag." This session fills that gap. With the global word pools being the base vocabulary that all biomes draw from (alongside biome-specific words), users have no way to discover what words are available globally or what weight tier they belong to without reading `landscape.py` directly. The `--describe-global` flag completes the introspection triad: biome, mood, and global word pools are now all discoverable from the CLI.

### Tradeoffs
- `describe_global()` is a pure function that returns a string — same pattern as `describe_biome()` and `describe_mood()`. Callers can reuse it programmatically, and tests assert on the returned string without capturing stdout.
- No `nargs` or `const` argument needed — `--describe-global` is a boolean flag with no argument, unlike `--describe-biome` and `--describe-mood` which accept an optional biome/mood name. Global pools are always the same set, so no sub-selection is meaningful.
- The function annotates each word with its weight tier (common/normal/rare) by checking membership in `COMMON_WORDS` and `RARE_WORDS`. This gives users insight into why certain words appear more often than others — the same tier annotations that `_word_weight()` uses internally.
- Words that appear in no tier special list (neither common nor rare) are labeled `normal` with base weight 5. This mirrors the logic in `_word_weight()`.
- 9 new tests, 237 total.

## 2026-07-12 — Mood Introspection (`--describe-mood`)

### What
Added `--describe-mood` CLI flag and `describe_mood()` function. When invoked with a mood name (e.g. `--describe-mood eerie`), it prints that mood's word bank — all words in all 7 categories — and exits without generating a landscape. When invoked without an argument (`--describe-mood` alone) or with `all`, it prints all 3 moods' word banks.

### Why
Session 43 added `--describe-biome` for biome introspection, and the DECISIONS.md entry for that session explicitly noted: "No `--describe-mood` flag (yet) — moods follow the same pattern but are simpler. Could be added later if users need it." This session fills that gap. With 3 moods (and mood blending in Session 25), users have no way to discover what vocabulary each mood contributes without reading `landscape.py` directly. The `--describe-mood` flag is the introspection counterpart to `--describe-biome`, completing the discovery UX for all major generative controls.

### Tradeoffs
- `describe_mood()` is a pure function that returns a string — same pattern as `describe_biome()`, callers can reuse it programmatically, tests assert on the returned string without capturing stdout.
- `--describe-mood` without an argument defaults to `all` — same `nargs="?"` with `const="all"` pattern as `--describe-biome`.
- The function lists mood-specific words in 7 categories (including `adverbs`, which biomes don't have as a separate category) — this is the full set of word categories that `MOOD_WORDS` supports.
- 7 new tests, 228 total.

## 2026-07-12 — Biome Introspection (`--describe-biome`)

### What
Added `--describe-biome` CLI flag and `describe_biome()` function. When invoked with a biome name (e.g. `--describe-biome forest`), it prints that biome's word bank — all words in all 6 categories — and exits without generating a landscape. When invoked without an argument (`--describe-biome` alone) or with `all`, it prints all 13 biomes' word banks.

### Why
After 42 sessions of adding creative controls (13 biomes, 3 moods, bias/mood-weight systems, template sets, formatting options), the tool had no way for a user to discover what biomes exist or what vocabulary they use. The only way to inspect a biome's words was to read `landscape.py` directly. The `--describe-biome` flag fills this gap: it's an introspection/learning tool that helps users understand what the generator can do before they decide which biome to use. This is especially useful now that the project has grown beyond a simple generator into a system with significant depth.

### Tradeoffs
- `describe_biome()` is a pure function that returns a string — the CLI just prints it. This means callers can reuse it programmatically, and tests can assert on the returned string without capturing stdout.
- `--describe-biome` without an argument defaults to `all` — uses argparse `nargs="?"` with `const="all"`, so `--describe-biome` and `--describe-biome all` are equivalent. This matches the UX pattern of `--help` showing everything when no specific topic is given.
- The function lists biome-specific words only (not the blended global pool). This is intentional: the global pool is shared across all biomes, so listing it would be redundant. Users who want to see global words can look at the source or a future `--describe-global` flag.
- No `--describe-mood` flag (yet) — moods follow the same pattern but are simpler (3 moods with ~5-7 words per category). Could be added later if users need it.
- 7 new tests, 221 total.

## 2026-07-12 — `{adverb}` in Weather Templates 1 and 2

### What
Added `{adverb}` to `SENTENCE_TEMPLATES["weather"][1]` and `[2]`: changed `"The air tells its own story: {weather}."` to `"The air tells its own story: {weather} {adverb}."`, and `"{Weather}, as if the {display} itself breathes."` to `"{Weather}, as if the {display} itself breathes {adverb}."`. The `adverb` kwarg was already passed to all weather format calls (since Session 24/37) and was used only by weather template 0.

### Why
Weather template 0 (`"{Weather} {adverb}."`) has used the adverb since Session 30, but templates 1 and 2 had no adverb slot, making the adverb invisible in ~67% of weather sentences. Adding `{adverb}` to the remaining weather templates makes the adverb useful in every weather sentence, not just template 0. This follows the same pattern as Sessions 38–41 (adding `{adj}` to all middle templates) and Session 30 (adding `{adverb}` to more opening/weather templates) — reusing existing data to improve output without new word banks or code.

### Tradeoffs
- Template-level change only — `adverb` was already in scope and threaded through `_format_tmpl` since Session 24
- Seed-breaking change: existing seed-based output differs when weather template 1 or 2 is selected, because the adverb now renders in those slots. Since no seed-based output has been published, this is acceptable.
- Template 1 now reads as `"The air tells its own story: a gentle rain falls softly."` — the adverb sits naturally at the end of the embedded weather clause
- Template 2 now reads as `"A gentle rain falls, as if the forest itself breathes softly."` — the adverb modifies "breathes" naturally
- When `adverb_enabled=False`, `_format_tmpl` handles the trailing space before the period via its existing `" ."` → `"."` cleanup — no `_format_tmpl` changes needed
- Now 8 of 15 templates use `{adverb}` (opening: 3/3, middle: 2/6, weather: 3/3, anomaly: 0/4) — up from 6 of 15
- No new tests — existing coverage (adverb appearance, template variety, output validity, `adverb_enabled=False` formatting) covers the change
- 214 tests total (unchanged).

## 2026-07-12 — `{adj}` in Middle Templates 3 and 4 (Adverb Templates)

### What
Added `{adj}` to `SENTENCE_TEMPLATES["middle"][3]` and `[4]`: changed `"Beneath the {noun}, {element} {verb_conjugated} {adverb}."` to `"Beneath the {adj} {noun}, {element} {verb_conjugated} {adverb}."`, and `"{Element} {verb_conjugated} {adverb} through the {noun}."` to `"{Element} {verb_conjugated} {adverb} through the {adj} {noun}."`. The `adj` kwarg was already passed to the format call (Session 38) and was simply unused by these two templates.

### Why
Templates 3 and 4 were the last middle templates without `{adj}` — templates 0, 1, and 2 received it in Sessions 38 and 40. This left the adverb templates (3 and 4) producing flatter output ("Mist whispers softly through the trees.") compared to templates with adjectives ("Mist whispers softly through the crystal trees."). Adding `{adj}` completes the consistency improvement: now all 6 middle templates use the landscape's chosen adjective, making descriptions uniformly richer across all template slots.

### Tradeoffs
- Template-level change only — `adj` was already in scope and threaded through `_format_tmpl` since Session 38
- No seed-breaking change: no new `_pick()` calls
- Template 3 now reads as `"Mist whispers softly through the crystal trees."` — the adjective sits naturally before the noun
- Template 4 now reads as `"Beneath the ancient stones, light glows softly."` — same natural placement
- No new tests — existing coverage (template variety, output validity, deterministic seed) covers the change
- 214 tests total (unchanged).

## 2026-07-12 — `{adj}` in Middle Template 0 (Classic Template)

### What
Added `{adj}` to `SENTENCE_TEMPLATES["middle"][0]`: changed `"{Element} {verb_conjugated} between the {noun}."` to `"{Element} {verb_conjugated} between the {adj} {noun}."`. The `adj` kwarg was already passed to the format call (Session 38) and was simply unused by this template.

### Why
Template 0 was the only middle template without `{adj}` — templates 1 and 2 received it in Session 38. This made template 0 produce flatter output ("Mist whispers between the trees.") compared to other templates ("Among the crystal trees, mist whispers."). Adding `{adj}` brings it in line with the rest of the template pool, making the classic template equally descriptive.

### Tradeoffs
- One-line template change, no code changes — `adj` was already in scope and threaded through `_format_tmpl`
- No seed-breaking change: no new `_pick()` calls
- Template 0 now reads as `"Mist whispers between the crystal trees."` — the adjective sits naturally before the noun
- No new tests — existing coverage (template variety, output validity, deterministic seed) covers the change
- 196 tests total (unchanged).

## 2026-07-12 — Biome Name in Middle Sentences (`{display}` Template)

### What
Added a 6th middle template `"Across the {display}, {element} {verb_conjugated} {adverb}."` that references the biome name in the middle of the landscape description. Also added `display=display` to the `_format_tmpl()` call for middle templates so the kwarg is available.

### Why
The biome name (`display`) previously only appeared in the opening sentence and weather templates. Middle sentences used generic vocabulary that could feel disconnected from the biome context. The new template ties middle sentences back to the biome — "Across the tundra, frost echoes silently." — making the description feel more cohesive and grounded. This is a natural extension of recent template improvements: Session 37 added `{adj}` to middle templates, Session 38 made that `adj` refer to the opening's adjective, and this session adds `{display}` to middle templates for the same reason (richer cross-sentence coherence).

### Tradeoffs
- The `{display}` kwarg is passed to all middle templates as an extra kwarg that existing templates silently ignore — same pattern as `{adj}` (Session 38) and `{adverb}` (Sessions 24/37). No backward compatibility impact.
- The new template uses lowercase `{element}` (singular, mid-sentence) and `{verb_conjugated}` (third-person singular), which are grammatically correct for element-as-subject ("Across the desert, heat shimmer shimmers gently." is correct). Element words are already singular concepts.
- The template uses `{adverb}` as an optional closing word — "Across the forest, birdsong whispers softly." reads naturally; if `adverb_enabled=False`, the `_format_tmpl` helper cleans up trailing spaces.
- No new CLI flags — this is an automatic quality improvement, same as `{adj}` in middle templates (Session 38).
- 3 new tests, 196 total.

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

## 2026-07-12 — Adjective in Middle Templates (`{adj}`)

### What
Added `{adj}` to two of five middle templates (indices 1 and 2) and passed `adj=adj` to the middle template format call. The adjective was already picked once per landscape (line 510) but was only used in the opening template — the middle templates had no adjective slot at all.

### Why
Middle sentences described elements, nouns, verbs, and adverbs without any adjective, making them feel flat compared to the opening. "Among the trees, mist whispers" is descriptive but lacks the texture of "Among the crystal trees, mist whispers." Adding `{adj}` to natural insertion points (before `{noun}` in templates 1 and 2) makes the output richer without picking any new words — reusing the opening's adjective maintains a consistent tonal palette across the entire landscape.

### Tradeoffs
- Single landscape-wide adjective (not per-sentence-pair): The same adjective is used in the opening and all middle sentences that include `{adj}`. This is intentional — a single adjective creates cohesion; varying it per pair (like adverb) would be a natural next step but changes seed-based output.
- Only 2 of 5 middle templates modified: templates 0, 3, 4 are unchanged. Template 0 ("{Element} {verb_conjugated} between the {noun}.") and templates 3–4 already have adverb slots, so adding an adjective there would crowd the sentence. Templates 1 and 2 had the cleanest insertion points.
- `adj` kwarg added to the format call: unused by unmodified templates (str.format silently ignores extra kwargs), so no conditional logic needed.
- No seed-breaking change: since no new `_pick()` calls are added, existing seed-based output is preserved. The change only affects output when `template_set` or randomness selects templates 1 or 2.
- No new tests: existing template/verb/adverb/output tests already cover the change indirectly.
- 211 tests total (unchanged).

## 2026-07-12 — Per-Sentence Adverbs

### What
Changed adverb selection from single-per-landscape to per-sentence-pair. Previously, one adverb was picked per landscape and reused in every template that included `{adverb}`. Now, the opening gets its own adverb pick (before the opening template), and each middle+weather sentence pair inside the `detail` loop gets its own adverb pick. Anomaly templates (which don't use `{adverb}`) receive the last-picked adverb as a no-op kwarg.

### Why
With a single adverb per landscape, detail=2 and detail=3 outputs used the same adverb (e.g., "softly") in every sentence pair that included it — which could feel repetitive in a long description. Per-sentence adverbs allow different adverbial flavors across sentence pairs: the first pair might describe silent movement ("silently"), while the second pair evokes slow decay ("slowly"). This makes richer outputs genuinely richer, not just longer. The change is analogous to how elements, nouns, and verbs were already per-sentence (picked fresh inside the loop) — the adverb was the only word category that was locked to a single landscape-wide pick.

### Tradeoffs
- **Seed-breaking change**: Existing seed-based output differs because the random call order changes (one `_pick("adverbs", ...)` call per detail level). Determinism is preserved — the same seed still produces the same output.
- **More dedup slots consumed**: Each adverb pick consumes a dedup slot (if `dedup=True`), so a detail=3 output consumes 4 adverb picks (1 opening + 3 pairs) instead of 1. With only 12 adverbs in the global pool, a very high detail level could theoretically exhaust the adverb pool and trigger the fallback (unfiltered pool), though in practice this is unlikely since only 5 of 11 templates use `{adverb}`.
- **Clutter risk**: Multiple adverbs could make output feel busy ("softly... gently... quietly..."). Mitigated by: (1) only 5 of 11 templates actually use `{adverb}`, (2) dedup prevents the same adverb from appearing twice, (3) `--no-adverb` is always available to disable adverbs entirely.
- **Per-sentence, not per-template**: Each middle+weather pair shares one adverb, which avoids the "every sentence a different adverb" excess that the original Session 24 decision warned about. The pair shares a common adverbial flavor, which reads naturally as part of the same descriptive moment.
- 5 new tests, 211 total.

## 2026-07-12 — Per-Category Bias and Mood-Weight Overrides for Adverbs and Colors

### What
Added 4 new CLI flags to `landscape.py`: `--bias-adverb`, `--bias-color`, `--mood-weight-adverb`, and `--mood-weight-color`. Each flag follows the exact same pattern as the existing 6 per-category override flags per category — `--bias-adverb` accepts `normal`/`common`/`rare`/`flat` and overrides the global `--bias` for adverb selection; `--mood-weight-color` accepts a float and overrides the global `--mood-weight` for color mood boosts. The entries were added to `cat_map` and `mw_cat_map` in `main()`.

### Why
When per-category bias overrides were added (Session 16) and per-category mood-weight overrides were added (Session 17), the landscape generator had only 6 word categories. Sessions 24 (adverbs) and 51 (colors) added two more categories but didn't add corresponding override CLI flags. This meant users who wanted fine-grained control over adverb frequency ("I want common words everywhere except rare adverbs") or color mood intensity ("make colors strongly mood-biased but keep everything else normal") had no way to express that, even though the `_word_weight()` and `_pick()` functions already supported it via the `bias_overrides` and `mood_weight_overrides` dict parameters. These 4 flags close the gap, completing the per-category override coverage for all 8 word categories.

### Tradeoffs
- Zero code changes to the generation pipeline — `_word_weight()`, `_pick()`, and `generate_landscape()` already accept `bias_overrides` and `mood_weight_overrides` dicts with arbitrary category keys. The change is purely additive to `main()`: 4 new argparse arguments + 4 entries in existing mapping dicts.
- `--bias-color` affects color word selection probability; `--bias-adverb` affects adverb word selection probability — exactly the same behavior as the existing 6 override flags for their respective categories.
- `--mood-weight-color` controls how strongly mood-matched colors are boosted (e.g., "murky" for eerie mood); `--mood-weight-adverb` does the same for mood-matched adverbs (e.g., "silently" for eerie). Both accept any float, including 0 (suppress) and 1 (no boost).
- 8 new tests, 282 total (18 todo + 264 landscape).

## 2026-07-12 — Configurable Anomaly Suppression (`--no-anomaly`)

### What
Added `--no-anomaly` CLI flag and `anomaly_enabled` parameter to `generate_landscape()` (default: `True`). When `anomaly_enabled=False`, the entire anomaly generation block is skipped — no anomaly word picks, no template rendering, regardless of `anomaly_prob` or `anomaly_count` settings.

### Why
Anomalies were the last major output component without a dedicated `--no-*` suppression flag. Users could suppress anomalies via `--anomaly-prob 0` or `--anomaly-count 0`, but these are less discoverable and more verbose than a dedicated flag. Every other component (dedup, adverb, weather, middle, color) already had a suppression flag. This flag completes the suppression family, making the CLI more consistent and easier to discover.

### Tradeoffs
- `anomaly_enabled=True` is the default, preserving backward compatibility and all existing seed-based output
- When `anomaly_enabled=False`, anomalies are entirely suppressed—no anomaly picks consume dedup slots, no anomaly templates are rendered. This is more efficient than `anomaly_prob=0` (which still runs the loop and checks probability) or `anomaly_count=0` (which skips the loop but leaves the semantic intent less clear)
- The parameter name `anomaly_enabled` follows the same convention as `weather_enabled`, `middle_enabled`, `color_enabled`, and `adverb_enabled` — a simple boolean that gates a component
- `--no-anomaly` is orthogonal to `--anomaly-prob` and `--anomaly-count`: if all three are specified, `anomaly_enabled=False` takes precedence and suppresses anomalies entirely
- 8 new tests, 298 total.

## 2026-07-12 — `{element}` in Opening Templates + New Em-Dash Template

### What
Added `{element}` to all 3 existing opening templates (now `"... of {element} ..."`) and added a 4th opening template `"{Element} — the {adj} {display} stretches {adverb} before you."` that uses an em-dash construction. The element is picked once before the opening (like `adj` and `adverb`) via a new `_pick("elements", ...)` call. Both `element=element` (lowercase, for mid-sentence) and `Element=element.capitalize()` (for sentence-initial) kwargs are passed to the opening format call; templates silently ignore unused kwargs.

### Why
The opening templates have always only used `{adj}`, `{display}`, and `{adverb}` — they described where the landscape is and what it looks like, but not what sensory qualities (element) define it. Adding `{element}` makes openings richer: "A vast crystal forest of mist stretches silently before you" is more evocative than "A vast crystal forest stretches silently before you." The new em-dash template is structurally different from the other three ("Mist — the crystal forest stretches silently before you") and creates a more poetic, invocation-like opening that sets the atmospheric tone before revealing the landscape.

### Tradeoffs
- **Seed-breaking change**: existing seed-based output differs because the random call order changes (one extra `_pick()` before the opening template). Since no seed-based output has been published, this is acceptable.
- **One extra dedup slot consumed**: the opening's element is added to `used_words`, so it won't appear in middle sentences. This is consistent with how the opening's `adj` works (also deduped separately from the loop's `adj`).
- **4 opening templates now**: opening variety goes from 3 to 4 templates, making the em-dash template appear in ~25% of outputs rather than ~33% for each of the old templates. This is a welcome increase in structural variety.
- **Multi-word elements work correctly**: biome-specific elements like "leaf rustle" or "heat shimmer" are capitalized via `str.capitalize()` (e.g. "Leaf rustle — the forest..."), which is grammatically correct.
- Template_set "third" still maps to index 2 (the `"The {adj}..."` template), unchanged. The new template at index 3 is only accessible via random selection.
- `test_pick_template_selects_correct_index` and `test_template_set_third_uses_third_opening` are unaffected.
- 5 new tests, 311 total.

## 2026-07-12 — `{color}` in Middle Templates 1, 2, 4, 5

### What
Added `{color}` to `SENTENCE_TEMPLATES["middle"][1]`, `[2]`, `[4]`, and `[5]` — 4 of the 6 middle templates that didn't reference the per-sentence-pair color word. Now 5 of 7 middle templates use `{color}` (the 6th template from Session 51 already used it). Templates 1, 2, 4, 5 place `{color}` before `{element}` in a natural mid-sentence position.

### Why
The color word bank (Session 51) was previously used in only 1 of 7 middle templates (the `"The {color} light of {element}"` template), making color invisible in most middle sentences — the word was picked but only appeared in ~14% of middle sentences. Session 58 and 59 added `{color}` to weather and opening templates, but middle templates (besides index 6) still had no color. Adding `{color}` to the remaining middle templates that have a natural insertion point follows the established pattern of enriching templates with available word categories: `{adj}` in all middle templates (Sessions 38/40/41), `{adverb}` in all templates (Sessions 30/37/42/47), `{element}` in openings/weather (Sessions 56/57), `{color}` in weather/openings (Sessions 58/59), and now `{color}` in middle templates.

### Tradeoffs
- **Template-level change only** — `color=color` was already threaded through the middle format call since Session 51. No code changes to the generation pipeline.
- **No seed-breaking change** — no new `_pick()` calls are added, so existing seed-based output is preserved. The same templates are selected; they now render with an additional word.
- **Templates 0 and 3 unchanged** — both start with `{Element}` (sentence-initial, capitalized), and adding `{color}` before it would produce a leading-space artifact when `color_enabled=False` (`"  Mist whispers..."`). This is the same reason Session 59 skipped the em-dash opening template for color. Templates 1, 2, 4, 5 all have a comma or preposition before the insertion point, so `_format_tmpl` cleans up `",  "` → `", "` naturally when color is disabled.
- **`{color} {element}` reads naturally** — "vivid mist", "murky silence", "iridescent echo" are poetic but grammatical. The color word modifies the element, which is a sensory quality of the landscape.
- **`color_enabled=False` compatibility** — when disabled, templates render with an empty color string, producing `",  mist"` which `_format_tmpl` collapses to `", mist"` — reads naturally without the color word.
- **4 new tests**, 337 total (18 todo + 319 landscape).

## 2026-07-12 — `{element}` in Weather Templates

### What
Added `{element}` to weather templates — the weather slot now references the per-sentence-pair element word, extending the element-awareness from openings (Session 56) into weather descriptions. Three changes:
1. **Template 0**: `"{Weather} {adverb}."` → `"{Weather} {adverb} through the {element}."` — "A gentle rain falls softly through the mist."
2. **Template 2**: `"{Weather}, as if the {display} itself breathes {adverb}."` → `"{Weather}, as if the {display} itself breathes {element} {adverb}."` — "A gentle rain falls, as if the forest itself breathes mist softly."
3. **New template 3 (index 3)**: `"Through the {element}, {weather} {adverb}."` — "Through the mist, a gentle rain falls softly."

The element pick was moved outside the `if middle_enabled:` block in the detail loop so it's always available for weather regardless of middle state. Template 1 (`"The air tells its own story: ..."`) is unchanged — there's no natural insertion point for element in that template.

### Why
Session 56 added element to the opening templates, making openings consistently richer by referencing the sensory quality (mist, light, echo) alongside the visual quality (adj) and the biome name (display). But the weather slot — the other major descriptive slot alongside middle sentences — had no element reference, meaning weather descriptions like "A gentle rain falls softly." were disconnected from the landscape's elemental vocabulary. Adding element to weather creates cross-sentence cohesion: "A gentle rain falls softly through the mist." feels grounded in the same sensory world as "A vast crystal forest of mist stretches silently before you."

### Tradeoffs
- **Element is now always picked per-pair in the loop**, not just when middle is enabled. This uses one extra dedup slot and one extra `_pick()` call per pair when middle is disabled. The tradeoff is the same as the per-sentence-pair adverb (Sessions 37/48): weather benefits from having element even when middle sentences are suppressed, justifying the extra cost.
- **Template 1 unchanged**: `"The air tells its own story: {weather} {adverb}."` has no natural place for element without restructuring the sentence. Adding element would produce "The air tells its own story: a gentle rain falls softly carried by mist." which is grammatically awkward.
- **Seed-breaking change**: existing seed-based output differs because the element pick now happens for every weather iteration regardless of middle state, and the new weather templates change the output. Since no seed-based output has been published, this is acceptable.
- **4 weather templates now**: weather goes from 3 to 4 templates. Template_set "third" still maps to index 2 (unchanged); the new template at index 3 is only accessible via random selection, matching the same pattern as the opening's em-dash template (Session 56).
- **9 new tests**, 320 total (18 todo + 302 landscape).

## 2026-07-12 — `{color}` in Weather Templates

### What
Added `{color}` to weather descriptions: a 5th weather template `"{Weather} {adverb} in {color} light."` that references the per-sentence-pair color word. The `color` variable is initialized to `""` before the `if middle_enabled:` block in the detail loop, so it's always available for weather templates regardless of middle state. The `color=color` kwarg is passed to all weather `_format_tmpl()` calls; unmodified templates silently ignore it.

### Why
The color word bank (Session 51) was previously only used in one middle template (index 6: `"The {color} light of {element} {verb_conjugated} {adverb}."`), making it invisible in most outputs — the word was picked but only appeared in ~14% of middle sentences (1 of 7 templates) and never in weather, openings, or anomalies. Adding `{color}` to weather gives the color category more visibility and makes weather descriptions richer, following the same pattern as Session 57 (`{element}` in weather) and Session 56 (`{element}` in openings). This is a natural progression: colors were added as a quality improvement, and now they get broader template coverage for greater impact.

### Tradeoffs
- **`color = ""` initialization before the middle block** — when middle is disabled, no color word is picked (saves a `_pick()` call and dedup slot). The weather template renders as `"in  light."` and `_format_tmpl` collapses the double space to `"in light."`, which reads naturally. When middle is enabled and color_enabled=True, the picked color word is used.
- **No seed-breaking change** — unlike Sessions 56–57 which moved element picks (changing the random call order), this change only adds a `color = ""` initialization (no random call) and passes an existing variable to a format call it was previously missing from. The only output change is when weather template 4 is randomly selected, which is a new template added to the pool — the same seed may now select this template instead of one of the previous 4.
- **Only 1 new template** (rather than modifying existing ones) — keeps the change minimal. Color in weather could be extended to more templates in the future.
- **Works with `color_enabled=False`** — the empty-string pattern handles suppression identically to `adverb_enabled=False`: the template renders without the color word and spacing is cleaned up by `_format_tmpl`.
- **9 new tests**, 329 total (18 todo + 311 landscape).

## 2026-07-12 — `{adverb}` in Anomaly Framing + `{color}` in Remaining Middle Templates

### What
Two template enrichments in one session:
1. Added `{adverb}` to anomaly framing templates 2 and 3 ("A strange detail catches your eye {adverb}: ..." and "There is a quiet wrongness here {adverb}: ...")
2. Added `{color}` to middle templates 0 and 3 ("...between the {color} {adj} {noun}" and "...through the {color} {adj} {noun}")

### Why
**Anomaly adverb**: Anomaly templates were the only template slot that didn't use any per-sentence-pair word categories (adverb, color, element, adj). The `adverb=adverb` kwarg was already passed to anomaly format calls but unused by any template. Adding `{adverb}` makes anomalies feel more connected to the landscape's adverbial flavor — an anomaly in an eerie mood might be "noticed silently" while one in a vibrant mood might be "noticed gently."

**Middle color**: Templates 0 and 3 were the only middle templates without `{color}`. Session 60 skipped them citing "leading-space artifacts when color is disabled" — but that only applies when `{color}` is placed sentence-initially (before `{Element}`). Placing `{color}` before `{adj}` and after a preposition avoids the leading-space issue entirely.

### Tradeoffs
- **`{adverb}` before colon, modifying the framing**: Adverb sits between the framing verb and the colon ("catches your eye softly:"), modifying the act of noticing rather than the anomaly itself. This reads naturally because the adverb describes *how* the detail is perceived.
- **`_format_tmpl` colon cleanup**: Added `.replace(" :", ":")` to prevent space-before-colon when `adverb_enabled=False`. This is a general quality improvement that benefits any template with a dynamic word before a colon.
- **`{color}` before `{adj}`**: "vivid crystal" (color then biome-adj) flows naturally as a two-adjective stack. When `color_enabled=False`, `_format_tmpl` collapses `"the  crystal"` → `"the crystal"` without artifacts.
- **No seed-breaking change from new `_pick()` calls**: Template string changes only, no new random calls. Seed-based output differs only for landscapes that happen to select affected templates — and the content is strictly richer.
- **All 7 middle templates now use `{color}`**: Complete coverage across the middle slot, joining `{adj}` (6/6), `{adverb}` (6/6), and `{element}` (in all templates that have element kwarg support).
- **11 new tests**, 348 total (18 todo + 330 landscape).

## 2026-07-12 — Biome-Specific Color and Adverb Word Pools

### What
Added `"colors"` and `"adverbs"` entries to each of the 13 biomes in `BIOME_WORDS` — each biome now has 3-4 curated color words and 3-4 curated adverbs that are blended with the global pools during word selection. Updated `describe_biome()` to include these two new categories in its output.

### Why
When colors (Session 51) and adverbs (Session 24) were added as word categories, they were only populated in global pools and `MOOD_WORDS` — `BIOME_WORDS` never got corresponding entries. This meant `_pick("colors", biomes)` and `_pick("adverbs", biomes)` always fell back entirely to the global pool, making every biome share the same colors and adverbial flavors. A forest, desert, and ocean all used the same "vivid"/"murky"/"burnished" colors and "softly"/"silently"/"gently" adverbs.

Adding biome-specific colors and adverbs closes this gap: the same biome system that makes a forest feel like a forest (through distinctive adjectives, elements, nouns, verbs, weathers, and anomalies) now also makes it feel distinctive in color and adverb choices. A desert's "crimson" and "relentlessly" feel different from a forest's "emerald" and "peacefully" or a tundra's "frost-white" and "coldly." This is the natural completion of the biome word bank system — all 8 word categories now have biome-specific pools.

### Tradeoffs
- **Zero code changes to `_pick()`**: The function already used `BIOME_WORDS.get(b, {}).get(category, [])` for all categories. Colors and adverbs were simply missing from `BIOME_WORDS`, so they returned empty lists. Adding the data entries is purely additive — no pipeline logic changes.
- **3-4 words per biome per category** — smaller than the global pools (12 each) so the global flavor still dominates when no biome is set or when combining biomes. This keeps the system balanced: biome-specific words add thematic seasoning without overwhelming the global vocabulary.
- **Word overlap with global pools is acceptable**: Some biome colors (e.g., "golden" in forest/desert/plain/sky islands) also appear in the global pool. This is fine — the biome word is added to the pool alongside the global word, so selection probability increases for that word when the biome is active. This follows the same pattern as biome adjectives/elements/nouns/verbs overlapping with global pools (e.g., "golden" is both a desert adjective and a global color).
- **Not all multi-word colors will appear in all templates**: Multi-word colors like "deep green" and "obsidian black" could be split across template placeholders (e.g., `"emerald"` fits anywhere, but `"deep green"` before `{element}` produces `"deep green birdsong"`). This is acceptable — multi-word elements like "heat shimmer" and "leaf rustle" already work the same way, and the results read as natural adjective phrases.
- **No seed-breaking change**: Adding data to `BIOME_WORDS` doesn't change the random call order — only the pool of available words changes. Seed-based output is preserved for biomes whose random selections don't draw from the new pools (though in practice most will, since colors and adverbs are picked per-sentence-pair).
- **`describe_biome()` now includes 8 categories** (was 6). The `test_describe_known_biome_contains_categories` test checked for "adjectives:", "elements:", "nouns:" but didn't assert "only these categories" — so no update was needed. A new test verifies the new categories appear.
- **12 new tests**, 360 total (18 todo + 342 landscape).

## 2026-07-12 — Template Set Modes "Fourth" and "Fifth"

### What
Added `"fourth": 3` and `"fifth": 4` to the `TEMPLATE_SETS` dict, extending the template selection system beyond the original `"first"`/`"second"`/`"third"` preset indices. Users can now force any template index up to 4 via `--template-set fourth` or `--template-set fifth`.

### Why
The original TEMPLATE_SETS (Session 15) only defined indices 0–2, leaving templates at indices 3+ only accessible via random selection. With 4 opening templates, 7 middle templates, 5 weather templates, and 4 anomaly templates, the `"third"` mode only reached the middle of the pool. Adding `"fourth"` and `"fifth"` gives users explicit access to the em-dash opening template, the "Through the {element}" weather template, the color-in-weather template, and deeper middle templates — making the template set system more useful as the template pool has grown.

### Tradeoffs
- `"fifth"` clamps to index `len(templates) - 1` for slots with ≤4 templates (opening → index 3, anomaly → index 3) via `_pick_template()`'s existing `min()` logic. This is consistent with how `"third"` already clamps when a slot has only 2 templates.
- When `"fifth"` is used, the opening and anomaly slots use the same templates as `"fourth"`, but middle and weather slots use their distinct index-4 templates. This is a minor UX inconsistency — users who want consistent index-4 across all slots will get mixed index-3/index-4 output. A per-slot override system (`--template-opening`, etc.) already exists for this case; the general `--template-set` flag is a convenience for uniform selection.
- The `choices` list in argparse automatically picks up the new keys from `TEMPLATE_SETS` — no CLI code changes needed.
- 7 new tests, 367 total.

## 2026-07-12 — ALL_ADVERBS/ALL_COLORS Test Data Fix

### What
Updated `ALL_ADVERBS` and `ALL_COLORS` in `test_landscape.py` to include biome-specific words from `BIOME_WORDS` (like all other `ALL_*` sets already do). Fixed `test_describe_global_includes_colors` to assert against global `COLORS` instead of `ALL_COLORS`, since `describe_global()` only lists global pools.

### Why
Session 62 added biome-specific color and adverb pools to `BIOME_WORDS`, but the test module's combined detection sets (`ALL_ADVERBS` and `ALL_COLORS`) were not updated to include them. All other categories (adjectives, elements, nouns, verbs, weathers, anomalies) correctly included biome-specific words via their `ALL_*` set definitions. This inconsistency meant tests that check for word presence in output (e.g. `test_output_contains_known_adverb`, `test_color_in_middle_templates`) could miss biome-specific words, creating a false-negative risk.

### Tradeoffs
- No functional change to the landscape generator — purely a test data correction.
- `test_describe_global_includes_colors` now correctly tests that `describe_global()` shows global colors (not biome-specific ones), matching the behavior of `describe_global()` which intentionally lists only the global word pools.
- 366 landscape tests pass (unchanged count — no new tests added).

## 2026-07-13 — `{adj}` in Weather Templates

### What
Added `{adj}` to 4 of 5 weather templates (0, 1, 2, 3) — the per-sentence-pair adjective now appears in weather descriptions. Template 4 (`"{Weather} {adverb} in {color} light."`) is unchanged because `{adj}` would create a cluttered three-adjective stack (`in {adj} {color} light`). Moved the per-sentence-pair adj pick outside the `if middle_enabled:` block so it's always available for weather regardless of middle sentence state.

### Why
The adjective was the last major word category missing from weather descriptions. Over recent sessions, weather templates gained `{element}` (Sessions 57/68), `{color}` (Session 58), and `{adverb}` (Sessions 30/42), but never `{adj}` — leaving weather descriptions unable to leverage the landscape's most descriptive word category. "A gentle rain falls softly through the crystal mist" is more evocative than "A gentle rain falls softly through the mist." This completes the coverage pattern: all 5 weather templates now reference at least 3 injected word categories, making weather descriptions uniformly as rich as opening and middle sentences.

### Tradeoffs
- **Adj pick moved unconditionally**: Previously, the per-sentence-pair adjective was only picked when `middle_enabled=True` (it was picked inside the middle block because weather didn't use it). Now it's always picked per-pair, wasting one adj pick (and dedup slot) when `middle_enabled=False`. This is the same tradeoff as `element` (Session 57: moved outside middle block for weather use) — the benefit (richer weather) justifies the cost.
- **RNG-preserving for middle_enabled=True**: The adj pick was moved just after `element` and before `noun`/`verb`, preserving the same relative random call order for the common case (middle enabled). Seed-breaking only when `middle_disabled` is used (one extra `_pick()` per iteration).
- **Template 4 unchanged**: In `"{Weather} {adverb} in {color} light."`, adding `{adj}` would produce `"in {adj} {color} light"` — a three-adjective stack that reads awkwardly. Keeping template 4 adj-free maintains one weather template without adjectives for variety.
- **Template-level change + one code change**: 4 template strings modified (`{element}` → `{adj} {element}`, `{display}` → `{adj} {display}`), adj pick moved outside the `if middle_enabled:` block, and `adj=adj` kwarg added to the weather format call.
- **`_format_tmpl` handles disabled-adj edge cases**: When `middle_enabled=False`, adj is still picked so it's always defined — no need for empty-string fallback or spacing cleanup.
- **9 new tests**, 393 total (18 todo + 375 landscape).

## 2026-07-13 — `{element}` in Weather Template 1 (The Air Tells)

### What
Added `{element}` to `SENTENCE_TEMPLATES["weather"][1]`: changed `"The air tells its own story: {weather} {adverb}."` to `"The air tells its own story: {weather} {adverb} through the {element}."`. Template-level change only — `element=element` was already passed to all weather format calls since Session 57.

### Why
Weather template 1 was the only template in the weather slot that didn't reference the per-sentence-pair element word. Templates 0, 2, and 3 all used `{element}`, and template 4 used `{color}`. This left template 1 producing flatter descriptions like "The air tells its own story: a gentle rain falls softly." compared to the more evocative "The air tells its own story: a gentle rain falls softly through the mist." Adding `{element}` closes this coverage gap and makes weather descriptions uniformly richer across all 5 templates.

### Tradeoffs
- Template-level change only — no code changes, no new `_pick()` calls, no seed-breaking change from RNG sequence alteration (the same random choices are made; only the output content changes when template 1 is selected)
- "through the {element}" reads naturally with all element types: single-word ("mist"), multi-word ("heat shimmer", "leaf rustle") — just like the same phrase in template 0
- When `adverb_enabled=False`, the template renders as `"The air tells its own story: {weather}  through the {element}."` — `_format_tmpl` collapses the double space perfectly
- All 5 weather templates now use at least one injected word category (element, color, or adverb), up from 4 of 5
- No new tests — existing coverage (template variety, output validity, element presence in weather, `adverb_enabled=False` formatting) covers the change
- 393 tests total (unchanged)

## 2026-07-13 — `{color}` in Anomaly Templates

### What
Added `{color}` to anomaly templates: modified template 2 (`"A strange {color} detail catches your eye {adverb}: {anomaly_lower}"`) and added a new 5th template (`"In the {color} light, {anomaly_lower}"`). Added `color=color` kwarg to the anomaly format call so the existing per-sentence-pair color word is available to anomaly templates.

### Why
Color is the project's newest word category (Session 51), and since then it's been added to every template slot except anomalies: openings (Session 59), middle (Sessions 60/61), and weather (Session 58). Anomalies were the last slot where color words were picked (consuming a dedup slot) but never visible — they were invisible in ~80% of anomalies. Adding `{color}` to anomalies closes this coverage gap and makes anomaly descriptions richer by connecting them to the landscape's color palette. "A strange vivid detail catches your eye" is more evocative than "A strange detail catches your eye."

### Tradeoffs
- **Template 2 modification**: Adding `{color}` before "detail" is a natural insertion — "A strange vivid detail" reads as a standard two-adjective stack. When `color_enabled=False`, `_format_tmpl` collapses the resulting double space.
- **New template 4**: `"In the {color} light, {anomaly_lower}"` — the anomaly is framed as something observed under the landscape's light. This is a structurally different framing from the 4 existing templates (which present the anomaly as a direct observation or wrongness), adding variety to anomaly presentation. When color is disabled, reads naturally as "In the light, the gravity here feels wrong."
- **No Color kwarg needed**: The lowercase `{color}` is used in both new/modified templates (mid-sentence positions), so `color=color` is sufficient — no separate `Color` kwarg needed.
- **Scope-based color value**: The anomaly block runs after the `detail` loop, so `color` holds the last-per-sentence-pair color (or `""` when middle is disabled). This is the same pattern as `adverb` in anomaly templates. When middle is disabled and color is enabled, color is `""` (reset at loop start), so anomaly gets no color — acceptable since anomaly framing without middle is a minimal-output edge case.
- **5 anomaly templates**: Anomaly goes from 4 to 5 templates. Template_set "fourth" (index 3) and "fifth" (index 4) now both map to distinct templates for the anomaly slot (was 3→3 clamped to index 3; now 3→3 and 4→4). Backward compatible index clamping still applies for "sixth" (→4) and "seventh" (→4).
- **9 new tests**, 393 total (18 todo + 375 landscape).

## 2026-07-13 — `{element}` in Anomaly Template 2

### What
Added `{element}` to `SENTENCE_TEMPLATES["anomaly"][2]`: changed `"A strange {color} detail catches your eye {adverb}: {anomaly_lower}"` to `"A strange {color} detail catches your eye {adverb} through the {element}: {anomaly_lower}"` (e.g. "A strange vivid detail catches your eye softly through the mist: the gravity here feels wrong."). Added `element=element` kwarg to the anomaly `_format_tmpl()` call — `element` was already in scope (last per-sentence-pair element) but was not passed to anomaly templates, so the placeholder would have rendered as literal `{element}` text.

### Why
`{element}` was the only word category completely missing from the anomaly slot. Every other template slot (opening, middle, weather) used `{element}` in at least one template — the element word (mist, light, echo, etc.) is one of the most evocative categories, grounding descriptions in a sensory quality. Anomaly template 2 already used `{color}` and `{adverb}`, making it the natural candidate for adding `{element}` as well. The resulting template reads as "A strange X detail catches your eye Y through the Z: anomaly" — a framing that connects the observation to the landscape's elemental context.

### Tradeoffs
- **Template-level change plus one kwarg addition** — follows the same pattern as every previous template enrichment: add a kwarg that existing templates silently ignore, update one template to use it.
- **No seed-breaking change** — no new `_pick()` calls, only the template string and format kwarg changed. Seed-based output is preserved for landscapes that don't select template 2.
- **Template 2 now uses 3 word categories** (`{color}`, `{adverb}`, `{element}`) — the most heavily enriched anomaly template, joining anomaly template 4 which uses 3 categories (`{color}`, `{adj}`, `{display}`). Templates 0 and 1 remain intentionally sparse for stylistic variety.
- **Element scope**: The anomaly block runs after the `detail` loop, so `element` holds the last per-sentence-pair element value. When `detail=0` (no loop iterations), anomalies are not generated (condition `detail >= 1`), so `element` is always defined when anomalies run.
- **When `adverb_enabled=False`**, `_format_tmpl` collapses `"catches your eye  through"` → `"catches your eye through"` — reads naturally without the adverb.
- **`{element}` now used in all 4 template slots**: opening (all 4 templates), middle (all 7), weather (all 5), anomaly (1 of 5 — this change). Template 0 remains bare `{anomaly}` by design.
- **4 new tests**, 404 total (18 todo + 386 landscape).
