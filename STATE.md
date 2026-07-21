# State

## 2026-07-21

### What was done (Session 196)
- **Added "reverie" preset** — the 10th preset and the first to use the peaceful+melancholy
  mood combination. Until now, no preset combined these two moods: pastoral uses pure peaceful,
  gloaming uses pure melancholy. The new preset fills a gentle-ache niche between them,
  providing a landscape that is both calming and wistful — a "reverie" for the beauty of
  transience.
- **"reverie" preset design**:
  - **Mood**: `["peaceful", "melancholy"]` — gentle calm meets wistful sadness, the
    register of beautiful melancholy.
  - **Weather**: gentle (1, prob=0.7) — peaceful's warm golden light and gentle breezes
    blend with melancholy's rain and mist, but softly; the weather supports the dreamy
    state without dominating.
  - **Anomalies**: subtle (1, prob=0.65) — soft-focus surrealness: peaceful's haze and
    honey-stretched time alongside melancholy's half-remembered melodies and impossible
    sky-reflections.
  - **Echoes**: high (2, prob=0.8) — the landscape remembers softly, with gentle sadness.
  - **Wistful**: high (2, prob=0.9) — yearning and nostalgia naturally suit the reverie
    register; the ache of beauty remembered.
  - **Mood atmosphere**: high (2, prob=0.9) — both peaceful's 6 atmosphere phrases
    (contentment, lingering light, stillness) and melancholy's 6 phrases (gentle sadness,
    quiet ache, suspended rain).
  - **Sound**: gentle (1, prob=0.6) — muffled, distant, as if heard through water or
    memory.
  - **Wildlife**: sparse (1, prob=0.3) — a reverie is introspective, not bustling.
  - **Legends**: sparse (1, prob=0.4) — reverie is about inner feeling, not folkloric
    narrative; legends appear rarely, softly.
  - **Simile/Metaphor/Personification**: gentle descending (0.7/0.6/0.5) — simile most
    natural for the reflective register; personification rarest, feeling too assertive.
  - **Time of day/Season/Perspective**: gentle (0.6 each) — framing without overwhelming.
  - **Travelogue**: enabled — journal framing suits the intimate, reflective register
    of a daydream.
- **Updated hardcoded preset lists**: `test_preset_produces_valid_output` and
  `test_preset_is_deterministic` now include `"reverie"` in their iteration lists.
- **No code logic changes**: The preset system dynamically reads `PRESETS` dict keys for
  `--preset` choices and all dynamic tests use `for name in PRESETS`, so the preset is
  auto-available without any other code modifications. Only the two tests with hardcoded
  preset name lists needed manual updates.
- **Tests**: 1169 pass (636 subtests) — same test count as Session 195, with 47 additional
  subtests (636 vs 589) from dynamic preset iteration tests picking up the new preset.

### Current status
Working. All 1169 tests pass (18 todo + 1169 landscape).

### Next likely steps
- Add more presets for diverse generation experiences (e.g. vibrant+melancholy, peaceful+desolate, eerie+desolate)
- Add a new biome or mood overlay
- Add biome-biased presets or biome-weight customization

## 2026-07-21

### What was done (Session 193)
- **Added "sanctuary" preset** — the 7th preset and the first to use vibrant as the
  sole mood. Until now, vibrant only appeared in combination presets (sublime with
  peaceful, dreamscape with eerie). The new preset fills a vibrant-abundance niche
  between pastoral (peaceful, calm) and sublime (vibrant+peaceful, maximal), providing
  a pure vibrant, life-celebrating generation experience.
- **"sanctuary" preset design**:
  - **Mood**: `["vibrant"]` — radiant, effulgent, life-abundant emotional register.
  - **Weather**: high (2, prob=0.9) — sunlight, butterflies, pollen shimmer.
  - **Anomalies**: moderate (1, prob=0.7) — beautiful surreal details like synesthetic
    colour-sound and coral pulse.
  - **Echoes**: high (2, prob=0.85) — the landscape remembers its own abundance.
  - **Wistful**: high (2, prob=0.85) — the beauty leaves a lingering ache.
  - **Mood atmosphere**: high (2, prob=0.9) — vibrant's 6 atmosphere phrases about
    bleeding colour, sub-audible song, and organic abundance.
  - **Sound**: high (2, prob=0.9) — birdsong, insect hum, the world singing.
  - **Wildlife**: high (2, prob=0.9) — abundant teeming life.
  - **Legends**: low (1, prob=0.5) — sparingly used; sanctuary is about immediate
    presence, not folkloric past.
  - **Simile/Metaphor/Personification**: high/moderate (0.85/0.85/0.7) — abundant
    figurative language for an abundant landscape.
  - **Time of day/Season/Perspective**: moderate (0.7 each) — gentle framing.
  - **Travelogue**: enabled — journal framing suits the intimate, present-tense
    register of a sanctuary.
- **Updated hardcoded preset lists**: `test_preset_produces_valid_output` and
  `test_preset_is_deterministic` now include `"sanctuary"` in their iteration lists.
- **No code logic changes**: The preset system dynamically reads `PRESETS` dict keys for
  `--preset` choices and all dynamic tests use `for name in PRESETS`, so the preset is
  auto-available without any other code modifications. Only the two tests with hardcoded
  preset name lists needed manual updates.
- **Tests**: 1169 pass (495 subtests) — same test count as Session 192, with 47 additional
  subtests (495 vs 448) from dynamic preset iteration tests picking up the new preset.

### Current status
Working. All 1169 tests pass (18 todo + 1169 landscape).

### Next likely steps
- Add more presets for diverse generation experiences (e.g. vibrant+desolate, peaceful+melancholy)
- Add a new biome or mood overlay
- Add biome-biased presets or biome-weight customization

## 2026-07-21

### What was done (Session 194)
- **Added "lament" preset** — the 8th preset and the first to use the eerie+melancholy
  mood combination. Until now, no preset combined these two moods: nightfall uses pure eerie,
  gloaming uses pure melancholy. The new preset fills a haunted-grief niche between them,
  providing a landscape that is both sorrowful and haunting — a "lament" for something lost.
- **"lament" preset design**:
  - **Mood**: `["eerie", "melancholy"]` — haunting AND sorrowful, the register of grief.
  - **Weather**: high (2, prob=0.9) — eerie weathers (cold wind, frost, stillness combined
    with melancholy weathers (rain, mist, grey light).
  - **Anomalies**: high (2, prob=0.85) — both eerie and melancholy anomalies about temporal
    distortion, wrong physics, and memory-based strangeness.
  - **Echoes**: high (2, prob=0.9) — the landscape remembers its grief.
  - **Wistful**: high (2, prob=0.9) — yearning and farewell suit the lament register.
  - **Mood atmosphere**: high (2, prob=0.9) — both eerie and melancholy atmosphere phrases
    about watchful silence, wrongness, gentle sadness, and quiet ache.
  - **Sound**: moderate (1, prob=0.7) — eerie whispers and moans, melancholy muffled sounds.
  - **Wildlife**: low (1, prob=0.3) — sparse; a lamenting landscape is sparsely inhabited.
  - **Legends**: moderate (1, prob=0.6) — folkloric tales of loss and haunting suit the register.
  - **Simile/Metaphor/Personification**: moderate descending (0.7/0.6/0.5) — figurative
    language for grief; simile most natural, personification rarest.
  - **Time of day/Season/Perspective**: moderate (0.6 each) — gentle framing without
    overwhelming.
  - **Travelogue**: enabled — journal framing suits intimate grief.
- **Updated hardcoded preset lists**: `test_preset_produces_valid_output` and
  `test_preset_is_deterministic` now include `"lament"` in their iteration lists.
- **No code logic changes**: The preset system dynamically reads `PRESETS` dict keys for
  `--preset` choices and all dynamic tests use `for name in PRESETS`, so the preset is
  auto-available without any other code modifications. Only the two tests with hardcoded
  preset name lists needed manual updates.
- **Tests**: 1169 pass (542 subtests) — same test count as Session 193, with 47 additional
  subtests (542 vs 495) from dynamic preset iteration tests picking up the new preset.

### Current status
Working. All 1169 tests pass (18 todo + 1169 landscape).

### Next likely steps
- Add more presets for diverse generation experiences (e.g. vibrant+desolate, peaceful+melancholy)
- Add a new biome or mood overlay
- Add biome-biased presets or biome-weight customization

## 2026-07-21

### What was done (Session 195)
- **Added "oasis" preset** — the 9th preset and the first to use the vibrant+desolate
  mood combination. Until now, no preset combined these two moods: sanctuary uses pure
  vibrant, wasteland uses pure desolate. The new preset fills a life-amid-barrenness
  niche between them, providing a landscape where vibrant abundance and desolate
  barrenness coexist in tension.
- **"oasis" preset design**:
  - **Mood**: `["vibrant", "desolate"]` — life and barrenness in generative tension.
  - **Weather**: high (2, prob=0.85) — both vibrant's warm/lively weathers (sunlight,
    butterflies, pollen shimmer) and desolate's harsh/scouring weathers (relentless
    wind, pale sun without warmth).
  - **Anomalies**: high (2, prob=0.85) — both moods contribute surreal juxtaposition
    anomalies: vibrant's synesthetic colour-sound, coral pulse alongside desolate's
    unearthly ground disintegration and temporal distortion.
  - **Echoes**: high (2, prob=0.8) — the landscape remembers both its abundance
    and its loss.
  - **Wistful**: high (2, prob=0.85) — the contrast between life and barrenness
    naturally evokes yearning and the desire to preserve what remains.
  - **Mood atmosphere**: high (2, prob=0.9) — both vibrant's 6 atmosphere phrases
    (bleeding colour, sub-audible song, organic abundance) and desolate's 6 phrases
    (silence as shape of loss, forgotten growth, withered hope).
  - **Sound**: moderate (1, prob=0.7) — vibrant sounds (birdsong, insect hum) push
    against desolate silence, creating a sonic landscape of contested space.
  - **Wildlife**: moderate (1, prob=0.6) — life persists against odds, sparse but
    tenacious.
  - **Legends**: moderate (1, prob=0.6) — folkloric tales of places where life
    finds a way, where abundance and barrenness meet.
  - **Simile/Metaphor/Personification**: moderate descending (0.8/0.7/0.6) —
    figurative language is well-suited for a landscape of contrasts; simile most
    natural, personification rarest.
  - **Time of day/Season/Perspective**: moderate (0.6 each) — gentle framing.
  - **Travelogue**: enabled — journal framing suits the discovery of a place where
    contradiction is the natural state.
- **Updated hardcoded preset lists**: `test_preset_produces_valid_output` and
  `test_preset_is_deterministic` now include `"oasis"` in their iteration lists.
- **No code logic changes**: The preset system dynamically reads `PRESETS` dict keys for
  `--preset` choices and all dynamic tests use `for name in PRESETS`, so the preset is
  auto-available without any other code modifications. Only the two tests with hardcoded
  preset name lists needed manual updates.
- **Tests**: 1169 pass (589 subtests) — same test count as Session 194, with 47 additional
  subtests (589 vs 542) from dynamic preset iteration tests picking up the new preset.

### Current status
Working. All 1169 tests pass (18 todo + 1169 landscape).

### Next likely steps
- Add more presets for diverse generation experiences (e.g. peaceful+melancholy)
- Add a new biome or mood overlay
- Add biome-biased presets or biome-weight customization

## 2026-07-21

### What was done (Session 192)
- **Expanded mood atmosphere phrase pools for all 5 moods** — each mood's
  MOOD_ATMOSPHERE pool grew from 4 to 6 phrases, adding 10 new atmosphere
  phrases total. This directly fulfills the third "Next likely step" from
  Session 191: "Expand mood atmosphere phrase pools for consistency."
- **New peaceful atmosphere phrases**:
  - "A quiet contentment settles over the world, as if everything is exactly
    where it should be." — contentment and rightness, a feeling that the
    universe is in proper order. Distinct from existing peaceful phrases about
    rest, stillness, and oxygen — this is about cosmic alignment and belonging.
  - "The light here seems to linger a little longer, as if time itself is
    reluctant to move on." — temporal stillness, light that overstays. Distinct
    from "world holds its breath" (held-breath anticipation) — this is about
    time itself slowing down through reluctance.
- **New eerie atmosphere phrases**:
  - "The shadows seem deeper than they should be, as if they have swallowed
    something of the light." — unnaturally deep shadows that have consumed
    light. Distinct from existing eerie phrases about wrongness, watchful
    silence, and hair-standing-up — this is about visual darkness that has
    actively consumed illumination.
  - "Nothing moves, yet you sense that everything has just finished moving —
    a world frozen mid-gesture." — a landscape caught in the instant after
    motion, frozen mid-action. Distinct from "wrongness in the air" (abstract
    unease) — this is about specific temporal arrest.
- **New vibrant atmosphere phrases**:
  - "The air itself vibrates with a frequency just below hearing, a song the
    world cannot stop singing." — sub-audible vibration, the world humming
    its own song. Distinct from existing vibrant phrases about bleeding colour,
    joyful intensity, and charged air — this is about an inaudible, constant
    vibrational song.
  - "Life presses in from every direction, as if the landscape itself cannot
    contain its own abundance." — overwhelming abundance, life exceeding the
    landscape's capacity. Distinct from "too full to contain itself" (bleeding
    colour/light) — this is about organic life pressure, not optical excess.
- **New desolate atmosphere phrases**:
  - "The silence here is not empty — it is the absence of everything that once
    was, a shape left by loss." — silence as the negative space of vanished
    things. Distinct from existing desolate phrases about hope withered, the
    land giving up, and emptiness as identity — this is about silence as the
    geometric trace of what departed.
  - "Nothing grows here, not because the land is incapable, but because it has
    forgotten how." — lost knowledge of growth, a forgetting more fundamental
    than incapacity. Distinct from "land has given up on itself" (volitional
    surrender) — this is about ontological forgetting.
- **New melancholy atmosphere phrases**:
  - "The rain does not fall — it hangs in the air, suspended between sky and
    earth, unwilling to commit to either." — rain as suspended indecision, a
    weather of ambivalence. Distinct from "gentle sadness in the air" (abstract
    sadness) — this is a specific weather phenomenon that embodies melancholy.
  - "Everything here is touched with the colour of a memory that refuses to
    fade, soft and persistent." — a persistent, colour-like memory that will
    not dim. Distinct from "half-forgotten lullaby" (which is about forgetting)
    — this is about a memory that actively refuses to fade.
- **Updated MOOD_ATMOSPHERE_INDICATORS** in test_landscape.py: Added 10 new
  invariant substrings (2 per mood) for test detection of the new atmosphere
  phrases. All existing mood atmosphere tests use dynamic checks over
  MOOD_ATMOSPHERE_INDICATORS, so no test logic changes were needed.
- **No code, CLI, or generation logic changes** — data-only expansion of the
  MOOD_ATMOSPHERE dict plus indicator additions. All existing tests use dynamic
  checks over MOOD_ATMOSPHERE keys and MOOD_ATMOSPHERE_INDICATORS, so no test
  modifications were needed beyond the indicator list.
- This directly fulfills the third "Next likely step" from Session 191: "Expand
  mood atmosphere phrase pools for consistency." All 5 moods now have 6
  atmosphere phrases each, matching the expanded pool sizes pattern from the
  mood word pool consistency initiative (Sessions 187–191).
- **Tests**: 1169 pass (448 subtests) — same as Session 191. Mood atmosphere
  tests use dynamic checks over MOOD_ATMOSPHERE_INDICATORS, so test count is
  unchanged.

### Current status
Working. All 1169 tests pass (18 todo + 1169 landscape).

### Next likely steps
- Add more presets for diverse generation experiences
- Add a new biome or mood overlay
- Add mood-atmosphere-aware presets with varied count/prob values

## 2026-07-21

### What was done (Session 189)
- **Expanded eerie mood word pools** — added 22 new words/phrases across 7 lexical
  categories (adjectives, elements, nouns, verbs, colors, adverbs, weathers) to bring
  eerie's pool sizes in line with melancholy and peaceful (expanded in Sessions 187
  and 188). Eerie anomalies already matched at 7 and were not expanded.
- **Eerie adjectives**: 7 → 12, added `watchful`, `unsettling`, `ghostly`, `cold`,
  `ancient` — watched-by-the-landscape, wrongness, spectral, fear-chill, and primordial
  adjectives. Existing pool: shadow, silent, forgotten, bone, obsidian, pale, deep.
- **Eerie elements**: 5 → 9, added `cold breath`, `whisper`, `moon shadow`, `presence` —
  exhalation of cold air, soft secretive sounds, lunar shadows, and sensed unseen being.
- **Eerie nouns**: 6 → 9, added `corridors`, `remains`, `thresholds` — enclosed
  passages, decayed remnants, and liminal crossing points.
- **Eerie verbs**: 6 → 9, added `watch`, `crawl`, `fester` — silent observation,
  insect-like movement, and biological decay.
- **Eerie colors**: 5 → 8, added `pitch`, `sickly`, `pallid` — absolute black,
  unhealthy green-yellow, and corpse-like paleness.
- **Eerie adverbs**: 5 → 7, added `stealthily`, `unnaturally` — furtive movement and
  wrongness of manner.
- **Eerie weathers**: 4 → 6, added:
  - `"a cold wind moans through the empty spaces, a sound without source"` —
    mournful, sourceless wind sound; fills the auditory eerie niche between stillness
    and active sound.
  - `"frost spreads in patterns that look like language, writing itself on every
    surface"` — linguistic frost patterns; visual eerie natural writing.
- **Eerie anomalies**: 7 (unchanged) — already matched the 6-entry target of other
  moods, no expansion needed.
- **Added TestEerieMood class** (8 tests) following the TestPeacefulMood/TestMelancholyMood
  pattern: does not break output (20 seeds), word weight boosted for eerie-matched words
  (shadow), word weight not boosted for unmatched words (crystal), combines with other
  moods (peaceful, vibrant, desolate, melancholy), deterministic with same seed,
  eerie-specific adjectives appear across 200 seeds, JSON output includes mood field,
  CLI flag exists.
- **No code, CLI, or generation logic changes** — data-only expansion of the
  MOOD_WORDS["eerie"] dictionary plus new test class. All existing tests use dynamic
  checks over MOOD_WORDS keys and sets, so no existing test modifications were needed.
- This directly fulfills the first "Next likely step" from Session 188: "Expand the
  remaining mood word pools (eerie, vibrant, desolate) for consistency." The eerie
  mood now has 12 adjectives, 9 elements, 9 nouns, 9 verbs, 8 colors, 7 adverbs,
  6 weathers, and 7 anomalies — matching the expanded pool sizes of melancholy and
  peaceful.
- **Tests**: 1171 pass (448 subtests) — 1153 landscape + 18 todo. Landscape tests
  grew from 1145 to 1153 (+8 for the new TestEerieMood class).

### Current status
Working. All 1171 tests pass (18 todo + 1153 landscape).

### Next likely steps
- Expand the remaining mood word pools (vibrant, desolate) for consistency
- Add more presets for diverse generation experiences
- Add a new biome or mood overlay

## 2026-07-21

### What was done (Session 190)
- **Expanded vibrant mood word pools** — added 19 new words/phrases across all 8
  lexical categories (adjectives, elements, nouns, verbs, colors, adverbs, weathers,
  anomalies) to bring vibrant's pool sizes in line with melancholy, peaceful, and eerie
  (expanded in Sessions 187, 188, and 189).
- **Vibrant adjectives**: 8 → 12, added `radiant`, `dazzling`, `resplendent`, `effulgent` —
  glowing radiance, overwhelming brightness, majestic beauty, and brilliant shining.
- **Vibrant elements**: 6 → 9, added `sunburst`, `perfume`, `coral glow` —
  explosive sunlight, intense sweet fragrance, and warm underwater light.
- **Vibrant nouns**: 6 → 9, added `blossoms`, `waterfalls`, `meadows` —
  floral bloom, cascading water, and open wildflower fields.
- **Vibrant verbs**: 6 → 9, added `dance`, `sparkle`, `blaze` —
  lively joyful movement, glittering reflected light, and intense burning brightness.
- **Vibrant colors**: 5 → 8, added `golden`, `saffron`, `magenta` —
  warm yellow-gold, bright orange-yellow, and vivid purple-red.
- **Vibrant adverbs**: 4 → 7, added `brightly`, `brilliantly`, `vividly` —
  luminosity, intense brightness, and intensity of manner.
- **Vibrant weathers**: 4 → 6, added:
  - `"a cascade of butterflies rises from the undergrowth in a riot of color"` —
    living color explosion as butterflies swarm upward; fills the animal-movement
    weather niche absent from existing vibrant weathers (warmth, light, water).
  - `"the air shimmers with pollen and sunlight, golden and alive"` —
    particulate shimmer where pollen and light fill the air; fills the golden
    particulate-light niche.
- **Vibrant anomalies**: 5 → 6, added:
  - `"The colors here have sound — a high, clear singing that shifts with every
    shade."` — synesthetic color-to-sound translation; adds an auditory/sensory
    cross-wiring register not present in the existing 5 anomalies (glow, pulse,
    light trails, melodies, lantern spores).
- **Added TestVibrantMood class** (8 tests) following the TestPeacefulMood/
  TestMelancholyMood/TestEerieMood pattern: does not break output (20 seeds),
  word weight boosted for vibrant-matched words (luminous), word weight not boosted
  for unmatched words (shadow), combines with other moods (peaceful, eerie, desolate,
  melancholy), deterministic with same seed, vibrant-specific adjectives appear across
  200 seeds, JSON output includes mood field, CLI flag exists.
- **No code, CLI, or generation logic changes** — data-only expansion of the
  MOOD_WORDS["vibrant"] dictionary plus new test class. All existing tests use dynamic
  checks over MOOD_WORDS keys and sets, so no existing test modifications were needed.
- This directly fulfills the first "Next likely step" from Session 189: "Expand the
  remaining mood word pools (vibrant, desolate) for consistency." The vibrant mood
  now has 12 adjectives, 9 elements, 9 nouns, 9 verbs, 8 colors, 7 adverbs,
  6 weathers, and 6 anomalies — matching the expanded pool sizes of melancholy,
  peaceful, and eerie.
- **Tests**: 1179 pass (448 subtests) — 1161 landscape + 18 todo. Landscape tests
  grew from 1153 to 1161 (+8 for the new TestVibrantMood class).

### Current status
Working. All 1179 tests pass (18 todo + 1161 landscape).

### Next likely steps
- Expand the remaining mood word pools (desolate) for consistency
- Add more presets for diverse generation experiences
- Add a new biome or mood overlay

## 2026-07-21

### What was done (Session 191)
- **Expanded desolate mood word pools** — added 23 new words/phrases across all 8
  lexical categories (adjectives, elements, nouns, verbs, colors, adverbs, weathers,
  anomalies) to bring desolate's pool sizes in line with melancholy, peaceful, eerie,
  and vibrant (expanded in Sessions 187, 188, 189, and 190).
- **Desolate adjectives**: 8 → 12, added `harsh`, `dead`, `blasted`, `wasted` —
  rough severity, lifeless inertness, weather-worn destruction, and devastated ruin.
- **Desolate elements**: 5 → 9, added `dust`, `rust`, `salt`, `hollow wind` —
  fine dry particulate, oxidized metal decay, sterile saline residue, and wind through
  empty spaces.
- **Desolate nouns**: 6 → 9, added `wasteland`, `skeletons`, `ashes` —
  barren empty region, organic/animal bone remains, and post-fire residue.
- **Desolate verbs**: 6 → 9, added `decay`, `wither`, `erode` —
  organic decomposition, desiccation and shriveling, and gradual geological wearing.
- **Desolate colors**: 5 → 8, added `dusty`, `rust`, `grey-brown` —
  muted dry particles, oxidized metal tone, and neutral desaturated earth tone.
- **Desolate adverbs**: 4 → 7, added `bitterly`, `mercilessly`, `endlessly` —
  intense cold/hostility, pitiless harshness, and infinite duration.
- **Desolate weathers**: 4 → 6, added:
  - `"a relentless wind scours the surface, scouring away all that is soft"` —
    persistent abrasive wind that strips everything bare; distinct from both
    "a biting wind carries ice crystals" (cold-focused) and "a hot wind scours
    the dunes" (heat-focused). Niche: constant erosive wind.
  - `"a pale sun hangs low in a colourless sky, giving light without warmth"` —
    cold distant sun providing illumination without heat; distinct from "the sun
    beats down without mercy" (hot punishing sun). Niche: cold light.
- **Desolate anomalies**: 5 → 6, added:
  - `"The ground beneath your feet crumbles into dust that does not come from this
    world."` — unearthly ground disintegration; adds material-decay and alien-origin
    register distinct from existing desolate anomalies (sand fall, no sky, shapes
    under ice, heat-freezing, distant figures).
- **Added TestDesolateMood class** (8 tests) following the TestVibrantMood/
  TestPeacefulMood pattern: does not break output (20 seeds), word weight boosted
  for desolate-matched words (barren), word weight not boosted for unmatched words
  (crystal), combines with other moods (peaceful, eerie, vibrant, melancholy),
  deterministic with same seed, desolate-specific adjectives appear across 200 seeds,
  JSON output includes mood field, CLI flag exists.
- **No code, CLI, or generation logic changes** — data-only expansion of the
  MOOD_WORDS["desolate"] dictionary plus new test class. All existing tests use dynamic
  checks over MOOD_WORDS keys and sets, so no existing test modifications were needed.
- This directly fulfills the first "Next likely step" from Session 190: "Expand the
  remaining mood word pools (desolate) for consistency." The desolate mood now has
  12 adjectives, 9 elements, 9 nouns, 9 verbs, 8 colors, 7 adverbs, 6 weathers, and
  6 anomalies — matching the expanded pool sizes of melancholy, peaceful, eerie,
  and vibrant. All 5 moods now have consistent pool sizes.
- **Milestone**: This completes the mood word pool consistency initiative begun in
  Session 187. All 5 moods (melancholy, peaceful, eerie, vibrant, desolate) now have
  matching expanded pool sizes (12/9/9/9/8/7/6/6 with minor variation).
- **Tests**: 1187 pass (448 subtests) — 1169 landscape + 18 todo. Landscape tests
  grew from 1161 to 1169 (+8 for the new TestDesolateMood class).

### Current status
Working. All 1187 tests pass (18 todo + 1169 landscape).

### Next likely steps
- Add more presets for diverse generation experiences
- Add a new biome or mood overlay
- Expand mood atmosphere phrase pools for consistency

## 2026-07-21

### What was done (Session 188)
- **Expanded peaceful mood word pools** — added 19 new words/phrases across all 8
  lexical categories (adjectives, elements, nouns, verbs, colors, adverbs, weathers,
  anomalies) to bring peaceful's pool sizes in line with melancholy (expanded in
  Session 187).
- **Peaceful adjectives**: 8 → 12, added `halcyon`, `dreamy`, `restful`, `languid` —
  nostalgic-peaceful, soft-focused, restorative, and slow-relaxed adjectives.
- **Peaceful elements**: 6 → 9, added `honey light`, `creek song`, `dusk warmth` —
  warm golden illumination, gentle flowing water sound, and evening comfort.
- **Peaceful nouns**: 6 → 9, added `hills`, `hollows`, `lakes` — gentle rolling forms,
  sheltered depressions, and still water bodies.
- **Peaceful verbs**: 6 → 9, added `nest`, `drift`, `float` — settling into rest,
  aimless gentle motion, and buoyant suspension.
- **Peaceful colors**: 6 → 8, added `cream`, `pastel` — soft off-white and muted,
  gentle hues.
- **Peaceful adverbs**: 6 → 8, added `dreamily`, `idly` — soft-focused reverie and
  unhurried ease.
- **Peaceful weathers**: 4 → 6, added:
  - `"a warm golden light bathes the landscape in soft comfort"` — enveloping golden
    illumination that soothes.
  - `"a gentle breeze carries the scent of fresh grass and wildflowers"` — olfactory
    breeze with fresh floral notes.
- **Peaceful anomalies**: 4 → 6, added:
  - `"The world feels softer than it should, as if seen through a gentle haze."` —
    perceptual softening, the world perceived through a gentle filter.
  - `"Time stretches like honey here, each moment thick and sweet."` — temporal
    viscosity, moments that linger with pleasant sweetness.
- **No code, CLI, or generation logic changes** — data-only expansion of the
  MOOD_WORDS["peaceful"] dictionary. All existing tests use dynamic checks over
  MOOD_WORDS keys and sets, so no test modifications were needed.
- This directly fulfills the first "Next likely step" from Session 187: "Expand the
  remaining mood word pools (peaceful, eerie, vibrant, desolate) for consistency."
  The peaceful mood now has 12 adjectives, 9 elements, 9 nouns, 9 verbs, 8 colors,
  8 adverbs, 6 weathers, and 6 anomalies — matching melancholy's expanded pool sizes.
- **Tests**: 1145 pass (448 subtests) — same count as Session 187.

### Current status
Working. All 1145 tests pass (18 todo + 1145 landscape).

### Next likely steps
- Expand the remaining mood word pools (eerie, vibrant, desolate) for consistency
- Add more presets for diverse generation experiences
- Add a new biome or mood overlay

## 2026-07-21

### What was done (Session 187)
- **Expanded melancholy mood word pools** — added 19 new words/phrases across all 8
  lexical categories (adjectives, elements, nouns, verbs, colors, adverbs, weathers,
  anomalies) to improve variety in melancholy-generated landscapes.
- **Melancholy adjectives**: 9 → 12, added `lonesome`, `overcast`, `muffled` — solitary,
  grey-sky, and subdued-qualitiy adjectives that deepen the melancholy register.
- **Melancholy elements**: 6 → 9, added `fog breath`, `candle glow`, `moss scent` —
  misty exhalation, weak warm light, and damp earthiness.
- **Melancholy nouns**: 6 → 9, added `shadows`, `windows`, `silhouettes` —
  indistinct forms and reflective surfaces that reinforce the soft-focus tone.
- **Melancholy verbs**: 7 → 9, added `yearn`, `mourn` — deep longing and
  quiet grief, the two most natural melancholy actions.
- **Melancholy colors**: 6 → 8, added `dove`, `lavender` — soft grey-blue and
  pale purple, both muted and tender tones.
- **Melancholy adverbs**: 5 → 7, added `tenderly`, `sadly` — gentle care and
  sorrowful manner.
- **Melancholy weathers**: 4 → 6, added:
  - `"a somber fog settles in the hollows, grey and patient"` — still, grey fog
    that waits in low places.
  - `"an amber twilight fades slowly into a bruised and heavy sky"` — fading
    evening light giving way to a weighty, bruised sky.
- **Melancholy anomalies**: 4 → 6, added:
  - `"A half-remembered melody drifts through the air, familiar yet impossible
    to place."` — ephemeral music that feels like a memory.
  - `"The sky reflects a landscape that is not this one — a place you almost
    recognize."` — impossible sky-reflection of an almost-familiar other place.
- **No code, CLI, or generation logic changes** — data-only expansion of the
  MOOD_WORDS["melancholy"] dictionary. All existing tests use dynamic checks over
  MOOD_WORDS keys and sets, so no test modifications were needed.
- This directly fulfills the first "Next likely step" from Session 186: "Expand
  the new melancholy word pools further." The melancholy mood now has 12 adjectives,
  9 elements, 9 nouns, 9 verbs, 8 colors, 7 adverbs, 6 weathers, and 6 anomalies.
- **Tests**: 1145 pass (448 subtests) — same count as Session 186.

### Current status
Working. All 1145 tests pass (18 todo + 1145 landscape).

### Next likely steps
- Expand the remaining mood word pools (peaceful, eerie, vibrant, desolate) for consistency
- Add more presets for diverse generation experiences
- Add a new biome or mood overlay

## 2026-07-21

### What was done (Session 186)
- **Added "gloaming" preset** — the 6th preset and the first to use the melancholy mood
  (added in Session 181). Until now, melancholy had no dedicated preset despite being
  available since Session 181. The new preset fills a twilight/rainy-day niche between
  pastoral (peaceful, sunny) and nightfall (eerie, dark), providing a wistful, soft-focus,
  introspective generation experience.
- **"gloaming" preset design**:
  - **Mood**: `["melancholy"]` — wistful, rainy, soft-focus emotional register.
  - **Weather**: high probability (2, prob=0.9) — rain, mist, and grey light.
  - **Anomalies**: moderate (1, prob=0.6) — melancholy-specific anomalies about memory
    and muted perception.
  - **Echoes**: high (2, prob=0.8) — atmospheric memory phrases fit the reflective tone.
  - **Wistful**: high (2, prob=0.9) — yearning closings complement the melancholy mood.
  - **Mood atmosphere**: high (2, prob=0.9) — melancholy's 4 atmosphere phrases about
    gentle sadness, soft heaviness, muffled sounds, and quiet ache.
  - **Legends**: low (1, prob=0.4) — sparingly used; folkloric lore feels too active for
    the introspective tone.
  - **Sounds**: moderate (1, prob=0.6) — hushed/muffled sonic register.
  - **Wildlife**: low (1, prob=0.3) — melancholy landscapes are quiet and sparsely
    inhabited.
  - **Time of day**: moderate (1, prob=0.7) — twilight/dusk/overcast times fit.
  - **Season**: moderate (1, prob=0.7) — autumn/early spring/rainy seasons fit.
  - **Perspectives**: moderate (1, prob=0.6) — adds spatial context without overwhelming.
  - **Simile/Metaphor/Personification**: moderate probabilities descending (0.7/0.6/0.5)
    — simile is most natural for melancholy, personification rarest.
  - **Travelogue**: enabled — journal-entry framing suits the reflective register.
- **Updated hardcoded preset lists**: `test_preset_produces_valid_output` and
  `test_preset_is_deterministic` now include `"gloaming"` in their iteration lists.
- **No code logic changes**: The preset system dynamically reads `PRESETS` dict keys for
  `--preset` choices and all dynamic tests use `for name in PRESETS`, so the preset is
  auto-available without any other code modifications. Only the two tests with hardcoded
  preset name lists needed manual updates.
- **Tests**: 1145 pass (18 todo + 1145 landscape) — same count as Session 185, with
  47 additional subtests (448 vs 401) from dynamic preset iteration tests.

### Current status
Working. All 1145 tests pass (18 todo + 1145 landscape).

### Next likely steps
- Expand the new melancholy word pools further
- Add more presets for diverse generation experiences
- Add a new biome or mood overlay

## 2026-07-21

### What was done (Session 184)
- **Expanded biome-specific weathers and anomalies for cave system, plain, and volcanic field**
  — each biome's weather pool grew from 5 to 7 entries and anomaly pool from 5 to 7
  entries, adding 6 new weathers and 6 new anomalies (12 phrases total). This is the
  8th–10th biomes to receive weather/anomaly expansion (following forest, ocean, desert
  in Session 180, ruined city in Session 182, and tundra, mountain range, swamp in
  Session 183).
- **New cave system weathers**:
  - `"a deep rumble echoes from the unseen depths, shaking loose ancient dust"` —
    subterranean tremor, a dynamic geological event shaking dust from ancient passages.
    Distinct from `"water drips in a slow, endless rhythm"` (steady dripping, not
    rumbling) and `"a draft carries the scent of deep earth"` (air movement, not
    vibration). Indicator: `"deep rumble echoes"`.
  - `"mineral-laden water trickles down the walls, leaving veins of silver and white"` —
    mineral deposition creating visible veins on cave walls. Distinct from `"water drips
    in a slow, endless rhythm"` (which is about auditory rhythm, not visual deposition)
    and `"a low mist hugs the cave floor"` (moisture in air, not on walls). Indicator:
    `"veins of silver and white"`.
- **New cave system anomalies**:
  - `"Your footsteps echo back as the voices of people who have not been born yet."` —
    temporal echo returning future voices instead of the present. Distinct from
    `"Passages rearrange when you blink"` (spatial, not temporal) and `"The cave breathes"`
    (kinetic, not auditory/temporal).
  - `"Fossils embedded in the cave walls shift their positions when no one is watching,
    forming new arrangements in the stone."` — animated fossils rearranging themselves
    when unobserved. Distinct from `"Stalactites grow toward each other at visible speed"`
    (mineral growth, not fossil movement).
- **New plain weathers**:
  - `"a thunderstorm brews on the distant edge of the plain, a curtain of black and silver
    advancing with purpose"` — approaching storm as a dramatic curtain across the plain.
    Distinct from `"a bank of fog rolls in from the horizon at dusk"` (fog, not storm)
    and `"clouds cast slow-moving shadows"` (passive clouds, not active storm front).
    Indicator: `"curtain of black and silver"`.
  - `"the setting sun paints the grasses gold and amber, turning the plain into a sea of
    fire"` — sunset illumination transforming the plain into a fiery expanse. Distinct
    from `"a warm wind sends ripples across the grass"` (wind-driven, not light-driven)
    and `"the sky stretches forever, blue and empty"` (daytime blue sky, not sunset).
    Indicator: `"plain into a sea of fire"`.
- **New plain anomalies**:
  - `"The wind carries whispers in a language that comes from the grass itself, not from
    any living throat."` — the grass speaking through the wind. Distinct from `"The grass
    grows in the shape of a language"` (visual linguistic patterns, not auditory speech).
    Adds an auditory/oracular register to the plain.
  - `"A single tree stands in the middle of the plain, though you remember there were no
    trees here a moment ago."` — impossible lone tree appearing unbidden. Distinct from
    `"Distant figures never get closer"` (humanoid figures, not arboreal) and `"There is
    no horizon"` (spatial boundary absence, not object appearance).
- **New volcanic field weathers**:
  - `"a low groan issues from deep within the earth, a sound that vibrates through bone
    before it reaches the ear"` — infrasonic volcanic groan, a body-felt sound. Distinct
    from `"steam vents hiss in ragged chorus"` (hissing steam, not deep groaning) and
    `"lava illuminates the smoke from below"` (visual, not auditory). Indicator:
    `"groan issues from deep"`.
  - `"lightning forks through the ash-filled sky, illuminating the wasteland in stark
    white flashes"` — volcanic lightning, dramatic electrical discharge through ash.
    Distinct from `"lava illuminates the smoke from below"` (steady glow from below,
    not sharp flashes from above). Indicator: `"lightning forks through"`.
- **New volcanic field anomalies**:
  - `"The ash does not fall — it rises, returning to the mountain as if the eruption is
    running backward in time."` — reversed ash fall, temporal inversion of eruption
    dynamics. Distinct from `"Lava flows uphill without reason"` (spatial reversal of
    lava, not temporal reversal of ash) and `"Molten rock flows in formations"` (rock
    patterns, not ash behavior).
  - `"Cracks in the earth glow with an inner light that does not illuminate, does not
    warm, but watches."` — sentient watchful light in fissures. Distinct from `"The
    heat does not burn — it freezes"` (temperature paradox, not light) and `"Obsidian
    shards show visions of the past"` (visual reflection, not ambient watching).
- **Updated WEATHER_INDICATORS** in test_landscape.py: Added 6 new invariant substrings
  for the new biome weather phrases so weather suppression/probability tests correctly
  cover the new weathers.
- **No code, CLI, or generation logic changes** — data-only expansion plus indicator
  additions. All existing tests use dynamic checks over `ALL_WEATHERS`, `ALL_ANOMALIES`,
  and `WEATHER_INDICATORS`, so no test logic changes were needed.
- This directly fulfills the first "Next likely step" from Session 183: "Expand biome-
  specific word pools further (more biomes, more entries)." 10 of 14 biomes now have
  expanded weathers/anomalies (forest, ocean, desert, ruined city, tundra, mountain
  range, swamp, cave system, plain, volcanic field). 4 biomes remain at 5 weathers and
  5 anomalies: coral reef, fungal grove, sky islands, crystal fields.
- Tests unchanged: 1145 passed (18 todo + 1145 landscape) — same as Session 183.

### Current status
Working. All 1163 tests pass (18 todo + 1145 landscape).

### Next likely steps
- Expand the new melancholy word pools further
- Add more presets for diverse generation experiences
- Add a new biome or mood overlay

## 2026-07-21

### What was done (Session 185)
- **Expanded biome-specific weathers and anomalies for the final 4 biomes**: coral reef,
  fungal grove, sky islands, and crystal fields — each biome's weather pool grew from
  5 to 7 entries and anomaly pool from 5 to 7 entries, adding 8 new weathers and 8 new
  anomalies (16 phrases total). This completes the biome-specific weather/anomaly
  expansion that began in Session 180 (forest, ocean, desert), continued through
  Session 182 (ruined city), Session 183 (tundra, mountain range, swamp), and Session
  184 (cave system, plain, volcanic field). All 14 biomes now have 7 weathers and 7
  anomalies each.
- **New coral reef weathers**:
  - `"a school of silvery fish wheels as one, a living constellation in the blue depths"` —
    coordinated fish movement as a living constellation. Distinct from `"sunlight dances
    on the water in shifting patterns"` (light pattern, not life) and `"warm currents
    drift through the coral canyons"` (current, not life). Indicator: `"living constellation"`.
  - `"bioluminescent plankton ignites in waves of blue-green fire at each breaking swell"` —
    bioluminescence triggered by wave action. Distinct from `"the water is clear and
    impossibly blue"` (color, not bioluminescence). Indicator: `"bioluminescent plankton ignites"`.
- **New coral reef anomalies**:
  - `"The coral has grown around a structure that was never built — pillars and archways
    of living calcium, older than any civilization."` — ancient organic architecture in
    the coral, structures that predate civilization. Distinct from `"The coral pulses in
    unison like a single heart"` (living unity, not architecture).
  - `"The water grows shallower the deeper you swim, as if the ocean has forgotten which
    way is down."` — impossible depth inversion, ocean losing its orientation. Distinct
    from `"Time passes differently here"` (temporal, not spatial).
- **New fungal grove weathers**:
  - `"bioluminescent caps pulse in slow waves of light, a breathing garden of soft fire"` —
    coordinated bioluminescent pulsing of mushroom caps. Distinct from `"the ground pulses
    with faint blue light"` (ground-level, not caps) and `"a warm mist carries the sweet
    scent of fungal bloom"` (olfactory, not visual). Indicator: `"caps pulse in slow waves"`.
  - `"a fine veil of spores settles on everything, muffling the world in velvet silence"` —
    spore veil creating acoustic muffling. Distinct from `"spore-laden rain falls in
    curtains of gold and silver"` (falling, not settled). Indicator: `"veil of spores settles"`.
- **New fungal grove anomalies**:
  - `"The mushrooms grow in the shape of things you have forgotten — lost faces, abandoned
    places, words you meant to say."` — mushrooms forming memory-shaped structures.
    Distinct from `"Spores form faces when they settle"` (simple faces, not complex
    memory shapes) and `"Fungal growths form temporary sculptures"` (abstract, not personal).
  - `"Breathing in, the spores carry whispers of a past that belongs to the grove, not
    to you."` — spores transmitting the grove's own memories through inhalation.
    Distinct from `"The mycelium network reacts to your thoughts"` (responding to you,
    not you receiving its past).
- **New sky islands weathers**:
  - `"a bank of luminous clouds rises from below, bathing the islands in pearl-grey light"` —
    luminous rising clouds creating soft ambient light. Distinct from `"clouds churn far
    below like a white sea"` (distant churning, not rising) and `"a thin mist wraps each
    island in solitude"` (wrapping, not rising upward). Indicator: `"bank of luminous clouds"`.
  - `"the stars pierce the thin air above with an intensity that feels like sound — cold,
    clear, infinite"` — extreme clarity of stars at high altitude, synesthetic
    sound-of-light. Distinct from `"lightning arcs silently between nearby islands"`
    (electrical discharge, not stellar). Indicator: `"stars pierce the thin air"`.
- **New sky islands anomalies**:
  - `"When you look down, you see yourself standing on a different island, looking up at
    this one."` — recursive self-observation, vertiginous Doppelgänger across the
    archipelago. Distinct from `"The islands orbit each other in a slow dance"` (orbital
    movement, not recursive selves) and `"The islands cast shadows onto the clouds below"`
    (shadow autonomy, not self-recursion).
  - `"The clouds below form words, forming and dissolving — a message from the sky to
    itself that no one can read."` — clouds writing ephemeral language. Distinct from
    `"A bell tolls from an island that no one has ever reached"` (auditory, not visual).
- **New crystal fields weathers**:
  - `"a cascade of prismatic light sweeps across the field as the sun shifts, painting
    everything in shifting spectra"` — sweeping spectrum of light across crystals as the
    sun moves. Distinct from `"light scatters into a thousand colors across the crystal
    faces"` (scattering, not sweeping) and `"the air shimmers with refracted light"`
    (ambient shimmer, not directional sweep). Indicator: `"cascade of prismatic light"`.
  - `"a shimmering heat haze rises from the crystal formations, distorting the world into
    liquid geometry"` — heat haze warping perception into fluid shapes. Distinct from
    `"the air shimmers with refracted light from a hidden source"` (light-based shimmer,
    not heat-based distortion). Indicator: `"liquid geometry"`.
- **New crystal fields anomalies**:
  - `"The crystals grow when you are not watching — a slow, patient accretion that reverses
    when you turn back."` — quantum-observer crystal growth that reverses under direct
    observation. Distinct from `"Every facet shows a different moment in time"` (time
    facets, not growth) and `"The crystals reflect a sky that is not above you"` (reflection,
    not accretion).
  - `"Your reflection in the crystal faces does not mirror you — it continues moving after
    you have stopped, living a life of its own."` — independent reflection with its own
    agency. Distinct from `"Shadows move in directions that contradict the position of the
    sun"` (shadow autonomy, not reflection autonomy).
- **Updated WEATHER_INDICATORS** in test_landscape.py: Added 8 new invariant substrings
  for the new biome weather phrases so weather suppression/probability tests correctly
  cover the new weathers.
- **No code, CLI, or generation logic changes** — data-only expansion plus indicator
  additions. All existing tests use dynamic checks over `ALL_WEATHERS`, `ALL_ANOMALIES`,
  and `WEATHER_INDICATORS`, so no test logic changes were needed.
- **Milestone**: This is the final batch of biome-specific weather/anomaly expansion.
  All 14 biomes now have 7 weathers and 7 anomalies each (up from the original 5 and 5).
  Over 5 sessions (180–185), 18 new weathers and 18 new anomalies (36 phrases total)
  were added across 14 biomes.
- Tests unchanged: 1145 passed (18 todo + 1145 landscape) — same as Session 184.

## 2026-07-21

### What was done (Session 183)
- **Expanded biome-specific weathers and anomalies for tundra, mountain range, and swamp**
  — each biome's weather pool grew from 5 to 7 entries and anomaly pool from 5 to 7
  entries, adding 6 new weathers and 6 new anomalies (12 phrases total). This is the
  5th–7th biomes to receive weather/anomaly expansion (following forest, ocean, desert
  in Session 180, and ruined city in Session 182).
- **New tundra weathers**:
  - `"a hoarfrost settles on every surface, turning the world to crystal and bone"` —
    hoarfrost crystallizing everything in a frozen white blanket. Distinct from `"ice
    crystals hang in the air like frozen diamonds"` (airborne, not settled) and `"snow
    falls in a world of white and silence" (active snowfall, not surface frost).
    Indicator: `"hoarfrost settles"`.
  - `"the wind screams across the open ice, carrying the sound of a thousand frozen
    voices"` — wind as an auditory scream across open ice. Distinct from `"a biting
    wind carries ice crystals"` (tactile, about crystal impact). Indicator:
    `"wind screams across"`.
- **New tundra anomalies**:
  - `"The permafrost exhales a breath of ancient air, carrying the smell of a world
    that died long ago."` — permafrost releasing prehistoric atmosphere. Distinct from
    `"The ice sings when the wind blows across it"` (musical, not olfactory) and `"Shapes
    move beneath the frozen surface"` (visual movement, not exhalation).
  - `"Your shadow freezes to the ground behind you, a dark stain on the white that does
    not fade."` — shadow as a permanent stain on the snow. Distinct from `"The aurora
    casts shadows that move on their own"` (independent moving shadows) — this is about
    the shadow being stuck, not autonomous.
- **New mountain range weathers**:
  - `"a sudden avalanche thunders down the slopes, a river of white and stone"` —
    avalanche as a dynamic catastrophic event. Distinct from all existing weathers
    (wind, cloud, snow fall, warm wind). No existing mountain range weather covers
    violent mass movement. Indicator: `"avalanche thunders"`.
  - `"clouds boil over the ridgeline, spilling into the valleys below in slow cascades"` —
    clouds spilling over ridges like slow waterfalls. Distinct from `"clouds cling to
    the peaks like shawls"` (static clinging, not dynamic spilling). Indicator:
    `"boil over the ridgeline"`.
- **New mountain range anomalies**:
  - `"The mountain breathes — a slow expansion and contraction of its entire mass, as
    if stone has lungs."` — the mountain as a living entity with breath. Distinct from
    `"Echoes return minutes after you speak"` (auditory, not kinetic). Adds a
    living-stone register.
  - `"Each step upward feels lighter, as if the mountain is pulling you toward its
    summit."` — reverse gravity / attraction toward the summit. Distinct from `"The
    mountain casts two shadows under a single sun"` (optical, not gravitational).
- **New swamp weathers**:
  - `"warm rain falls in heavy droplets, each splash releasing a puff of mist from the
    stagnant water"` — warm rain causing mist explosions on contact with still water.
    Distinct from `"fog rolls low over the black water"` (fog rolling in, not rain on
    water) and `"thunder rolls across the marsh without lightning"` (auditory, not
    percussive). Indicator: `"warm rain falls in heavy droplets"`.
  - `"a slow rain of shed leaves and seed pods patters on the dark water, a percussion
    of tiny impacts"` — organic debris falling on water like a percussion instrument.
    Distinct from `"gnats swarm in the stagnant heat"` (living insects, not falling
    debris). Indicator: `"shed leaves and seed pods"`.
- **New swamp anomalies**:
  - `"The water is perfectly still, yet the reflection shows ripples that never reach
    the surface."` — reflection out of sync with reality, showing movement where there
    is none. Distinct from `"The water reflects a world that no longer exists"` (a
    different world, not the same world with different physics).
  - `"Trees that were on your left are now on your right, though you never turned
    around."` — impossible physical rearrangement of the environment. Distinct from
    `"Will-o'-wisps flicker in perfect constellations"` (light-based, not spatial).
- **Updated WEATHER_INDICATORS** in test_landscape.py: Added 6 new invariant substrings
  for the new biome weather phrases so weather suppression/probability tests correctly
  cover the new weathers.
- **No code, CLI, or generation logic changes** — data-only expansion plus indicator
  additions. All existing tests use dynamic checks over `ALL_WEATHERS`, `ALL_ANOMALIES`,
  and `WEATHER_INDICATORS`, so no test logic changes were needed.
- This directly fulfills the first "Next likely step" from Session 182: "Expand biome-
  specific word pools further (more biomes, more entries)." 7 of 14 biomes now have
  expanded weathers/anomalies (forest, ocean, desert, ruined city, tundra, mountain
  range, swamp). 7 biomes remain at 5 weathers and 5 anomalies.
- Tests unchanged: 1145 passed (18 todo + 1145 landscape) — same as Session 182.

### Current status
Working. All 1163 tests pass (18 todo + 1145 landscape).

### Next likely steps
- Expand biome-specific word pools further (more biomes, more entries)
- Add more presets for diverse generation experiences
- Expand the new melancholy word pools further

## 2026-07-21

### What was done (Session 182)
- **Expanded biome-specific weathers and anomalies for "ruined city"** — the
  only human-constructed (ruined) biome in the project. Weathers grew from 5→7
  and anomalies from 5→7, adding 4 new phrases total. This is the 4th biome to
  get expanded weathers/anomalies (following forest, ocean, and desert in
  Session 180).
- **New ruined city weathers**:
  - `"a heavy fog settles in the lower streets, swallowing the ground floor of
    every building"` — urban fog filling the lower levels of abandoned structures.
    Distinct from all existing ruined city weathers (ash, smog, wind, drizzle,
    dust devils). Indicator: `"swallowing the ground floor"`.
  - `"rain drums on broken glass and rusted metal in a rhythm without pattern"` —
    percussive rain on debris creating an arrhythmic soundscape. Distinct from
    `"a rust-colored drizzle stains the concrete further"` (which is about
    staining and visual effect, not sound). Indicator: `"rain drums on"`.
- **New ruined city anomalies**:
  - `"The silhouettes of people flicker in doorways — frozen mid-stride, mid-word,
    mid-thought — from a time that never was."` — ghostly frozen figures from an
    unreal past, like a city that never existed. Distinct from `"Shadows of people
    who aren't there move along the walls"` (existing, which describes moving
    shadows vs. frozen silhouettes here). This is about temporal freezing rather
    than fluid ghost movement.
  - `"Every street leads back to the same intersection, no matter which direction
    you choose."` — impossible looping street geometry. Distinct from `"The street
    signs point in directions that don't exist"` (misleading signs vs. looping
    streets) and `"The city gives birth to new streets at night"` (map
    self-modification vs. looping).
- **Updated WEATHER_INDICATORS** in test_landscape.py: Added 2 new invariant
  substrings (`"swallowing the ground floor"`, `"rain drums on"`) so weather
  suppression/probability tests correctly cover the new ruined city weather
  phrases.
- **No code, CLI, or generation logic changes** — data-only expansion plus
  indicator additions. All existing tests use dynamic checks over
  `ALL_WEATHERS`, `ALL_ANOMALIES`, and `WEATHER_INDICATORS`, so no test logic
  changes were needed.
- This directly fulfills the first "Next likely step" from Session 181: "Expand
  biome-specific word pools further (more biomes, more entries)." 4 of 14 biomes
  now have expanded weathers/anomalies (forest, ocean, desert, ruined city).
  10 biomes remain at 5 weathers and 5 anomalies.
- Tests unchanged: 1163 tests pass (18 todo + 1145 landscape) — same as
  Session 181.

### Current status
Working. All 1163 tests pass (18 todo + 1145 landscape).

### Next likely steps
- Expand biome-specific word pools further (more biomes, more entries)
- Add more presets for diverse generation experiences
- Expand the new melancholy word pools further

## 2026-07-21

### What was done (Session 181)
- **Added new mood overlay: "melancholy"** — a wistful, rainy, soft-focus emotional
  register that fills the mood gap between "peaceful" (calm/gentle) and "desolate"
  (barren/hopeless). This is the first new mood since the desolate mood was added
  alongside the others at inception.
- **MOOD_WORDS["melancholy"] entry created** with 8 full word pools:
  - **Adjectives (9)**: wistful, rain-soaked, grey, faded, weeping, hushed, somber, tender, sighing
  - **Elements (6)**: rain scent, grey light, distant thunder, wet stone, amber glow, tear-warmth
  - **Nouns (6)**: rainclouds, puddles, veils, whispers, echoes, doorways
  - **Verbs (7)**: weep, fade, linger, sigh, ache, remember, drift
  - **Colors (6)**: grey, silver, pale blue, muted, soft grey, faded rose
  - **Adverbs (5)**: softly, quietly, wistfully, slowly, heavily
  - **Weathers (4)**: a soft rain falls without end, mist clings to everything, the light is grey and tender, a quiet drizzle dampens the world
  - **Anomalies (4)**: rain falling upward carrying tears, shadows holding silent memories, world in slow motion weighted with unspoken things, colors draining to grey when looked at directly
- **MOOD_ATMOSPHERE["melancholy"] added** with 4 atmosphere phrases:
  - "There is a gentle sadness in the air, like the end of a beautiful day."
  - "The world feels soft and heavy, as if it is holding its breath and remembering."
  - "Every sound seems muffled, as though the landscape itself is lost in thought."
  - "A quiet ache hangs in the air, tender and familiar, like a half-forgotten lullaby."
- **Added TestMelancholyMood class** (8 tests) following the TestPeacefulMood pattern:
  - Does not break output (20 seeds)
  - Word weight boosted for melancholy-matched words (wistful)
  - Word weight not boosted for unmatched words (crystal)
  - Combines with other moods (eerie, peaceful, desolate)
  - Deterministic with same seed
  - Melancholy-specific adjectives appear across 200 seeds
  - JSON output includes mood field
  - CLI flag exists
- **Updated 7 existing test methods** that hardcoded mood lists to include "melancholy":
  `test_describe_all_contains_all_moods`, `test_describe_all_moods_flag_prints_multiple`,
  `test_peaceful_mood_combine_with_other_moods`, `test_does_not_break_output`,
  `test_works_with_all_moods`, `test_works_with_mood_combine`,
  `test_multi_atmosphere_with_count_three`, `test_does_not_repeat_same_phrase`.
- **Added MELANCHOLY_ATMOSPHERE_INDICATORS** to MOOD_ATMOSPHERE_INDICATORS for
  test detection of melancholy atmosphere phrases.
- This directly fulfills the second "Next likely step" from Session 180:
  "Add a new mood overlay." The melancholy mood is the 5th mood (joining peaceful,
  eerie, vibrant, desolate) and the first new mood addition.
- Tests: 1163 pass (18 todo + 1145 landscape) — up from 1155.
  Landscape tests grew from 1137 to 1145 (+8 for the new test class).

### Current status
Working. All 1163 tests pass (18 todo + 1145 landscape).

### Next likely steps
- Expand biome-specific word pools further (more biomes, more entries)
- Add more presets for diverse generation experiences
- Expand the new melancholy word pools further

## 2026-07-21

### What was done (Session 180)
- **Expanded biome-specific weathers and anomalies for forest, ocean, and desert**
  — each biome's weather pool grew from 5 to 7 entries and anomaly pool from 5
  to 7 entries, adding 6 new weathers and 6 new anomalies (12 phrases total).
  This is the first expansion of any biome-specific word pool.
- **New forest weathers**:
  - `"a flock of birds rises from the canopy in a rush of wings"` — sudden bird
    flush, a brief explosive ascent of birds from the canopy. Distinct from `"a
    soft wind stirs the leaves overhead"` (wind, not birds) and `"sunlight filters
    through the canopy"` (light, not movement). Indicator: `"rush of wings"`.
  - `"a heavy mist settles between the trees, turning the world to silhouettes"` —
    dense ground fog in the forest that reduces the world to shapes. Distinct from
    `"sunlight filters through the canopy in golden beams"` (sunny, not foggy).
    Indicator: `"world to silhouettes"`.
- **New forest anomalies**:
  - `"The trees have faces carved into their bark — faces that change expression
    when you look away."` — living watching tree faces, distinct from `"Every leaf
    faces the same direction"` (vegetative orientation, not faces) and `"The trees
    grow in a perfect circle"` (geometry, not faces).
  - `"A path appears where there was none before, leading deeper into the woods."` —
    shifting forest path that materializes unbidden, distinct from `"Fungal spores
    hang in the air"` (airborne, not path-based).
- **New ocean weathers**:
  - `"a squall line approaches, whipping the surface into white foam"` — sudden
    storm squall, distinct from `"waves roll in from an unseen horizon"` (regular
    waves) and `"rain falls on the surface like a thousand drummers"` (rain).
    Indicator: `"white foam"`.
  - `"the sea is glass-calm, reflecting the sky so perfectly you cannot tell where
    one begins"` — dead calm mirror surface, distinct from `"the water is eerily
    still and black"` (dark stillness, not reflection). Indicator: `"glass-calm"`.
- **New ocean anomalies**:
  - `"The ocean breathes — a slow rise and fall of the entire surface, as if the
    sea itself has lungs."` — ocean as living breather, distinct from `"The water
    glows with an inner light"` (luminous, not breathing).
  - `"A shipwreck floats on the horizon, but it is the same shipwreck that was
    there yesterday, and the day before."` — persistent unchanging shipwreck,
    distinct from `"Whales sing in frequencies that vibrate through bone"` (auditory,
    not visual).
- **New desert weathers**:
  - `"a haboob swallows the horizon, a wall of dust and sand advancing with
    terrible purpose"` — massive dust storm wall, distinct from `"sandstorms
    gather on the horizon like walls of amber"` (distant, less immediate).
    Indicator: `"haboob swallows"`.
  - `"the air shimmers with phantom pools of water that vanish as you approach"` —
    mirage pools that recede, distinct from `"heat ripples rise from the sand in
    waves"` (heat haze, not water illusion). Indicator: `"phantom pools"`.
- **New desert anomalies**:
  - `"The stars are too close here — you can hear them humming."` — audible stars,
    distinct from `"The stars rearrange themselves into unfamiliar constellations"`
    (visual rearrangement, not auditory).
  - `"Cacti and rocks cast shadows that point inward toward a single, unseen
    center."` — convergent shadow geometry, distinct from `"The dunes form perfect
    geometric spirals"` (dune patterns, not shadows).
- **Updated WEATHER_INDICATORS** in test_landscape.py: Added 6 new invariant
  substrings for the new biome weather phrases so weather suppression/probability
  tests correctly cover the new biome weathers.
- **No code, CLI, or generation logic changes** — data-only expansion plus
  indicator additions. All existing tests use dynamic checks over `ALL_WEATHERS`,
  `ALL_ANOMALIES`, and `WEATHER_INDICATORS`, so no test logic changes were needed.
- This directly fulfills the first "Next likely step" from Session 179: "Expand
  biome-specific word pools (weathers, anomalies per biome)." This is the first
  expansion of biome-specific pools since the project began — every biome had
  exactly 5 weathers and 5 anomalies from inception.
- Tests unchanged: 1155 tests pass (18 todo + 1137 landscape) — same as Session 179.

### Current status
Working. All 1155 tests pass (18 todo + 1137 landscape).

### Next likely steps
- Expand biome-specific word pools further (more biomes, more entries)
- Add a new mood overlay
- Add more presets for diverse generation experiences

## 2026-07-21

### What was done (Session 179)
- **Expanded WEATHERS from 15 to 20 entries** — 5 new weather phrases covering
  sleet, debris swirl, sunbreak, humidity, and dust — niches underrepresented
  in the existing 15.
- **Expanded ANOMALIES from 15 to 20 entries** — 5 new anomaly phrases covering
  phantom self, responsive vegetation, temporal voice echo, temperature inversion,
  and fractal repetition — niches underrepresented in the existing 15.
- **New weathers**:
  - `"a sharp wind drives needles of sleet through the air"` — sleet/freezing
    rain, a cold precipitation distinct from snow (existing) and fog (existing).
    Covers icy mixed precipitation. Indicator: `"drives needles of sleet"`.
  - `"leaves and debris swirl in sudden eddies of wind"` — dynamic debris swirl,
    distinct from "ash drifts slowly downward" (slow, ash) and "mist curls along
    the ground" (low, mist). This is about active wind-driven debris. Indicator:
    `"swirl in sudden eddies"`.
  - `"the sun breaks through the clouds in shafts of amber light"` — dramatic
    sunbreak, distinct from "the air shimmers with heat" (heat shimmer) and
    "lightning flickers on the horizon" (storm light). Covers sudden sunlight.
    Indicator: `"shafts of amber light"`.
  - `"the air hangs heavy and damp, thick enough to taste"` — oppressive humidity,
    distinct from "a still calm lingers" (dry stillness) and "the air grows thick
    with the promise of thunder" (storm pressure). Covers heavy wet air.
    Indicator: `"heavy and damp"`.
  - `"a fine dust rises in spirals, catching the light like scattered gold"` —
    dust devils/particulate light, distinct from "ash drifts slowly downward"
    (falling ash) and "mist curls along the ground" (moisture). Covers dry
    particulate rising. Indicator: `"fine dust rises in spirals"`.
- **New anomalies**:
  - `"You see your own figure in the distance, walking a path you have not yet
    taken."` — phantom self/premonition, distinct from "Every step you take rings
    twice" (temporal echo of past steps). This is about a future self seen ahead.
  - `"The plants turn to face you as you pass, their leaves tracking your
    movement."` — responsive vegetation, no existing anomaly covers living
    plants reacting to the observer.
  - `"Your words echo back to you in a voice that is yours, but not from this
    moment."` — temporal voice echo, distinct from "Every step you take rings
    twice" (footstep echo). This is about spoken words returned from another time.
  - `"The air is warm here, though frost covers the ground at your feet."` —
    temperature inversion, no existing anomaly covers localized impossible
    temperature.
  - `"Every rock, every tree, every blade of grass is arranged in the same
    pattern, repeated to infinity."` — fractal repetition, distinct from "The
    geometry of the landscape follows rules you cannot quite recall" (uncanny
    geometry). This is about visible identical repetition.
- **Updated WEATHER_INDICATORS** in test_landscape.py: Added 5 new invariant
  substrings for the new weather phrases so that weather suppression/probability
  tests correctly cover the new phrases.
- **No code, CLI, or generation logic changes** — data-only expansion plus
  indicator additions. All existing tests use dynamic checks over `ALL_WEATHERS`,
  `ALL_ANOMALIES`, and `WEATHER_INDICATORS`, so no test logic changes were needed.
- **New words are default-weight**: All 10 new entries use the "normal" weight
  tier, appropriate for balanced appearance rates under normal bias. None are
  marked COMMON or RARE.
- This directly fulfills the first "Next likely step" from Session 178: "Expand
  global word pools further (WEATHERS, ANOMALIES from 15 to 20)." All 8 global
  pools are now at 20 entries — a milestone for consistency.
- Tests unchanged: 1155 tests pass (18 todo + 1137 landscape) — same as Session 178.

### Current status
Working. All 1155 tests pass (18 todo + 1137 landscape).

### Next likely steps
- Expand biome-specific word pools (weathers, anomalies per biome)
- Add a new mood overlay
- Add more presets for diverse generation experiences

## 2026-07-21

### What was done (Session 178)
- **Expanded 5 global word pools from 15 to 20 entries each** — ELEMENTS, NOUNS,
  VERBS, ADVERBS, and COLORS each gained 5 carefully chosen entries, adding 25
  new words/phrases total. ADJECTIVES was already at 20 from Session 173 and was
  not expanded.
- **ELEMENTS (+5)**: `hoarfrost` (frozen crystalline deposit), `sunflare` (intense
  solar burst), `earth scent` (geosmin/petrichor), `moon glow` (reflected lunar
  light), `raindamp` (active wetness/humidity). These cover cold/growth, celestial/
  radiant, earthy/mineral, nocturnal/celestial, and aqueous/moisture niches
  underrepresented in the existing 15.
- **NOUNS (+5)**: `ridges` (linear elevated crests), `waterfalls` (vertical aquatic
  cascades), `chambers` (enclosed interior rooms), `passages` (narrow connecting
  routes), `ledges` (horizontal shelf-like projections). These cover linear/
  vertical/interior/transitional/horizontal niches underrepresented in the
  existing 15.
- **VERBS (+5)**: `emerge` (appearance/coming-into-being), `curl` (sinuous winding),
  `mirror` (reflection/copying), `linger` (persistence/remaining), `surge`
  (forceful forward motion). These cover emergence, sinuous, reflective,
  persistent, and forceful movement niches underrepresented in the existing 15.
- **ADVERBS (+5)**: `abruptly` (sudden/sharp), `wearily` (tired/exhausted),
  `fiercely` (intense/forceful), `hesitantly` (uncertain/reluctant), `lightly`
  (gentle/delicate). These cover suddenness, fatigue, intensity, uncertainty, and
  delicacy niches underrepresented in the existing 15.
- **COLORS (+5)**: `ochre` (warm earth yellow), `vermilion` (bright red-orange),
  `teal` (blue-green), `plum` (deep purple), `ash` (pale grey-white). These cover
  warm earth, vibrant red-orange, blue-green, deep purple, and pale grey niches
  underrepresented in the existing 15.
- **No code, CLI, or generation logic changes** — data-only expansion. All existing
  tests use dynamic checks over `ALL_ADJECTIVES`, `ALL_ELEMENTS`, etc. (derived
  sets that auto-include new additions), so no test modifications were needed.
  No `WEATHER_INDICATORS` update needed because no weather entries were added.
- **New words are default-weight**: All 25 new entries use the "normal" weight
  tier, appropriate for balanced appearance rates under normal bias. None are
  marked COMMON or RARE.
- This directly fulfills the first "Next likely step" from Session 177: "Expand
  global word pools further (more adjectives, elements, nouns, verbs)." All 8
  global pools are now at 20 entries (ADJECTIVES was already at 20 from Session
  173; WEATHERS and ANOMALIES remain at 15 from Session 173 and can be expanded
  in a future session).
- Tests unchanged: 1137 landscape tests pass (399 subtests), 18 todo unchanged.
- Total: 1155 tests pass.

### Current status
Working. All 1155 tests pass (18 todo + 1137 landscape).

### Next likely steps
- Expand global word pools further (WEATHERS, ANOMALIES from 15 to 20)
- Expand biome-specific word pools (weathers, anomalies per biome)
- Add a new mood overlay
- Add more presets for diverse generation experiences

## 2026-07-21

### What was done (Session 177)
- **Added new biome: "crystal fields"** — a surface landscape of massive crystal
  formations, prismatic light, and resonant mineral energy. This is the 14th biome
  and the first new biome since "sky islands" was added.
- **BIOMES list expanded**: `"crystal fields"` added to the 13 existing biomes.
- **BIOME_WORDS entry created** with 8 full word pools (adjectives, elements,
  nouns, verbs, colors, adverbs, weathers, anomalies):
  - **Adjectives (8)**: `prismatic`, `faceted`, `resonant`, `shard-strewn`,
    `refractive`, `geometric`, `crystalline`, `iridescent`
  - **Elements (7)**: `crystal hum`, `prism light`, `shard glow`, `facet gleam`,
    `refracted ray`, `resonance`, `glass chime`
  - **Nouns (7)**: `spires`, `facets`, `prisms`, `shards`, `clusters`, `geodes`,
    `formations`
  - **Verbs (7)**: `refract`, `resonate`, `gleam`, `scatter`, `chime`, `catch`,
    `split`
  - **Colors (7)**: `prismatic`, `glass-clear`, `lavender`, `rose-quartz`,
    `citrine`, `amethyst`, `beryl`
  - **Adverbs (5)**: `brilliantly`, `sharply`, `clearly`, `geometrically`,
    `brightly`
  - **Weathers (5)**: light scattering across crystal faces, low hum from deep
    formations, crystals singing in the wind, crystal dust floating like gems,
    shimmering refracted light
  - **Anomalies (5)**: sky reflected in crystals, facets showing different times,
    sound traveling in straight lines, crystal harmonies forming impossible chords,
    shadows contradicting the sun
- **Designed to fill a unique niche**: No existing biome covers a crystalline/
  reflective surface landscape. "crystal fields" sits between "cave system"
  (underground minerals) and "volcanic field" (destructive earth forces) but is
  an open-air landscape of growth, refraction, and resonance.
- **3 new tests** in `TestNewBiomes` (`test_crystal_fields_in_biomes_list`,
  `test_crystal_fields_produces_valid_output`,
  `test_crystal_fields_uses_specific_vocabulary`) — following the same pattern
  as the 3 existing "new biome" test sets. Also updated
  `test_new_biomes_appear_in_random_selection` to include `"crystal fields"`.
- Tests pass: 1137 landscape tests (+3 from 1134), 18 todo unchanged.
- Total: 1155 tests pass.

### Current status
Working. All 1155 tests pass (18 todo + 1137 landscape).

### Next likely steps
- Expand global word pools further (more adjectives, elements, nouns, verbs)
- Expand biome-specific word pools (weathers, anomalies per biome)
- Add a new mood overlay
- Add more presets for diverse generation experiences

## 2026-07-21

### What was done (Session 176)
- **Added `wistful_count` and `wistful_prob` to all 5 presets** with varied,
  meaningful values that enhance each preset's character:
  - **nightfall**: `wistful_count=2, wistful_prob=0.8` — twice the yearning in
    a reflective, eerie setting, but not guaranteed each time
  - **pastoral**: `wistful_count=1, wistful_prob=0.7` — occasional gentle
    wistfulness, matching the peaceful tone
  - **sublime**: `wistful_count=2, wistful_prob=0.9` — near-certain double
    wistfulness befitting the rich, vibrant setting
  - **wasteland**: `wistful_count=1, wistful_prob=1.0` — always exactly one
    wistful phrase; desolation always carries a pang
  - **dreamscape**: `wistful_count=2, wistful_prob=0.85` — dreamlike double
    wistfulness with a slight chance of suppression
- Prior to this session, all 5 presets had `"wistful": True` but none specified
  `wistful_count` or `wistful_prob`, so they all used the defaults (1 and 1.0).
  Now each preset has distinctive wistful density, matching the varied count/prob
  values every other feature (echo, legend, sound, wildlife, time, season,
  perspective, simile, metaphor, personification, mood_atmosphere) already had
  in their presets.
- This directly fulfills the final "Next likely step" from Session 175:
  "Add wistful_count/wistful_prob to presets with varied values."
- Tests unchanged: still 1134 landscape tests pass (18 todo unchanged).

### Current status
Working. All 1152 tests pass (18 todo + 1134 landscape).

### Next likely steps
- Expand global word pools further (more adjectives, elements, nouns, verbs)
- Expand biome-specific word pools (weathers, anomalies per biome)
- Add a new biome or mood

## 2026-07-19

### What was done (Session 173)
- **Expanded all 8 global word pools** — ADJECTIVES (16→20), ELEMENTS (10→15),
  NOUNS (12→15), VERBS (10→15), ADVERBS (12→15), COLORS (12→15),
  WEATHERS (12→15), and ANOMALIES (12→15) — adding 29 new words/phrases total.
  This is the first expansion of these foundational pools since the project began.
- **ADJECTIVES**: Added `phantom`, `hollow`, `sunless`, `star-scattered` —
  spectral/void/celestial adjectives not represented in the existing 16.
- **ELEMENTS**: Added `phosphorescence`, `thunder`, `breath`, `resonance`,
  `glimmer` — luminous/auditory/vital elements not represented in the existing 10.
- **NOUNS**: Added `monoliths`, `terraces`, `basins` — grand/terraced/concave
  landscape forms not represented in the existing 12.
- **VERBS**: Added `breathe`, `sing`, `shiver`, `bloom`, `fold` —
  organic/auditory/transformative verbs not represented in the existing 10.
- **ADVERBS**: Added `lazily`, `heavily`, `perpetually` —
  languid/dense/endless adverbs not represented in the existing 12.
- **COLORS**: Added `opal`, `argent`, `sepia` —
  iridescent/silver/antique colors not represented in the existing 12 colors.
- **WEATHERS**: Added `"a thin mist rises from the warming stone"`,
  `"a slow wind carries the smell of distant rain"`,
  `"the air grows thick with the promise of thunder"` —
  thermal-rising/scent-carrying/pressure-building weathers not represented
  in the existing 12.
- **ANOMALIES**: Added `"The light here has no source — it simply exists."`,
  `"Every step you take rings twice, once now and once long ago."`,
  `"Birds glide in spirals that form equations no living eye has solved."` —
  sourceless-light/temporal-echo/mathematical-bird anomalies not represented
  in the existing 12.
- **Updated WEATHER_INDICATORS** in test_landscape.py: Added 3 new invariant
  substrings for the new weather phrases (`"thin mist rises from"`,
  `"smell of distant rain"`, `"promise of thunder"`) so that weather
  suppression/probability tests correctly cover the new phrases.
- No code, CLI, or generation logic changes — data-only expansion plus indicator
  additions. All existing tests use dynamic checks over `ALL_ADJECTIVES`,
  `ALL_ELEMENTS`, etc. (which auto-include global + biome words), so no test
  modifications were needed beyond WEATHER_INDICATORS.
- Each new word is in the default "normal" weight tier — not COMMON or RARE —
  appropriate for balanced appearance rates under normal bias.
- This directly fulfills the second "Next likely step" from Session 172:
  "Expand the global word pools (ADJECTIVES, ELEMENTS, NOUNS, etc.)."
  These pools had been at their original sizes since Session 1 (entire project
  lifespan) and were overdue for expansion.

### Current status
Working. All 1144 tests pass (18 todo + 1126 landscape).

### Next likely steps
- Expand global word pools further (more adjectives, elements, nouns, verbs)
- Expand biome-specific word pools (weathers, anomalies per biome)
- Add a new biome or mood

## 2026-07-19

### What was done (Session 172)
- **Expanded TRAVELOGUE word bank from 4 to 9 prefix/suffix pairs** — 5 new
  prefix constructions and 5 new suffix constructions added, covering expedition
  narrative styles not represented in the existing 4:
  - **New prefixes**: `"Captain's log, supplemental. Day {day}. The {display} has
    appeared on the horizon."` (sci-fi log), `"Letter from the expedition, day
    {day}. I write to you from the {display}."` (epistolary), `"Field notes, day
    {day}. The {display} eludes easy description."` (scientific field notes),
    `"Dispatch {day}. The {display} stretches before us, indifferent and vast."`
    (terse dispatch), `"I have journeyed {day} days to reach the {display}, and
    now I stand at its edge."` (personal travel narrative).
  - **New suffixes**: `"I sit at the edge of camp and watch the {display} settle
    into darkness."` (reflective evening), `"The map does not capture what the
    {display} truly is."` (cartographic humility), `"I will need many more days
    to cross the {display}, if the weather holds."` (forward planning),
    `"The {display} offers no answers, but it asks better questions than I do."`
    (philosophical), `"Tomorrow, the {display} will still be here, waiting."`
    (endurance/perseverance).
- **Updated test indicators**: Added new unique invariant substrings to
  `TestTravelogue.TRAVELOGUE_INDICATORS`, `TestTravelogue.TRAVELOGUE_SUFFIX_INDICATORS`,
  and the module-level `TRAVELOGUE_INDICATORS` (used by `TestNoTravelogue`).
- **Fixed hardcoded prefix check** in `TestPresets.test_preset_with_travelogue_produces_framed_output`
  — added the 5 new prefix substrings to the `has_travelogue` conditional.
- **Fixed regex** in `TestTravelogue.test_travelogue_contains_day_number` — the
  original regex `\bday (\d+)\b` only matched "day N" order. New prefixes use
  `Dispatch {day}.` and `journeyed {day} days`, so the regex was broadened to
  `\bday \d+|\d+ days?\b` with case-insensitive flag.
- No code, CLI, or generation logic changes — data-only expansion plus test
  updates. All existing travelogue tests use dynamic checks over the lists.
- Each new prefix/suffix occupies a distinct narrative niche. None overlap with
  the existing 4 prefixes or 4 suffixes.
- This directly fulfills the first "Next likely step" from Session 171: "Expand
  travelogue word bank (more prefix/suffix pairs, more narrative styles)."
  TRAVELOGUE was the only word bank below 20 phrases — now at 9 prefixes and 9
  suffixes.

### Current status
Working. All 1144 tests pass (18 todo + 1126 landscape).

### Next likely steps
- Expand word bank further with more niche constructions
- Expand the global word pools (ADJECTIVES, ELEMENTS, NOUNS, etc.)
- Add a new biome or mood

## 2026-07-19

### What was done (Session 171)
- **Expanded PERSPECTIVES word bank from 15 to 20 phrases** — 5 new perspective
  constructions added, covering spatial/vantage niches not represented in the
  existing 15:
  - `"Through a cleft in the {adj} {color} {element}, the {display} reveals
    itself {adverb} in a sudden, vertiginous glimpse."` — a narrow aperture
    (cleft/gap) revealing the landscape in a sudden vertiginous instant.
    Distinct from "Up close" (steady texture observation) and "Seen from the
    heights" (unfolding panorama). This is about a narrow opening that yields a
    dizzying full view. Indicator: `"vertiginous glimpse"`.
  - `"At the foot of the {display}, the {adj} {color} {element} rises {adverb}
    in a vertical cascade that dwarfs the sky."` — looking up from the base at
    a towering vertical rise. Distinct from "At ground level" (overwhelming
    scale in general) and "Approaching" (silhouette growing on the horizon).
    This is about immediate vertical ascent from the base. Indicator:
    `"vertical cascade that dwarfs"`.
  - `"Peering over the edge of the {display}, the {adj} {color} {element}
    drops {adverb} into a depth that swallows the light."` — looking down from
    a precipice into a light-consuming abyss. Distinct from "Seen from above"
    (static pattern from above) and "Drifting above" (aerial floating). This
    is about vertigo-inducing depth beneath a ledge. Indicator:
    `"depth that swallows"`.
  - `"From across a {adj} chasm of {color} {element}, the {display} appears
    {adverb} suspended, a vision in the middle of the air."` — the landscape
    seen across a separating gulf, appearing as a suspended floating vision.
    Distinct from "From a distance" (whisper on the horizon, diminishing) and
    "Reflected in a pool" (transformed reflection). This is about the landscape
    as a vision suspended across a void. Indicator: `"suspended, a vision in"`.
  - `"From the summit of the {display}, the {adj} {color} {element} radiates
    {adverb} in all directions, a world without edges."` — a 360-degree summit
    panorama without boundaries. Distinct from "Seen from the heights"
    (unfolding like an arranged map) and "The {display} stretches" (into a
    single distance). This is about radial, unbounded expansion in every
    direction. Indicator: `"world without edges"`.
- **Added 5 new indicators to `PERSPECTIVE_INDICATORS`** in test_landscape.py:
  `"vertiginous glimpse"`, `"vertical cascade that dwarfs"`,
  `"depth that swallows"`, `"suspended, a vision in"`,
  `"world without edges"` — each is a unique invariant substring for dynamic
  test matching.
- No code, CLI, or generation logic changes — data-only expansion plus
  indicator additions. All existing perspective tests use dynamic checks over
  `PERSPECTIVE_INDICATORS` and `len(PERSPECTIVES)`, requiring no test
  modifications.
- Each phrase is curated to fit a distinct spatial/vantage niche: narrow cleft
  revelation, base-to-summit vertical, precipice depth, chasm-suspended vision,
  summit panorama. None overlap with the existing 15 phrases.
- This directly fulfills the first "Next likely step" from Session 170: "Expand
  perspectives word bank (more phrases, more varied constructions)."
  PERSPECTIVES was the most overdue major bank — last expanded in Session 147
  (23 sessions ago) when perspectives was first introduced. All major word banks
  are now at 20 phrases — a milestone for the project.
- Tests unchanged: still 1126 landscape tests pass (18 todo unchanged).

### Current status
Working. All 1144 tests pass (18 todo + 1126 landscape).

### Next likely steps
- Expand travelogue word bank (more prefix/suffix pairs, more narrative styles)

## 2026-07-19

### What was done (Session 170)
- **Expanded WILDLIFE word bank from 15 to 20 phrases** — 5 new wildlife
  constructions added, covering wildlife niches not represented in the existing 15:
  - `"Bats wheel {adverb} through the {adj} twilight of the {display}, {color} shapes
    against the fading {element}."` — nocturnal flyers wheeling through twilight, bats
    as elusive silhouettes against the fading sky. Distinct from "bird of prey circles"
    (diurnal hunter, clear view) and "small birds flit" (daytime, small-scale). This is
    about silent, erratic flight at dusk. Indicator: `"Bats wheel"`.
  - `"A {adj} snake coils {adverb} among the {color} {element} of the {display},
    tasting the air with a forked tongue."` — a reptile coiled in stillness, sensing
    the world through its tongue. No existing wildlife phrase describes a reptile or
    ground-level predator lying in ambush. Distinct from "something hunts at the edge"
    (mammalian predator tracking prey) and "something small chitters" (noisy, visible).
    Indicator: `"forked tongue"`.
  - `"Fish leap {adverb} from the {adj} waters of the {display}, {color} flashes
    arcing through the {element}."` — aquatic life breaking the surface, brief
    silver/gold arcs of motion. No existing wildlife phrase describes any aquatic
    creature. Distinct from "Fireflies drift" (airborne insects, not water) and
    "hum of wings rises" (collective buzz, not individual leaping). Indicator:
    `"Fish leap"`.
  - `"Crows roost {adverb} in the {adj} branches of the {display}, their {color} eyes
    tracking your every move."` — carrion birds as watchful sentinels, their collective
    gaze following the traveler. Distinct from "bird of prey circles" (active hunting,
    solitary) and "eyes watch from the shadows" (unidentified watcher, not specifically
    avian). This is about recognized scavenger birds observing you. Indicator:
    `"Crows roost"`.
  - `"{adj} moths flutter {adverb} around the {color} {element} of the {display},
    drawn by a light only they can see."` — delicate moths drawn to an invisible light,
    silent and ethereal. Distinct from "Fireflies drift" (which glow with their own
    light) and "hum of wings" (collective swarm sound). This is about silent,
    individual, light-seeking insects. Indicator: `"moths flutter"`.
- **Added 5 new indicators to `WILDLIFE_INDICATORS`** in test_landscape.py:
  `"Bats wheel"`, `"forked tongue"`, `"Fish leap"`, `"Crows roost"`,
  `"moths flutter"` — each is a unique invariant substring for dynamic test matching.
- No code, CLI, or generation logic changes — data-only expansion plus indicator
  additions. All existing wildlife tests use dynamic checks over `WILDLIFE_INDICATORS`
  and `len(WILDLIFE)`, requiring no test modifications.
- Each phrase is curated to fit a distinct wildlife niche: nocturnal flyers,
  ground-level reptile, aquatic leaping, scavenger sentinels, delicate light-seeking
  insects. None overlap with the existing 15 phrases.
- This directly fulfills the first "Next likely step" from Session 169: "Expand
  wildlife word bank (more phrases, more varied constructions)." WILDLIFE was the
  most overdue bank alongside PERSPECTIVES — last expanded in Session 143 (26 sessions
  ago) when it grew from 10 to 15. All major word banks except PERSPECTIVES (15) are
  now at 20 phrases.
- Tests unchanged: still 1126 landscape tests pass (18 todo unchanged).

### Current status
Working. All 1144 tests pass (18 todo + 1126 landscape).

### Next likely steps
- Expand perspectives word bank (more phrases, more varied constructions)
- Expand travelogue word bank (more prefix/suffix pairs, more narrative styles)

## 2026-07-19

### What was done (Session 169)
- **Expanded SOUNDSCAPES word bank from 17 to 20 phrases** — 3 new soundscape
  constructions added, covering sonic niches not represented in the existing 17:
  - `"A distant thunder rumbles {adverb} from beneath the {display}, a {adj} sound
    that vibrates through the {color} {element}."` — deep subterranean thunder, a
    rumbling vibration from beneath the world. Distinct from "drone rises and falls"
    (continuous mechanical hum) and "something large shifts and settles" (discrete
    movement). This is about deep, sustained vibration. Indicator: `"thunder rumbles"`.
  - `"Steam hisses {adverb} from fissures in the {adj} {element} of the {display}, a
    {color} breath of heat escaping."` — geothermal hissing/steam escaping from
    fissures. Distinct from "crackles like distant radio static" (electrical, not
    steam) and "breathing" (organic, not geothermal). Indicator: `"Steam hisses"`.
  - `"A {adj} clicking echoes {adverb} through the {display}, a {color} sound that
    never quite settles into a pattern."` — irregular clicking/ticking, a broken
    rhythm that resists pattern. Distinct from "rhythm pulses" (regular, patient
    pulse) and "note rings out" (single discrete note). Indicator:
    `"never quite settles into a pattern"`.
- **Added 3 new indicators to `SOUND_INDICATORS`** in test_landscape.py:
  `"thunder rumbles"`, `"Steam hisses"`, `"never quite settles into a pattern"` —
  each is a unique invariant substring for dynamic test matching.
- No code, CLI, or generation logic changes — data-only expansion plus indicator
  additions. All existing soundscape tests use dynamic checks over `SOUND_INDICATORS`,
  requiring no test modifications.
- Each phrase is curated to fit a distinct sonic niche: subterranean thunder,
  geothermal hissing, irregular clicking. None overlap with the existing 17 phrases.
- This directly fulfills the first "Next likely step" from Session 168: "Expand other
  word banks (soundscapes, wildlife, perspectives) with more phrases." SOUNDSCAPES
  was the smallest major bank at 17 phrases — now at 20 alongside all other major banks.
- Tests unchanged: still 1126 landscape tests pass (18 todo unchanged).

### Current status
Working. All 1144 tests pass (18 todo + 1126 landscape).

### Next likely steps
- Expand wildlife word bank (more phrases, more varied constructions)
- Expand perspectives word bank (more phrases, more varied constructions)
- Expand travelogue word bank (more prefix/suffix pairs, more narrative styles)

- **Expanded WISTFUL word bank from 15 to 20 phrases** — 5 new wistful constructions
  added, covering emotional/reflective niches not represented in the existing 15:
  - `"The {display} holds the stories you whispered into its silence, keeping them safe
    long after you have gone."` — the landscape as a confidant/keeper of secrets,
    holding whispered confessions in trust. Distinct from "carry a piece" (which is
    about carrying a fragment with you) and "settled into your bones" (internalized
    presence). Indicator: `"whispered into its silence"`.
  - `"Every place you visit after the {display} feels like a copy, a pale imitation of
    what you have seen."` — the landscape as the original benchmark against which
    everything else is judged and found wanting. Distinct from "world outside feels
    diminished" (which is about the world being lesser, not an imitation/copy).
    Indicator: `"pale imitation"`.
  - `"The {display} feels like a story you arrived too late to hear the beginning of,
    and had to leave before the end."` — the landscape as an interrupted narrative,
    a story you arrived in the middle of and missed both start and conclusion.
    Distinct from "version of yourself behind" (a self left behind) and "wish you could
    stay longer" (desire to remain). Indicator: `"too late to hear"`.
  - `"No matter where you go, the {display} remains the fixed point against which all
    other places are measured."` — the landscape as an unchanging anchor of memory,
    the reference point against which all future places are compared. Distinct from
    "settled into your bones" (carried within you) and "carry a piece" (fragment
    carried). Indicator: `"fixed point against"`.
  - `"The {display} belongs to a time that is passing, and you were fortunate to have
    seen it before it faded completely."` — the landscape as a bygone era glimpsed at
    the final moment of its existence. Distinct from "fortunate to have walked" (gratitude
    for having visited regardless of time) and "part of you will always remain" (part
    stays behind). Indicator: `"before it faded"`.
- **Added 5 new indicators to `WISTFUL_INDICATORS`** in test_landscape.py:
  `"whispered into its silence"`, `"pale imitation"`, `"too late to hear"`,
  `"fixed point against"`, `"before it faded"` — each is a unique invariant substring
  for dynamic test matching.
- **Added same 5 indicators to `WISTFUL_INDICATORS_PHRASES`** — consistent with the
  pattern; all new indicators are safe for `--no-wistful` suppression tests.
- **Updated hardcoded `wistful_indicators`** in TestPresets
  `test_preset_with_wistful_produces_wistful_output` — this test used a locally-defined
  list rather than the class or module-level constants, requiring a manual update.
- No code, CLI, or generation logic changes — data-only expansion plus indicator
  additions. All existing wistful tests use dynamic checks over `WISTFUL_INDICATORS`
  or `WISTFUL_INDICATORS_PHRASES`, requiring no test modifications.
- Each phrase is curated to fit a distinct wistful niche: keeper of secrets, benchmark
  imitation, interrupted story, fixed reference point, fading glimpse. None overlap with
  the existing 15 phrases.
- This directly fulfills the second "Next likely step" from Session 167: "Expand wistful
  word bank further (more phrases, more varied constructions)." WISTFUL was last expanded
  in Session 162 (5 sessions ago) when it grew from 10 to 15. Every other major word bank
  was already at 20 phrases.
- Tests unchanged: still 1126 landscape tests pass (18 todo unchanged).

### Current status
Working. All 1144 tests pass (18 todo + 1126 landscape).

### Next likely steps
- Expand simile word bank further (more phrases, more varied constructions)
- Expand other word banks (soundscapes, wildlife, perspectives) with more phrases

## 2026-07-19

### What was done (Session 166)
- **Expanded METAPHORS word bank from 15 to 20 phrases** — 5 new metaphor constructions
  added, covering figurative identity niches not represented in the original 15:
  - `"The {display} is a {adj} bridge of {color} {element}, arching {adverb} between what
    is remembered and what is lost."` — the landscape as a bridge connecting past and
    present across the gulf of forgetting. Distinct from "threshold" (which is about
    passage/transition) and "argument" (which is about conflict/tension). Indicator:
    `"arching between"`.
  - `"The {display} is a {adj} tide of {color} {element}, pulled {adverb} by a forgotten
    gravity."` — the landscape as a cyclical force drawn by an invisible pull. Distinct
    from "heart" (which is about rhythmic pulse of life) and "anchor" (which is about
    steadiness/resistance). Indicator: `"forgotten gravity"`.
  - `"The {display} is a {adj} garden of {color} {element}, cultivated {adverb} by an
    unseen hand."` — the landscape as a cultivated garden tended by invisible forces.
    Distinct from "forge" (which is about active creation/hammering) and "feast" (which
    is about abundance/consumption). Indicator: `"unseen hand"`.
  - `"The {display} is a {adj} veil of {color} {element}, concealing {adverb} a world
    within a world."` — the landscape as a veil hiding a deeper nested reality.
    Distinct from "mirror" (which is about reflection/revelation) and "threshold" (which
    is about passage). Indicator: `"world within a world"`.
  - `"The {display} is a {adj} tomb of {color} {element}, sealed {adverb} around the
    silence of ages."` — the landscape as a tomb containing ancient silence. Distinct
    from "wound" (which is about injury/bleeding) and "armor" (which is about
    protection). Indicator: `"silence of ages"`.
- **Added 5 new indicators to `METAPHOR_INDICATORS`** in test_landscape.py:
  `"arching between"`, `"forgotten gravity"`, `"unseen hand"`,
  `"world within a world"`, `"silence of ages"` — each is a unique invariant substring
  for dynamic test matching.
- No code, CLI, or generation logic changes — data-only expansion plus indicator
  additions. All existing metaphor tests use dynamic checks over `METAPHOR_INDICATORS`,
  requiring no test modifications.
- Each phrase is curated to fit a distinct figurative niche: timeless bridge, cyclical
  tide, cultivated garden, concealing veil, sealed tomb. None overlap with the existing
  15 phrases.
- This directly fulfills the first "Next likely step" from Session 165: "Expand metaphor
  word bank further (more phrases, more varied constructions)." METAPHORS was the most
  overdue bank alongside PERSONIFICATIONS — last expanded in Session 159 (6 sessions
  ago). ECHOES (20), TIMES_OF_DAY (20), SEASONS (20), LEGENDS (20), and SIMILES (20)
  were all at 20 phrases, while METAPHORS and PERSONIFICATIONS were at 15.
- Tests unchanged: still 1126 landscape tests pass (18 todo unchanged).

### Current status
Working. All 1144 tests pass (18 todo + 1126 landscape).

### Next likely steps
- Expand simile word bank further (more phrases, more varied constructions)
- Expand wistful word bank further (more phrases, more varied constructions)

## 2026-07-19

### What was done (Session 167)
- **Expanded PERSONIFICATIONS word bank from 15 to 20 phrases** — 5 new personification
  constructions added, covering human-action niches not represented in the original 15:
  - `"The {display} roars {adverb} with a {adj} voice of {color} {element}, shaking the
    sky."` — the landscape as a roaring entity with a voice of raw power that trembles
    the heavens. Distinct from "voice carries" (which is about beauty/song) and "weeps"
    (which is about grief/sorrow). This is about elemental force and power. Indicator:
    `"shaking the sky"`.
  - `"The {display} waits {adverb} in {adj} patience, its {color} {element} holding a
    breath that spans ages."` — the landscape in patient anticipation across ages.
    Distinct from "dreams" (unconscious sleep) and "listens" (active attention). This
    is about purposeful stillness and waiting. Indicator: `"breath that spans ages"`.
  - `"The {adj} {element} of the {display} teaches {adverb}, each {color} facet a word
    in an ancient lesson."` — the landscape as an active teacher revealing wisdom through
    its features. Distinct from "remembers" (passive memory/history) and "whispers"
    (secret knowledge). This is about active instruction. Indicator: `"ancient lesson"`.
  - `"The {display} burns {adverb} with a {adj} {color} fire that the {element} cannot
    quench."` — the landscape as an inextinguishable inner fire. Distinct from "heart
    beats" (pulse/vitality) and "dances" (artistic movement). This is about consuming
    elemental fire. Indicator: `"cannot quench"`.
  - `"The {display} towers {adverb} in {adj} stillness, a {color} {element} standing
    against the sky."` — the landscape asserting its vertical presence against the sky.
    Distinct from "reaches out" (horizontal grasping) and "bows" (lowering in reverence).
    This is about vertical majesty. Indicator: `"standing against the sky"`.
- **Added 5 new indicators to `PERSONIFICATION_INDICATORS`** in test_landscape.py:
  `"shaking the sky"`, `"breath that spans ages"`, `"ancient lesson"`,
  `"cannot quench"`, `"standing against the sky"` — each is a unique invariant substring
  for dynamic test matching.
- No code, CLI, or generation logic changes — data-only expansion plus indicator
  additions. All existing personification tests use dynamic checks over
  `PERSONIFICATION_INDICATORS`, requiring no test modifications.
- Each phrase is curated to fit a distinct human-action niche: roaring power, patient
  waiting, active teaching, inextinguishable burning, vertical towering. None overlap
  with the existing 15 phrases.
- This directly fulfills the first "Next likely step" from Session 166: "Expand
  personification word bank further (more phrases, more varied constructions)."
  PERSONIFICATIONS was the only bank at 15 phrases — now all major word banks are at
  20 phrases (ECHOES, TIMES_OF_DAY, SEASONS, LEGENDS, SIMILES, METAPHORS,
  PERSONIFICATIONS).
- Tests unchanged: still 1126 landscape tests pass (18 todo unchanged).

### Current status
Working. All 1144 tests pass (18 todo + 1126 landscape).

### Next likely steps
- Expand simile word bank further (more phrases, more varied constructions)
- Expand wistful word bank further (more phrases, more varied constructions)
- Expand travelogue word bank (more prefix/suffix pairs, more narrative styles)

## 2026-07-19

### What was done (Session 165)
- **Expanded SIMILES word bank from 15 to 20 phrases** — 5 new simile constructions
  added, covering figurative niches not represented in the original 15:
  - `"The {display} rises {adverb} like a {adj} temple of {color} {element}, each
    tier reaching toward the sky."` — sacred architecture rising, the landscape as
    a temple reaching upward. Distinct from "stretches like a tapestry" (woven
    sprawl, not vertical rise) and "unfolds like a dream" (gradual revelation, not
    structural ascent). Indicator: `"reaching toward the sky"`.
  - `"The {display} stirs {adverb} like a {adj} beast of {color} {element}, rousing
    from a sleep outlasting ages."` — awakening beast, the landscape as a creature
    emerging from aeons-long slumber. Distinct from "breathes like a great slumbering
    element" (steady breath, not awakening) and "moves through the display like a
    living thing" (continuous motion, not emerging). Indicator: `"rousing from a
    sleep"`.
  - `"The {color} {element} of the {display} curls {adverb} like a {adj} wave frozen
    at the moment of breaking."` — frozen wave, motion arrested at its peak.
    Distinct from "shifts like a living map" (continuous change) and "edge trembles
    like a line drawn in liquid" (trembling, not frozen). Indicator: `"wave frozen"`.
  - `"The {adj} {element} of the {display} burns {adverb} like a {color} flame that
    needs no fuel."` — self-sustaining flame, the element as an inexhaustible fire.
    Distinct from "glow like embers" (dying embers, not active flame) and "light
    pools like water in a dry element-bed" (liquid, not fire). Indicator: `"needs no
    fuel"`.
  - `"The {display} reflects {adverb} like a {adj} {color} mirror of {element},
    showing a world that never was."` — alternate reflection, the landscape as a
    mirror into an impossible world. Distinct from "feels like a half-remembered
    memory" (internal emotion, not external mirror) and "light of the display falls
    like dust" (downward fall, not reflection). Indicator: `"world that never was"`.
  - Each new phrase uses 3-5 template slots (`{display}`, `{adj}`, `{color}`,
    `{element}`, `{adverb}`) and occupies a distinct figurative niche: sacred
    architecture, awakening beast, frozen wave, self-sustaining flame, alternate
    mirror.
- **Added 5 new indicators to `SIMILE_INDICATORS`** in test_landscape.py:
  `"reaching toward the sky"`, `"rousing from a sleep"`, `"wave frozen"`,
  `"needs no fuel"`, `"world that never was"` — each is a unique invariant
  substring for dynamic test matching.
- **Fixed fragile `PERSPECTIVE_INDICATORS` entry `"like a living map"`** — changed
  to `"unfolds beneath you"` because `"like a living map"` matched the simile
  phrase "...shifts like a living map..." which the RNG drift from the new similes
  exposed. `"unfolds beneath you"` is unique to the perspective phrase "Drifting
  above the display, the expanse unfolds beneath you like a living map" and immune
  to cross-feature matching.
- **Fixed fragile `METAPHOR_INDICATORS` entry `"that never was"`** — changed to
  `"memories of a"` because `"that never was"` would match the new simile phrase
  "showing a world that never was". The metaphor phrase is "The shapes of the
  display are memories of a element that never was" — `"memories of a"` is the
  invariant substring that uniquely identifies it.
- No code, CLI, or generation logic changes — data-only expansion plus indicator
  additions and two indicator fixes. All existing simile tests use dynamic checks
  over `ALL_SIMILES` (which is `set(SIMILES)`) or `SIMILE_INDICATORS`, requiring
  no test modifications.
- Each phrase is curated to fit a distinct figurative niche: sacred architecture,
  awakening beast, frozen wave, self-sustaining flame, alternate mirror. None
  overlap with the existing 15 phrases.
- This directly fulfills the first "Next likely step" from Session 164: "Expand
  simile word bank further (more phrases, more varied constructions)." SIMILES was
  the most overdue figurative language bank alongside METAPHORS and PERSONIFICATIONS
  — last expanded in Session 158 (6 sessions ago) when it grew from 10 to 15.
  ECHOES (20), TIMES_OF_DAY (20), SEASONS (20), and LEGENDS (20) were all larger.
- Tests unchanged: still 1126 landscape tests pass (18 todo unchanged).

### Current status
Working. All 1144 tests pass (18 todo + 1126 landscape).

### Next likely steps
- Expand metaphor word bank further (more phrases, more varied constructions)
- Expand personification word bank further (more phrases, more varied constructions)
- Expand simile word bank further (more phrases, more varied constructions)

## 2026-07-19

### What was done (Session 164)
- **Expanded SEASONS word bank from 15 to 20 phrases** — 5 new seasonal
  constructions added, covering seasonal/atmospheric niches not represented in the
  original 15:
  - `"Summer thunderheads pile on the horizon, the air heavy with electricity and the
    scent of rain"` — summer thunderstorm build-up, air charged with electrical
    tension before the storm breaks. Distinct from "Spring thunder rolls across a
    landscape reborn from rain" (spring rebirth, not summer electrical tension).
    Indicator: `"thunderheads pile"`.
  - `"An Indian summer warmth lingers in the golden light, leaves just beginning to
    turn at their edges"` — Indian summer / early autumn warmth with leaves at the
    first blush of color, a brief return of warmth before decay. Distinct from "A
    sharp autumn chill" (cold, not warm) and "Autumn has turned the landscape into a
    study in gold and decay" (advanced autumn, not early). Indicator: `"Indian summer
    warmth lingers"`.
  - `"Snow falls in a thick white silence, erasing the world one flake at a time"`
    — active heavy snowfall as an erasing, transformative process. Distinct from
    "The first snow of winter has fallen, muffling the world in white" (first snow,
    muffling after the fact) and "A hard winter freeze transforms the landscape into
    a palace of crystal and ice" (freeze state, not active snowfall). Indicator:
    `"thick white silence"`.
  - `"Spring wildflowers blanket the landscape in cascades of color, as if the earth
    itself celebrates"` — spring bloom as a colorful celebratory eruption. Distinct
    from "the first buds push through the thawing earth" (early spring, nascent buds)
    and "The tender green of late spring covers everything in new growth" (foliage,
    not flowers). Indicator: `"Spring wildflowers blanket"`.
  - `"Autumn fog wraps the landscape in grey stillness, the world reduced to soft
    suggestion"` — autumn fog as soft grey diffusion, muting the world. Distinct
    from "Late autumn strips the landscape bare" (bareness, not diffusion) and "A
    pale autumn sun hangs low" (direct sun, not fog). Indicator: `"Autumn fog wraps
    the landscape"`.
  - Each new phrase is a literal string (not a template), consistent with all existing
    SEASONS entries, and occupies a distinct seasonal niche: summer thunderstorm,
    Indian summer warmth, heavy snowfall, spring wildflowers, autumn fog.
- **Added 5 new indicators to `SEASON_INDICATORS`** in test_landscape.py:
  `"thunderheads pile"`, `"Indian summer warmth lingers"`, `"thick white silence"`,
  `"Spring wildflowers blanket"`, `"Autumn fog wraps the landscape"` — each is a
  unique invariant substring for dynamic test matching.
- No code, CLI, or generation logic changes — data-only expansion plus indicator
  additions. All existing season tests use dynamic checks over `ALL_SEASONS` (which
  is `set(SEASONS)`) or `SEASON_INDICATORS`, requiring no test modifications. The
  `describe_seasons` tests loop over `SEASONS` and use `len(SEASONS)`, adapting
  automatically.
- Each phrase is curated to fit a distinct seasonal niche: summer thunderstorm
  electrical tension, Indian summer warmth, active heavy snowfall, spring
  wildflower bloom, autumn fog stillness. None overlap with the existing 15 phrases.
- This directly fulfills the first "Next likely step" from Session 163: "Expand
  seasons word bank (more phrases, more varied constructions)." SEASONS was the
  most overdue bank — last expanded in Session 135 (28 sessions ago) when it grew
  from 10 to 15. Every other major bank had been expanded more recently.
- Tests unchanged: still 1126 landscape tests pass (18 todo unchanged).

### Current status
Working. All 1144 tests pass (18 todo + 1126 landscape).

### Next likely steps
- Expand simile word bank further (more phrases, more varied constructions)
- Expand metaphor word bank further (more phrases, more varied constructions)
- Expand personification word bank further (more phrases, more varied constructions)

## 2026-07-19

### What was done (Session 163)
- **Expanded TIMES_OF_DAY word bank from 15 to 20 phrases** — 5 new time-of-day
  constructions added, covering temporal/atmospheric niches not represented in the
  original 15:
  - `"Sunset bleeds across the landscape in ribbons of amber and rose"` — dramatic
    sunset as flowing color, adding a painterly sunset register distinct from dusk
    (fading to darkness) and twilight (night taking hold). Indicator: `"amber and rose"`.
  - `"A full moon rises over the landscape, turning everything to silver and shadow"`
    — full moon night with transformative silver light, distinct from the crescent
    moon of "Midnight beneath a crescent moon" and the blackness of "starless night".
    Indicator: `"full moon rises"`.
  - `"The heavy stillness of noon settles over the landscape like a held breath"`
    — noon as oppressive stillness and breathless pause, distinct from "blazing noon
    sun" which is harsh and punishing rather than still. Indicator: `"heavy stillness of noon"`.
  - `"The deepest dark before dawn wraps the landscape in a final moment of absolute
    night"` — pre-dawn as the darkest hour, a liminal moment before light returns,
    distinct from "dead of night" (night holding the land) and "starless night"
    (pressing down). Indicator: `"deepest dark before dawn"`.
  - `"Low grey clouds press down upon the landscape, muting the world in soft silver
    light"` — overcast/grey day with muted silver light, distinct from "storm-heavy
    sky" which is about threat and coming storms rather than soft diffusion.
    Indicator: `"Low grey clouds"`.
  - Each new phrase is a literal string (not a template), consistent with all existing
    TIMES_OF_DAY entries, and occupies a distinct temporal niche: dramatic sunset,
    full moon night, noon stillness, pre-dawn darkness, overcast grey day.
- **Added 5 new indicators to `TIME_INDICATORS`** in test_landscape.py:
  `"amber and rose"`, `"full moon rises"`, `"heavy stillness of noon"`,
  `"deepest dark before dawn"`, `"Low grey clouds"` — each is a unique invariant
  substring for dynamic test matching.
- No code, CLI, or generation logic changes — data-only expansion plus indicator
  additions. All existing time-of-day tests use dynamic checks over `ALL_TIMES_OF_DAY`
  (which is `set(TIMES_OF_DAY)`) or `TIME_INDICATORS`, requiring no test modifications.
  The `describe_times` tests loop over `TIMES_OF_DAY` and use `len(TIMES_OF_DAY)`,
  adapting automatically.
- Each phrase is curated to fit a distinct temporal/atmospheric niche: dramatic
  sunset, full moon night, oppressive noon stillness, pre-dawn liminal darkness,
  overcast grey day. None overlap with the existing 15 phrases.
- This directly fulfills the first "Next likely step" from Session 162: "Expand
  time-of-day word bank (more phrases, more varied constructions)." TIMES_OF_DAY
  was the most overdue bank alongside SEASONS and SIMILES — last expanded in
  Session 133 (29 sessions ago) when it grew from 10 to 15.
- Tests unchanged: still 1126 landscape tests pass (18 todo unchanged).

### Current status
Working. All 1144 tests pass (18 todo + 1126 landscape).

### Next likely steps
- Expand seasons word bank (more phrases, more varied constructions)
- Expand simile word bank further (more phrases, more varied constructions)
- Expand metaphor word bank further (more phrases, more varied constructions)

## 2026-07-19

### What was done (Session 162)
- **Expanded WISTFUL word bank from 10 to 15 phrases** — 5 new wistful constructions added,
  covering emotional/reflective niches not represented in the original 10:
  - `"You count yourself fortunate to have walked through the {display}, if only once."`
    — gratitude and honor for having witnessed the landscape, a tone of humble thankfulness.
    Distinct from "words will never be enough" (ineffability) and "lucky enough to see it"
    (which is about uniqueness). Indicator: `"fortunate to have walked"`.
  - `"The {display} has settled into your bones, a quiet presence you carry wherever you
    go."` — the landscape as an internalized, somatic presence that travels with you.
    Distinct from "carry a piece" (which is about carrying a fragment) and "always remain"
    (which is about staying behind). Indicator: `"settled into your bones"`.
  - `"The world outside the {display} feels diminished, as though you have seen something
    the rest of the world has not."` — the landscape as an experience that diminishes
    everything else by comparison, a secret only you now carry. Distinct from "never be
    the same" (personal transformation) and "nowhere else in the world like" (uniqueness
    of place). Indicator: `"the rest of the world has not"`.
  - `"You left a version of yourself behind in the {display}, one that still walks its
    paths in silence."` — a doppelgänger/alternate-self left behind in the landscape,
    adding a ghostly, bifurcated-self register. Distinct from "always remain" (a piece
    stays) and "carry a piece" (a piece goes with you); this is about a whole self left
    behind. Indicator: `"version of yourself behind"`.
  - `"In quiet moments you find yourself back in the {display}, as if it exists just
    behind your eyelids."` — the landscape as a persistent afterimage, accessed in quiet
    moments by closing one's eyes. Distinct from "half-remembered dream" (which is about
    the dreamlike quality of the memory) and "lingers in your thoughts" (cognitive
    lingering); this is about voluntary re-access through sensory recall. Indicator:
    `"just behind your eyelids"`.
  - Each new phrase uses only the `{display}` template slot (like all existing wistful
    phrases) and occupies a distinct emotional niche: gratitude, internalized presence,
    diminished outside world, bifurcated self, sensory afterimage.
- **Added 5 new indicators to `WISTFUL_INDICATORS`** in the TestWistful class:
  `"fortunate to have walked"`, `"settled into your bones"`, `"the rest of the world has
  not"`, `"version of yourself behind"`, `"just behind your eyelids"` — each is a unique
  invariant substring for dynamic test matching.
- **Added same 5 indicators to `WISTFUL_INDICATORS_PHRASES`** — consistent with the
  pattern; all new indicators are safe for `--no-wistful` suppression tests.
- **Updated hardcoded `wistful_indicators`** in `TestPresets.test_preset_with_wistful_produces_wistful_output`
  — this test used a locally-defined list rather than the class or module-level constants,
  so it needed a manual update to include the new indicators.
- No code, CLI, or generation logic changes — data-only expansion plus indicator
  additions. Most existing wistful tests use dynamic checks over `WISTFUL_INDICATORS`
  or `WISTFUL_INDICATORS_PHRASES`, requiring no test modifications. The one exception
  was the hardcoded list in `TestPresets`.
- Each phrase is curated to fit a distinct wistful niche: gratitude/thankfulness,
  internalized somatic presence, diminished outside world, bifurcated self, sensory
  afterimage. None overlap with the existing 10 phrases.
- This directly fulfills the "Next likely steps" from Session 161: "Expand wistful word
  bank (more phrases, more varied constructions)." Wistful was the smallest bank at 10
  phrases and the most overdue since its creation in Session 123 (38 sessions ago).
- Tests unchanged: still 1126 landscape tests pass (18 todo unchanged).

### Current status
Working. All 1144 tests pass (18 todo + 1126 landscape).

### Next likely steps
- Expand time-of-day word bank (more phrases, more varied constructions)
- Expand seasons word bank (more phrases, more varied constructions)
- Expand simile word bank further (more phrases, more varied constructions)

## 2026-07-19

### What was done (Session 161)
- **Expanded ECHOES word bank from 15 to 20 phrases** — 5 new echo constructions added,
  covering atmospheric niches not represented in the original 15:
  - `"The {adj} roads of the {display} lead nowhere {adverb}, their {color} {element}
    worn smooth by travelers who never were."` — the landscape's paths as ghost
    infrastructure leading nowhere, suggesting a non-existent history. The only echo
    describing roads or routes; distinct from "holds its breath" (anticipation) and
    "important happened" (past event). Indicator: `"roads of the"`.
  - `"Fragments of {color} whispers drift {adverb} through the {adj} air of the {display}
    {time_word}."` — half-heard auditory fragments, incoherent whispers. Distinct from
    "wind carries a memory... a voice with no mouth" (a single coherent voice) and
    "echoes of the past linger" (generalized lingering). Indicator: `"Fragments of"`.
  - `"The {display} mourns {adverb} {time_word}, its {adj} {color} {element} heavy with
    a grief that knows no end."` — the landscape actively grieving, adding a sorrow/
    mourning register distinct from "holds its breath" (anticipation) and "older than
    any sound" (primordial silence). Indicator: `"mourns"`.
  - `"Beneath the surface of the {display}, layer upon layer of {adj} {color} {element}
    tells a story written {adverb} in sediment and stone."` — geological/archaeological
    layering as a palimpsest. Distinct from "deep time" (which is about temporal
    pressure) and "outside of time" (timelessness); this is about visible strata.
    Indicator: `"layer upon layer of"`.
  - `"The {display} marks the {adj} boundary between the {color} {element} and something
    that lies just beyond the world."` — the landscape as a liminal boundary between
    reality and something beyond. Distinct from "outside of time" (temporal) and
    "something vast turns over in its sleep" (subterranean). Indicator: `"boundary between the"`.
  - Each new phrase uses 3-5 template slots (`{display}`, `{adj}`, `{color}`, `{element}`,
    `{adverb}`, `{time_word}`) and occupies a distinct atmospheric niche: forgotten paths,
    auditory fragments, landscape mourning, geological layering, liminal boundary.
- **Added 5 new indicators to `ECHO_INDICATORS`** in the test module:
  `"roads of the"`, `"Fragments of"`, `"mourns"`, `"layer upon layer of"`,
  `"boundary between the"` — each is a unique invariant substring for dynamic test matching.
- **Added same 5 indicators to `NO_ECHO_INDICATORS`** — consistent with the pattern;
  none of the new indicators collide with legend phrases, so all are safe for `--no-echo`
  suppression tests.
- No code, CLI, or generation logic changes — data-only expansion plus indicator
  additions. All existing echo tests use dynamic checks over `ECHO_INDICATORS`, so no
  test modifications were needed.
- Each phrase is curated to fit a distinct atmospheric niche: forgotten ghost roads,
  fragmentary whispers, landscape mourning, geological palimpsest, liminal boundary.
  None overlap with the existing 15 phrases.
- This directly fulfills the "Next likely steps" from Session 160: "Expand global word
  banks (more echoes, more time-of-day, more seasons)." Echoes were the most overdue
  bank — last expanded in Session 122 (38 sessions ago).
- Tests unchanged: still 1126 landscape tests pass (18 todo unchanged).

### Current status
Working. All 1144 tests pass (18 todo + 1126 landscape).

### Next likely steps
- Expand time-of-day word bank (more phrases, more varied constructions)
- Expand seasons word bank (more phrases, more varied constructions)
- Expand wistful word bank (more phrases, more varied constructions)
- Expand simile word bank further (more phrases, more varied constructions)

## 2026-07-19

### What was done (Session 159)
- **Expanded METAPHORS word bank from 10 to 15 phrases** — 5 new metaphor constructions
  added, covering figurative identity niches not represented in the original 10:
  - `"The {display} is a {adj} armor of {color} {element}, worn {adverb} by the earth
    itself."` — the landscape as protective armor worn by the planet, adding a
    protection/defense metaphor (the only metaphor comparing the landscape to
    something worn as a shield). Indicator: `"armor of"`.
  - `"The {adj} {element} of the {display} is a {color} song sung {adverb} by stones
    and sky."` — the landscape's element as a musical expression sung by the earth
    itself, adding a celebratory/expressive metaphor (distinct from the existing
    "language" metaphor which implies communication — this is pure expression).
    Indicator: `"sung by stones"`.
  - `"The {display} is a {adj} forge where {color} {element} is hammered {adverb}
    into shapes yet unknown."` — the landscape as a transformative forge, adding a
    creation/transformation metaphor (the only metaphor with a workshop/foundry
    register). Indicator: `"forge where"`.
  - `"The {display} is an {adj} anchor of {color} {element}, holding {adverb} the
    world steady against time."` — the landscape as a cosmic anchor providing
    stability, adding a grounding/permanence metaphor (the only metaphor describing
    the landscape as a stabilizing force that holds the earth in place against
    temporal erosion). Indicator: `"anchor of"`.
  - `"The {display} is a {adj} feast of {color} {element}, spread {adverb} for those
    with eyes to see."` — the landscape as a sensory feast/banquet, adding an
    abundance/richness metaphor (the only metaphor equating the landscape to
    something consumed by the senses). Indicator: `"feast of"`.
  - Each new phrase uses 4-5 template slots (`{display}`, `{adj}`, `{color}`,
    `{element}`, `{adverb}`) and occupies a distinct figurative niche: armor,
    song, forge, anchor, feast.
- **Added 5 new indicators to `METAPHOR_INDICATORS`** in the test module:
  `"armor of"`, `"sung by stones"`, `"forge where"`, `"anchor of"`, `"feast of"` —
  each is a unique invariant substring for dynamic test matching.
- No code, CLI, or generation logic changes — data-only expansion plus indicator
  additions. All existing metaphor tests use dynamic count checks and loop over
  `METAPHOR_INDICATORS`, so no test modifications were needed.
- Each phrase is curated to fit a distinct figurative niche: protection/armor,
  celebratory song, transformative forge, grounding anchor, sensory feast.
  None overlap with the existing 10 phrases.
- This directly fulfills the first "Next likely step" from Session 158: "Expand
  metaphor word bank (more phrases, more varied constructions)."
- Tests unchanged: still 1126 landscape tests pass (18 todo unchanged).

### Current status
Working. All 1144 tests pass (18 todo + 1126 landscape).

### Next likely steps
- Expand personification word bank (more phrases, more varied constructions)
- Expand simile word bank further (more phrases, more varied constructions)
- Expand global word banks (more echoes, more time-of-day, more seasons)

## 2026-07-15

### What was done (Session 158)
- **Expanded SIMILES word bank from 10 to 15 phrases** — 5 new simile constructions
  added, covering figurative niches not represented in the original 10:
  - `"The {color} light pools in the {adj} hollows of the {display} like water in a
    dry {element}-bed."` — light as liquid pooling in the landscape's contours,
    adding a hydrographic simile (the only simile comparing light to water).
    Indicator: `"like water in a dry"`.
  - `"The {adj} {element} of the {display} shifts {adverb} like a living map of
    {color} light and shadow."` — the landscape as a mutable living map, distinct
    from the existing tapestry/weaving simile (which implies fixed woven structure).
    Indicator: `"shifts like a living map"`.
  - `"The {display} rises and falls {adverb} like the {adj} chest of a sleeping
    {color} {element}."` — the landscape breathing on a cosmic scale, using rise-and-
    fall rhythm. Distinct from the existing "breathes like a great slumbering
    {element}" which focuses on the sound/presence of breath rather than the visual
    rhythm of expansion and contraction. Indicator: `"rises and falls like the"`.
  - `"The {adj} horizon of the {display} trembles {adverb} like a {color} line drawn
    in liquid {element}."` — the horizon as a trembling drawn line, adding an
    edge/blur simile (the only horizon-specific simile in the bank). Indicator:
    `"drawn in liquid"`.
  - `"The {display} feels like a {adj} memory of {color} {element}, half-remembered
    and fading {adverb}."` — the landscape as an abstract emotional/experiential
    memory, the only simile in the bank that equates the landscape to a feeling
    rather than a visual object. Indicator: `"half-remembered and fading"`.
  - Each new phrase uses 4-5 template slots (`{display}`, `{adj}`, `{color}`,
    `{element}`, `{adverb}`) and occupies a distinct figurative niche: light-as-
    water, living-map, cosmic-breath, trembling-horizon, fading-memory.
- **Added 5 new indicators to `SIMILE_INDICATORS`** in the test module: `"like water
  in a dry"`, `"shifts like a living map"`, `"rises and falls like the"`,
  `"drawn in liquid"`, `"half-remembered and fading"` — each is a unique invariant
  substring for dynamic test matching.
- **Fixed fragile `PERSONIFICATION_INDICATORS` entry `"breath of"`** — changed to
  `"filling the air"` because `"breath of"` matched the metaphor phrase "Each breath
  of the {display} is a {color} prayer..." which RNG drift from the new similes
  exposed. `"filling the air"` is unique to the personification phrase and immune to
  cross-feature matching.
- No code, CLI, or generation logic changes — data-only expansion plus indicator
  additions and one indicator fix. All existing simile tests use dynamic count checks
  and loop over `SIMILE_INDICATORS`, so no test modifications were needed.
- Each phrase is curated to fit a distinct figurative niche: light-as-water,
  living-map, cosmic-breath, trembling-horizon, fading-memory. None overlap with
  the existing 10 phrases.
- This directly fulfills the first "Next likely step" from Session 157: "Expand
  simile word bank (more phrases, more varied constructions)."
- Tests unchanged: still 1126 landscape tests pass (18 todo unchanged).

### Current status
Working. All 1144 tests pass (18 todo + 1126 landscape).

### Next likely steps
- Expand metaphor word bank (more phrases, more varied constructions)
- Expand personification word bank (more phrases, more varied constructions)
- Expand simile word bank further (more phrases, more varied constructions)
- Expand global word banks (more echoes, more time-of-day, more seasons)

## 2026-07-15

### What was done (Session 157)
- **Added per-preset simile, metaphor, personification to all remaining presets** —
  `sublime`, `wasteland`, and `dreamscape` now have `simile_enabled`,
  `metaphor_enabled`, `personification_enabled` with curated count and probability
  values, following the same pattern as `nightfall` and `pastoral` (which already
  had them from earlier sessions).
  - **sublime** (vibrant+peaceful, rich): simile_enabled=True, count=2, prob=0.9;
    metaphor_enabled=True, count=2, prob=0.9; personification_enabled=True,
    count=1, prob=0.8. Matches the preset's high-density pattern — multiple simile
    and metaphor phrases almost always present, personification somewhat less
    frequent to avoid over-humanizing the sublime landscape.
  - **wasteland** (desolate, sparse): simile_enabled=True, count=1, prob=0.5;
    metaphor_enabled=True, count=1, prob=0.4; personification_enabled=True,
    count=1, prob=0.3. A progressive decay (0.5 → 0.4 → 0.3) reflecting the
    increasing "richness" of each device — simile is simplest and most appropriate
    for a wasteland, metaphor less so, personification rarest (a desolate wasteland
    rarely speaks, dreams, or weeps).
  - **dreamscape** (eerie+vibrant, surreal): simile_enabled=True, count=2, prob=0.85;
    metaphor_enabled=True, count=2, prob=0.85; personification_enabled=True,
    count=1, prob=0.75. Matches the preset's surreal density — multiple simile and
    metaphor phrases fit dreamlike landscapes well, personification slightly less
    frequent.
  - All three presets now have `simile_enabled`, `simile_count`, `simile_prob`,
    `metaphor_enabled`, `metaphor_count`, `metaphor_prob`, `personification_enabled`,
    `personification_count`, `personification_prob` set with non-default values.
  - The gating code in `main()` was already in place (lines 2087-2104) and checks
    `if "simile_enabled" in preset` — only the PRESETS dict values were needed.
- **Added 3 new tests** in `TestPresets`:
  - `test_all_presets_include_simile_enabled_count_and_prob` — verifies every preset
    has `simile_enabled`, `simile_count`, `simile_prob` with valid ranges (5 subtests).
  - `test_all_presets_include_metaphor_enabled_count_and_prob` — verifies every preset
    has `metaphor_enabled`, `metaphor_count`, `metaphor_prob` with valid ranges (5
    subtests).
  - `test_all_presets_include_personification_enabled_count_and_prob` — verifies every
    preset has `personification_enabled`, `personification_count`,
    `personification_prob` with valid ranges (5 subtests).
  - Follows the exact same pattern as `test_all_presets_include_mood_atmosphere_count_and_prob`.
- This fulfills the fifth "Next likely step" from Session 156: "Add per-preset
  simile_count, simile_prob, metaphor_count, metaphor_prob, personification_count,
  personification_prob with curated values." All 5 presets now have curated values
  for all three poetic device dimensions (simile, metaphor, personification),
  completing the preset integration trajectory for the figurative language system.
- Tests increased from 1123 to 1126 landscape tests (18 todo unchanged).

### Current status
Working. All 1144 tests pass (18 todo + 1126 landscape).

### Next likely steps
- Expand simile word bank (more phrases, more varied constructions)
- Expand metaphor word bank (more phrases, more varied constructions)
- Expand personification word bank (more phrases, more varied constructions)
- Expand global word banks (more echoes, more time-of-day, more seasons)

## 2026-07-15

### What was done (Session 156)
- **Added personification dimension (`--personification`)** — a new poetic device
  feature that gives human qualities to the landscape (e.g. breathing, gazing,
  whispering, dreaming), following the pattern of simile (comparison) and metaphor
  (identity) as the third figurative language register.
  - New `PERSONIFICATIONS` word bank of 10 curated phrases, each attributing a
    human action or quality to the landscape:
    - "The {display} breathes {adverb}, its {adj} breath of {color} {element} filling the air."
    - "The {display} turns its {adj} gaze {adverb} toward the {color} {element}."
    - "The {adj} {element} of the {display} whispers {adverb} in a {color} language older than words."
    - "The {display} dreams {adverb} of {color} {element}, its {adj} slumber deep and ancient."
    - "The {adj} heart of the {display} beats {adverb}, each pulse sending {color} {element} through the land."
    - "The {display} reaches out with {adj} hands of {color} {element}, grasping {adverb} at the sky."
    - "The {adj} voice of the {display} carries {adverb} across the {color} {element}, a song older than memory."
    - "The {display} remembers {adverb} a time when the {element} was {adj} and the {color} light was young."
    - "The {adj} {element} of the {display} listens {adverb} to the {color} silence between stars."
    - "The {display} weeps {adverb} tears of {color} {element}, each drop a {adj} story falling to the earth."
  - Each phrase uses 3-5 template slots (`{display}`, `{adj}`, `{color}`, `{element}`, `{adverb}`)
    and attributes a distinct human action: breathing, gazing, whispering, dreaming,
    heartbeat, reaching/grasping, singing, remembering, listening, weeping.
  - Off by default (`personification_enabled=False`), preserving all existing seed-based output.
- **Added `--personification` CLI flag** (boolean, default: off) — follows the same
  pattern as `--simile`, `--metaphor`, `--echo`, `--sound`, etc.
- **Added `--no-personification` CLI flag** — disables personification phrases
  overriding presets, following the same pattern as `--no-simile`, `--no-metaphor`, etc.
- **Added `--personification-count` and `--personification-prob` CLI flags** —
  users can control how many personification phrases appear per landscape (0-3,
  default: 1) and how often each roll succeeds (0.0-1.0, default: 1.0), following
  the exact same pattern as simile and metaphor count/prob controls.
- **Added `personification_enabled`, `personification_count`, `personification_prob`
  params to `generate_landscape()`** — defaults False, 1, and 1.0 respectively,
  preserving all existing behavior.
- **Added personification generation** in `generate_landscape()` right after metaphor
  (before echo), with dedup via `used_personifications` set to prevent repeats.
  Sentence order: opening → detail → weather → anomaly → simile → metaphor →
  **personification** → echo → sound → wildlife → legend → wistful → travelogue.
- **Added `"personification_enabled"`, `"personification_count"`,
  `"personification_prob"` to JSON metadata** when non-default — consistent with
  all other feature metadata patterns.
- **Added `describe_personifications()` function and `--describe-personifications`
  CLI flag** — users can inspect all 10 personification phrases with index numbers,
  following the exact same introspection pattern as `describe_similes()`,
  `describe_metaphors()`, etc.
- **Added preset gating for `personification_enabled`, `personification_count`,
  `personification_prob`** — follows the same pattern as all other preset gating,
  so presets can optionally configure personification use in a future session.
- Added 51 new tests:
  - **TestPersonification (22 tests)**: disabled by default, enabled appears, valid
    output, determinism, differs from plain, detail=0, JSON format, JSON field
    present/absent, works with echo, legend, travelogue, sound, wistful, time-of-day,
    season, wildlife, perspective, mood atmosphere, poetic format, all biomes, CLI flag.
  - **TestDescribePersonifications (8 tests)**: returns string, header, all phrases,
    index numbers, last index, CLI flag, stdout output, no landscape generated.
  - **TestNoPersonification (5 tests)**: flag exists via CLI, disables personification
    with presets (5 subtests), works with other features, JSON output, explicit
    `--personification` override.
  - **TestPersonificationCount (9 tests)**: default is one, zero suppresses,
    multi-personification with count=2 and count=3, no repeat same phrase, valid
    output for all counts, determinism, JSON format, JSON field, CLI flag.
  - **TestPersonificationProb (7 tests)**: default is one, zero suppresses, valid
    output for all probs, always has personification with prob=1.0, determinism,
    JSON field, CLI flag.
- This fulfills the third "Next likely step" from Session 155: "Add personification
  dimension (giving human qualities to the landscape)." Personification is the third
  poetic device dimension after simile (Session 153) and metaphor (Session 155),
  completing the simile→metaphor→personification trajectory for the figurative
  language system.
- Tests increased from 1072 to 1123 landscape tests (18 todo unchanged), subtests
  from 373 to 424.

### Current status
Working. All 1141 tests pass (18 todo + 1123 landscape), 424 subtests.

### Next likely steps
- Expand simile word bank (more phrases, more varied constructions)
- Expand metaphor word bank (more phrases, more varied constructions)
- Expand personification word bank (more phrases, more varied constructions)
- Expand global word banks (more echoes, more time-of-day, more seasons)
- Add per-preset simile_count, simile_prob, metaphor_count, metaphor_prob, personification_count, personification_prob with curated values

## 2026-07-15

### What was done (Session 155)
- **Added metaphor dimension (`--metaphor`)** — a new poetic device feature that adds
  direct equative statements (X is Y) comparing the landscape to an evocative image,
  following the pattern of simile but using identity rather than similarity.
  - New `METAPHORS` word bank of 10 curated phrases, each a direct is/are statement:
    - "The {display} is a {adj} cathedral of {color} {element}, built by no human hand."
    - "The {adj} {element} of the {display} is a living chronicle of all that has passed."
    - "The {color} light of the {display} is a {adj} language spoken only by the {element}."
    - "Each breath of the {display} is a {color} prayer {adverb} offered to the {adj} {element}."
    - "The {display} is a {adj} wound in the world, bleeding {color} {element} into the sky."
    - "The {adj} shapes of the {display} are {color} memories of a {element} that never was."
    - "The {display} is a {adj} threshold between the world of {color} {element} and something older."
    - "The {adj} silence of the {display} is a {color} mirror held {adverb} up to the {element}."
    - "The {display} is an {adj} argument between {color} {element} and the sky, neither side willing to yield."
    - "The {adj} heart of the {display} is a {color} {element} beating {adverb} beneath the surface."
  - Each phrase uses 3-5 template slots (`{display}`, `{adj}`, `{color}`, `{element}`, `{adverb}`)
    and asserts identity (is/are) rather than comparison (like), creating a stronger
    figurative language register than simile.
  - Off by default (`metaphor_enabled=False`), preserving all existing seed-based output.
- **Added `--metaphor` CLI flag** (boolean, default: off) — follows the same pattern
  as `--simile`, `--echo`, `--sound`, etc.
- **Added `--no-metaphor` CLI flag** — disables metaphor phrases overriding presets,
  following the same pattern as `--no-simile`, `--no-echo`, etc.
- **Added `--metaphor-count` and `--metaphor-prob` CLI flags** — users can control
  how many metaphor phrases appear per landscape (0-3, default: 1) and how often
  each roll succeeds (0.0-1.0, default: 1.0), following the exact same pattern as
  `--simile-count`/`--simile-prob` and all other count/prob controls.
- **Added `metaphor_enabled`, `metaphor_count`, `metaphor_prob` params to
  `generate_landscape()`** — defaults False, 1, and 1.0 respectively, preserving all
  existing behavior.
- **Added metaphor generation** in `generate_landscape()` right after simile
  (before echo), with dedup via `used_metaphors` set to prevent repeats. Sentence
  order: opening → detail → weather → anomaly → simile → **metaphor** → echo →
  sound → wildlife → legend → wistful → travelogue.
- **Added `"metaphor_enabled"`, `"metaphor_count"`, `"metaphor_prob"` to JSON
  metadata** when non-default — consistent with all other feature metadata patterns.
- **Added `describe_metaphors()` function and `--describe-metaphors` CLI flag** —
  users can inspect all 10 metaphor phrases with index numbers, following the exact
  same introspection pattern as `describe_similes()`, `describe_echoes()`, etc.
- **Added preset gating for `metaphor_enabled`, `metaphor_count`, `metaphor_prob`**
  — follows the same pattern as all other preset gating, so presets can optionally
  configure metaphor use in a future session.
- Added 51 new tests:
  - **TestMetaphor (22 tests)**: disabled by default, enabled appears, valid output,
    determinism, differs from plain, detail=0, JSON format, JSON field present/absent,
    works with echo, legend, travelogue, sound, wistful, time-of-day, season, wildlife,
    perspective, mood atmosphere, poetic format, all biomes, CLI flag.
  - **TestDescribeMetaphors (8 tests)**: returns string, header, all phrases, index
    numbers, last index, CLI flag, stdout output, no landscape generated.
  - **TestNoMetaphor (5 tests)**: flag exists via CLI, disables metaphor with presets
    (5 subtests), works with other features, JSON output, explicit `--metaphor` override.
  - **TestMetaphorCount (9 tests)**: default is one, zero suppresses, multi-metaphor
    with count=2 and count=3, no repeat same phrase, valid output for all counts,
    determinism, JSON format, JSON field, CLI flag.
  - **TestMetaphorProb (7 tests)**: default is one, zero suppresses, valid output for
    all probs, always has metaphor with prob=1.0, determinism, JSON field, CLI flag.
- This fulfills the second "Next likely step" from Session 154: "Add metaphor
  dimension (direct equative statements like 'the {display} is a {adj} {color}
  {element} of forgotten things')." Metaphor is the second poetic device dimension
  after simile, completing the simile→metaphor trajectory for the figurative language
  system.
- Tests increased from 1020 to 1072 landscape tests (18 todo unchanged), subtests
  from 355 to 373.

### Current status
Working. All 1090 tests pass (18 todo + 1072 landscape), 373 subtests.

### Next likely steps
- Expand simile word bank (more phrases, more varied constructions)
- Expand metaphor word bank (more phrases, more varied constructions)
- Add personification dimension (giving human qualities to the landscape)
- Expand global word banks (more echoes, more time-of-day, more seasons)
- Add per-preset simile_count, simile_prob, metaphor_count, metaphor_prob with curated values

## 2026-07-15

### What was done (Session 154)
- **Added `--simile-count` and `--simile-prob` CLI flags** — users can now control
  how many simile phrases appear per landscape (0-3, default: 1) and how often
  each roll succeeds (0.0-1.0, default: 1.0), following the exact same pattern as
  `--echo-count`/`--echo-prob`, `--sound-count`/`--sound-prob`,
  `--wildlife-count`/`--wildlife-prob`, etc.
  - `simile_count=0` suppresses all simile phrases (alternative to `--no-simile`)
  - `simile_count=1` (default) produces exactly 1 phrase (existing behavior)
  - `simile_count=2` and `simile_count=3` produce multiple distinct simile phrases
    with dedup (preventing the same phrase from appearing twice)
  - Each roll independently draws `rng.random() < simile_prob`
  - Default `simile_count=1, simile_prob=1.0` preserves backward compatibility —
    all existing seed-based output with `--simile` is unchanged
- **Added `simile_count` and `simile_prob` params to `generate_landscape()`**
  — defaults 1 and 1.0 respectively, preserving all existing behavior.
- **Added `simile_count` and `simile_prob` to JSON metadata** when non-default
  values are used — consistent with all other count/prob metadata patterns.
- **Added preset gating for `simile_count` and `simile_prob`** — follows the same
  pattern as all other count/prob gating, so presets can optionally configure
  simile density in a future session.
- **Added `TestSimileCount` (10 tests)** — default is one, zero suppresses,
  multi-simile with count=2 and count=3, no repeat same phrase, valid output for
  all counts, determinism, JSON format, JSON field, CLI flag.
- **Added `TestSimileProb` (7 tests)** — default is one, zero suppresses, valid
  output for all probs, always has simile with prob=1.0, determinism, JSON field,
  CLI flag.
- **Fixed `SIMILE_INDICATORS`** — 3 indicators were broken because `{adverb}`
  injection between the verb and "like" (e.g. "stretches {adverb} like a")
  caused the indicator "stretches like a" to never match "stretches silently like
  a". Replaced with invariant substrings that work with any adverb:
  `"tapestry of"`, `"slumbering"`, `"dream of"`.
- This fulfills the "[Add simile] count/prob controls" trajectory — simile was the
  only multi-phrase feature without count/prob controls. Every multi-phrase feature
  (echo, sound, wildlife, perspective, time, season, mood atmosphere, weather,
  anomaly, legend) now has count and probability controls.
- Tests increased from 1003 to 1020 landscape tests (18 todo unchanged), subtests
  unchanged at 355.

### Current status
Working. All 1038 tests pass (18 todo + 1020 landscape), 355 subtests.

### Next likely steps
- Expand simile word bank (more phrases, more varied constructions)
- Add metaphor dimension (direct equative statements like "the {display} is a {adj}
  {color} {element} of forgotten things")
- Add personification dimension (giving human qualities to the landscape)
- Expand global word banks (more echoes, more time-of-day, more seasons)
- Add per-preset simile_count and simile_prob with curated values

## 2026-07-15

### What was done (Session 153)
- **Added `--simile` CLI flag and `SIMILES` word bank (10 phrases)** — a new poetic
  device dimension that adds a figurative language simile comparison to the landscape
  description, following the pattern of `like a...` constructions.
  - 10 curated simile phrases, each using `{display}`, `{adj}`, `{color}`,
    `{element}`, and `{adverb}` template injections (3-5 slots per phrase):
    - "The {display} stretches {adverb} like a {adj} tapestry of {color} {element}."
    - "The {adj} {element} moves through the {display} like a living thing."
    - "The {color} light of the {display} falls like {adj} dust upon the {element}."
    - "The {adj} {display} breathes {adverb} like a great slumbering {element}."
    - "The {color} {element} of the {display} shimmers like a {adj} veil."
    - "The {adj} shapes of the {display} glow like embers of {color} {element}."
    - "The {element} of the {display} wraps around everything like a {adj} shroud."
    - "The {adj} silence of the {display} hangs like a {color} {element} in the air."
    - "The {display} unfolds {adverb} like a {adj} dream of {color} {element}."
    - "The {adj} edges of the {display} bleed into the surroundings like {color} {element}."
  - Each simile compares a landscape aspect to an evocative image: a tapestry, a living
    thing, dust, a slumbering giant, a veil, embers, a shroud, something suspended in
    the air, a dream, or something bleeding into its surroundings.
  - Off by default (`simile_enabled=False`), preserving all existing seed-based output.
  - Placed after anomaly and before echo in the sentence order: opening → detail →
    anomaly → **simile** → echo → sound → wildlife → legend → wistful.
  - Suppressed at detail=0 (like echoes, soundscapes, wildlife, legends, wistful).
  - Seed-breaking when enabled: one `rng.choice(SIMILES)` call shifts subsequent random
    picks. Determinism is preserved (same seed + same args = same output).
  - Works with all features: detail=0, prose/poetic/json, combine, echo, legend,
    sound, wildlife, perspective, time-of-day, season, mood atmosphere, travelogue,
    wistful, all biomes.
- **Added `--no-simile` CLI flag** — users can now explicitly disable simile phrases
  even when using presets that might enable them. Follows the exact same pattern as
  `--no-echo`, `--no-legend`, `--no-sound`, etc.
  - `--no-simile` forces `simile_enabled=False` regardless of preset config.
  - Post-preset override block ensures `--no-simile` always wins after all gating.
- **Added `--describe-similes` CLI flag and `describe_similes()` function** — users
  can inspect all 10 simile phrases with index numbers, following the exact same
  introspection pattern as `describe_echoes()`, `describe_legends()`, etc.
- **Added `"simile_enabled"` to JSON metadata** when enabled — e.g.
  `"simile_enabled": True`.
- **Added preset gating for `simile_enabled`** — follows the same pattern as all other
  preset gating, so presets can optionally enable similes in a future session.
- Added 35 new tests (20 in `TestSimile`, 8 in `TestDescribeSimiles`, 4 in
  `TestNoSimile`, plus `test_simile_works_with_mood_atmosphere` and
  `test_simile_works_with_perspective`):
  - `TestSimile` (20 tests): disabled by default, enabled appears, valid output,
    determinism, differs from plain, detail=0, JSON format, JSON field present/absent,
    works with echo, legend, travelogue, sound, wistful, time-of-day, season, wildlife,
    perspective, mood atmosphere, poetic format, all biomes, CLI flag.
  - `TestDescribeSimiles` (8 tests): returns string, header, all phrases, index
    numbers, last index, CLI flag, stdout output, no landscape generated.
  - `TestNoSimile` (4 tests): flag exists via CLI, disables simile with presets,
    works with other features, JSON output, explicit `--simile` override.
- This fulfills the second "Next likely step" from Session 152: "Add a
  narrative/poetic device dimension (simile, metaphor, personification as separate
  controllable features)." Similes are the first concrete implementation of this
  poetic device dimension.
- Tests increased from 968 to 1003 landscape tests (18 todo unchanged), subtests
  from 337 to 355.

### Current status
Working. All 1021 tests pass (18 todo + 1003 landscape), 355 subtests.

### Next likely steps
- Expand simile word bank (more phrases, more varied constructions)
- Add metaphor dimension (direct equative statements like "the {display} is a {adj}
  {color} {element} of forgotten things")
- Add personification dimension (giving human qualities to the landscape)
- Expand global word banks (more echoes, more time-of-day, more seasons)

## 2026-07-15

### What was done (Session 152)
- **Added `--no-mood-atmosphere` CLI flag** — users can now explicitly disable mood
  atmosphere phrases even when using presets that enable them. Follows the exact same
  pattern as `--no-echo`, `--no-legend`, `--no-sound`, `--no-time`, `--no-season`,
  `--no-wildlife`, `--no-perspective`, `--no-travelogue`, and `--no-wistful.
  - `--no-mood-atmosphere` forces `mood_atmosphere=False` regardless of preset config
    or explicit `--mood-atmosphere`.
  - Post-preset override block ensures `--no-mood-atmosphere` always wins after all
    gating.
- **Fixed preset gating for mood atmosphere** — the preset gating at line 1888
  previously lacked the `not args.no_mood_atmosphere` guard that every other preset
  gating check has. Without this, a hypothetical `--no-mood-atmosphere` flag would
  have been ignored for presets that set `mood_atmosphere=True`. This is now fixed.
- Added 6 new tests in `TestNoMoodAtmosphere`:
  - `test_no_mood_atmosphere_flag_exists_via_cli` — flag exists
  - `test_no_mood_atmosphere_disables_with_preset` (5 subtests) — disables mood
    atmosphere with all 5 presets
  - `test_no_mood_atmosphere_preset_without_flag_still_has_atmosphere` (5 subtests)
    — presets still include mood atmosphere without `--no-mood-atmosphere`
  - `test_no_mood_atmosphere_works_with_other_features` — works with echo, legend,
    sound
  - `test_no_mood_atmosphere_with_explicit_mood_atmosphere_override` — differs from
    `mood_atmosphere=True` with same seed
  - `test_no_mood_atmosphere_does_not_affect_json_output` — no `mood_atmosphere` in
    JSON when disabled
- This fulfills the third "Next likely step" from Session 151: "Add `--no-mood-atmosphere`
  flag for symmetry with other `--no-*` flags."
- Tests increased from 962 to 968 landscape tests (18 todo unchanged), subtests
  from 327 to 337.

### Current status
Working. All 986 tests pass (18 todo + 968 landscape), 337 subtests.

### Next likely steps
- Expand global word banks (more echoes, more time-of-day, more seasons)
- Add a narrative/poetic device dimension (simile, metaphor, personification
  as separate controllable features)

## 2026-07-15

### What was done (Session 151)
- **Added `mood_atmosphere_count` and `mood_atmosphere_prob` to all 5 presets** with
  curated values that match each preset's mood/theme:
  - `nightfall`: `mood_atmosphere_count=2, mood_atmosphere_prob=0.7` — multiple
    atmosphere phrases, not always present, matching echo/sound/legend/wildlife/
    time/season/perspective count and prob
  - `pastoral`: `mood_atmosphere_count=1, mood_atmosphere_prob=0.6` — single gentle
    atmosphere phrase, occasionally absent for serene stillness
  - `sublime`: `mood_atmosphere_count=2, mood_atmosphere_prob=0.95` — rich atmospheric
    framing almost always present
  - `wasteland`: `mood_atmosphere_count=1, mood_atmosphere_prob=1.0` — always a stark
    desolate atmosphere phrase
  - `dreamscape`: `mood_atmosphere_count=2, mood_atmosphere_prob=0.85` — surreal
    atmosphere usually present
- The gating code was already in place from Session 150 — only the PRESETS dict values
  needed updating, following the same pattern as every other per-preset count/prob
  integration (echo, sound, wildlife, perspective, time, season, etc.).
- Added 1 new test in TestPresets
  (`test_all_presets_include_mood_atmosphere_count_and_prob`) — verifies every preset
  includes `mood_atmosphere_count` and `mood_atmosphere_prob` with valid ranges,
  following the same pattern as `test_all_presets_include_perspective_count_and_prob`.
- This fulfills the third "Next likely step" from Session 150: "Add per-preset
  mood_atmosphere_count and mood_atmosphere_prob with curated values."
- Tests increased from 961 to 962 landscape tests (18 todo unchanged), subtests
  from 322 to 327.

### Current status
Working. All 980 tests pass (18 todo + 962 landscape), 327 subtests.

### Next likely steps
- Expand global word banks (more echoes, more time-of-day, more seasons)
- Add a narrative/poetic device dimension (simile, metaphor, personification
  as separate controllable features)
- Add `--no-mood-atmosphere` flag for symmetry with other `--no-*` flags

## 2026-07-15

### What was done (Session 150)
- **Added `--mood-atmosphere-count` and `--mood-atmosphere-prob` CLI flags** —
  users can now control how many mood atmosphere phrases appear per landscape
  (0-3, default: 1) and how often each roll succeeds (0.0-1.0, default: 1.0),
  following the exact same pattern as `--echo-count`/`--echo-prob`,
  `--sound-count`/`--sound-prob`, `--wildlife-count`/`--wildlife-prob`,
  `--perspective-count`/`--perspective-prob`, `--time-count`/`--time-prob`,
  and `--season-count`/`--season-prob`.
  - `mood_atmosphere_count=0` suppresses all mood atmosphere phrases (alternative
    to not using `--mood-atmosphere`)
  - `mood_atmosphere_count=1` (default) produces exactly 1 phrase (existing behavior)
  - `mood_atmosphere_count=2` and `mood_atmosphere_count=3` produce multiple
    distinct mood atmosphere phrases with dedup (preventing the same phrase from
    appearing twice)
  - Each roll independently picks a random mood from the available active moods,
    then picks a unique phrase from that mood's pool
  - `mood_atmosphere_prob=0.0` suppresses all mood atmosphere phrases even with
    `mood_atmosphere_count > 0`
  - Each of `mood_atmosphere_count` rolls independently draws
    `rng.random() < mood_atmosphere_prob`
  - Default `mood_atmosphere_count=1, mood_atmosphere_prob=1.0` preserves backward
    compatibility — all existing seed-based output with `--mood-atmosphere` is
    unchanged
- **Added `mood_atmosphere_count` and `mood_atmosphere_prob` params to
  `generate_landscape()`** — defaults 1 and 1.0 respectively, preserving all
  existing behavior.
- **Added `mood_atmosphere_count` and `mood_atmosphere_prob` to JSON metadata**
  when non-default values are used — consistent with all other count/prob metadata
  patterns.
- **Added preset gating for `mood_atmosphere_count` and `mood_atmosphere_prob`**
  — follows the same pattern as all other count/prob gating, so presets can
  optionally configure mood atmosphere density in a future session.
- Added 15 new tests (9 in `TestMoodAtmosphereCount`, 6 in `TestMoodAtmosphereProb`):
  - `TestMoodAtmosphereCount`: default is one, zero suppresses, multi-atmosphere
    with count=3, no repeat same phrase, valid output for all counts, determinism,
    JSON format, JSON field, CLI flag.
  - `TestMoodAtmosphereProb`: default is one, zero suppresses, valid output for
    all probs, determinism, JSON field, CLI flag.
- This fulfills the third "Next likely step" from Session 149: "Add count/prob
  controls for mood atmosphere (e.g. multiple atmosphere phrases)."
- Tests increased from 946 to 961 landscape tests (18 todo unchanged), subtests
  unchanged at 322.

### Current status
Working. All 979 tests pass (18 todo + 961 landscape), 322 subtests.

### Next likely steps
- Expand global word banks (more echoes, more time-of-day, more seasons)
- Add a narrative/poetic device dimension (simile, metaphor, personification
  as separate controllable features)
- Add per-preset mood_atmosphere_count and mood_atmosphere_prob with curated values

## 2026-07-15

### What was done (Session 149)
- **Added `mood_atmosphere` to all 5 presets** with `mood_atmosphere: True`:
  - nightfall, pastoral, sublime, wasteland, dreamscape all now include mood
    atmosphere framing by default, matching their mood configuration.
  - Presets that use mood (all 5) now automatically add an emotional-register
    atmosphere phrase between the opening and the detail sentences.
  - wasteland (mood=desolate) and dreamscape (mood=eerie+vibrant) now get
    their corresponding atmosphere framing.
- **Added preset gating for `mood_atmosphere`** in `main()` — follows the same
  pattern as color_enabled gating: only applies when the CLI flag is at its
  default (False), so explicit `--no-mood-atmosphere` can override.
- **Added 1 new test** (`test_all_presets_include_mood_atmosphere`) — verifies
  every preset includes `mood_atmosphere=True`.
- **Fixed latent test fragility** in `WILDLIFE_INDICATORS`: changed `"lone"` to
  `"A lone"` because `"lone"` matches `"alone"` in soundscape phrases
  (e.g. "Footsteps echo... though you are alone"), causing a false positive in
  `test_no_wildlife_disables_wildlife_with_preset`. The new RNG state from
  adding mood_atmosphere to presets caused a different soundscape to be selected
  that exposed this pre-existing test issue.
- This fulfills the first "Next likely step" from Session 148: "Add mood
  atmosphere to presets with appropriate values."
- Tests increased from 945 to 946 landscape tests (18 todo unchanged), subtests
  from 317 to 322.

### Current status
Working. All 946 tests pass (18 todo + 946 landscape), 322 subtests.

### Next likely steps
- Expand global word banks (more echoes, more time-of-day, more seasons)
- Add a narrative/poetic device dimension (simile, metaphor, personification
  as separate controllable features)
- Add count/prob controls for mood atmosphere (e.g. multiple atmosphere phrases)

## 2026-07-15

### What was done (Session 148)
- **Added mood atmosphere system (`--mood-atmosphere`)** — a new sensory dimension
  that adds mood-specific atmospheric framing phrases to establish the emotional
  register of the landscape, going beyond the existing word-weight biasing system.
  - New `MOOD_ATMOSPHERE` dict with 4 curated phrases per mood (16 total):
    - **peaceful**: gentle stillness, soft air, tranquil rhythm, world holding
      its breath — warm, serene, accepting register
    - **eerie**: wrongness in the air, thick watchful silence, primal fear,
      ancient cold attention — unsettling, ominous, numinous register
    - **vibrant**: borderless energy, colour bleeding from everything, fierce
      joyful intensity, electric golden air — exuberant, overflowing, alive
    - **desolate**: hope withered long ago, the land giving up, desolation as a
      held breath, emptiness as identity — stark, abandoned, mournful register
  - Each phrase is a standalone sentence inserted between the opening description
    and the detail/weather/anomaly sentences, creating a natural emotional bridge
    from "what the landscape looks like" to "how to feel about it."
  - Off by default (`mood_atmosphere=False`), preserving all existing seed-based
    output for users who use `--mood` without `--mood-atmosphere`.
  - Picks one active mood randomly (if multiple moods are set via combined mood)
    and then picks one phrase from that mood's pool via `rng.choice()`.
  - When mood is not set, `mood_atmosphere=True` has no effect — no phrase is
    inserted (consistent: no mood, no atmosphere).
  - Works with all features: detail=0, prose/poetic/json, combine, echo, legend,
    soundscape, wildlife, time-of-day, season, perspective, travelogue, wistful,
    all biomes, all presets.
  - Seed-breaking when enabled: one `rng.choice(MOOD_ATMOSPHERE[mood])` call
    and possibly one `rng.choice(active_moods)` call shift subsequent random
    picks. Determinism is preserved (same seed + same args = same output).
- **Added `mood_atmosphere` param to `generate_landscape()`** — defaults to
  `False`, preserving all existing behavior.
- **Added `--mood-atmosphere` CLI flag** (boolean, default: off) — follows the
  same pattern as `--echo`, `--sound`, `--wildlife`, `--time`, `--season`,
  `--perspective`, etc.
- **Added `"mood_atmosphere": True` to JSON metadata** when enabled — consistent
  with all other boolean feature metadata patterns.
- **Added 16 new tests** in `TestMoodAtmosphere`:
  - Disabled by default (no atmosphere appears with `mood="eerie"` alone)
  - Enabled appears with mood (atmosphere phrases present with `mood_atmosphere=True`)
  - Valid output for all 4 moods, all biomes, detail=0, JSON, poetic, combine
  - Determinism (same seed + same args = same output)
  - Differs from mood-without-atmosphere
  - JSON format and JSON field presence/absence
  - Works with other features (echo, sound, wildlife, time, season, perspective)
  - Works with combined moods (mood atmosphere picks from one of the active moods)
  - CLI flag existence
  - No atmosphere when mood is None even with `mood_atmosphere=True`
- This fulfills the second "Next likely step" from Session 147: "Add a 'mood'
  dimension that affects how the entire landscape feels (beyond word-weight
  biasing)." After 6 consecutive sessions of word bank expansions and count/prob
  controls (Sessions 142-147), this adds a genuinely new atmospheric dimension
  that changes the landscape's emotional register through narrative framing
  rather than just word frequency.
- Tests increased from 929 to 945 landscape tests (18 todo unchanged), subtests
  from 304 to 317.

### Current status
Working. All 963 tests pass (18 todo + 945 landscape), 317 subtests.

### Next likely steps
- Expand global word banks (more echoes, more time-of-day, more seasons)
- Add mood atmosphere to presets with appropriate values
- Add a narrative/poetic device dimension (simile, metaphor, personification
  as separate controllable features)
- Add count/prob controls for mood atmosphere (e.g. multiple atmosphere phrases)

## 2026-07-15

### What was done (Session 147)
- **Expanded PERSPECTIVES word bank from 10 to 15 phrases** — 5 new perspective
  phrases added, covering spatial vantage niches not represented in the original 10:
  - `"Beneath the {display}, unseen {adj} roots of {color} {element} hold the
    landscape together {adverb} in the dark"` — underground/below-surface
    perspective, looking up from beneath the landscape's visible structure
  - `"Moving {adverb} through the {display}, the {adj} {color} {element} parts
    and closes around you like a living curtain"` — dynamic passage through the
    landscape, the traveler in motion (no existing perspective involves motion)
  - `"Approaching the {display}, its {adj} silhouette of {color} {element} grows
    {adverb} against the horizon line"` — arrival/approach perspective, the
    landscape resolving from the horizon (distinct from static "From a distance")
  - `"Reflected in a {adj} pool of {color} {element}, the {display} appears
    {adverb} transformed, its secrets floating on the surface"` — mirror/
    reflection perspective, the landscape seen doubled in water or ice
  - `"Drifting {adverb} above the {display}, the {adj} expanse of {color}
    {element} unfolds beneath you like a living map"` — dynamic floating/drifting
    aerial perspective (distinct from static analytical "Seen from above" and
    god's-eye "Seen from the heights")
- **Added 5 new indicators to `PERSPECTIVE_INDICATORS`** in the test module:
  `"hold the landscape together"`, `"parts and closes around"`,
  `"grows against the horizon"`, `"appears transformed"`,
  `"like a living map"` — each is a unique invariant substring for dynamic test
  matching.
- No code, CLI, or test logic changes — data-only expansion plus indicator
  additions. All existing perspective tests use dynamic count checks and loop
  over `PERSPECTIVE_INDICATORS`, so no test modifications were needed.
- Each phrase is curated to fit a distinct spatial perspective niche: underground,
  in-motion passage, approach/arrival, mirror reflection, drifting aerial.
  None overlap with the existing 10 phrases.
- This directly fulfills the first "Next likely step" from Session 146:
  expand global word banks (more perspective phrases).
- Tests unchanged: still 929 landscape tests pass (304 subtests), 18 todo tests.

### Current status
Working. All 929 tests pass (18 todo + 911 landscape), 304 subtests.

### Next likely steps
- Expand other global word banks (more echoes, more time-of-day, more seasons)
- Add a "mood" dimension that affects how the entire landscape feels
  (beyond word-weight biasing)
- Add a narrative/poetic device dimension (simile, metaphor, personification
  as separate controllable features)

## 2026-07-15

### What was done (Session 146)
- **Added `--perspective-count` and `--perspective-prob` CLI flags** — users can
  now control how many perspective phrases appear per landscape (0-3, default: 1)
  and how often each roll succeeds (0.0-1.0, default: 1.0), following the exact
  same pattern as `--time-count`/`--time-prob`, `--season-count`/`--season-prob`,
  `--echo-count`/`--echo-prob`, `--sound-count`/`--sound-prob`,
  `--weather-count`/`--weather-prob`, `--wildlife-count`/`--wildlife-prob`, and
  `--legend-count`/`--legend-prob`.
  - `perspective_count=0` suppresses all perspective phrases (alternative to
    `--no-perspective`)
  - `perspective_count=1` (default) produces exactly 1 phrase (existing behavior)
  - `perspective_count=2` and `perspective_count=3` produce multiple distinct
    perspective phrases with dedup (preventing the same phrase from appearing twice)
  - `perspective_prob=0.0` suppresses all perspective phrases even with
    `perspective_count > 0`
  - Each of `perspective_count` rolls independently draws `rng.random() < perspective_prob`
  - Default `perspective_count=1, perspective_prob=1.0` preserves backward
    compatibility — all existing seed-based output with `--perspective` is unchanged
- **Added `perspective_count` and `perspective_prob` params to `generate_landscape()`**
  — defaults 1 and 1.0 respectively, preserving all existing behavior.
- **Added `perspective_count` and `perspective_prob` to JSON metadata** when non-default
  values are used — consistent with echo/season/time/weather/wildlife metadata patterns.
- **Added perspective_count and perspective_prob to all 5 presets** with curated values
  that match each preset's mood/theme:
  - `nightfall`: `perspective_count=2, perspective_prob=0.7` — multiple perspective
    phrases, not always present, matching echo/sound/legend/season/time prob
  - `pastoral`: `perspective_count=1, perspective_prob=0.6` — single gentle perspective
    phrase, occasionally absent for serene solitude
  - `sublime`: `perspective_count=2, perspective_prob=0.95` — rich perspective detail
    almost always present
  - `wasteland`: `perspective_count=1, perspective_prob=1.0` — always a stark perspective
    phrase
  - `dreamscape`: `perspective_count=2, perspective_prob=0.85` — surreal perspective
    usually present
- **Added preset gating for `perspective_count` and `perspective_prob`** — follows the
  same pattern as all other count/prob gating.
- Added 16 new tests (9 in `TestPerspectiveCount`, 6 in `TestPerspectiveProb`, 1 in
  `TestPresets`):
  - `TestPerspectiveCount` (9 tests): default is one, zero suppresses, multi-perspective
    with count=3, no repeat same phrase, valid output for all counts, determinism, JSON
    format, JSON field, CLI flag.
  - `TestPerspectiveProb` (6 tests): default is one, zero suppresses, valid output for
    all probs, determinism, JSON field, CLI flag.
  - `TestPresets`: `test_all_presets_include_perspective_count_and_prob` (5 subtests)
    — verifies every preset includes `perspective_count` and `perspective_prob` with
    valid ranges.
- This fulfills the "Next likely steps" from Session 145: add `--perspective-count`,
  `--perspective-prob` for configurable perspective density, and per-preset perspective
  count and probability.
- Tests increased from 913 to 929 total (18 todo + 911 landscape), subtests from 299
  to 304.

### Current status
Working. All 929 tests pass (18 todo + 911 landscape), 304 subtests.

### Next likely steps
- Expand global word banks (more perspective phrases, more echoes,
  more time-of-day, more seasons)
- Add a "mood" dimension that affects how the entire landscape feels
  (beyond word-weight biasing)
- Add a narrative/poetic device dimension (simile, metaphor, personification
  as separate controllable features)

## 2026-07-15

### What was done (Session 144)
- **Expanded SOUNDSCAPES word bank from 12 to 17 phrases** — 5 new soundscape
  phrases added, covering sonic niches not represented in the original 12:
  - `"Water drips {adverb} from the {adj} surfaces of the {display}, each
    drop a bright {color} note against the {element}."` — water dripping as
    percussion, the only liquid/water sound in the bank
  - `"A {adj} music drifts {adverb} through the {display}, as if the {color}
    {element} itself has learned to sing."` — melodic/musical quality,
    distinct from existing rhythmic pulses and single ringing notes
  - `"The wind howls {adverb} through the {adj} reaches of the {display}, a
    {color} sound that seems to shape the very {element}."` — wind howling
    as a forceful shaping presence, distinct from existing shattering-glass
    wind sound
  - `"{adj} voices whisper {adverb} in the {display}, a chorus of {color}
    sounds that never form words."` — choral voices/many murmuring presences,
    distinct from the single whisper at the edge of hearing
  - `"The {adj} bones of the {display} groan {adverb}, a deep {color} sound
    that resonates through the {element}."` — structural creaking/groaning,
    adding the sound of the landscape's own body straining
- **Added 5 new indicators to `SOUND_INDICATORS`** in the test module:
  `"each drop a bright"`, `"learned to sing"`, `"shape the very"`,
  `"never form words"`, `"resonates through the"` — each is a unique invariant
  substring for dynamic test matching.
- No code, CLI, or test logic changes — data-only expansion plus indicator
  additions. All existing sound tests use dynamic count checks and loop
  over `SOUND_INDICATORS`, so no test modifications were needed.
- Each phrase is curated to fit a distinct sonic niche: water percussion,
  melodic singing, wind howling, choral voices, structural groaning.
  None overlap with existing phrases.
- This directly fulfills the first "Next likely step" from Session 143:
  expand other global word banks (more soundscapes).
- Tests unchanged: still 880 landscape tests pass (281 subtests), 18 todo tests.

### Current status
Working. All 880 landscape tests pass (281 subtests), 18 todo tests.

### Next likely steps
- Expand other global word banks (more echoes, more time-of-day, more seasons)
- Add spatial geometry dimension (e.g. scale, perspective, distance)

## 2026-07-15

### What was done (Session 143)
- **Expanded WILDLIFE word bank from 10 to 15 phrases** — 5 new wildlife phrases
  added, covering wildlife niches not represented in the original 10:
  - `"Fireflies drift {adverb} through the {adj} air of the {display}, each
    {color} spark a brief luminous trail."` — fireflies/bioluminescent insects,
    the only insect-specific phrase in the bank
  - `"Something hunts {adverb} at the edge of the {display} — patient, {adj},
    tasting the {color} {element}."` — predator stalking, adding a predator-prey
    dynamic not present in original phrases
  - `"A {adj} bird of prey circles {adverb} overhead, a dark {color} silhouette
    against the {element}."` — aerial predator (bird of prey), the only
    flying-hunter phrase in the bank
  - `"Beneath the {display}, {adj} things build {adverb}, weaving {color}
    {element} into their hidden structures."` — nest-building/engineering
    creatures, adding construction behavior absent from the original 10
  - `"The {adverb} hum of {color} wings rises from the {adj} depths of the
    {display} like a living {element}."` — insect swarm as a collective presence,
    the only swarm/buzzing phrase in the bank
- **Added 5 new indicators to `WILDLIFE_INDICATORS`** in the test module:
  `"Fireflies drift"`, `"Something hunts"`, `"bird of prey circles"`,
  `"hidden structures"`, `"wings rises from"` — each is a unique invariant
  substring for dynamic test matching.
- No code, CLI, or test logic changes — data-only expansion plus indicator
  additions. All existing wildlife tests use dynamic count checks and loop
  over `WILDLIFE_INDICATORS`, so no test modifications were needed.
- Each phrase is curated to fit a distinct wildlife niche: bioluminescent
  insects, predator stalking, bird of prey, nest-building creatures, insect
  swarm. None overlap with existing phrases.
- This directly fulfills the first "Next likely step" from Session 142: expand
  other global word banks (more wildlife).
- Tests unchanged: still 880 landscape tests pass (281 subtests), 18 todo tests.

### Current status
Working. All 880 landscape tests pass (281 subtests), 18 todo tests.

### Next likely steps
- Expand other global word banks (more echoes, more soundscapes, more
  time-of-day, more seasons)
- Add spatial geometry dimension (e.g. scale, perspective, distance)

## 2026-07-15

### What was done (Session 142)
- **Added `--wildlife-count` and `--wildlife-prob` CLI flags** — users can now
  control how many wildlife phrases appear per landscape (0-3, default: 1) and
  how often each roll succeeds (0.0-1.0, default: 1.0), following the exact same
  pattern as `--time-count`/`--time-prob`, `--season-count`/`--season-prob`,
  `--echo-count`/`--echo-prob`, `--sound-count`/`--sound-prob`,
  `--weather-count`/`--weather-prob`, and `--legend-count`/`--legend-prob`.
  - `wildlife_count=0` suppresses all wildlife phrases (alternative to
    `wildlife_enabled=False`)
  - `wildlife_count=1` (default) produces exactly 1 phrase (existing behavior)
  - `wildlife_count=2` and `wildlife_count=3` produce multiple distinct wildlife
    phrases with dedup (preventing the same phrase from appearing twice)
  - `wildlife_prob=0.0` suppresses all wildlife phrases even with
    `wildlife_count > 0`
  - Each of `wildlife_count` rolls independently draws `rng.random() < wildlife_prob`
  - Default `wildlife_count=1, wildlife_prob=1.0` preserves backward
    compatibility — all existing seed-based output with `--wildlife` is unchanged
- **Added `wildlife_count` and `wildlife_prob` params to `generate_landscape()`**
  — defaults 1 and 1.0 respectively, preserving all existing behavior.
- **Added `wildlife_count` and `wildlife_prob` to JSON metadata** when non-default
  values are used — consistent with echo/season/time/weather metadata patterns.
- **Added wildlife_count and wildlife_prob to all 5 presets** with curated values
  that match each preset's mood/theme:
  - `nightfall`: `wildlife_count=2, wildlife_prob=0.7` — multiple wildlife
    phrases, not always present, matching echo/sound/legend/season/time prob
  - `pastoral`: `wildlife_count=1, wildlife_prob=0.6` — single gentle wildlife
    phrase, occasionally absent for serene solitude
  - `sublime`: `wildlife_count=2, wildlife_prob=0.95` — rich wildlife detail
    almost always present
  - `wasteland`: `wildlife_count=1, wildlife_prob=1.0` — always a stark wildlife
    phrase (but wildlife_enabled=False so moot)
  - `dreamscape`: `wildlife_count=2, wildlife_prob=0.85` — surreal wildlife
    usually present
- **Added preset gating for `wildlife_count` and `wildlife_prob`** — follows the
  same pattern as all other count/prob gating, so presets can optionally
  configure wildlife density (not yet added to any preset).
- Added 16 new tests (9 in `TestWildlifeCount`, 6 in `TestWildlifeProb`, 1 in
  `TestPresets`):
  - `TestWildlifeCount` (9 tests): default is one, zero suppresses, multi-wildlife
    with count=3, no repeat same phrase, valid output for all counts, determinism,
    JSON format, JSON field, CLI flag.
  - `TestWildlifeProb` (6 tests): default is one, zero suppresses, valid output
    for all probs, determinism, JSON field, CLI flag.
  - `TestPresets`: `test_all_presets_include_wildlife_count_and_prob` (5 subtests)
    — verifies every preset includes `wildlife_count` and `wildlife_prob` with
    valid ranges.
- This fulfills the "Next likely steps" from Session 141: add `--wildlife-count`,
  `--wildlife-prob` for configurable wildlife density, and per-preset wildlife
  count and probability.
- Tests increased from 882 to 898 total (18 todo + 880 landscape), subtests
  unchanged at 276.

### Current status
Working. All 898 tests pass (18 todo + 880 landscape), 276 subtests.

### Next likely steps
- Expand other global word banks (more echoes, more soundscapes, more
  time-of-day, more seasons, more wildlife)
- Add spatial geometry dimension (e.g. scale, perspective, distance)

## 2026-07-15

### What was done (Session 141)
- **Added wildlife/inhabitants as a new sensory dimension** — a new `WILDLIFE`
  word bank of 10 evocative phrases describing creatures and inhabitants in the
  landscape (e.g. "A herd of {adj} deer picks its way {adverb} through the
  {display}.", "Eyes watch from the shadows of the {display} — patient,
  unblinking, {adj}.", "Tracks in the {adj} earth suggest a presence that moves
  {adverb} just ahead through the {display}.").
  - Each phrase uses `{display}`, `{adverb}`, `{color}`, `{adj}`, `{element}`
    template placeholders, following the same pattern as soundscapes.
  - Off by default (`wildlife_enabled=False`), preserving all existing seed-based
    output for users who don't use `--wildlife`.
  - Picked via `rng.choice(WILDLIFE)` — one phrase appended per landscape when
    enabled.
  - Suppressed at detail=0 (like echoes/legends/soundscapes/wistful) — wildlife
    feels like a detail that only makes sense with at least a minimal description.
  - Works with all features: detail=0, prose/poetic/json, combine, echo, legend,
    soundscape, travelogue, wistful, time-of-day, season, all biomes.
  - Seed-breaking when enabled: one `rng.choice()` call shifts subsequent random
    picks. Determinism is preserved (same seed + same args = same output).
- **Added `--wildlife` CLI flag** (boolean, default: off) — follows the same
  pattern as `--echo`, `--legend`, `--sound`, `--time`, `--season`.
- **Added `--describe-wildlife` CLI flag and `describe_wildlife()` function** —
  users can inspect all 10 wildlife phrases with index numbers, following the
  exact same introspection pattern as `describe_echoes()`, `describe_legends()`,
  etc.
- **Added `"wildlife_enabled"` to JSON metadata** when enabled — e.g.
  `"wildlife_enabled": True`.
- **Added `"wildlife_enabled"` to 4 of 5 presets** — `nightfall`, `pastoral`,
  `sublime`, and `dreamscape` all enable wildlife by default. `wasteland` has
  `wildlife_enabled: False` (thematic — desolate wasteland shouldn't teem with
  life). This follows the established pattern: add as opt-in CLI flag, then
  integrate into presets in the same session.
  - Preset gating checks `args.wildlife is False and not args.no_wildlife`
    before applying the preset value — consistent with all other preset gating.
  - Seed-breaking when presets are used: one extra `rng.choice(WILDLIFE)` call
    shifts subsequent random picks. Determinism is preserved (same seed + same
    args = same output).
- **Added `--no-wildlife` CLI flag** — users can now explicitly disable wildlife
  phrases even when using presets that enable them. Follows the exact same
  pattern as `--no-echo`, `--no-legend`, `--no-sound`, `--no-travelogue`,
  `--no-wistful`, `--no-time`, `--no-season`.
  - `--no-wildlife` forces `wildlife_enabled=False` regardless of preset config
    or explicit `--wildlife`.
  - Post-preset override block ensures `--no-wildlife` always wins after all
    gating.
- Added 35 new tests (20 in `TestWildlife`, 9 in `TestDescribeWildlife`, 5 in
  `TestNoWildlife`, 1 in `TestPresets`):
  - `TestWildlife` (20 tests): disabled by default, enabled appears, valid
    output, determinism, differs from plain, detail=0, JSON format/field,
    combine, echo, legend, travelogue, sound, wistful, time-of-day, season,
    poetic format, all biomes, CLI flag.
  - `TestDescribeWildlife` (9 tests): returns string, header, all phrases,
    index numbers, last index, CLI flag, stdout, no landscape generated.
  - `TestNoWildlife` (5 tests): flag exists via CLI, disables wildlife with
    presets (5 subtests), works with other features, JSON output, explicit
    `--wildlife` override.
  - `TestPresets`: `test_all_presets_include_wildlife_enabled` (5 subtests).
- This directly fulfills the second "Next likely step" from Session 140: add
  inhabitants/wildlife as a new sensory dimension. After many sessions of word
  bank expansions, this adds a genuinely new dimension to the landscape generator.
- Tests increased from 847 to 882 total (18 todo + 864 landscape), subtests
  from 253 to 276.

### Current status
Working. All 898 tests pass (18 todo + 880 landscape), 276 subtests.

## 2026-07-15

### What was done (Session 139)
- **Added `time_count` and `time_prob` to all 5 presets** with curated values
  that match each preset's mood/theme:
  - `nightfall`: `time_count=2, time_prob=0.7` — multiple time-of-day phrases,
    not always present, matching echo/sound/legend/season count and prob
  - `pastoral`: `time_count=1, time_prob=0.6` — single gentle temporal phrase,
    occasionally absent for serene timelessness
  - `sublime`: `time_count=2, time_prob=0.95` — rich temporal detail almost
    always present
  - `wasteland`: `time_count=1, time_prob=1.0` — always a stark temporal
    reference
  - `dreamscape`: `time_count=2, time_prob=0.85` — surreal temporal framing
    usually present
- The gating code was already in place from Session 136 — only the PRESETS
  dict values needed updating, following the same pattern as every other
  per-preset count/prob integration (echo, sound, weather, legend, season).
- Added 1 new test in TestPresets (`test_all_presets_include_time_count_and_prob`)
  — verifies every preset includes `time_count` and `time_prob` with valid
  ranges, following the same pattern as
  `test_all_presets_include_season_count_and_prob`.
- This directly fulfills the last "Next likely step" from Session 138: add
  `--time-count`, `--time-prob` to presets with curated values.
- Tests increased from 846 to 847 total (18 todo + 829 landscape), subtests
  from 248 to 253.

### Current status
Working. All 847 tests pass (18 todo + 829 landscape), 253 subtests.

### Next likely steps
- Expand global word banks (more time-of-day, more echoes, more legends, more
  soundscapes, more seasons)
- Add inhabitants/wildlife as a new sensory dimension
- Add spatial geometry dimension (e.g. scale, perspective, distance)

## 2026-07-15

### What was done (Session 138)
- **Added `season_count` and `season_prob` to all 5 presets** with curated values
  that match each preset's mood/theme:
  - `nightfall`: `season_count=2, season_prob=0.7` — multiple seasonal phrases,
    not always present, matching echo/sound/legend count and prob
  - `pastoral`: `season_count=1, season_prob=0.6` — single gentle seasonal phrase,
    occasionally absent for serene timelessness
  - `sublime`: `season_count=2, season_prob=0.95` — rich seasonal detail almost
    always present
  - `wasteland`: `season_count=1, season_prob=1.0` — always a stark seasonal
    phrase
  - `dreamscape`: `season_count=2, season_prob=0.85` — surreal seasonal phrases
    usually present
- The gating code was already in place from Session 137 — only the PRESETS dict
  values needed updating, following the same pattern as every other per-preset
  count/prob integration (echo, sound, weather, legend, etc.).
- Added 1 new test in TestPresets (`test_all_presets_include_season_count_and_prob`)
  — verifies every preset includes `season_count` and `season_prob` with valid
  ranges, following the same pattern as `test_all_presets_include_sound_count_and_prob`.
- This directly fulfills the last "Next likely step" from Session 137: add
  `--season-count`, `--season-prob` to presets with curated values.
- Tests increased from 845 to 846 total (18 todo + 828 landscape), subtests
  unchanged at 243.

### Current status
Working. All 846 tests pass (18 todo + 828 landscape), 243 subtests.

### Next likely steps
- Expand global word banks (more time-of-day, more echoes, more legends, more
  soundscapes, more seasons)
- Add inhabitants/wildlife as a new sensory dimension
- Add spatial geometry dimension (e.g. scale, perspective, distance)
- Add `--time-count`, `--time-prob` to presets with curated values (same pattern
  as season_count/season_prob)

## 2026-07-15

### What was done (Session 137)
- **Added `--season-count` and `--season-prob` CLI flags** — users can now control
  how many seasonal phrases appear per landscape (0-3, default: 1) and how often
  each roll succeeds (0.0-1.0, default: 1.0), following the exact same pattern as
  `--time-count`/`--time-prob`, `--echo-count`/`--echo-prob`,
  `--sound-count`/`--sound-prob`, and `--weather-count`/`--weather-prob`.
  - `season_count=0` suppresses all seasonal phrases (alternative to `--no-season`)
  - `season_count=1` (default) produces exactly 1 phrase (existing behavior)
  - `season_count=2` and `season_count=3` produce multiple distinct seasonal phrases
    with dedup (preventing the same phrase from appearing twice)
  - `season_prob=0.0` suppresses all seasonal phrases even with `season_count > 0`
  - Each of `season_count` rolls independently draws `rng.random() < season_prob`
  - Default `season_count=1, season_prob=1.0` preserves backward compatibility —
    all existing seed-based output with `--season` is unchanged
- **Added `season_count` and `season_prob` params to `generate_landscape()`** —
  defaults 1 and 1.0 respectively, preserving all existing behavior.
- **Added `season_count` and `season_prob` to JSON metadata** when non-default
  values are used — `season` is a list of strings when multiple phrases are
  generated, and a single string when only one (backward compatible).
- **Added preset gating for `season_count` and `season_prob`** — follows the same
  pattern as `time_count`/`time_prob` gating, so presets can optionally configure
  seasonal density (not yet added to any preset).
- Added 16 new tests (9 in `TestSeasonCount`, 7 in `TestSeasonProb`):
  - `TestSeasonCount`: default is one, zero suppresses, multi-season with count=3,
    no repeat same phrase, valid output for all counts, determinism, JSON format,
    JSON field, CLI flag.
  - `TestSeasonProb`: default is one, zero suppresses, valid output for all probs,
    determinism, JSON field, CLI flag.
- Added `SEASON_INDICATORS` list (15 invariant substrings from SEASONS)
  for use by the new tests.
- This fulfills the first "Next likely step" from Session 136: add
  `--season-count`, `--season-prob` for configurable seasonal density.
- Tests increased from 812 to 845 total (18 todo + 827 landscape), subtests
  unchanged at 243.

### Current status
Working. All 845 tests pass (18 todo + 827 landscape), 243 subtests.

### Next likely steps
- Expand global word banks (more time-of-day, more echoes, more legends, more
  soundscapes, more seasons)
- Add inhabitants/wildlife as a new sensory dimension
- Add spatial geometry dimension (e.g. scale, perspective, distance)
- Add `--season-count`, `--season-prob` to presets with curated values

## 2026-07-15

### What was done (Session 136)
- **Added `--time-count` and `--time-prob` CLI flags** — users can now control how
  many time-of-day phrases appear per landscape (0-3, default: 1) and how often
  each roll succeeds (0.0-1.0, default: 1.0), following the exact same pattern as
  `--echo-count`/`--echo-prob`, `--sound-count`/`--sound-prob`, and
  `--weather-count`/`--weather-prob`.
  - `time_count=0` suppresses all time-of-day phrases (alternative to `--no-time`)
  - `time_count=1` (default) produces exactly 1 phrase (existing behavior)
  - `time_count=2` and `time_count=3` produce multiple distinct time-of-day phrases
    with dedup (preventing the same phrase from appearing twice)
  - `time_prob=0.0` suppresses all time-of-day even with `time_count > 0`
  - Each of `time_count` rolls independently draws `rng.random() < time_prob`
  - Default `time_count=1, time_prob=1.0` preserves backward compatibility — all
    existing seed-based output with `--time` is unchanged
- **Added `time_count` and `time_prob` params to `generate_landscape()`** —
  defaults 1 and 1.0 respectively, preserving all existing behavior.
- **Added `time_count` and `time_prob` to JSON metadata** when non-default values
  are used — `time_of_day` is a list of strings when multiple phrases are
  generated, and a single string when only one (backward compatible).
- **Added preset gating for `time_count` and `time_prob`** — follows the same
  pattern as `echo_count`/`echo_prob` gating, so presets can optionally configure
  time-of-day density (not yet added to any preset).
- Added 15 new tests (9 in `TestTimeCount`, 6 in `TestTimeProb`):
  - `TestTimeCount`: default is one, zero suppresses, multi-time with count=3,
    no repeat same phrase, valid output for all counts, determinism, JSON format,
    JSON field, CLI flag.
  - `TestTimeProb`: default is one, zero suppresses, valid output for all probs,
    determinism, JSON field, CLI flag.
- Added `TIME_INDICATORS` list (15 invariant substrings from TIMES_OF_DAY)
  for use by the new tests.
- This fulfills the third "Next likely step" from Session 134/135: add
  `--time-count`, `--time-prob` for configurable time-of-day density.
- Tests increased from 797 to 812 total (18 todo + 794 landscape), subtests
  unchanged at 243.

### Current status
Working. All 812 tests pass (18 todo + 794 landscape), 243 subtests.

### Next likely steps
- Add `--season-count`, `--season-prob` for configurable seasonal density
- Expand global word banks (more time-of-day, more echoes, more legends, more
  soundscapes)
- Add inhabitants/wildlife as a new sensory dimension
- Add spatial geometry dimension (e.g. scale, perspective, distance)

### What was done (Session 134)
- **Added seasonal variation system** — a new `SEASONS` word bank of 10 evocative
  seasonal phrases (e.g. "It is early spring — the first buds push through the
  thawing earth", "Deep winter wraps the landscape in silence and frost") that
  establish the time of year, adding a seasonal-temporal dimension alongside
  the existing time-of-day system.
  - Each phrase is a standalone sentence prepended to the opening with a period,
    following the exact same pattern as time-of-day.
  - 10 curated phrases covering: early spring, high summer, autumn, deep winter,
    late spring, midsummer, early autumn, first snow, late autumn, spring thunder.
  - Off by default (`season_enabled=False`), preserving all existing seed-based
    output.
  - Picked via `rng.choice(SEASONS)` — one phrase prepended when enabled.
  - Works with all features: detail=0, prose/poetic/json, combine, echo, legend,
    soundscape, travelogue, wistful, time-of-day, presets.
  - Not suppressed at detail=0 (like time-of-day) — season is a framing prefix
    suitable even for minimal descriptions.
  - When both season and time-of-day are enabled, season comes first (outermost
    framing), then time-of-day, then the opening. E.g. "It is early spring.
    Dawn breaks over the landscape. A vast crystal forest..."
  - Seed-breaking when enabled: one `rng.choice()` call before the time-of-day
    pick, shifting subsequent random picks. Determinism is preserved (same seed
    + same args = same output).
- **Added `--season` CLI flag** (boolean, default: off) — follows the same
  pattern as `--time`, `--echo`, `--legend`, `--sound`.
- **Added `--describe-seasons` CLI flag and `describe_seasons()` function** —
  users can inspect all 10 seasonal phrases with index numbers, following the
  exact same introspection pattern as `describe_times()`, `describe_echoes()`,
  etc.
- **Added `"season"` to JSON metadata when enabled** — contains the full phrase
  string (e.g. `"season": "It is early spring — the first buds push through the
  thawing earth"`).
- **Added `"season_enabled": True` to all 5 presets** — every preset (`nightfall`,
  `pastoral`, `sublime`, `wasteland`, `dreamscape`) now includes seasonal framing
  by default. This follows the same trajectory as every other sensory feature:
  add as opt-in, then integrate into presets in the same session.
  - Preset gating checks `args.season is False and not args.no_season` before
    applying the preset value — consistent with all other preset gating.
  - Seed-breaking when presets are used: one extra `rng.choice(SEASONS)` call
    before the time-of-day/shift shifts subsequent random picks. Determinism
    is preserved (same seed + same args = same output).
- **Added `--no-season` CLI flag** — users can now explicitly disable seasonal
  phrases even when using presets that enable them. Follows the exact same
  pattern as `--no-time`, `--no-echo`, `--no-legend`, `--no-sound`,
  `--no-travelogue`, and `--no-wistful`.
  - `--no-season` forces `season_enabled=False` regardless of preset config or
    explicit `--season`.
  - Post-preset override block ensures `--no-season` always wins after all gating.
- Added 35 new tests (20 in `TestSeason`, 8 in `TestDescribeSeasons`, 6 in
  `TestNoSeason`, 1 in `TestPresets`):
  - `TestSeason` (20 tests): disabled by default, enabled appears, valid output,
    determinism, differs from plain, prepends opening, JSON format, detail=0,
    combine, echo, legend, travelogue, sound, wistful, CLI flag, works with
    time-of-day, JSON field present/absent, poetic format, all biomes.
  - `TestDescribeSeasons` (8 tests): returns string, header, all phrases, index
    numbers, last index, CLI flag, stdout output, no landscape generated.
  - `TestNoSeason` (6 tests): flag exists via CLI, disables season with all 5
    presets (5 subtests), works with other features, JSON output, explicit
    `--season` override.
  - `TestPresets`: `test_all_presets_include_season_enabled` (5 subtests).
- This fulfills the first "Next likely step" from Session 133: add seasonal
  variation as another temporal dimension.
- Tests increased from 780 to 797 total (18 todo + 779 landscape), subtests from
  222 to 243.

### Current status
Working. All 797 tests pass (18 todo + 779 landscape), 243 subtests.

### Next likely steps
- Expand global word banks (more time-of-day, more echoes, more legends, more
  soundscapes)
- Add inhabitants/wildlife as a new sensory dimension
- Add `--time-count`, `--time-prob` for configurable time-of-day density
- Add `--season-count`, `--season-prob` for configurable seasonal density
- Add spatial geometry dimension (e.g. scale, perspective, distance)

## 2026-07-15

### What was done (Session 135)
- **Expanded SEASONS word bank from 10 to 15 phrases** — 5 new seasonal phrases
  added, covering seasonal niches not represented in the original 10:
  - `"Late winter's grip loosens as meltwater carves through the ice"` — late
    winter thaw, the transition between winter and spring
  - `"The lengthening shadows of late summer stretch across fields heavy with
    seed"` — late summer abundance sloping toward autumn
  - `"A pale autumn sun hangs low as the landscape prepares for winter's rest"` —
    autumn's quiet preparation for dormancy
  - `"A hard winter freeze transforms the landscape into a palace of crystal and
    ice"` — winter's stark crystalline beauty, distinct from deep winter
    (silence/frost) and first snow (muffled in white)
  - `"The soft persistent rain of early spring washes winter's last traces
    away"` — cleansing spring rain, a gentler complement to spring thunder
- Each phrase is curated to fit a distinct seasonal niche: late winter thaw, late
  summer abundance, autumn dormancy preparation, hard winter freeze, persistent
  spring rain. None overlap with existing phrases.
- No code, CLI, or test changes — data-only expansion. All 797 tests still pass
  (18 todo + 779 landscape), 243 subtests unchanged.
- This directly fulfills the first "Next likely step" from Session 134: expand
  global word banks (more seasons).

## 2026-07-15

### What was done (Session 132)
- **Added time-of-day to all 5 presets** — every preset (`nightfall`, `pastoral`,
  `sublime`, `wasteland`, `dreamscape`) now includes `"time_of_day_enabled": True`,
  making time-of-day phrases active by default when using any preset. This follows
  the same trajectory as every other sensory feature (echoes: Session 88, legends:
  Session 97, travelogue: Session 106, wistful: Session 110, soundscapes:
  Session 113): add the feature as opt-in, then integrate into presets.
  - Each preset gets one randomly chosen time-of-day phrase from the 10-phrase
    pool — matching the preset's mood.
  - Preset gating checks `args.time is False and not args.no_time` before applying
    the preset value — consistent with all other preset gating.
  - Seed-breaking when presets are used: one extra `rng.choice(TIMES_OF_DAY)` call
    before the opening shifts subsequent random picks. Determinism is preserved
    (same seed + same args = same output).
- **Added `--no-time` CLI flag** — users can now explicitly disable time-of-day
  phrases even when using presets that enable them. Follows the exact same pattern
  as `--no-echo`, `--no-legend`, `--no-sound`, `--no-travelogue`, and `--no-wistful`.
  - `--no-time` forces `time_of_day_enabled=False` regardless of preset config or
    explicit `--time`.
  - Post-preset override block ensures `--no-time` always wins after all gating.
- Added 7 new tests (1 structural + 6 functional):
  - `test_all_presets_include_time_of_day_enabled` (5 subtests) — verifies every
    preset has `"time_of_day_enabled": True`.
  - `TestNoTime` (6 tests): flag exists via CLI, disables time with all 5 presets
    (5 subtests), works with other features, JSON output, explicit `--time` override.
- This fulfills the two most obvious "Next likely steps" from Session 131: add
  time-of-day to presets (Step 1) and add `--no-time` flag (Step 2).
- Tests increased from 773 to 780 total (18 todo + 762 landscape), subtests from
  207 to 222.

### What was done (Session 133)
- **Expanded TIMES_OF_DAY word bank from 10 to 15 phrases** — 5 new time-of-day
  phrases added, covering temporal niches not represented in the original 10:
  - `"Late afternoon stretches long shadows across the landscape"` — late afternoon
    before golden hour, covering the long-shadow period between noon and dusk
  - `"A storm-heavy sky presses down upon the landscape"` — stormy/overcast
    conditions, the only non-clear-sky temporal setting
  - `"The blue hour casts a deep indigo glow across the landscape"` — the
    photographic/atmospheric blue hour between daylight and full darkness
  - `"The witching hour settles over the landscape in absolute stillness"` — 3 AM
    supernatural hour, distinct from midnight (crescent moon) and dead of night
  - `"Morning mist clings to the landscape like a half-remembered dream"` —
    misty/mysterious morning, a different register from dawn and early morning
- Each phrase is curated to fit a distinct temporal niche: late afternoon, stormy,
  blue hour, witching hour, misty morning. None overlap with existing phrases.
- No code, CLI, or test changes — data-only expansion. All 780 tests still pass
  (18 todo + 762 landscape), 222 subtests unchanged.
- This directly fulfills the first "Next likely step" from Session 132: expand
  global word banks (more time-of-day phrases).

### Current status
Working. All 780 tests pass (18 todo + 762 landscape), 222 subtests.

### Next likely steps
- Add seasonal variation as another temporal dimension
- Expand global word banks (more echoes, more legends, more soundscapes)
- Add inhabitants/wildlife as a new sensory dimension
- Add `--time-count`, `--time-prob` for configurable time-of-day density

## 2026-07-14

### What was done (Session 131)
- **Added time-of-day system** — a new `TIMES_OF_DAY` word bank of 10 evocative phrases (e.g. "Dawn breaks over the landscape", "The dead of night holds the land in darkness", "The golden hour before sunset paints everything amber") that establish when the landscape is being viewed, adding a temporal-setting dimension distinct from the existing `TIME_WORDS` (which are narrative adverbs like "already", "still").
  - Each phrase is a standalone sentence prepended to the opening with a period: `"Dawn breaks over the landscape. A vast crystal forest of vivid mist stretches..."`.
  - 10 curated phrases covering: dawn, dead of night, blazing noon, dusk, early morning, midnight moonlight, twilight, golden hour, first light, starless night.
  - Off by default (`time_of_day_enabled=False`), preserving all existing seed-based output.
  - Picked via `rng.choice(TIMES_OF_DAY)` — one phrase prepended when enabled.
  - Works with all features: detail=0, prose/poetic/json, combine, echo, legend, soundscape, travelogue, wistful, presets.
  - Not suppressed at detail=0 (unlike echoes/legends) — time-of-day is a framing prefix suitable even for minimal descriptions.
  - Seed-breaking when enabled: one `rng.choice()` call before the opening template, shifting subsequent picks. Determinism is preserved (same seed + same args = same output).
- Added `--time` CLI flag (boolean, default: off) — follows the same pattern as `--echo`, `--legend`, `--sound`.
- Added `--describe-times` CLI flag and `describe_times()` function — users can inspect all 10 time-of-day phrases with index numbers, following the exact same introspection pattern as `describe_echoes()`, `describe_legends()`, etc.
- Added `"time_of_day"` to JSON metadata when enabled — contains the full phrase string (e.g. `"time_of_day": "Dawn breaks over the landscape"`).
- Added 27 new tests:
  - `TestTimeOfDay` (20 tests): disabled by default, enabled appears, output validity, determinism, differs from plain, prepends opening, JSON format, JSON field present/absent, detail=0, combine, echo, legend, travelogue, sound, wistful, poetic format, all biomes, CLI flag existence.
  - `TestDescribeTimes` (7 tests): returns string, header, all phrases, index numbers, last index, CLI flag, stdout output, no landscape generation.
- This fulfills the "Add a new sensory dimension (e.g. time-of-day)" next step explicitly called out in Sessions 123–130. After 6 consecutive sessions of word bank expansions, this adds a genuinely new temporal dimension.
- Tests increased from 746 to 773 total (18 todo + 755 landscape), subtests from 201 to 207.

### Current status
Working. All 773 tests pass (18 todo + 755 landscape), 207 subtests.

### Next likely steps
- Add time-of-day to presets (opt-in per-preset like echo/legend/sound)
- Add `--no-time` flag for symmetry with other `--no-*` flags
- Add seasonal variation as another temporal dimension
- Further expand global word banks (more echoes, legends, soundscapes, wistful phrases)
- Add inhabitants/wildlife as a new sensory dimension

## 2026-07-14

### What was done (Session 130)
- **Expanded biome-specific weather and anomaly banks for all 13 biomes** — each biome now has +2 weathers and +2 anomalies (52 new entries total), the sixth and seventh expansions of biome-specific word banks after Sessions 125 (adjectives/elements), 126 (nouns), 127 (verbs), 128 (colors), and 129 (adverbs). Prior to this, all biomes had exactly 3 weathers and 3 anomalies. Now each biome has 5 weathers and 5 anomalies:
  - **forest** (3→5 weathers): +"a light drizzle filters through the canopy like whispered secrets", "the forest floor releases the scent of damp earth after rain"
  - **forest** (3→5 anomalies): +"The trees grow in a perfect circle around a patch of sky that never clouds.", "Every creature in the forest falls silent at the same moment each day."
  - **desert** (3→5 weathers): +"sandstorms gather on the horizon like walls of amber", "a rare rain falls, each drop sizzling against the hot stone"
  - **desert** (3→5 anomalies): +"Footprints behind you fill with water that has no source.", "The stars rearrange themselves into unfamiliar constellations at midnight."
  - **ocean** (3→5 weathers): +"rain falls on the surface like a thousand drummers", "a deep fog bank rolls across the water, swallowing the horizon"
  - **ocean** (3→5 anomalies): +"Pressure changes in ways that do not correspond to depth.", "Whales sing in frequencies that vibrate through bone, though no whales are near."
  - **tundra** (3→5 weathers): +"ice crystals hang in the air like frozen diamonds", "a strange warmth rises from beneath the permafrost"
  - **tundra** (3→5 anomalies): +"The snow remembers every footprint ever pressed into it.", "A mountain in the distance has not moved, yet it is closer than yesterday."
  - **mountain range** (3→5 weathers): +"snow falls in heavy silence, muffling the world", "a warm wind descends from the peaks, carrying the scent of distant valleys"
  - **mountain range** (3→5 anomalies): +"There is a peak that appears only in reflections.", "The mountain casts two shadows under a single sun."
  - **swamp** (3→5 weathers): +"a phosphorescent mist rises from the water at dusk", "thunder rolls across the marsh without lightning"
  - **swamp** (3→5 anomalies): +"Moss-covered trees whisper conversations from a century past.", "Every pair of eyes in the swamp blinks in perfect unison."
  - **cave system** (3→5 weathers): +"a low mist hugs the cave floor, cool and thick", "an underground stream sings somewhere in the darkness"
  - **cave system** (3→5 anomalies): +"Stalactites and stalagmites grow toward each other at visible speed.", "The darkness here has weight — it presses against your back."
  - **plain** (3→5 weathers): +"a slow breeze carries the scent of wildflowers from miles away", "a bank of fog rolls in from the horizon at dusk"
  - **plain** (3→5 anomalies): +"The grass grows in the shape of a language that predates humanity.", "Every footstep you take is echoed by a second set of footsteps that stop when you stop."
  - **volcanic field** (3→5 weathers): +"sulfur fumes drift across the cracked earth in low-lying clouds", "a hot rain of ash and cinders falls without warning"
  - **volcanic field** (3→5 anomalies): +"The ground beneath your feet pulses with a heartbeat that is not your own.", "Molten rock flows in formations that spell out coordinates to nowhere."
  - **coral reef** (3→5 weathers): +"underwater currents carry a symphony of clicks and pops", "the tide pulls in patterns that do not follow the moon"
  - **coral reef** (3→5 anomalies): +"The reef glows in wavelengths visible only to something that has been watching.", "Time passes differently here — hours feel like minutes, minutes like hours."
  - **ruined city** (3→5 weathers): +"a rust-colored drizzle stains the concrete further", "dust devils spin through collapsed intersections"
  - **ruined city** (3→5 anomalies): +"The city gives birth to new streets at night — a map that redraws itself.", "All the doors in the city are slightly ajar, as if someone just left."
  - **fungal grove** (3→5 weathers): +"spore-laden rain falls in curtains of gold and silver", "a warm mist carries the sweet scent of fungal bloom"
  - **fungal grove** (3→5 anomalies): +"The mycelium network reacts to your thoughts — the glow shifts as you approach.", "Fungal growths form temporary sculptures that collapse and reform in endless cycles."
  - **sky islands** (3→5 weathers): +"rain falls upward from the cloud sea below", "a thin mist wraps each island in solitude"
  - **sky islands** (3→5 anomalies): +"The islands cast shadows onto the clouds below — shadows that move independently.", "Gravity weakens at the center of each island, as if the land itself is trying to float free."
- Each weather and anomaly is curated to the biome's thematic identity — desert anomalies (footprints filling with water, stars rearranging), ocean weathers (rain like drummers, fog swallowing the horizon), cave anomalies (stalactites growing visibly, darkness with weight), sky island anomalies (shadows moving independently, gravity weakening), etc.
- No code, CLI, or test changes — data-only expansion. All 746 tests still pass (18 todo + 728 landscape), 201 subtests.
- Weathers appear in weather templates via `_pick("weathers", ...)` which blends biome-specific weathers with the global WEATHERS pool (12 entries). Expanding biome weathers from 3→5 means 62% more biome-specific weather variety, making weather descriptions more distinctive per biome.
- Anomalies appear in anomaly templates via `_pick("anomalies", ...)` which blends biome-specific anomalies with the global ANOMALIES pool (8 entries). Expanding biome anomalies from 3→5 means 62% more biome-specific anomaly variety, making anomalies feel more grounded in the landscape.
- Weathers and anomalies were the last two biome word bank categories at their original size (3 each). After 5 consecutive sessions expanding individual categories (adjectives/elements, nouns, verbs, colors, adverbs), this session completed the final two in a single pass.

### What was done (Session 129)
- **Expanded biome-specific adverb banks for all 13 biomes** — each biome now has +2 adverbs (26 new entries total), the fifth expansion of biome-specific word banks after Sessions 125 (adjectives/elements), 126 (nouns), 127 (verbs), and 128 (colors). Prior to this, all biomes had exactly 3 adverbs. Now each biome has 5 adverbs:
  - **forest** (3→5): +"wistfully", "invitingly"
  - **desert** (3→5): +"mercilessly", "brutally"
  - **ocean** (3→5): +"rhythmically", "hypnotically"
  - **tundra** (3→5): +"bitterly", "indifferently"
  - **mountain range** (3→5): +"steadily", "proudly"
  - **swamp** (3→5): +"sullenly", "lazily"
  - **cave system** (3→5): +"remotely", "inexorably"
  - **plain** (3→5): +"tranquilly", "openly"
  - **volcanic field** (3→5): +"fiercely", "explosively"
  - **coral reef** (3→5): +"vibrantly", "flowingly"
  - **ruined city** (3→5): +"hollowly", "wearily"
  - **fungal grove** (3→5): +"organically", "prolifically"
  - **sky islands** (3→5): +"weightlessly", "distantly"
- Each adverb is curated to the biome's thematic identity — harsh adverbs for desert (mercilessly, brutally), marine adverbs for ocean (rhythmically, hypnotically), ruin adverbs for ruined city (hollowly, wearily), aerial adverbs for sky islands (weightlessly, distantly), etc.
- No code, CLI, or test changes — data-only expansion. All 746 tests still pass (18 todo + 728 landscape), 201 subtests.
- Adverbs appear in multiple template slots (opening templates, middle templates, echo phrases, soundscape phrases), so expanding them has broad per-word impact on output variety.
- This fulfills the "Expand remaining biome word bank categories (adverbs, weathers, anomalies)" next step from Session 128. Adverbs were the smallest biome category at 3 words each.

### Current status
Working. All 746 tests pass (18 todo + 728 landscape), 201 subtests.

### Next likely steps
- Expand remaining biome word bank categories (weathers, anomalies)
- Add new sensory dimension (e.g. seasonal variation, time-of-day, spatial geometry, inhabitants/wildlife)

### What was done (Session 128)
- **Expanded biome-specific color banks for all 13 biomes** — each biome now has +2 colors (26 new entries total), the fourth expansion of biome-specific word banks after Sessions 125 (adjectives/elements), 126 (nouns), and 127 (verbs). Prior to this, all biomes had exactly 4 colors. Now each biome has 6 colors:
- **Expanded biome-specific color banks for all 13 biomes** — each biome now has +2 colors (26 new entries total), the fourth expansion of biome-specific word banks after Sessions 125 (adjectives/elements), 126 (nouns), and 127 (verbs). Prior to this, all biomes had exactly 4 colors. Now each biome has 6 colors:
  - **forest** (4→6): +"woodland", "forest green"
  - **desert** (4→6): +"sand", "terracotta"
  - **ocean** (4→6): +"aquamarine", "indigo"
  - **tundra** (4→6): +"permafrost white", "glacier blue"
  - **mountain range** (4→6): +"stone grey", "alpine"
  - **swamp** (4→6): +"khaki", "peat brown"
  - **cave system** (4→6): +"cave-dark", "mineral blue"
  - **plain** (4→6): +"tawny", "dusty rose"
  - **volcanic field** (4→6): +"scoria red", "pumice grey"
  - **coral reef** (4→6): +"scarlet", "coral pink"
  - **ruined city** (4→6): +"pale grey", "verdigris"
  - **fungal grove** (4→6): +"mushroom beige", "sporescent"
  - **sky islands** (4→6): +"dawn pink", "storm grey"
- Each color is curated to the biome's thematic identity — geological colors for mountain ranges (stone grey, alpine), marine colors for ocean (aquamarine, indigo), ruin colors for ruined city (pale grey, verdigris), aerial colors for sky islands (dawn pink, storm grey), etc.
- No code, CLI, or test changes — data-only expansion. All 746 tests still pass (18 todo + 728 landscape), 201 subtests.
- Colors appear in multiple template slots (opening templates, middle templates, weather templates, anomaly templates, echo phrases, soundscape phrases), so expanding them has broad per-word impact on output variety.

### Current status
Working. All 746 tests pass (18 todo + 728 landscape), 201 subtests.

### Next likely steps
- Expand remaining biome word bank categories (adverbs, weathers, anomalies)
- Add new sensory dimension (e.g. seasonal variation, time-of-day, spatial geometry, inhabitants/wildlife)

### What was done (Session 127)
- **Expanded biome-specific verb banks for all 13 biomes** — each biome now has +2 verbs (26 new entries total), the third expansion of biome-specific word banks after Session 125's adjective/element expansion and Session 126's noun expansion. Prior to this, all biomes had exactly 5 verbs. Now each biome has 7 verbs:
  - **forest** (5→7): +"dapple", "sigh"
  - **desert** (5→7): +"wither", "glare"
  - **ocean** (5→7): +"swell", "roar"
  - **tundra** (5→7): +"shiver", "blast"
  - **mountain range** (5→7): +"sculpt", "shelter"
  - **swamp** (5→7): +"sink", "rot"
  - **cave system** (5→7): +"carve", "murmur"
  - **plain** (5→7): +"ripple", "gleam"
  - **volcanic field** (5→7): +"spit", "quake"
  - **coral reef** (5→7): +"spawn", "flicker"
  - **ruined city** (5→7): +"fracture", "whine"
  - **fungal grove** (5→7): +"spiral", "weep"
  - **sky islands** (5→7): +"glide", "sail"
- Each verb is curated to the biome's thematic identity — geological verbs for mountain ranges (sculpt, shelter), marine verbs for ocean (swell, roar), ruin verbs for ruined city (fracture, whine), aerial verbs for sky islands (glide, sail), etc.
- No code, CLI, or test changes — data-only expansion. All 746 tests still pass (18 todo + 728 landscape), 201 subtests.
- Verbs appear in multiple middle template slots (e.g. "The {adj} {noun} {verb} {adverb} with {color} {element}"), so expanding them has broad per-word impact on output variety.

### What was done (Session 126)
- **Expanded biome-specific noun banks for all 13 biomes** — each biome now has +2 nouns (26 new entries total), the second expansion of biome-specific word banks after Session 125's adjective/element expansion. Prior to this, biome nouns were at 5 entries for 10 biomes and 6 entries for 3 biomes (ruined city, fungal grove, sky islands). Now all biomes have 7–8 nouns:
  - **forest** (5→7): +"understory", "clearings"
  - **desert** (5→7): +"wadis", "buttes"
  - **ocean** (5→7): +"gyres", "thermals"
  - **tundra** (5→7): +"moraines", "frost heaves"
  - **mountain range** (5→7): +"coloirs", "cirques"
  - **swamp** (5→7): +"sloughs", "tupelos"
  - **cave system** (5→7): +"flowstones", "pillars"
  - **plain** (5→7): +"savannas", "swales"
  - **volcanic field** (5→7): +"fumaroles", "tuff cones"
  - **coral reef** (5→7): +"sea fans", "crevices"
  - **ruined city** (6→8): +"skeletons", "rubble piles"
  - **fungal grove** (6→8): +"mycelia", "sporocarps"
  - **sky islands** (6→8): +"thermals", "wind shears"
- Each noun is curated to the biome's thematic identity — geological features for mountain ranges, fungal anatomy for fungal groves, wreckage for ruined cities, etc.
- No code, CLI, or test changes — data-only expansion. All 746 tests still pass (18 todo + 728 landscape), 201 subtests.
- Nouns are used in multiple template slots (opening templates, middle templates), so expanding them has broad per-word impact on output variety.

### What was done (Session 124)
- **Expanded LEGENDS word bank from 15 to 20 phrases** — 5 new folkloric/historical phrases added, covering underrepresented legend themes:
  - `"The {display} appears in the dreams of those who have never seen it."` — prophetic dreams, unconscious connection to a place never visited
  - `"There is a bell in the {display} that rings only when no one is listening."` — paradoxical observation, observer-effect mystery
  - `"The {display} has a scent that cannot be described, only remembered."` — ineffable sensory quality, the limits of language
  - `"Every path through the {display} leads to the same clearing, no matter where you start."` — impossible geography, labyrinthine convergence
  - `"The {display} was built by no one, for no purpose, and yet it endures."` — purposeless endurance, existential mystery
- Added 5 new indicators to `LEGEND_INDICATORS` (`"appears in the dreams of those who have never"`, `"bell in the"`, `"scent that cannot be described"`, `"leads to the same clearing"`, `"built by no one"`) — each is a unique invariant substring that won't collide with other word bank output.
- No new tests or code changes beyond word bank expansion — all 728 landscape tests (746 total) still pass.
- Legends were last expanded in Session 98 (10→15). This is the second expansion (15→20), making legends the largest word bank alongside echoes (15).
- Tests unchanged: still 746 total (18 todo + 728 landscape), 201 subtests.

### Current status
Working. All 746 tests pass (18 todo + 728 landscape), 201 subtests.

### Next likely steps
- Expand other word banks (more wistful phrases, more soundscapes, more weathers)
- Add new sensory dimension (e.g. seasonal variation, time-of-day, spatial geometry)

### What was done (Session 123)
- **Expanded WISTFUL word bank from 6 to 10 phrases** — 4 new wistful phrases added, covering underrepresented wistful themes:
  - `"You will never be the same after visiting the {display}."` — irreversible transformation, the place changes the observer
  - `"There is nowhere else in the world like the {display}, and you have been lucky enough to see it."` — uniqueness + gratitude, rare privilege of experience
  - `"The {display} feels more like a memory of a place you have always known than a place you have just discovered."` — uncanny familiarity, recognition of the never-before-seen
  - `"You will try to tell others about the {display}, but the words will never be enough."` — ineffability, the limits of language to capture experience
- Added 4 new indicators to `WISTFUL_INDICATORS` in `TestWistful` (`"never be the same after visiting"`, `"nowhere else in the world like"`, `"more like a memory of a place"`, `"words will never be enough"`) and to `WISTFUL_INDICATORS_PHRASES` in the suppression-test module.
- Fixed the hardcoded indicator list in `test_preset_with_wistful_produces_wistful_output` — the list was a copy of the original 6 and didn't include the new 4 indicators, causing the test to fail with presets that happen to select one of the new phrases at seed=42. Updated from 6 to 10 indicators to match the expanded bank.
- No new tests or code changes beyond word bank expansion — all 746 tests still pass.
- Wistful was last modified in Session 108 (creation). This is its first expansion, making it consistent with the pattern of expanding other word banks (echoes: Session 122, soundscapes: Session 121, weathers: Session 120, legends: Session 98).

### Current status
Working. All 746 tests pass (18 todo + 728 landscape), 201 subtests.

### Next likely steps
- Expand other word banks (more legends, more wistful phrases is now at 10 — could go further)
- Add new sensory dimension (e.g. seasonal variation, time-of-day, spatial geometry)

### What was done (Session 122)
- **Expanded ECHOES word bank from 10 to 15 phrases** — 5 new atmospheric echo phrases added, covering underrepresented atmospheric themes:
  - `"Light {adverb} bends through the {adj} air of the {display} like something {color} is calling."` — visual refraction and color, light as summoning force
  - `"The wind carries a memory through the {display} {time_word}, a voice with no mouth."` — wind as carrier of memory, uncanny audible absence
  - `"Deep beneath the {display}, something vast turns over {adverb} in its sleep."` — subterranean presence, deep geological movement
  - `"The {display} holds its breath {time_word}, waiting for something that has not yet arrived."` — anticipation, the landscape poised on a threshold
  - `"There is a {color} scent of {element} caught in the {adj} air of the {display}."` — synesthetic scent, olfactory memory woven into the atmosphere
- Added 5 new `ECHO_INDICATORS` (`"bends through the"`, `"wind carries a memory"`, `"vast turns over"`, `"holds its breath"`, `"caught in the"`) — each is a unique invariant substring that won't collide with other word bank output.
- Added same 5 indicators to `NO_ECHO_INDICATORS` (none contain "remembers", so all are safe for no-echo suppression tests).
- No new tests or code changes beyond word bank expansion — all 728 landscape tests (746 total) still pass.
- This was the first explicit "Next likely step" from Session 121: expand other word banks (echoes had not been expanded since Session 78).
- Tests unchanged: still 746 total (18 todo + 728 landscape), 201 subtests.

### What was done (Session 121)
- **Expanded SOUNDSCAPES word bank from 8 to 12 phrases** — 4 new soundscape patterns added to increase auditory variety:
  - `"A low drone rises and falls {adverb} somewhere deep in the {display}."` — deep mechanical drone, persistent subconscious hum
  - `"The {element} of the {display} crackles {adverb} like distant radio static."` — natural electrical/static texture
  - `"Footsteps echo {adverb} through the {display}, though you are alone."` — uncanny presence, lone observer illusion
  - `"From the {adj} depths of the {display}, a single {color} note rings out {adverb}."` — pure musical tone, unexpected clarity
- Added 4 new `SOUND_INDICATORS` in the test module (`"drone rises and falls"`, `"crackles like distant"`, `"Footsteps echo through"`, `"note rings out"`) — each is a unique substring that won't collide with other word bank output.
- No new tests or code changes beyond word bank expansion — all 728 landscape tests (746 total) still pass.
- This directly fulfills the first "Next likely step" from Session 120: expand other word banks (soundscape phrases).

### What was done (Session 120)
- **Expanded WEATHERS word bank from 8 to 12 phrases** — 4 new weather patterns added to increase atmospheric variety:
  - `"snow falls in heavy flakes"` — wintry precipitation, common weight
  - `"a cold fog rolls in from nowhere"` — mysterious incursion
  - `"the ground exhales a thin vapor"` — organic/eerie exhalation
  - `"lightning flickers on the horizon"` — distant electrical drama
- Added `"snow falls in heavy flakes"` to `COMMON_WORDS` (snow is a common weather phenomenon across many biomes). The other 3 new phrases use normal weight (default, not in COMMON or RARE).
- Added 4 new `WEATHER_INDICATORS` in the test module (`"snow falls"`, `"cold fog rolls"`, `"exhales a thin"`, `"flickers on the"`) — each is a unique substring that won't collide with other word bank output.
- No new tests or code changes beyond word bank expansion — all 746 existing tests still pass.
- This directly fulfills the first "Next likely step" from Session 119: expand word banks (weather phrases).

### Current status
Working. All 746 tests pass (18 todo + 728 landscape), 201 subtests.

### Next likely steps
- Expand other word banks (more soundscapes, more legends)
- Add new sensory dimension (e.g. seasonal variation, time-of-day, spatial geometry)

### What was done (Session 119)
- **Added `--no-echo`, `--no-legend`, and `--no-sound` CLI flags** — users can now explicitly disable echo phrases, legend phrases, and soundscape phrases even when using presets that enable them. This fills the remaining symmetry gap in the `--no-*` flag family called out in Session 118's "Next likely steps."
  - `--no-echo` forces `echo_enabled=False` regardless of preset configuration or `--echo`
  - `--no-legend` forces `legend_enabled=False` regardless of preset configuration or `--legend`
  - `--no-sound` forces `sound_enabled=False` regardless of preset configuration or `--sound`
  - Post-preset override block in `main()` ensures `--no-*` always wins after all preset gating
  - Preset gating updated: checks `not args.no_echo` / `not args.no_legend` / `not args.no_sound` before applying preset values
  - No changes to `generate_landscape()` — only `main()` preset gating and CLI argument definitions
- Added 18 new tests (6 in `TestNoEcho`, 6 in `TestNoLegend`, 6 in `TestNoSound`):
  - `TestNoEcho`: flag exists via CLI, disables echo with all 5 presets (5 subtests), works with other features, JSON output, explicit `--echo` override
  - `TestNoLegend`: flag exists via CLI, disables legend with all 5 presets (5 subtests), works with other features, JSON output, explicit `--legend` override
  - `TestNoSound`: flag exists via CLI, disables sound with all 5 presets (5 subtests), works with other features, JSON output, explicit `--sound` override
- Added `NO_ECHO_INDICATORS` constant in the test module — a subset of `ECHO_INDICATORS` that excludes `"remembers"` (which collides with legend phrase "remembers those who built it"). Used by `TestNoEcho` suppression tests where legends may be present.
- This fulfills the "Next likely steps" from Session 118: echo, legend, and sound were the last features with on/off switches that the presets enable.
- Tests increased from 728 to 746 total (18 todo + 728 landscape), subtests from 171 to 201

### Current status
Working. All 746 tests pass (18 todo + 728 landscape), 201 subtests.

### Next likely steps
- Expand word banks (more weather phrases, more sounds, more legends)
- Add new sensory dimension (e.g. seasonal variation, time-of-day, spatial geometry)

### What was done (Session 118)
- **Added `--no-travelogue` and `--no-wistful` CLI flags** — users can now explicitly disable travelogue journal framing and wistful emotional coda even when using presets that enable them. This fills a symmetry gap with the existing `--no-*` flag family (`--no-adverb`, `--no-color`, `--no-element`, `--no-time-word`, `--no-weather`, `--no-anomaly`, `--no-middle`, `--no-dedup`).
  - `--no-travelogue` forces `travelogue=False` regardless of preset configuration or `--travelogue`
  - `--no-wistful` forces `wistful=False` regardless of preset configuration or `--wistful`
  - Post-preset override block in `main()` ensures `--no-*` always wins after all preset gating
  - Preset gating updated: checks `not args.no_travelogue` / `not args.no_wistful` before applying preset values
  - No changes to `generate_landscape()` — only `main()` preset gating and CLI argument definitions
- Added 12 new tests (6 in `TestNoTravelogue`, 6 in `TestNoWistful`):
  - `TestNoTravelogue`: flag exists via CLI, disables travelogue with all 5 presets (5 subtests), works with other features, JSON output, explicit `--travelogue` override
  - `TestNoWistful`: flag exists via CLI, disables wistful with all 5 presets (5 subtests), works with other features, JSON output, explicit `--wistful` override
- This was called out in the "Next likely steps" from Session 117: travelogue and wistful were the last features with on/off switches that lacked explicit `--no-*` flags. Echo, legend, and soundscape also lack `--no-*` flags, but they are opt-in features (default off); travelogue and wistful are opt-in too, but the `--no-*` flags are useful when using presets which enable them.
- Tests increased from 716 to 728 total (18 todo + 710 landscape), subtests from 151 to 171

### Current status
Working. All 728 tests pass (18 todo + 710 landscape), 171 subtests.

### Next likely steps
- Add `--no-echo`, `--no-legend`, `--no-sound` flags for symmetry (though these are also opt-in, they'd be useful with presets)
- Expand word banks (more weather phrases, more sounds, more legends)
- Add new sensory dimension (e.g. seasonal variation, time-of-day, spatial geometry)

### What was done (Session 117)
- **Added `--weather-count` CLI flag** and `weather_count` parameter to `generate_landscape()` — users can now control how many weather descriptions appear per detail level (0-3, default: 1), following the exact same pattern as `--echo-count` (Session 78) and `--sound-count` (Session 114):
  - `weather_count=0` suppresses all weather descriptions
  - `weather_count=1` (default) produces exactly 1 weather sentence per detail level (existing behavior)
  - `weather_count=2` and `weather_count=3` produce multiple weather descriptions per detail level
  - Uses `used_words` dedup via `_pick()` to prevent repeating the same weather phrase within a landscape
- **Added `--weather-prob` CLI flag** and `weather_prob` parameter to `generate_landscape()` — users can now control how often weather descriptions appear per roll (0.0 = never, 1.0 = always, default 1.0 preserves existing behavior):
  - `weather_prob=0.0` suppresses all weather even with `weather_count > 0`
  - Each of `weather_count` rolls independently draws `rng.random() < weather_prob`
  - Default `weather_prob=1.0` is fully backward compatible — all existing seed-based output is unchanged
- Added `weather_count` and `weather_prob` to JSON metadata when `weather_enabled=True`
- Added preset gating for `weather_count` and `weather_prob` — follows the same pattern as `echo_count`/`echo_prob` and `sound_count`/`sound_prob` gating
- **Added `weather_count` and `weather_prob` to all 5 presets** — each preset now has curated weather density and probability values:
  - `nightfall`: `weather_count=2, weather_prob=1.0` — multiple eerie weather descriptions always present
  - `pastoral`: `weather_count=1, weather_prob=0.8` — single gentle weather, occasionally absent for serene silence
  - `sublime`: `weather_count=2, weather_prob=1.0` — rich atmospheric detail always present
  - `wasteland`: `weather_count=1, weather_prob=1.0` — singular bleak weather always present
  - `dreamscape`: `weather_count=2, weather_prob=0.9` — surreal weather usually present
- Added 19 new tests (9 in `TestWeatherCount`, 7 in `TestWeatherProb`, 3 in `TestPresets`):
  - `TestWeatherCount`: default is one, zero suppresses, multi-weather with count=3, valid output for all counts, determinism, JSON format and field, CLI flag, works with detail=0
  - `TestWeatherProb`: default is one, zero suppresses, always with prob=1.0, valid output for all probs, determinism, JSON field, CLI flag
  - `TestPresets`: `test_all_presets_include_weather_count_and_prob` (5 subtests), `test_preset_weather_count_affects_output`, `test_preset_weather_prob_affects_output`
- This is the natural evolution of the weather system: previous sessions gave weather on/off (Session 40) and weather time-word injection (Session 96), but weather was the last major feature without count/prob control. Echo, legend, anomaly, and soundscape all had count and prob; now weather completes the set.
- Tests increased from 697 to 716 total (18 todo + 698 landscape), subtests from 146 to 151

### Current status
Working. All 716 tests pass (18 todo + 698 landscape).

### Next likely steps
- Add `--no-travelogue` and `--no-wistful` flags for symmetry with other `--no-*` flags
- Expand word banks (more weather phrases, more sounds, more legends)
- Add new sensory dimension (e.g. seasonal variation, time-of-day, spatial geometry)

### What was done (Session 115)
- **Added `--sound-prob` CLI flag** and `sound_prob` parameter to `generate_landscape()` — users can now control how often soundscape phrases appear per roll (0.0 = never, 1.0 = always, default 1.0 preserves existing behavior), following the exact same pattern as `--echo-prob` (Session 87) and `--legend-prob` (Session 102):
  - `sound_prob=0.0` suppresses all soundscape phrases even with `sound_enabled=True` and `sound_count > 0`
  - Each of `sound_count` rolls independently draws `rng.random() < sound_prob`
  - `sound_prob` included in JSON metadata when `sound_enabled=True`
  - Default `sound_prob=1.0` is fully backward compatible — all existing seed-based output with `--sound` is unchanged
- Added preset gating for `sound_prob` — follows the same pattern as `echo_prob` and `legend_prob` gating
- Added 7 new tests in `TestSoundProb` class:
  - `test_sound_prob_default_is_one` — default matches `sound_prob=1.0`
  - `test_sound_prob_zero_suppresses_soundscape` — zero suppresses all soundscape phrases
  - `test_sound_prob_one_always_has_soundscape` — 1.0 always produces soundscape phrases
  - `test_sound_prob_produces_valid_output` — various probs produce valid output
  - `test_sound_prob_is_deterministic` — same seed + same prob = same output
  - `test_sound_prob_json_includes_field` — JSON has `sound_prob` when enabled
  - `test_sound_prob_flag_exists_via_cli` — `--sound-prob` CLI flag exists
- This is the natural evolution of the soundscape system: Session 112 added on/off, Session 113 added to presets, Session 114 added sound-count, now sound-prob completes the trajectory, matching the echo and legend systems' trajectories (on/off → count → prob).
- Tests increased from 687 to 694 total (18 todo + 676 landscape), subtests unchanged at 137

### What was done (Session 116)
- **Added `sound_count` and `sound_prob` to all 5 presets** — each preset now has curated soundscape density and probability values that match its mood/theme:
  - `nightfall`: `sound_count=2, sound_prob=0.7` — eerie sounds (whispers, breaths) appear often but not always, matching echo_count=2, echo_prob=0.7
  - `pastoral`: `sound_count=1, sound_prob=0.5` — gentle sounds occasionally, matching echo_count=1, echo_prob=0.5
  - `sublime`: `sound_count=2, sound_prob=0.95` — rich soundscape almost always, matching echo_count=3, echo_prob=1.0
  - `wasteland`: `sound_count=2, sound_prob=1.0` — sounds of ruin (glass shattering, wind shifting) always present, matching legend_count=2, legend_prob=1.0
  - `dreamscape`: `sound_count=2, sound_prob=0.9` — surreal sounds usually present, matching echo_count=2, echo_prob=1.0
- The gating code for `sound_count` and `sound_prob` was already in place (lines 1321-1324 of `landscape.py`) from Sessions 114/115 — presets were the last part of the soundscape infrastructure not using these parameters. This follows the same trajectory as echo (Session 103 added echo_count/echo_prob to presets after Sessions 78/87) and legend (Session 103 added legend_count/legend_prob to presets after Sessions 101/102).
- Added 3 new tests in `TestPresets`:
  - `test_all_presets_include_sound_count_and_prob` — verifies every preset has both fields with valid ranges (5 subtests)
  - `test_preset_sound_count_affects_output` — verifies sound_count=0 differs from sound_count=1
  - `test_preset_sound_prob_affects_output` — verifies sound_prob=0.0 differs from sound_prob=1.0
- **Fixed `test_preset_with_soundscape_produces_soundscape_output`** — renamed to `test_preset_with_soundscape_produces_valid_output` and changed to check for valid output structure only (not specific soundscape content), since presets now have probabilistic sound_prob values that don't guarantee soundscape presence on every seed. This matches the pattern of `test_preset_with_legend_produces_legend_output` which only checks for valid output.
- This completes the per-preset soundscape tuning, following the same trajectory as echo and legend: on/off → presets (on/off only) → count → prob → per-preset count+prob.
- Tests increased from 694 to 697 total (18 todo + 679 landscape), subtests from 137 to 146

### What was done (Session 114)
- **Added `--sound-count` CLI flag** and `sound_count` parameter to `generate_landscape()` — users can now control how many soundscape phrases appear per landscape (0-3, default: 1), following the exact same pattern as `--echo-count` (Session 79) and `--legend-count` (Session 101):
  - `sound_count=0` suppresses soundscapes (equivalent to not using `--sound`)
  - `sound_count=1` (default) produces exactly 1 soundscape phrase (existing behavior)
  - `sound_count=2` and `sound_count=3` produce multiple soundscape phrases with dedup
  - Uses a `used_sounds` set to prevent repeating the same phrase within a landscape (same pattern as echoes and legends)
  - When pool is exhausted (count > 8), falls back to the full pool
- Added `sound_count` to JSON metadata when `sound_enabled=True` — emits `"sound_count": <N>` alongside `"sound_enabled": true`
- Added preset gating for `sound_count` — follows the same pattern as `echo_count` and `legend_count` gating
- Added 9 new tests in `TestSoundCount` class:
  - `test_sound_count_default_is_one` — default matches `sound_count=1`
  - `test_sound_count_zero_suppresses_soundscape` — zero suppresses all soundscape phrases
  - `test_sound_count_two_sometimes_has_multiple` — count=3 sometimes produces 2+ indicators
  - `test_sound_count_does_not_repeat_same_sound` — no duplicate soundscape phrases within a landscape
  - `test_sound_count_produces_valid_output` — all counts 0-3 produce valid output (40 seeds)
  - `test_sound_count_is_deterministic` — same seed + same count = same output
  - `test_sound_count_works_with_json_format` — JSON text field contains valid output
  - `test_sound_count_json_includes_field` — JSON has `sound_count` when enabled
  - `test_sound_count_flag_exists_via_cli` — `--sound-count` CLI flag exists
- **Fixed `SOUND_INDICATORS`** — replaced generic words ("hums", "whispers", "breathing") that collided with general landscape vocabulary with unique long substrings from each soundscape phrase. "hums" and "whispers" appear in verb/adverb word banks and caused false positives in dedup and suppression tests.
- This is the natural evolution of the soundscape system: Session 112 added on/off, Session 113 added to presets, now sound-count gives users fine-grained density control, matching the echo and legend systems' trajectories (on/off → count → prob).
- Tests increased from 678 to 687 total (18 todo + 669 landscape), subtests unchanged at 137

### What was done (Session 113)
- **Added `sound_enabled` to all 5 presets** — `nightfall`, `pastoral`, `sublime`, `wasteland`, and `dreamscape` now each include `"sound_enabled": True`, so every preset includes an auditory soundscape phrase by default. Previously, soundscapes were only accessible via the explicit `--sound` flag.
- Added **preset gating for soundscape in `main()`** — follows the exact same pattern as `travelogue` and `wistful`: if the preset includes `sound_enabled` and `--sound` was not explicitly passed (still `False`), the preset's value is applied.
- Added 2 new tests in `TestPresets`:
  - `test_all_presets_include_sound_enabled` — verifies every preset has `"sound_enabled": True` (5 subtests)
  - `test_preset_with_soundscape_produces_soundscape_output` — verifies all 5 presets produce soundscape output (5 subtests)
- This completes the soundscape integration into presets, following the same pattern as echoes (Session 88), legends (Session 97), travelogue (Session 106), and wistful (Session 110): add feature, then add to presets.
- Tests increased from 676 to 678 total (18 todo + 660 landscape), subtests from 127 to 137

### What was done (Session 112)
- **Added Soundscape system** (`--sound` CLI flag, `sound_enabled` parameter) — a new word bank of 8 curated soundscape phrases that describe what the landscape sounds like, adding an auditory dimension distinct from the existing visual, atmospheric, cultural, and emotional layers:
  - `SOUNDSCAPES` bank includes phrases like "The forest hums softly with a tone that seems to come from everywhere at once." and "You hear the tundra breathing — a slow, crystal rhythm that shakes the silence."
  - All 8 phrases use `{display}`, `{adverb}`, `{color}`, `{adj}`, and/or `{element}` injection — matching the injection patterns of echoes
  - Off by default (`sound_enabled=False`), so all existing seed-based output is unchanged
  - Phrase picked via `rng.choice(SOUNDSCAPES)` and formatted with current per-landscape word values
  - Suppressed at `detail=0` (same pattern as echoes, legends, wistful)
  - Placed after echoes and before legends — creating a sensory flow: atmospheric memory → present sounds → cultural context
- Added **`describe_sounds()` function** and **`--describe-sounds` CLI flag** — users can inspect all 8 soundscape phrases with index numbers, following the same pattern as every other describe-* feature
- Added **`"sound_enabled": true` to JSON metadata** when `sound_enabled=True` — follows the same pattern as echo_enabled, legend_enabled, travelogue, and wistful
- Added 24 new tests:
  - 8 tests in `TestDescribeSounds` — mirrors `TestDescribeEchoes` pattern (returns string, header, all phrases, index numbers, last-index, CLI flag, stdout, no landscape)
  - 16 tests in `TestSoundscape` — covers disabled by default, enabled appears, biome name injection, output validity, determinism, detail=0 suppression, compatibility with echo/legend/travelogue/wistful, JSON metadata (present + absent), differs from plain, CLI flag existence, stdout output
- Tests increased from 652 to 676 total (18 todo + 658 landscape), subtests unchanged at 127

## 2026-07-14

### What was done (Session 111)
- **Added `describe_wistful()` function** and `--describe-wistful` CLI flag — users can now inspect all 6 wistful phrases with their index numbers, following the exact same pattern as `describe_travelogue()` (Session 107), `describe_legends()` (Session 99), and `describe_echoes()` (Session 86):
  - Shows all wistful phrases with `[0]`–`[5]` index markers
  - CLI exits immediately after printing — no landscape generation occurs when `--describe-wistful` is used
- Added 8 new tests in `TestDescribeWistful` class:
  - `test_describe_wistful_returns_string` — verifies `describe_wistful()` returns a string
  - `test_describe_wistful_contains_header` — verifies output contains "wistful phrases" header
  - `test_describe_wistful_contains_all_phrases` — verifies all 6 wistful phrases appear in output
  - `test_describe_wistful_contains_index_numbers` — verifies `[0]` and `[1]` index markers
  - `test_describe_wistful_shows_all_phrases` — verifies last index `[5]` is present
  - `test_describe_wistful_flag_exists_via_cli` — verifies `main` is callable
  - `test_describe_wistful_flag_prints_to_stdout` — verifies CLI output via stdout capture
  - `test_describe_wistful_no_landscape_generated` — verifies early exit (no landscape generation)
- This closes a test coverage gap: wistful was introduced in Session 108 with functional tests for the feature, but the wistful introspection had no dedicated test coverage, unlike travelogue (Session 107), legends (Session 99), and echoes (Session 86) which all have introspection tests.
- Tests increased from 626 to 634 landscape tests (644 → 652 total), subtests unchanged at 127

## 2026-07-14

### What was done (Session 110)
- **Added `wistful` to all 5 presets** — `nightfall`, `pastoral`, `sublime`, `wasteland`, and `dreamscape` now each include `"wistful": True`, so every preset includes the wistful emotional coda by default. Previously, wistful was only accessible via the explicit `--wistful` flag.
- Added **preset gating for wistful in `main()`** — follows the exact same pattern as `travelogue`: if the preset includes `wistful` and `--wistful` was not explicitly passed (still `False`), the preset's value is applied.
- Fixed **`test_wistful_works_with_preset`** — removed the redundant `wistful=True` kwarg now that presets include `wistful` (would cause `multiple values for keyword argument` error).
- Added 2 new tests in `TestPresets`:
  - `test_all_presets_include_wistful` — verifies every preset has `"wistful": True` (5 subtests)
  - `test_preset_with_wistful_produces_wistful_output` — verifies all 5 presets produce wistful output (5 subtests)
- This completes the wistful integration into presets, following the same pattern as travelogue (Session 106) and legends (Session 97): add to PRESETS dict, add gating in main(), add structural tests. Wistful was the last feature (alongside echoes, legends, travelogue) with an on/off switch that was not in any preset.
- Tests increased from 642 to 644 landscape tests (660 total), subtests from 117 to 127

### What was done (Session 109)
- **Added `wistful` to JSON metadata** — when `wistful=True`, the JSON output now includes `"wistful": true`, following the same pattern as `travelogue` (Session 105) and `echo_enabled`/`legend_enabled` (Sessions 97/100). Previously, wistful framing was invisible in JSON metadata — consumers had no way to detect wistful state without parsing the text field for wistful phrases.
- Added 2 new tests in `TestWistful`:
  - `test_wistful_works_with_json` updated to verify `"wistful"` key exists and is `True`
  - `test_wistful_json_field_absent_when_disabled` — verifies JSON omits `wistful` when `wistful=False` (default)
- Tests increased from 623 to 624 landscape tests (641 → 642 total), subtests unchanged at 117

### What was done (Session 108)
- **Added `--wistful` CLI flag** and `wistful` parameter to `generate_landscape()` — appends a bittersweet, yearning closing phrase to the landscape, adding an emotional coda in a different register from echoes (atmospheric), legends (folkloric), and travelogue (narrative journaling):
  - 6 curated `WISTFUL` phrases, each referencing `{display}` (biome name): "You wish you could stay longer in the forest.", "Part of you will always remain in the forest.", "The forest calls to you even as you turn away.", "You carry a piece of the forest with you now.", "Someday you will return to the forest.", "The forest lingers in your thoughts like a half-remembered dream."
  - Off by default (`wistful=False`), so all existing seed-based output is unchanged
  - Phrase picked via `rng.choice(WISTFUL)` and formatted with `display=display`
  - Suppressed at `detail=0` (same pattern as echoes and legends)
  - Works with all existing features: echo, legend, travelogue, presets, JSON, poetic, combine, etc.
  - Seed-breaking when enabled: `rng.choice()` adds a random call before the travelogue block. Determinism is preserved (same seed + same args = same output)
  - Placed after legends and before the travelogue suffix, so wistful reflections sit inside the travelogue journal frame (when enabled) — creating a narrative arc: journal opens → description → echoes → legends → wistful reflection → journal closes
- Added 15 new tests in `TestWistful` class:
  - `test_wistful_disabled_by_default` — wistful phrase should not appear without the flag
  - `test_wistful_enabled_appears` — wistful phrase appears when enabled
  - `test_wistful_contains_biome_name` — biome name is injected into wistful phrase
  - `test_wistful_produces_valid_output` — output is valid string (20 seeds)
  - `test_wistful_is_deterministic` — same seed = same output
  - `test_wistful_works_with_detail_zero` — works with minimal output
  - `test_wistful_works_with_echo` — works with echoes enabled
  - `test_wistful_works_with_legend` — works with legends enabled
  - `test_wistful_works_with_travelogue` — works with travelogue enabled
  - `test_wistful_works_with_json` — JSON format includes wistful text
  - `test_wistful_differs_from_plain` — wistful output differs from plain
  - `test_wistful_flag_exists_via_cli` — verifies `main` is callable
  - `test_wistful_flag_prints_to_stdout` — verifies CLI output via stdout capture
  - `test_wistful_works_with_preset` — works with all 5 presets (5 subtests)
  - `test_wistful_suppressed_at_detail_zero` — wistful phrase should not appear at detail=0
- This is a genuinely novel addition: it adds an emotional register (bittersweet longing, nostalgia-for-places-never-visited, the ache of departure) that no existing feature covers. Echoes evoke timeless presence, legends evoke cultural memory, travelogue frames as journal — wistful evokes personal emotional response to the landscape.
- Tests increased from 608 to 623 landscape tests (626 → 641 total), subtests from 112 to 117

### What was done (Session 107)
- **Added `--describe-travelogue` CLI flag** and `describe_travelogue()` function — users can now inspect all 4 travelogue prefixes and 4 travelogue suffixes with their index numbers, following the exact same pattern as `--describe-echoes` (Session 86) and `--describe-legends` (Session 99):
  - Shows both prefixes and suffixes in separate sections with `[0]`–`[3]` index markers
  - CLI exits immediately after printing — no landscape generation occurs when `--describe-travelogue` is used
- Added 11 new tests in `TestDescribeTravelogue` class:
  - `test_describe_travelogue_returns_string` — verifies `describe_travelogue()` returns a string
  - `test_describe_travelogue_contains_header` — verifies output contains both "travelogue prefixes" and "travelogue suffixes" headers
  - `test_describe_travelogue_contains_all_prefixes` — verifies all 4 prefix templates appear in output
  - `test_describe_travelogue_contains_all_suffixes` — verifies all 4 suffix templates appear in output
  - `test_describe_travelogue_contains_index_numbers` — verifies `[0]` and `[1]` index markers
  - `test_describe_travelogue_shows_all_prefixes` — verifies last prefix index `[3]` is present
  - `test_describe_travelogue_shows_all_suffixes` — verifies last suffix index `[3]` is present
  - `test_describe_travelogue_flag_exists_via_cli` — verifies `main` is callable
  - `test_describe_travelogue_flag_prints_to_stdout` — verifies CLI output via stdout capture
  - `test_describe_travelogue_no_landscape_generated` — verifies early exit (no landscape generation)
- This closes a test coverage gap: travelogue was introduced in Session 104 with functional tests for the feature, but the travelogue introspection had no dedicated test coverage, unlike echoes (Session 86) and legends (Session 99) which have had introspection tests since their early sessions.
- Tests increased from 598 to 608 landscape tests (616 → 626 total), subtests unchanged at 112

### What was done (Session 106)
- **Added `travelogue` to all 5 presets** — `nightfall`, `pastoral`, `sublime`, `wasteland`, and `dreamscape` now each include `"travelogue": True`, so every preset frames the landscape as a travel journal entry by default. Previously, travelogue was only accessible via the explicit `--travelogue` flag.
- Added **preset gating for travelogue in `main()`** — follows the exact same pattern as `legend_enabled`: if the preset includes `travelogue` and `--travelogue` was not explicitly passed (still `False`), the preset's value is applied.
- Added 2 new tests in `TestPresets`:
  - `test_all_presets_include_travelogue` — verifies every preset has `"travelogue": True` (5 subtests)
  - `test_preset_with_travelogue_produces_framed_output` — verifies all 5 presets produce travelogue-framed output (5 subtests)
- This completes the travelogue integration into presets, following the same pattern as legends (Session 97) and echoes (Session 88): add to `PRESETS` dict, add gating in `main()`, add structural tests. Travelogue was the last feature (alongside echoes, legends) with an on/off switch that was not in any preset.
- Tests increased from 596 to 598 landscape tests (614 → 616 total), subtests from 102 to 112

### What was done (Session 105)
- **Added `travelogue` to JSON metadata** — when `travelogue=True`, the JSON output now includes `"travelogue": true`, following the same pattern as `echo_enabled` (Session 100) and `legend_enabled` (Session 97). Previously, travelogue framing was invisible in JSON output — consumers had no way to distinguish a travelogue-framed landscape from a plain one via metadata.
- Added 2 new tests in `TestTravelogue`:
  - `test_travelogue_json_includes_field` — verifies JSON has `travelogue` when True
  - `test_travelogue_json_field_absent_when_disabled` — verifies JSON omits `travelogue` when False (default)
- Tests increased from 594 to 596 landscape tests (612 → 614 total), subtests unchanged at 102

### What was done (Session 104)
- **Added `--travelogue` CLI flag** and `travelogue` parameter to `generate_landscape()` — frames the generated landscape description as a travel journal entry, adding a narrative prefix (e.g. "Journal entry, day 247. I have reached the forest at last.") and a narrative suffix (e.g. "I will venture deeper into the forest come morning."):
  - 4 curated `TRAVELOGUE_PREFIXES` and 4 curated `TRAVELOGUE_SUFFIXES` — each referencing `{display}` (biome name) and `{day}` (random number 1–365)
  - Day number picked via `rng.randint(1, 365)` — adds a concrete, grounded detail to the framing
  - Prefix inserted at position 0, suffix appended at the end, so the landscape description sits inside a narrative frame
  - Works with all existing features: detail, echo, legend, presets, combine, JSON, poetic, etc.
  - Seed-breaking when enabled: `rng.randint()` and `rng.choice()` for prefix/suffix add random calls before the joiner. Determinism is preserved (same seed + same args = same output)
  - Travelogue is off by default (`travelogue=False`), so all existing seed-based output is unchanged
- Added 13 new tests in `TestTravelogue` class:
  - `test_travelogue_disabled_by_default` — travelogue framing should not appear without the flag
  - `test_travelogue_enabled_appears` — travelogue prefix appears when enabled
  - `test_travelogue_contains_biome_name` — biome name appears in travelogue output
  - `test_travelogue_contains_day_number` — day number appears in travelogue output
  - `test_travelogue_produces_valid_output` — output is valid string (20 seeds)
  - `test_travelogue_is_deterministic` — same seed = same output
  - `test_travelogue_ends_with_suffix` — suffix phrase appears at the end
  - `test_travelogue_works_with_detail_zero` — works with minimal output
  - `test_travelogue_works_with_echo` — works with echoes enabled
  - `test_travelogue_works_with_legend` — works with legends enabled
  - `test_travelogue_works_with_preset` — CLI flag exists
  - `test_travelogue_works_with_json` — JSON format includes framed text
  - `test_travelogue_differs_from_plain` — travelogue output differs from plain
- This is a genuinely novel addition: it transforms the same core landscape generation into a different genre (exploration narrative) without changing the description itself — the travelogue is a narrative frame, not a content modifer
- Tests increased from 599 to 612 total (18 todo + 594 landscape), subtests unchanged at 102

### What was done (Session 103)
- **Added `legend_count` and `legend_prob` to all 5 presets** — each preset now has curated legend density and probability values that match its mood/theme:
  - `nightfall`: `legend_count=2, legend_prob=0.7` — eerie folk tales, not always present
  - `pastoral`: `legend_count=1, legend_prob=0.6` — occasional tranquil legend
  - `sublime`: `legend_count=2, legend_prob=0.9` — rich mythic context, almost always
  - `wasteland`: `legend_count=2, legend_prob=1.0` — every landscape has a forgotten-history legend
  - `dreamscape`: `legend_count=2, legend_prob=0.85` — surreal folk tales, usually present
- The gating code for `legend_count` and `legend_prob` was already in place (lines 1163-1166 of `landscape.py`) from Sessions 101/102 — presets were the last part of the legend infrastructure not using these parameters
- Complements the existing `echo_count` and `echo_prob` in presets (nightfall: echo_count=2, echo_prob=0.7; pastoral: echo_count=1, echo_prob=0.5; sublime: echo_count=3, echo_prob=1.0; dreamscape: echo_count=2, echo_prob=1.0) — now legends have the same per-preset tuning
- Added 3 new tests in `TestPresets`:
  - `test_all_presets_include_legend_count_and_prob` — verifies every preset has both fields with valid ranges (5 subtests)
  - `test_preset_legend_count_affects_output` — verifies legend_count=0 differs from legend_count=1
  - `test_preset_legend_prob_affects_output` — verifies legend_prob=0.0 differs from legend_prob=1.0
- This completes the preset legend integration: on/off (Session 97), count (Session 101), prob (Session 102), now per-preset tuning (this session)
- Tests increased from 596 to 599 total (18 todo + 581 landscape), subtests from 93 to 102

### What was done (Session 102)
- **Added `--legend-prob` CLI flag** and `legend_prob` parameter to `generate_landscape()` — users can now control how often legend phrases appear per roll (0.0 = never, 1.0 = always, default 1.0 preserves existing behavior), following the exact same pattern as `--echo-prob` (Session 87):
  - `legend_prob=0.0` suppresses all legends even with `legend_enabled=True` and `legend_count > 0`
  - Each of `legend_count` rolls independently draws `rng.random() < legend_prob`
  - `legend_prob` included in JSON metadata when `legend_enabled=True`
  - Default `legend_prob=1.0` is fully backward compatible — all existing seed-based output with `--legend` is unchanged
- Added preset gating for `legend_prob` — follows the same pattern as `echo_prob` gating
- Added 7 new tests in `TestLegendProb` class:
  - `test_legend_prob_default_is_one` — default matches `legend_prob=1.0`
  - `test_legend_prob_zero_suppresses_legends` — zero suppresses all legends
  - `test_legend_prob_one_always_has_legend` — 1.0 always produces legends
  - `test_legend_prob_produces_valid_output` — various probs produce valid output
  - `test_legend_prob_is_deterministic` — same seed + same prob = same output
  - `test_legend_prob_json_includes_field` — JSON has `legend_prob` when enabled
  - `test_legend_prob_flag_exists_via_cli` — `--legend-prob` CLI flag exists
- This is the natural evolution of the legend system: Session 96's legend was initially a simple on/off switch, then `--legend-count` was added in Session 101; now `--legend-prob` gives users fine-grained density control, matching the echo system's trajectory (echo on/off → echo-count → echo-prob)
- Tests increased from 589 to 596 total (18 todo + 578 landscape), subtests unchanged at 93

### What was done (Session 101)
- **Added `--legend-count` CLI flag** and `legend_count` parameter to `generate_landscape()` — users can now control how many legend phrases appear per landscape (0-3, default: 1 preserves existing behavior), following the exact same pattern as `--echo-count` (Session 78):
  - `legend_count=0` suppresses legends (equivalent to `legend_enabled=False`)
  - `legend_count=1` (default) produces exactly 1 legend phrase (existing behavior)
  - `legend_count=2` and `legend_count=3` produce multiple legend phrases with dedup
  - Uses a `used_legends` set to prevent repeating the same phrase within a landscape (same pattern as echoes)
  - When pool is exhausted (count > 15), falls back to the full pool
- Added `legend_count` to JSON metadata when `legend_enabled=True` — emits `"legend_count": <N>` alongside `"legend_enabled": true`
- Added preset gating for `legend_count` — follows the same pattern as `echo_count` gating
- Added 12 new tests in `TestLegendCount` class:
  - `test_legend_count_default_is_one` — default produces at most 1 legend
  - `test_legend_count_zero_suppresses_legends` — count=0 suppresses all legends
  - `test_legend_count_two_produces_two_phrases` — count=2 sometimes produces 2+ indicators
  - `test_legend_count_three_produces_three_phrases` — count=3 sometimes produces 3+ indicators
  - `test_legend_count_no_repeats` — no duplicate legend phrases within a landscape
  - `test_legend_count_is_deterministic` — same seed + same count = same output
  - `test_legend_count_works_with_combine` — works with `--combine`
  - `test_legend_count_json_includes_field` — JSON has `legend_count` when enabled
  - `test_legend_count_json_absent_when_disabled` — JSON omits `legend_count` when disabled
  - `test_legend_count_flag_exists_via_cli` — `--legend-count` CLI flag exists
  - `test_legend_count_works_with_echo` — works with `--echo`
  - `test_legend_count_detail_zero_suppresses_legends` — detail=0 suppresses even with count>0
- This is the natural evolution of the legend system: Session 78's echo was initially a simple on/off switch before `--echo-count` and `--echo-prob` were added in later sessions; now legends follow the same trajectory
- Tests increased from 577 to 589 total (18 todo + 571 landscape), subtests unchanged at 93

### What was done (Session 100)
- **Added `echo_enabled` to JSON metadata** — when `echo_enabled=True`, the JSON output now includes `"echo_enabled": true`, matching the same pattern as `legend_enabled` (Session 97). Previously, echo metadata only emitted `echo_prob` and `echo_count`, with no explicit boolean for whether echo was active.
- Added 2 new tests:
  - `test_echo_json_includes_field` — verifies JSON has `echo_enabled` when True
  - `test_echo_json_field_absent_when_disabled` — verifies JSON omits `echo_enabled` when False (default)
- Tests increased from 575 to 577 total (18 todo + 559 landscape), 93 subtests unchanged

### What was done (Session 99)
- **Added `TestDescribeLegends` test class** — 8 new introspection tests for `describe_legends()` and `--describe-legends`, following the exact same pattern as `TestDescribeEchoes` (Session 86):
  - `test_describe_legends_returns_string` — verifies `describe_legends()` returns a string
  - `test_describe_legends_contains_header` — verifies output contains "legends" header
  - `test_describe_legends_contains_all_legends` — verifies all 15 legend phrases appear in output
  - `test_describe_legends_contains_index_numbers` — verifies `[0]` and `[1]` index markers
  - `test_describe_legends_shows_all_legends` — verifies last index `[14]` is present
  - `test_describe_legends_flag_exists_via_cli` — verifies `main` is callable
  - `test_describe_legends_flag_prints_to_stdout` — verifies CLI output via stdout capture
  - `test_describe_legends_no_landscape_generated` — verifies early exit (no landscape generation)
- This closes a test coverage gap: `describe_legends()` was introduced in Session 96 with functional tests for the legend feature, but the `describe_legends()` introspection function itself had no dedicated test coverage, unlike `describe_echoes()` which has had introspection tests since Session 86
- Tests increased from 549 to 557 total (18 todo + 539 landscape), 93 subtests unchanged

### What was done (Session 98)
- **Expanded LEGENDS bank from 10 to 15 phrases** — 5 new folkloric/historical phrases added, doubling the variety of cultural/folkloric context appended to landscapes:
  - "The {display} remembers those who built it, even if no one else does." — memory of makers, hidden history
  - "They say the {display} can be seen from far away, but no path leads to it." — unreachable, mythic distance
  - "Every stone in the {display} was placed by hand, long before anyone lived here." — ancient construction, deep past
  - "When the wind moves through the {display}, it sounds like a name you almost recognize." — uncanny familiarity, near-memory
  - "There is a well in the {display} that no one has ever reached the bottom of." — bottomless mystery, unknowable depth
- New phrases only use `{display}` injection (same as existing 10) — no changes to generation logic, tests, or CLI
- Updated `LEGEND_INDICATORS` in test module with 5 new invariant substrings for the new phrases
- Tests unchanged: still 549 total (18 todo + 531 landscape), 93 subtests

### What was done (Session 97)
- Added **legends to all 5 presets** — `legend_enabled=True` in `nightfall`, `pastoral`, `sublime`, `wasteland`, and `dreamscape`, so every preset now includes a folkloric legend by default. Previously, legends were only accessible via the explicit `--legend` flag.
- Added **`legend_enabled` preset gating in `main()`** — follows the exact same pattern as `echo_enabled`: if the preset includes `legend_enabled` and `--legend` was not explicitly passed (still `False`), the preset's value is applied.
- Added **`legend_enabled` to JSON metadata** — when `legend_enabled=True`, the JSON output now includes `"legend_enabled": true`, following the same pattern as `echo_enabled` JSON metadata.
- Added 4 new tests:
  - `test_legend_json_includes_field` — verifies JSON output has `legend_enabled` when True
  - `test_legend_json_field_absent_when_disabled` — verifies JSON output omits `legend_enabled` when False (default)
  - `test_all_presets_include_legend_enabled` — verifies all 5 presets contain `"legend_enabled": True` (5 subtests)
  - `test_preset_with_legend_produces_legend_output` — verifies all 5 presets produce valid output with legends (5 subtests)
- Tests increased from 545 to 549 total (18 todo + 531 landscape), subtests from 83 to 93

### What was done (Session 96)
- Added **`{time_word}` temporal injection into all 5 weather templates** — the weather slot now receives the per-landscape time word, completing temporal framing coverage across all template categories (openings, anomalies, echoes, and now weather)
  - All 5 weather templates now end with `{time_word}.` — e.g. "A gentle rain falls softly through the vivid crystal mist already." / "The air tells its own story: a gentle rain falls softly through the vivid crystal mist still."
- Added `time_word=time_word` kwarg to the weather `_format_tmpl()` call — `time_word` was already in scope (picked per-landscape before the opening template) but was not passed to weather templates, so the placeholder would have rendered as literal `{time_word}` text
- Weather was the last template category completely missing `{time_word}` — openings (Sessions 89–90), echoes (Session 91), and anomalies (Session 94) already had it; now weather completes the coverage
- When `time_word_enabled=False`, `_format_tmpl` handles spacing cleanup naturally: `"  {time_word}."` → the time word is empty and placed right before the period, so only `" ."` appears → the existing `" ." → "."` replace chain removes it cleanly
- Added 11 tests in `TestWeatherTimeWord` class: placeholder presence, output validity, time word appearance, determinism, time-word-disabled formatting, mood+bias, detail=3, JSON, disabled differs, combine, and per-template-set statistical tests (5 subtests for first–fifth template sets)
- Tests increased from 522 to 533 total (18 todo + 515 landscape), subtests from 78 to 83

### What was done (Session 96)
- Added **Legends system** — a new `LEGENDS` word bank of 10 curated folkloric phrases that append cultural/historical context to the landscape, distinct from echoes (atmospheric/emotional) and anomalies (surreal/uncanny)
  - Examples: "The oldest maps leave the forest blank.", "Locals say the ruined city was not here a century ago.", "Beneath the tundra, something older than stone is buried."
  - All 10 legends reference `{display}` — the biome name is injected into each phrase, so legends feel grounded in the landscape context (e.g. "The forest is marked on no map" vs "The ruined city is marked on no map")
  - Picked via `rng.choice(LEGENDS)` — one legend per landscape when enabled
  - Works with `--combine`: legends reference the combined biome display (e.g. "forest and desert")
  - Suppressed at `detail=0` (same pattern as echoes and anomalies)
- Added `--legend` CLI flag (default: off, same pattern as `--echo`) and `legend_enabled` parameter to `generate_landscape()`
- Added `--describe-legends` CLI flag and `describe_legends()` function — follows the same introspection pattern as `--describe-echoes`
- Added 12 tests in `TestLegend` class: disabled by default, appears when enabled, output validity, determinism, poetic format, JSON format, detail=0 suppression, CLI flag existence, biome injection, works with echo, combine, mood and bias
- Tests increased from 533 to 545 total (18 todo + 527 landscape), subtests unchanged at 83

### What was done (Session 94)
- Added **`{time_word}` injection into 2 anomaly templates** — the anomaly slot now receives the per-landscape time word, grounding surreal/uncanny descriptions in the same temporal frame as openings and echoes
  - Template 1: `"Something is not right with the {display} — {anomaly}"` → `"Something is not right with the {display} {time_word} — {anomaly}"` — e.g. "Something is not right with the forest already — The gravity here feels wrong."
  - Template 3: `"There is a quiet wrongness here {adverb}: {anomaly_lower}"` → `"There is a quiet wrongness here {adverb} {time_word}: {anomaly_lower}"` — e.g. "There is a quiet wrongness here silently now: the horizon curves upward."
- Added `time_word=time_word` kwarg to the anomaly `_format_tmpl()` call — `time_word` was already in scope (picked per-landscape before the opening template) but was not passed to anomaly templates, so the placeholder would have rendered as literal `{time_word}` text
- The anomaly slot was the last template category completely missing `{time_word}` — openings (Session 89–90) and echoes (Session 91) already had it, now anomalies complete the coverage
- When `time_word_enabled=False`, `_format_tmpl` handles spacing cleanup naturally: `"  —"` → `" —"` (template 1) and `" :"` → `":"` (template 3) via its existing replace chain
- Added 12 tests in `TestAnomalyTimeWord` class: placeholder presence, output validity, time word appearance, determinism, time-word-disabled formatting, mood+bias, detail=3, JSON, disabled differs, combine, and per-template statistical tests (both "not right" and "wrongness" phrases)
- Tests increased from 511 to 522 total (18 todo + 504 landscape), subtests unchanged at 78

### What was done (Session 93)
- Added **`--no-time-word` CLI flag** and `time_word_enabled` parameter to `generate_landscape()` — users can now suppress temporal time words in landscape descriptions, following the exact same pattern as `--no-element` (Session 92) and the previous `--no-*` flags
  - `time_word_enabled=True` (default) preserves existing behavior — a time word is picked per-landscape via `rng.choice()` and injected into all 4 opening templates and 2 echo phrases
  - `time_word_enabled=False` skips the time word pick and passes `""` to all template format calls — time words don't participate in `_pick()` (they use `rng.choice()` directly), so no dedup slots or `_pick()` calls are consumed
  - `_format_tmpl` handles the empty-string cleanup naturally via its existing replace chain — no double-space or trailing-space artifacts occur because time words always appear mid-to-late sentence (after an adverb or before a period)
- Time words were the last temporal/narrative category without a suppression flag — this completes the `--no-*` suppression family: `--no-adverb` (Session 34), `--no-color` (Session 53), `--no-element` (Session 92), and now `--no-time-word`
- Fixed **`test_describe_global_contains_all_categories`** — added `"time words"` to the expected category list so the test correctly verifies that `describe_global()` includes time words (a test coverage gap introduced when time words were added in Session 89)
- Added 12 tests in `TestTimeWordFlag` class: `test_time_word_enabled_default_same_as_before`, `test_time_word_disabled_still_produces_valid_output`, `test_time_word_disabled_differs_from_enabled`, `test_time_word_disabled_deterministic`, `test_time_word_disabled_no_formatting_artifacts`, `test_time_word_disabled_no_time_words_in_output`, `test_time_word_disabled_flag_exists_via_cli`, `test_time_word_disabled_works_with_detail_three`, `test_time_word_disabled_works_with_mood_and_bias`, `test_time_word_disabled_works_with_combine`, `test_time_word_disabled_works_with_echo`
- Tests increased from 499 to 511 total (18 todo + 493 landscape), subtests unchanged at 78

### What was done (Session 92)
- Added **`--no-element` CLI flag** and `element_enabled` parameter to `generate_landscape()` — users can now suppress element words in landscape descriptions, following the exact same pattern as `--no-color` (Session 53) and other `--no-*` flags
  - `element_enabled=True` (default) preserves existing behavior — element words are picked per-sentence-pair for opening, middle, weather, anomaly, and echo templates
  - `element_enabled=False` skips the element pick entirely and passes `""` for both `{element}` and `{Element}` (capitalized) to all template format calls
  - `_format_tmpl` handles the resulting double-space and leading-space artifacts via `.strip()` and the existing replace chain — `"of  "` → `"of "`, `"  silently"` → `"silently"`, etc.
- Added **`.strip()` to `_format_tmpl()`** — a general quality improvement that removes leading/trailing whitespace from formatted template output. This is a no-op for all existing templates (none produce leading/trailing spaces in normal operation), but prevents formatting artifacts when `{Element}` (sentence-initial in opening template 3 and middle templates 0/3) evaluates to an empty string due to `element_enabled=False`
- Elements were the last major word category (alongside adverbs, colors) without an off switch — this completes the `--no-*` suppression flag set for word categories: `--no-adverb` (Session 34), `--no-color` (Session 53), and now `--no-element`
- Added 10 tests in `TestElementFlag` class: `test_element_enabled_default_same_as_before`, `test_element_disabled_still_produces_valid_output`, `test_element_disabled_differs_from_enabled`, `test_element_disabled_deterministic`, `test_element_disabled_no_formatting_artifacts`, `test_element_disabled_flag_exists_via_cli`, `test_element_disabled_works_with_detail_three`, `test_element_disabled_works_with_mood_and_bias`, `test_element_disabled_works_with_combine`, `test_element_disabled_no_elements_in_output`
- Tests increased from 489 to 499 total (18 todo + 481 landscape), subtests unchanged at 78

### What was done (Session 91)
- Added **`{time_word}` temporal injection into 2 echo phrases** — the echo system now passes `time_word=time_word` to `_format_tmpl()`, so phrases that contain `{time_word}` render with the per-landscape time word, grounding atmospheric echoes in the landscape's temporal frame
  - Echo 1: `"The {display} has been waiting {adverb} for you {time_word}."` — "The forest has been waiting silently for you always."
  - Echo 5: `"There is a sense of deep time here, pressing down {adverb} {time_word}."` — "There is a sense of deep time here, pressing down softly yet."
- Added `time_word=time_word` kwarg to the echo `_format_tmpl()` call — `time_word` was already in scope (picked per-landscape before the opening template) but was not passed to echo templates
- 8 remaining echo phrases without `{time_word}` kept as-is for structural variety — the time word injection split (2 of 10) matches the element, color, and adj injection splits (also 2 of 10), since time words pair most naturally with phrases that already reference temporal concepts ("has been waiting", "deep time")
- Added 8 new tests in `TestEchoTimeWord` class: output presence, determinism, waiting-phrase specific, deep-time phrase specific, detail=0 compatibility, adverb-disabled compatibility, combine compatibility, and 6 biome subtests
- Tests increased from 481 to 489 total (18 todo + 471 landscape), subtests from 72 to 78

### What was done (Session 90)
- Expanded **`{time_word}` to opening templates 1, 2, and 3** — the temporal injection that was only in template 0 (`"...before you {time_word}."`) now applies to all 4 opening templates:
  - Template 1 (`Before you,...comes into view`): `"...comes into view {adverb} {time_word}."`
  - Template 2 (`The...lies ahead`): `"...lies {adverb} ahead {time_word}."`
  - Template 3 (`{Element} —...stretches before you`): `"...stretches {adverb} before you {time_word}."`
- No code changes needed — `time_word` was already picked once per landscape and passed to all format calls; only the template strings changed
- This fulfills the explicit note from Session 89's DECISIONS.md: "if the feature proves useful, it can be expanded to other templates in future sessions"
- Added 3 new tests in `TestTimeWords`: `test_time_word_appears_in_second_opening`, `test_time_word_appears_in_third_opening`, `test_time_word_appears_in_fourth_opening`
- Tests increased from 478 to 481 total (18 todo + 463 landscape), subtests unchanged at 72

### What was done (Session 89)
- Added **`{time_word}` temporal injection in opening template 0** — a small `TIME_WORDS` bank (6 words: already, still, yet, now, once, always) picked once per landscape via `rng.choice()` and injected into opening template 0 as `"...before you {time_word}."` — e.g. "A vast crystal forest of vivid mist stretches silently before you already." / "...before you still." / "...before you now."
- Added **`{time_word}` temporal injection in opening template 0** — a small `TIME_WORDS` bank (6 words: already, still, yet, now, once, always) picked once per landscape via `rng.choice()` and injected into opening template 0 as `"...before you {time_word}."` — e.g. "A vast crystal forest of vivid mist stretches silently before you already." / "...before you still." / "...before you now."
- Time words add **narrative temporal texture** — positioning the scene as something already present, still ongoing, or yet to fully arrive — filling a gap in the vocabulary system that had adjectives (quality), adverbs (manner), colors (visual), elements (sensory), moods (emotional), and echoes (atmospheric) but nothing for temporal framing
- Picked via `rng.choice()` (not `_pick()`) — intentionally outside the weighted-selection/dedup/mood/bias system, keeping it simple and ensuring it never conflicts with other word categories
- Added `"time words"` to `describe_global()` categories so time words are discoverable via `--describe-global`
- 7 new tests in `TestTimeWords` class: output presence, determinism, output validity, detail=0, JSON format, `describe_global` inclusion, and 6 biome subtests
- Tests increased from 471 to 478 total (18 todo + 460 landscape), subtests from 66 to 72

### What was done (Session 88)
- Added **PRESETS system** — 5 named preset configurations that bundle multiple CLI flags into a single `--preset` name:
  - `nightfall`: eerie mood, rare bias, anomaly_prob=0.8, anomaly_count=2, echo on with prob 0.7, echo_count=2
  - `pastoral`: peaceful mood, no anomalies, echo on with prob 0.5
  - `sublime`: vibrant+peaceful mood blend, common bias, echo on with prob 1.0, echo_count=3
  - `wasteland`: desolate mood, no colors, anomaly_prob=1.0, anomaly_count=3, echo on
  - `dreamscape`: eerie+vibrant mood blend, flat bias, anomaly_prob=1.0, echo on, detail=2
- Presets apply only when the corresponding CLI arg has its default value — explicit flags always override preset values (e.g. `--preset wasteland --mood eerie` uses eerie mood, not desolate)
- Added `--describe-presets` introspection flag and `describe_presets()` function — lists all 5 presets with their settings, same pattern as `--describe-biome`, `--describe-templates`, etc.
- Presets don't change any generation code — they're purely a CLI convenience layer that supplies kwargs to `generate_landscape()`
- Added 13 tests in `TestPresets` class: structural assertions (preset data integrity), output validity (all 5 presets × 5 seeds), determinism (all 5 presets), CLI integration (`--preset`, `--describe-presets`, early exit with describe), and 10 subtests
- Tests increased from 476 to 489 total (18 todo + 471 landscape, 66 subtests)

### What was done (Session 80)
- Added **`{display}` injection into echo phrases** — 5 of 10 ECHOES now contain `{display}` placeholders that render the biome name, making echo phrases feel connected to the landscape context instead of reading as generic atmospheric text
  - "The land remembers." → "The {display} remembers." — "The forest remembers."
  - "This place has been waiting for you." → "The {display} has been waiting for you." — "The tundra has been waiting for you."
  - "Nothing here has changed in a thousand years." → "Nothing in the {display} has changed in a thousand years." — "Nothing in the ruined city has changed in a thousand years."
  - "The echoes of the past linger in the air." → "The echoes of the past linger in the air of the {display}." — "The echoes of the past linger in the air of the desert."
  - "Something important happened here once." → "Something important happened in the {display} once." — "Something important happened in the plain once."
- Changed the echo block in `generate_landscape()` to use `_format_tmpl(echo, display=display)` instead of bare `parts.append(echo)` — templates without `{display}` are unaffected (str.format silently ignores extra kwargs)
- 5 remaining echoes without `{display}` (e.g. "The silence here is older than any sound.") kept as-is for structural variety — not every echo needs to reference the biome
- Refactored existing echo tests to use `ECHO_INDICATORS` (invariant substrings) instead of raw `ECHOES` strings, since `{display}` in the source strings no longer matches rendered output
- Added 6 new tests in `TestEcho`: `test_echo_display_injection_contains_biome_name`, `test_echo_display_respects_combine`, `test_echo_display_without_display_phrase_still_works`, `test_echo_display_is_deterministic`, `test_echo_display_works_with_all_biomes` (with 5 subtests)
- Tests increased from 433 to 438 total (18 todo + 420 landscape)

### What was done (Session 81)
- Added **`{adverb}` injection into 5 echo phrases** — echo phrases now pick up the per-landscape adverb, making them feel connected to the landscape's adverbial flavor instead of reading as fixed text:
  - "The {display} remembers." → "The {display} remembers {adverb}." — "The tundra remembers silently."
  - "The {display} has been waiting for you." → "The {display} has been waiting {adverb} for you." — "The tundra has been waiting silently for you."
  - "The echoes of the past linger in the air of the {display}." → "The echoes of the past linger {adverb} in the air of the {display}." — "...linger softly in the air of the desert."
  - "There is a sense of deep time here, pressing down gently." → "There is a sense of deep time here, pressing down {adverb}." — "...pressing down slowly." (replaces hardcoded "gently" with the shared adverb pool)
  - "The stones remember what the wind has forgotten." → "The stones remember {adverb} what the wind has forgotten." — "The stones remember patiently what the wind has forgotten."
- Added `adverb=adverb` kwarg to the echo `_format_tmpl()` call — `adverb` was already in scope (last per-sentence-pair adverb or opening adverb for detail=0) but was not passed to echo templates
- Echo phrases without `{adverb}` (remaining 5) are unaffected — `_format_tmpl` silently ignores extra kwargs
- 5 remaining echoes without `{adverb}` kept as-is for structural variety
- `_format_tmpl` handles `adverb_enabled=False` cleanup naturally — "remembers ." → "remembers.", "linger  in" → "linger in", etc.
- Updated `ECHO_INDICATORS` invariant substrings: `"remembers."` → `"remembers"` (since the period is no longer adjacent), `"linger in the air"` → `"echoes of the past"` (since adverb separates "linger" from "in")
- Added 3 new tests in `TestEcho`: `test_echo_adverb_injection_contains_adverb`, `test_echo_adverb_respects_no_adverb`, `test_echo_adverb_is_deterministic`
- Tests increased from 438 to 441 total (18 todo + 423 landscape)

### What was done (Session 82)
- Added **`{element}` injection into 2 echo phrases** — the echo system now passes `element=element` to `_format_tmpl()`, so phrases that contain `{element}` render with the last-picked element word (from the detail loop), grounding abstract atmospheric echoes in the landscape's sensory substance:
  - "You feel as though you are being watched by the landscape itself." → "You feel as though you are being watched by the {element} itself." — "You feel as though you are being watched by the mist itself." / "...by the silence itself."
  - "This place exists outside of time." → "This place exists outside of time, in the {element}." — "...outside of time, in the mist." / "...in the silence."
- Added `element=element` kwarg to the echo `_format_tmpl()` call — `element` was already in scope (last-picked from the detail loop, or opening element for detail=0) but was not passed to echo templates
- 5 remaining echo phrases without `{element}` kept as-is for structural variety — the element injection split (2 of 10) is smaller than display (5 of 10) and adverb (5 of 10) because element words are more concrete and not all echo phrases benefit from referencing the physical element
- Added 5 new tests in `TestEcho`: `test_echo_element_injection_contains_element`, `test_echo_element_in_in_time_phrase`, `test_echo_element_is_deterministic`, `test_echo_element_works_with_detail_zero`, `test_echo_element_works_with_combine`
- Tests increased from 441 to 446 total (18 todo + 428 landscape)

### What was done (Session 84)
- Added **`{adj}` injection into 2 echo phrases** — the echo system now passes `adj=adj` to `_format_tmpl()`, so phrases that contain `{adj}` render with the per-sentence-pair adjective word, making echo phrases feel connected to the landscape's adjectival palette:
  - "The {display} remembers {adverb}." → "The {adj} {display} remembers {adverb}." — "The crystal tundra remembers silently."
  - "Something important happened in the {display} once." → "Something important happened in the {adj} {display} once." — "Something important happened in the crystal tundra once."
- Added `adj=adj` kwarg to the echo `_format_tmpl()` call — `adj` was already in scope (last per-sentence-pair adjective) but was not passed to echo templates
- 8 remaining echo phrases without `{adj}` kept as-is for structural variety — the adjective injection split (2 of 10) matches the element and color injection splits (also 2 of 10), since adjectives pair most naturally with biome names in phrases that already reference the biome
- No ECHO_INDICATORS changes needed — both modified phrases retain their invariant substrings ("remembers" and "important happened")
- Added 7 new tests in `TestEcho`: `test_echo_adj_injection_contains_adj`, `test_echo_adj_in_remembers_phrase`, `test_echo_adj_is_deterministic`, `test_echo_adj_works_with_detail_zero`, `test_echo_adj_works_with_combine`, `test_echo_adj_works_with_no_adverb`, `test_echo_adj_works_with_all_biomes`
- Tests increased from 453 to 460 total (18 todo + 442 landscape)

### What was done (Session 85)
- **Fixed color-pick bug with `--no-middle`**: when `middle_enabled=False`, the per-sentence-pair color pick was skipped because it was nested inside the `if middle_enabled:` block. Weather templates reference `{color}`, so `--no-middle` always produced weather sentences without color words (even when `color_enabled=True`).
  - Moved the color pick (`if color_enabled: color = _pick("colors", ...)`) outside the `if middle_enabled:` block, so it runs every iteration regardless of middle state.
  - The opening color pick (before the loop) was already correct — only per-sentence-pair colors were affected.
- **Seed-breaking**: the random call order changes for all cases (color is now picked before noun/verb instead of after), so existing seed-based output shifts. This is acceptable for a correctness fix.
- Added 1 new test: `test_weather_color_appears_with_middle_disabled` in `TestColors`
- Tests increased from 460 to 461 total (18 todo + 443 landscape)

### What was done (Session 86)
- Added **`--describe-echoes` CLI flag** and `describe_echoes()` function — users can now inspect all 10 echo phrases with their index numbers, completing the introspection feature set alongside `--describe-biome`, `--describe-mood`, `--describe-global`, and `--describe-templates`
  - Pure function returns a string with all echo phrases listed by index, matching the same pattern as `describe_templates()`
  - CLI exits immediately after printing — no landscape generation occurs when `--describe-echoes` is used
- Added 8 tests in `TestDescribeEchoes` class: string type, header presence, all echoes included, index numbers, last-index validation, CLI flag existence, stdout output, no landscape generation
- Tests increased from 461 to 469 total (18 todo + 451 landscape)

### What was done (Session 87)
- Added **`--echo-prob` CLI flag** and `echo_prob` parameter to `generate_landscape()` — users can now control how often echo phrases appear per roll (0.0 = never, 1.0 = always, default 1.0 preserves existing behavior)
  - Follows the exact same pattern as `--anomaly-prob` (Session 16): each echo roll independently draws `rng.random() < echo_prob`
  - When `echo_prob=0.0`, echoes never appear even with `echo_enabled=True` and `echo_count > 0`
  - `echo_prob` included in JSON metadata when `echo_enabled=True`
  - Default `echo_prob=1.0` is fully backward compatible — all existing seed-based output with `--echo` is unchanged
- Added 7 tests in `TestEchoProb` class: default is 1.0, zero suppression, high frequency, multi-prob validity, determinism, JSON metadata, CLI flag existence
- Tests increased from 469 to 476 total (18 todo + 458 landscape)

### What was done (Session 83)
- Added **`{color}` injection into 2 echo phrases** — the echo system now passes `color=color` to `_format_tmpl()`, so phrases that contain `{color}` render with the per-sentence-pair color word, grounding abstract atmospheric echoes in the landscape's visual palette:
  - "You feel as though you are being watched by the {element} itself." → "You feel as though you are being watched by the {color} {element} itself." — "You feel as though you are being watched by the vivid mist itself." / "...by the murky silence itself."
  - "This place exists outside of time, in the {element}." → "This place exists outside of time, in the {color} {element}." — "...outside of time, in the vivid mist." / "...in the murky silence."
- Added `color=color` kwarg to the echo `_format_tmpl()` call — `color` was already in scope (last-picked from the detail loop, or opening color for detail=0) but was not passed to echo templates
- 8 remaining echo phrases without `{color}` kept as-is for structural variety — the color injection split (2 of 10) matches the element injection split (also 2 of 10), since color words are most natural when paired with element words in the same phrase
- Updated `test_echo_element_injection_contains_element` to check for `"by the "` and `" itself"` separately (instead of `f"by the {e} itself"`) since the color word now sits between "by the" and the element
- Added 7 new tests in `TestEcho`: `test_echo_color_injection_contains_color`, `test_echo_color_in_watched_phrase`, `test_echo_color_in_time_phrase`, `test_echo_color_is_deterministic`, `test_echo_color_works_with_detail_zero`, `test_echo_color_works_with_combine`, `test_echo_color_works_with_color_disabled`
- Tests increased from 446 to 453 total (18 todo + 435 landscape)

### What was done (Session 51)
- Added **color word bank** (`COLORS`) to `landscape.py` — a new word category with 12 words across 3 weight tiers (4 common: vivid, burnished, stark, murky; 4 normal: lurid, mottled, bleached, veined; 4 rare: iridescent, fluorescent, scintillating, coruscating)
- Added mood-specific color lists to each mood in `MOOD_WORDS`: eerie gets dark/desaturated colors, vibrant gets bright/luminous colors, desolate gets muted/bleached colors
- Integrated colors into the full pipeline: global pool in `_pick()`, per-sentence-pair selection in `generate_landscape()`, mood-boost in `_word_weight()`, cross-sentence dedup, and weight tiers (common/rare)
- Added new 7th middle template: `"The {color} light of {element} {verb_conjugated} {adverb}."` — produces lines like "The vivid light of mist shimmers gently."
- Updated `describe_global()` to include the colors category
- Added 12 tests in `TestColors` class: output presence, middle-template appearance, determinism, mood boost (matched and unmatched), weight tiers, template structure, detail=3 compatibility, middle-disabled compatibility, JSON output, and `describe_global` inclusion
- Tests increased from 256 to 268 total (18 todo + 250 landscape)

## 2026-07-11

### What was done (Session 16)
- Added **per-category bias overrides** via 6 CLI flags (`--bias-adjective`, `--bias-element`, `--bias-noun`, `--bias-verb`, `--bias-weather`, `--bias-anomaly`) and `bias_overrides` parameter to `generate_landscape()` — users can now control word selection bias independently per category
  - Each flag accepts the same choices as `--bias`: `normal`, `common`, `rare`, `flat`
  - When set, overrides the global `--bias` for that specific category
  - Example: `--bias common --bias-adjective rare` = common words everywhere except rare adjectives
- Added `bias_overrides` dict parameter to `_pick()` — resolves `bias_overrides.get(category, global_bias)` for each pick
- No changes to `_word_weight()` (it already accepts a bias string — the override is resolved before calling it)
- Added 7 tests: `test_bias_overrides_default_does_not_change_output`, `test_bias_overrides_empty_dict_equals_no_override`, `test_bias_overrides_produces_valid_output`, `test_bias_adjective_override_rare_reduces_common_adjectives`, `test_bias_element_override_common_increases_common_elements`, `test_bias_overrides_multiple_categories`, `test_bias_overrides_flag_exists_via_cli`
- Tests increased from 95 to 102 total (18 todo + 84 landscape)

## 2026-07-11

### What was done (Session 15)
- Added **`--template-set` CLI flag** and `template_set` parameter to `generate_landscape()` — exposes template selection control to users
  - `"random"` (default): random choice per slot (existing behavior, backward compatible)
  - `"first"`: always uses index 0 for every slot (opening="A vast...", middle="{Element}...", weather="{Weather}.", anomaly="{anomaly}")
  - `"second"`: always uses index 1 for every slot (opening="Before you...", middle="Among the...", weather="The air tells...", anomaly="Something is not right...")
  - `"third"`: always uses index 2 for every slot (opening="The...", middle="The {noun}...", weather="...as if the...", anomaly="A strange detail...")
- Added `TEMPLATE_SETS` dict mapping mode names to `None` (random) or an int index
- Added `_pick_template(slot, template_set)` helper used by all 4 template slots (opening, middle, weather, anomaly)
- Added 9 tests: `test_template_set_default_is_random`, `test_template_set_first_uses_first_opening`, `test_template_set_second_uses_second_opening`, `test_template_set_third_uses_third_opening`, `test_template_set_first_is_deterministic`, `test_template_set_second_middle_has_expected_pattern`, `test_template_set_third_weather_has_expected_pattern`, `test_template_set_flag_exists_via_cli`, `test_pick_template_selects_correct_index`
- Tests increased from 86 to 95 total (18 todo + 77 landscape)

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

### What was done (Session 11)
- Added **`--bias` CLI flag** and `bias` parameter to `generate_landscape()` exposing the word-weight system for user control
  - Four modes: `normal` (default, common=10 / normal=5 / rare=1), `common` (common=20, further skews toward frequent words), `rare` (rare=3, makes uncommon words appear more often), `flat` (all=1, uniform selection)
  - `BIAS_MODES` dict maps mode names to weight triples
  - `_word_weight()` now accepts a `bias` parameter; `_pick()` threads it through
- Added 6 tests: `test_bias_default_is_normal`, `test_bias_modes_affect_word_weights`, `test_bias_flat_produces_valid_output`, `test_bias_common_increases_common_word_frequency`, `test_bias_rare_increases_rare_word_frequency`, `test_bias_flag_exists_via_cli`
- Tests increased from 64 to 70 total (18 todo + 52 landscape)

### What was done (Session 12)
- Added **`--show-seed` CLI flag** and `show_seed` parameter to `generate_landscape()` — when set, the seed used is appended in square brackets (e.g. `[seed=42]`)
  - If a seed is provided via `--seed`, that seed is shown
  - If no seed is provided, a random seed is auto-generated, the RNG is seeded with it, and that seed is shown — making every output reproducible
- Added 5 tests: `test_show_seed_with_provided_seed_shows_seed`, `test_show_seed_default_hides_seed`, `test_show_seed_without_seed_generates_seed`, `test_show_seed_output_is_reproducible`, `test_show_seed_flag_works_via_cli`
- Tests increased from 70 to 75 total (18 todo + 57 landscape)

### What was done (Session 13)
- Added **mood/emotion overlay** via `--mood` CLI flag and `mood` parameter to `generate_landscape()`
  - Three moods: `eerie`, `vibrant`, `desolate`
  - Each mood defines a curated set of tone-matched words per category (adjectives, elements, nouns, verbs, weathers, anomalies)
- Added `MOOD_WORDS` dict and `MOOD_BOOST = 5` constant
- Updated `_word_weight()` to accept `mood` and `category` params — when a word matches the active mood's category list, its weight is multiplied by `MOOD_BOOST` (5x), making mood-themed words much more likely without excluding other vocabulary
- `mood` parameter threads through `_pick()` → `_word_weight()` for all word selections
- Mood works orthogonally to `--bias`: bias sets the base weight distribution, mood multiplies on top; they compose naturally
- Added 5 tests: `test_mood_does_not_break_output`, `test_mood_word_weight_boosted_for_matched_words`, `test_mood_word_weight_not_boosted_for_unmatched_words`, `test_mood_category_specific_boost`, `test_mood_flag_exists_via_cli`
- Tests increased from 75 to 80 total (18 todo + 62 landscape)

### What was done (Session 14)
- Added **`--mood-weight` CLI flag** and `mood_weight` parameter to `generate_landscape()` — a float multiplier (default: 5) that controls how strongly mood-matched words are boosted
  - `--mood-weight 1` means no mood boost (equivalent to no mood)
  - `--mood-weight 0` suppresses mood words entirely (weight = 0)
  - Higher values (e.g. 10, 20) make mood words dominate the output
  - `--mood-weight` replaces the hard-coded `MOOD_BOOST = 5` constant, threading through `_word_weight()` → `_pick()` → `generate_landscape()` → CLI
- `MOOD_BOOST` kept as module-level constant (default value), so existing code that imports it still works
- Added 6 tests: `test_mood_weight_one_equals_no_boost`, `test_mood_weight_zero_suppresses_mood_words`, `test_mood_weight_high_magnifies_boost`, `test_mood_weight_default_matches_mood_boost`, `test_mood_weight_produces_valid_output`, `test_mood_weight_flag_exists_via_cli`
- Tests increased from 80 to 86 total (18 todo + 68 landscape)

## 2026-07-11

### What was done (Session 17)
- Added **per-category mood-weight overrides** via 6 CLI flags (`--mood-weight-adjective`, `--mood-weight-element`, `--mood-weight-noun`, `--mood-weight-verb`, `--mood-weight-weather`, `--mood-weight-anomaly`) and `mood_weight_overrides` dict parameter to `generate_landscape()` — users can now control mood weight independently per category
  - Each flag accepts a float (same as `--mood-weight`), overriding the global mood weight for that specific category
  - Example: `--mood eerie --mood-weight 5 --mood-weight-adjective 20` = eerie mood with heavy adjective skew but normal boost for everything else
- Added `mood_weight_overrides` dict parameter to `_word_weight()` — resolves `mood_weight_overrides.get(category, mood_weight)` for each mood-boost computation
- Added `mood_weight_overrides` parameter to `_pick()` and `generate_landscape()` — threads through to `_word_weight()` the same way `bias_overrides` threads through to `_pick()`
- Added 7 tests: `test_mood_weight_overrides_default_does_not_change_output`, `test_mood_weight_overrides_empty_dict_equals_no_override`, `test_mood_weight_overrides_produces_valid_output`, `test_mood_weight_adjective_override_high_boosts_mood_adjectives`, `test_mood_weight_element_override_zero_suppresses_mood_elements`, `test_mood_weight_overrides_multiple_categories`, `test_mood_weight_overrides_cli_flags_exist`
- Tests increased from 102 to 109 total (18 todo + 91 landscape)

## 2026-07-11

### What was done (Session 19)
- Added **cross-sentence word dedup**: `_pick()` now accepts an optional `used_words` set — when provided, already-used words are excluded from the selection pool and the newly chosen word is added to the set
- In `generate_landscape()`, a single `used_words = set()` is threaded through all `_pick()` calls, so no word can be selected more than once per landscape (across all categories: adjectives, elements, nouns, verbs, weathers, anomalies)
- If the filtered pool is empty (all words exhausted), falls back to the unfiltered pool — so edge cases with tiny biome word banks don't crash
- Backward compatible: `used_words=None` (default) preserves the existing behavior for tests or direct `_pick()` calls that don't need dedup
- Updated `test_detail_two_is_longer_than_one` to `test_detail_two_has_more_sentences_than_one` (counts periods instead of char length) to avoid a statistical edge case where anomaly text at detail=1 happens to equal the extra sentence pair at detail=2
- Added 5 tests: `test_word_dedup_via_used_words_parameter`, `test_word_dedup_across_multiple_picks_same_category`, `test_word_dedup_across_categories`, `test_word_dedup_without_used_words_still_works`, `test_word_dedup_still_produces_valid_output`, `test_word_dedup_does_not_break_format_modes`
- Tests increased from 116 to 122 total (18 todo + 104 landscape)

## 2026-07-11

### What was done (Session 20)
- Added **configurable anomaly probability** via `--anomaly-prob` CLI flag and `anomaly_prob` parameter to `generate_landscape()` — users can now control how often anomalies appear (0.0 = never, 1.0 = always, default 0.3 preserves existing behavior)
  - Replaced the hardcoded `random.random() < 0.3` with `random.random() < anomaly_prob`
  - This was the last remaining magic number in the generation logic
- Added 5 tests: `test_anomaly_prob_default_works`, `test_anomaly_prob_zero_suppresses_anomalies`, `test_anomaly_prob_one_always_has_anomaly`, `test_anomaly_prob_produces_valid_output`, `test_anomaly_prob_flag_exists_via_cli`
- Tests increased from 122 to 127 total (18 todo + 109 landscape)

## 2026-07-11

### What was done (Session 21)
- Fixed **`--count` + `--seed` interaction**: previously, `--seed 42 --count 3` produced the same output 3 times because every loop iteration passed the same seed. Now the seed auto-increments per iteration (`seed + i`), so each output is unique and individually reproducible
  - `--seed 42 --count 3` is equivalent to running `--seed 42`, `--seed 43`, `--seed 44` separately
  - `--count` without `--seed` (fully random) is unaffected
- One-line change in `main()`: `effective_seed = args.seed + i if args.seed is not None else None`
- Added 4 tests in `TestCountWithSeed` class: `test_count_seed_sequence_produces_unique_outputs`, `test_count_seed_sequence_is_reproducible`, `test_count_seed_sequence_different_from_single_seed`, `test_count_without_seed_produces_varied_outputs`
- Tests increased from 127 to 131 total (18 todo + 113 landscape)

## 2026-07-11

### What was done (Session 22)
- Added **3 new biomes**: `ruined city`, `fungal grove`, and `sky islands` — expanding the landscape generator beyond purely natural environments into weird, unusual settings
  - **ruined city**: post-urban decay vocabulary (crumbling, rusted, skeletal facades and girders)
  - **fungal grove**: bioluminescent mushroom forest (spore glow, mycelial, caps and hyphae)
  - **sky islands**: floating archipelago above the clouds (cloud-wreathed, ethereal, archipelagos and updrafts)
- Added 11 tests in `TestNewBiomes` class: `test_ruined_city_in_biomes_list`, `test_fungal_grove_in_biomes_list`, `test_sky_islands_in_biomes_list`, `test_ruined_city_produces_valid_output`, `test_fungal_grove_produces_valid_output`, `test_sky_islands_produces_valid_output`, `test_ruined_city_uses_specific_vocabulary`, `test_fungal_grove_uses_specific_vocabulary`, `test_sky_islands_uses_specific_vocabulary`, `test_new_biomes_appear_in_random_selection`, `test_combine_with_new_biome_uses_vocabulary`
- Tests increased from 131 to 142 total (18 todo + 124 landscape)

## 2026-07-11

### What was done (Session 23)
- **Fixed noun-verb agreement in middle template 3**: Changed `{verb_conjugated}` to `{verb}` in `SENTENCE_TEMPLATES["middle"][2]` — the third middle template was `"The {noun} {verb_conjugated} with {element}."`, which produced grammatically incorrect outputs like "The trees whispers with light." (plural noun + singular verb). Now produces "The trees whisper with light." (plural noun + bare verb).
  - Templates 1 and 2 are unaffected — their subject (`{Element}` and `{element}`) are singular, so `{verb_conjugated}` is correct there.
- Added 2 tests: `test_middle_third_template_uses_bare_verb` (direct template string assertion) and `test_middle_third_end_to_end_bare_verb` (smoke test with `template_set="third"`).
- Tests increased from 142 to 144 total (18 todo + 126 landscape)

## 2026-07-11

### What was done (Session 24)
- Added **adverb word category** (`ADVERBS`) to `landscape.py` — a new 12-word global adverb pool with weighted tiers (4 common, 4 rare)
  - Common adverbs: softly, gently, silently, quietly
  - Rare adverbs: relentlessly, patiently, eternally, ceaselessly
  - Normal adverbs: endlessly, slowly, constantly, subtly
- Added **mood-specific adverbs** to each mood in `MOOD_WORDS`: eerie gets silent/slow/eternal adverbs, vibrant gets gentle/soft/endless, desolate gets relentless/constant/slow
- Added `"adverbs"` to the global pool dict in `_pick()` — fully integrated with weighted selection, bias, mood boosts, per-category bias/mood-weight overrides, and cross-sentence word dedup
- `generate_landscape()` picks a single adverb per landscape (before the sentence loop), threaded through all format calls as `{adverb}` — templates that don't use it ignore it
- Added **2 new middle templates** with `{adverb}`:
  - `"{Element} {verb_conjugated} {adverb} through the {noun}."` (index 3)
  - `"Beneath the {noun}, {element} {verb_conjugated} {adverb}."` (index 4)
- Existing 3 middle templates are unchanged — `template_set="first/second/third"` and `template_overrides` still work
- Added 6 tests: `test_output_contains_known_adverb`, `test_adverb_appears_in_middle_templates`, `test_adverb_with_mood_does_not_break_output`, `test_adverb_is_deterministic_with_seed`, `test_adverb_with_detail_three_produces_valid_output`, `test_adverb_word_weight_function_works`
- Tests increased from 144 to 150 total (18 todo + 132 landscape)

## 2026-07-11

### What was done (Session 26)
- Added **JSON output format** via `--format json` CLI flag — outputs a structured JSON object with the landscape `text` plus metadata fields (`biome`, `seed`, `mood`, `bias`, `detail`, `template_set`, `anomaly_prob`, and any overrides)
  - When `--combine` is used, includes both `biome` (display string) and `biomes` (list of all combined biomes)
  - When `--mood` is set, includes `mood` as a list (even for a single mood, for consistency)
  - The `text` field contains the clean prose without bracketed biome/seed tags — metadata goes in JSON fields instead
  - All existing `--format` modes (`prose`, `poetic`) are unchanged
- Added `import json` to `landscape.py`
- Added 9 tests: `test_format_json_valid_json`, `test_format_json_contains_text_key`, `test_format_json_contains_biome_key`, `test_format_json_contains_seed_when_provided`, `test_format_json_text_matches_prose`, `test_format_json_with_combine_includes_biomes_list`, `test_format_json_includes_mood_when_set`, `test_format_json_does_not_have_bracketed_tags`, `test_format_json_works_with_all_formats_flag`
- Tests increased from 155 to 164 total (18 todo + 146 landscape)

### What was done (Session 25)
- Added **mood blending**: `--mood` CLI flag now uses `action="append"` and accepts multiple values — users can blend moods by repeating the flag (e.g. `--mood eerie --mood vibrant`) to create hybrid tonal palettes
  - `--mood eerie --mood vibrant` = haunting beauty (eerie's silence + vibrant's light)
  - `--mood eerie --mood desolate` = bleak and unsettling (both lean into darkness/stillness)
  - `--mood vibrant --mood desolate` = beauty amidst decay (vibrant's glow + desolate's barren)
  - `--mood eerie --mood vibrant --mood desolate` = all three (most words from any mood list get boosted)
- Modified `_word_weight()` to accept `mood` as a string (single mood, backward compatible), list, or tuple — when a word matches **any** active mood's category list, the mood-weight boost applies
  - The `break` on first match ensures the boost is applied once (not compounded) even if a word appears in multiple moods' lists
- No changes to `_pick()` or `generate_landscape()` signatures — `mood` threaded through as before, both string and list callers work
- `--mood` CLI changed from `type=str, choices=...` to `action="append", type=str, choices=...` — single usage (`--mood eerie`) produces a 1-element list internally, which `_word_weight()` normalizes the same way as a bare string
- Added 5 tests: `test_mood_combine_does_not_break_output`, `test_mood_combine_uses_words_from_both`, `test_mood_combine_different_from_single_mood`, `test_mood_combine_all_three_still_valid`, `test_mood_combine_cli_flag_accepts_multiple`
- Tests increased from 150 to 155 total (18 todo + 137 landscape)

## 2026-07-11

### What was done (Session 28)
- Added **`{adverb}` to the third opening template** — changed `"The {adj} {display} lies ahead."` to `"The {adj} {display} lies {adverb} ahead."` in `SENTENCE_TEMPLATES["opening"]`. The adverb is already picked per-landscape and passed to all template format calls, but only middle templates used it. Now the opening template can produce lines like "The crystal forest lies silently ahead.", making the opener more expressive.
- No new tests needed — existing template tests (`test_output_starts_with_valid_opening`, `test_template_set_third_uses_third_opening`, `test_template_set_third_weather_has_expected_pattern`) all still pass because the opening start ("The ") and index 2 are unchanged.
- Tests: still 167 (18 todo + 149 landscape)

### What was done (Session 29)
- Added **`--anomaly-count` CLI flag** and `anomaly_count` parameter to `generate_landscape()` — users can now control how many anomaly rolls happen per landscape (default: 1, range 0–3)
  - Each anomaly independently rolls against `anomaly_prob`, so `--anomaly-count 3 --anomaly-prob 0.5` yields ~1–2 anomalies on average
  - `--anomaly-count 0` suppresses anomalies regardless of `anomaly_prob` (alternative to `--anomaly-prob 0`)
  - Replaced the single `if` block with a `for _ in range(anomaly_count)` loop
  - Added `anomaly_count` to JSON metadata output
- Added 6 tests: `test_anomaly_count_default_is_one`, `test_anomaly_count_zero_no_anomalies`, `test_anomaly_count_two_sometimes_has_multiple`, `test_anomaly_count_produces_valid_output`, `test_anomaly_count_flag_exists_via_cli`, `test_anomaly_count_json_includes_field`
- Tests increased from 167 to 173 total (18 todo + 155 landscape)

### What was done (Session 30)
- **Added `{adverb}` to opening templates 0 and 1, and weather template 1** — the adverb is now used in all 3 opening templates (was only in template 2/third) and in the first weather template (was not used by any weather template)
  - Opening 0: `"A vast {adj} {display} stretches {adverb} before you."` (previously no adverb)
  - Opening 1: `"Before you, a {adj} {display} comes into view {adverb}."` (previously no adverb)
  - Weather 1: `"{Weather} {adverb}."` (previously `"{Weather}."`)
  - No code changes needed — `adverb` was already threaded through all format calls
  - No new tests — existing adverb and template tests cover the change
- Tests: still 173 total (18 todo + 155 landscape)

## 2026-07-11

### What was done (Session 32)
- Added **`--output` / `-o` CLI flag** — writes generated landscapes to a file instead of stdout
  - Refactored `main()` to collect all output into a list, then either write to file or print to stdout
  - When `--output` is used, output goes only to the file (nothing printed to terminal)
  - Works with `--count`: all landscapes are written to the file, separated by blank lines
  - Backward compatible: without `--output`, behavior is identical to before
- Added 5 tests in `TestOutputFlag` class: `test_output_flag_writes_to_file`, `test_output_file_contains_generated_text`, `test_output_file_matches_stdout_output`, `test_output_with_count_writes_all_landscapes`, `test_output_flag_exists_via_cli`
- Tests increased from 177 to 182 total (18 todo + 164 landscape)

## 2026-07-12

### What was done (Session 33)
- Added **`--no-dedup` CLI flag** and `dedup` parameter to `generate_landscape()` — users can now disable cross-sentence word deduplication when they want to allow repeated words in the output
  - `dedup=True` (default) preserves existing behavior — `used_words` set is created and threaded through all `_pick()` calls
  - `dedup=False` passes `used_words=None`, so the dedup logic in `_pick()` is entirely bypassed
  - No changes to `_pick()` — `used_words=None` (the default for that parameter) already means "no dedup"
  - Follows the pattern of `--anomaly-prob` and other quality-of-life flags: automatic improvements are configurable
- Added 6 tests in `TestDedupFlag` class: `test_dedup_default_is_true`, `test_dedup_disabled_still_produces_valid_output`, `test_dedup_flag_exists_via_cli`, `test_dedup_disabled_produces_deterministic_output`, `test_dedup_disabled_works_with_detail_three`, `test_dedup_disabled_works_with_mood_and_bias`
- Tests increased from 182 to 188 total (18 todo + 170 landscape)

## 2026-07-12

### What was done (Session 34)
- Added **`--no-adverb` CLI flag** and `adverb_enabled` parameter to `generate_landscape()` — users can now disable adverb insertion in generated descriptions
  - `adverb_enabled=True` (default) preserves existing behavior — an adverb is picked per-landscape and threaded through templates
  - `adverb_enabled=False` skips the adverb pick entirely and passes an empty string to all template format calls
  - Follows the same pattern as `--no-dedup` (Session 33): automatic quality improvement made configurable
- Added **`_format_tmpl(template, **kwargs)` helper** — wraps `str.format()` with post-processing that collapses double spaces and removes space-before-period artifacts that occur when `{adverb}` is empty
  - Used for all 4 template format calls (opening, middle, weather, anomaly) — the helper is a no-op when `{adverb}` has a real value
- Added 8 tests in `TestAdverbFlag` class: `test_adverb_enabled_default_same_as_before`, `test_adverb_disabled_still_produces_valid_output`, `test_adverb_disabled_differs_from_enabled`, `test_adverb_disabled_deterministic`, `test_adverb_disabled_no_formatting_artifacts`, `test_adverb_disabled_flag_exists_via_cli`, `test_adverb_disabled_works_with_detail_three`, `test_adverb_disabled_works_with_mood_and_bias`
- Tests increased from 188 to 196 total (18 todo + 178 landscape)

## 2026-07-12

### What was done (Session 35)
- Fixed **`--format json --count N` output**: previously, each landscape was a valid JSON object but they were concatenated with `\n\n`, producing an invalid JSON document that tools like `jq` could not parse
  - When `--format json` is used with `--count N` (N > 1), `main()` now wraps the items in a JSON array (`[...]`) separated by commas
  - Single-landscape JSON output (`--count 1` or default) is unchanged — still a single JSON object
  - Prose and poetic output formats are unaffected — still joined by `\n\n`
- One-line change in `main()`: added an `if`/`else` block that checks `args.format == "json" and len(lines) > 1`
- Added 4 tests in `TestJsonWithCount` class: `test_format_json_count_one_is_single_object`, `test_format_json_count_two_is_array`, `test_format_json_count_three_all_valid_json`, `test_format_json_count_array_items_have_unique_biomes`
- Tests increased from 196 to 200 total (18 todo + 182 landscape)

## 2026-07-12

### What was done (Session 36)
- Added **`--biome-weight` CLI flag** and `biome_weights` parameter to `generate_landscape()` — users can now control how often specific biomes appear during random selection
  - Accepts comma-separated `biome=weight` pairs (e.g. `--biome-weight forest=5,desert=1,sky_islands=10`)
  - Biomes with higher weights are more likely to be selected; weight 0 suppresses a biome entirely
  - If all biomes have weight 0, falls back to equal probability (doesn't crash)
  - Only affects random biome selection — has no effect when `--biome` or `--combine` is used
  - Included in JSON metadata output as `biome_weights`
- Backward compatible: default (`None` or `{}`) produces identical output to before
- Added 6 tests in `TestBiomeWeights` class: `test_biome_weights_default_does_not_change_output`, `test_biome_weights_produces_valid_output`, `test_biome_weights_zero_suppresses_biome`, `test_biome_weights_all_zero_falls_back`, `test_biome_weights_flag_exists_via_cli`, `test_biome_weights_json_includes_field`
- Tests increased from 200 to 206 total (18 todo + 188 landscape)

## 2026-07-12

### What was done (Session 37)
- Changed adverb from single-per-landscape to **per-sentence-pair**: previously the same adverb was used for the opening and every middle+weather sentence pair; now each sentence pair (and the opening) gets its own adverb pick
  - Opening still picks its own adverb once before the template
  - Inside the `detail` loop, a fresh adverb is picked for each middle+weather pair
  - Anomaly templates (which don't use `{adverb}`) still receive the last-picked adverb as a kwarg (no-op)
- `adverb_enabled` behavior is unchanged: when `False`, all adverb slots are empty strings
- This is a **seed-breaking change**: existing seed-based output differs because the random call order changes (one extra `_pick` call per detail level). Determinism is preserved: the same seed still produces the same output.
- Per-sentence adverbs make detail=2 and detail=3 outputs richer by allowing different adverbial flavors across sentence pairs (e.g., "silently" in the first pair, "gently" in the second)
- Added 5 tests: `test_per_sentence_adverb_uses_multiple_adverbs`, `test_per_sentence_adverb_deterministic`, `test_per_sentence_adverb_detail_three_has_more_adverb_variety`, `test_per_sentence_adverb_respects_adverb_disabled`, `test_per_sentence_adverb_with_adverb_enabled_default`
- Tests increased from 206 to 211 total (18 todo + 193 landscape)

## 2026-07-12

### What was done (Session 38)
- Added **`{adj}` to middle templates 1 and 2** — the opening's adjective is now visible in middle sentences for richer descriptions
  - Template 1: `"Among the {noun}, {element} {verb_conjugated}."` → `"Among the {adj} {noun}, {element} {verb_conjugated}."` (e.g. "Among the crystal trees, mist whispers.")
  - Template 2: `"The {noun} {verb} with {element}."` → `"The {adj} {noun} {verb} with {element}."` (e.g. "The crystal stones glow with light.")
- Added `adj=adj` kwarg to `_format_tmpl(middle_tmpl, ...)` call — the `adj` variable was already in scope (picked per-landscape at line 510) and unused by middle templates. Now templates that include `{adj}` resolve to the opening's adjective, while unmodified templates (0, 3, 4) silently ignore the extra kwarg.
- No new tests needed — existing template and output tests cover the change
- Tests: still 211 total (18 todo + 193 landscape)

## 2026-07-12

### What was done (Session 39)
- Added **biome name reference in middle sentences**: new 6th middle template `"Across the {display}, {element} {verb_conjugated} {adverb}."` now references the biome name (`display`) in middle sentences, so the landscape description stays grounded in its biome context throughout (not just in the opening and weather)
  - Example: "Across the forest, birdsong whispers softly." or "Across the ruined city, dust settles ceaselessly."
- Made `display` kwarg available to all middle templates by adding `display=display` to the `_format_tmpl()` call — existing templates silently ignore the extra kwarg, new template uses it
- No code changes beyond adding the template string and one kwarg — follows the existing pattern established by `{adj}` in middle templates (Session 38) and `{adverb}` (Sessions 24/37)
- Added 3 tests: `test_middle_template_display_exists_in_pool` (direct string assertion), `test_middle_template_with_display_appears_in_output` (statistical — appears across 300 seeds), `test_middle_template_display_composable_with_combine` (works with `--combine`)
- Tests increased from 193 to 196 total (18 todo + 178 landscape)

## 2026-07-12

### What was done (Session 40)
- Added `{adj}` to the classic middle template (index 0): `"{Element} {verb_conjugated} between the {adj} {noun}."` — previously `"{Element} {verb_conjugated} between the {noun}."` without an adjective, making it the only middle template that didn't use the already-picked landscape adjective
  - Example output: "Mist whispers between the crystal trees." instead of "Mist whispers between the trees."
  - The `adj` kwarg was already passed to the middle template format call (from Session 38), so this is a one-line template string change with no code changes
- No new tests — existing template and output tests cover the change
- Tests: still 196 total (18 todo + 178 landscape)

## 2026-07-12

### What was done (Session 41)
- Added `{adj}` to middle templates 3 and 4 — the last two middle templates that didn't use the landscape's adjective:
  - Template 3: `"Mist whispers softly through the crystal trees."` (was `"Mist whispers softly through the trees."`)
  - Template 4: `"Beneath the ancient stones, light glows softly."` (was `"Beneath the stones, light glows softly."`)
  - The `adj` kwarg was already passed to the middle template format call (from Session 38), so this is a template-level change only — no code changes
- Now all 6 middle templates use `{adj}`, making descriptions consistently richer across all template slots
- No new tests — existing template and output tests cover the change
- Tests: 214 total (18 todo + 196 landscape)

## 2026-07-12

### What was done (Session 42)
- Added `{adverb}` to weather templates 1 and 2 — the adverb is now used in all 3 weather templates (was only in template 0)
  - Template 1: `"The air tells its own story: {weather}."` → `"The air tells its own story: {weather} {adverb}."` (e.g. "The air tells its own story: a gentle rain falls softly.")
  - Template 2: `"{Weather}, as if the {display} itself breathes."` → `"{Weather}, as if the {display} itself breathes {adverb}."` (e.g. "A gentle rain falls, as if the forest itself breathes softly.")
  - No code changes needed — `adverb` was already threaded through all weather format calls; `_format_tmpl` handles the trailing-space cleanup when `adverb_enabled=False`
- The adverb now appears in 8 of 15 templates (opening: 3/3, middle: 2/6, weather: 3/3, anomaly: 0/4) — up from 6 of 15
- No new tests — existing adverb and template tests cover the change
- Tests: still 214 total (18 todo + 196 landscape)

## 2026-07-12

### What was done (Session 43)
- Added **`--describe-biome` CLI flag** and `describe_biome()` function — users can now inspect the word bank for any biome without reading the source code
  - `--describe-biome forest` prints all word categories (adjectives, elements, nouns, verbs, weathers, anomalies) for the forest biome
  - `--describe-biome` (no argument) or `--describe-biome all` lists all 13 biomes with their word banks
  - Unknown biome names produce a clear error message
  - The function returns a string (no side effects) so it can be tested and reused programmatically
  - CLI exits immediately after printing — no landscape generation occurs when `--describe-biome` is used
- Added 7 tests in `TestDescribeBiome` class: `test_describe_known_biome_contains_name`, `test_describe_known_biome_contains_categories`, `test_describe_unknown_biome_returns_error`, `test_describe_all_contains_all_biomes`, `test_describe_biome_flag_exists_via_cli`, `test_describe_biome_flag_prints_to_stdout`, `test_describe_all_flag_prints_multiple_biomes`
- Tests increased from 214 to 221 total (18 todo + 203 landscape)

## 2026-07-12

### What was done (Session 44)
- Added **`--describe-mood` CLI flag** and `describe_mood()` function — users can now inspect the word bank for any mood without reading the source code
  - `--describe-mood eerie` prints all word categories (adjectives, elements, nouns, verbs, adverbs, weathers, anomalies) for the eerie mood
  - `--describe-mood` (no argument) or `--describe-mood all` lists all 3 moods with their word banks
  - Unknown mood names produce a clear error message
  - The function returns a string (pure, no side effects) so it can be tested and reused programmatically
  - CLI exits immediately after printing — no landscape generation occurs when `--describe-mood` is used
- Added 7 tests in `TestDescribeMood` class: `test_describe_known_mood_contains_name`, `test_describe_known_mood_contains_categories`, `test_describe_unknown_mood_returns_error`, `test_describe_all_contains_all_moods`, `test_describe_mood_flag_exists_via_cli`, `test_describe_mood_flag_prints_to_stdout`, `test_describe_all_moods_flag_prints_multiple`
- Tests increased from 221 to 228 total (18 todo + 210 landscape)

## 2026-07-12

### What was done (Session 45)
- Added **`--describe-global` CLI flag** and `describe_global()` function — users can now inspect all global word pools (adjectives, elements, nouns, verbs, weathers, anomalies, adverbs) with per-word weight tier annotations (common/normal/rare) without reading the source code
  - Lists every global word in each category, grouped by weight tier (common: crystal, shadow, ...; normal: ember, frost, ...; rare: glass, brass, ...)
  - Pure function returns a string (no side effects) — same pattern as `describe_biome()` and `describe_mood()`, callers can reuse it programmatically, tests assert on the returned string
  - CLI exits immediately after printing — no landscape generation occurs when `--describe-global` is used
- Follows the same pattern as `--describe-biome` (Session 43) and `--describe-mood` (Session 44), completing the introspection triad: biome, mood, and global word pools are now all discoverable from the CLI
- This was explicitly anticipated as a future gap in DECISIONS.md (Session 43): "Users who want to see global words can look at the source or a future `--describe-global` flag."
- Added 9 tests in `TestDescribeGlobal` class: `test_describe_global_returns_string`, `test_describe_global_contains_header`, `test_describe_global_contains_all_categories`, `test_describe_global_contains_weight_tiers`, `test_describe_global_contains_known_common_words`, `test_describe_global_contains_known_rare_words`, `test_describe_global_flag_exists_via_cli`, `test_describe_global_flag_prints_to_stdout`, `test_describe_global_no_landscape_generated`
- Tests increased from 228 to 237 total (18 todo + 219 landscape)

## 2026-07-12

### What was done (Session 46)
- Added **`--no-weather` CLI flag** and `weather_enabled` parameter to `generate_landscape()` — users can now suppress weather descriptions while keeping opening, middle, and anomaly sentences
  - `weather_enabled=True` (default) preserves existing behavior
  - `weather_enabled=False` skips the weather pick and template in the detail loop — only middle sentences are generated for each detail iteration
  - Follows the same pattern as `--no-dedup` (Session 33) and `--no-adverb` (Session 34): automatic quality improvement made configurable
  - Works with `detail=0` (opening only, no-op) and `--format json`
- Added 9 tests in `TestWeatherFlag` class: `test_weather_enabled_default_same_as_before`, `test_weather_disabled_still_produces_valid_output`, `test_weather_disabled_differs_from_enabled`, `test_weather_disabled_has_fewer_sentences`, `test_weather_disabled_deterministic`, `test_weather_disabled_works_with_detail_three`, `test_weather_disabled_works_with_mood_and_bias`, `test_weather_disabled_works_with_json_format`, `test_weather_disabled_flag_exists_via_cli`
- Tests increased from 237 to 246 total (18 todo + 228 landscape)

## 2026-07-12

### What was done (Session 47)
- Added **`{adverb}` to middle templates 0, 1, and 2** — the last 3 middle templates that didn't use the per-sentence-pair adverb. Now all 6 middle templates use `{adverb}`:
  - Template 0: `"{Element} {verb_conjugated} {adverb} between the {adj} {noun}."` (was `"...between the {adj} {noun}."`)
  - Template 1: `"Among the {adj} {noun}, {element} {verb_conjugated} {adverb}."` (was `"...{element} {verb_conjugated}."`)
  - Template 2: `"The {adj} {noun} {verb} {adverb} with {element}."` (was `"...{verb} with {element}."`)
- No code changes needed — `adverb` was already threaded through all middle template format calls (since Session 24/37); `_format_tmpl` handles the `adverb_enabled=False` cleanup
- The adverb now appears in 11 of 15 templates (opening: 3/3, middle: 6/6, weather: 3/3, anomaly: 0/4) — up from 8 of 15
- No new tests — existing adverb and template tests cover the change
- Tests: still 246 total (18 todo + 228 landscape)

## 2026-07-12

### What was done (Session 48)
- Added **`--no-middle` CLI flag** and `middle_enabled` parameter to `generate_landscape()` — users can now suppress middle sentences while keeping opening, weather, and anomaly sentences
  - `middle_enabled=True` (default) preserves existing behavior
  - `middle_enabled=False` skips element/noun/verb picks and middle template rendering in the detail loop — only weather sentences are generated for each detail iteration
  - The per-sentence-pair adverb pick still happens even when middle is disabled, so weather templates get their adverb
  - Composes orthogonally with all other controls: `--no-middle --no-weather` produces opening + anomaly only
  - Follows the same pattern as `--no-dedup` (Session 33), `--no-adverb` (Session 34), and `--no-weather` (Session 46)
- Added 10 tests in `TestMiddleFlag` class: `test_middle_enabled_default_same_as_before`, `test_middle_disabled_still_produces_valid_output`, `test_middle_disabled_differs_from_enabled`, `test_middle_disabled_has_fewer_sentences`, `test_middle_disabled_deterministic`, `test_middle_disabled_works_with_detail_three`, `test_middle_disabled_works_with_mood_and_bias`, `test_middle_disabled_works_with_json_format`, `test_middle_disabled_works_with_no_weather`, `test_middle_disabled_flag_exists_via_cli`
- Tests increased from 246 to 256 total (18 todo + 238 landscape)

## 2026-07-12

### What was done (Session 49)
- Changed **adjective from single-per-landscape to per-sentence-pair**: previously the same adjective was used for the opening and every middle sentence; now each sentence pair (and the opening) gets its own adjective pick
  - Opening still picks its own adjective once before the template
  - Inside the `detail` loop, a fresh adjective is picked for each middle+weather pair
  - Middle templates get the per-pair adjective instead of the opening's adjective
  - Follows the exact same pattern as the per-sentence-pair adverb change (Session 37)
- This is a **seed-breaking change**: existing seed-based output differs because the random call order changes (one extra `_pick` call per detail level). Determinism is preserved: the same seed still produces the same output.
- Per-sentence adjectives make detail=2 and detail=3 outputs richer by allowing different adjectival flavors across sentence pairs (e.g., "crystal" in the first pair, "ancient" in the second)
- Fixed `test_bias_common_increases_common_word_frequency` to count total occurrences instead of binary presence/absence — the old test had a ceiling effect flake (both counts near 300/300)
- Added 5 tests: `test_per_sentence_adj_uses_multiple_adjectives`, `test_per_sentence_adj_deterministic`, `test_per_sentence_adj_detail_three_has_more_adjective_variety`, `test_per_sentence_adj_respects_middle_disabled`, `test_per_sentence_adj_with_adverb_disabled`
- Tests increased from 256 to 261 total (18 todo + 243 landscape)

## 2026-07-12

### What was done (Session 50)
- **Refactored random state to use local `random.Random()` instances** — `generate_landscape()` no longer calls `random.seed()`, which modified the global `random` module state and could interfere with other code using `random` in the same process
  - `_pick()` and `_pick_template()` now accept an optional `rng` parameter (defaults to global `random` for backward compatibility)
  - `generate_landscape()` creates a local `rng = random.Random(seed)` when a seed is given, or `rng = random.Random()` (fresh, from `os.urandom`) when no seed is given
  - All random calls within the generation pipeline use the local `rng` instance: `rng.choice()`, `rng.choices()`, `rng.random()`, `rng.randint()`
- When `--show-seed` is used without `--seed`, the auto-generated seed now comes from a temporary `Random()` instance instead of the global state — functionally identical behavior
- Updated `test_count_without_seed_produces_varied_outputs` to call `generate_landscape()` directly without `random.seed()` pre-seeding (the old test relied on controlling global state, which no longer applies)
- This is a **seed-breaking change**: existing seed-based output differs because the internal RNG sequence changes (different `Random` implementation details). Determinism is preserved: the same seed still produces the same output.
- No new tests needed — existing 261 tests cover determinism, reproducibility, and output validity

### Current status
Working. All 261 tests pass (18 todo + 243 landscape).

## 2026-07-12

### What was done (Session 52)
- Added **`--bias-adverb` and `--bias-color` CLI flags** — the per-category bias override system (Session 16) had CLI flags for 6 categories (adjectives, elements, nouns, verbs, weathers, anomalies) but missed adverbs and colors. These two new flags complete coverage for all 8 word categories that `_pick()` supports.
- Added **`--mood-weight-adverb` and `--mood-weight-color` CLI flags** — same gap in the per-category mood-weight override system (Session 17): flags existed for 6 categories but not adverbs/colors. Now all 8 categories have per-category mood-weight CLI control.
- Added 8 new tests: `test_bias_adverb_override_rare_reduces_common_adverbs`, `test_bias_color_override_common_increases_common_colors`, `test_bias_overrides_multiple_with_new_categories`, `test_bias_overrides_produces_valid_output_adverb_color`, `test_mood_weight_adverb_override_high_boosts_mood_adverbs`, `test_mood_weight_color_override_zero_suppresses_mood_colors`, `test_mood_weight_overrides_multiple_with_new_categories`, `test_mood_weight_overrides_produces_valid_output_adverb_color`
- Tests increased from 274 to 282 total (18 todo + 264 landscape)

### What was done (Session 53)
- Added **`--no-color` CLI flag** and `color_enabled` parameter to `generate_landscape()` — users can now disable color word insertion in landscape descriptions
  - `color_enabled=True` (default) preserves existing behavior — a color word is picked per-sentence-pair and used in the `{color}` middle template
  - `color_enabled=False` skips the color pick entirely and passes an empty string to the template format call; `_format_tmpl` cleans up any double-space artifacts (same pattern as `adverb_enabled=False` from Session 34)
  - Follows the same pattern as `--no-adverb` (Session 34), `--no-weather` (Session 46), `--no-middle` (Session 48): automatic quality improvement made configurable
  - Fills the gap explicitly noted as a tradeoff in DECISIONS.md (Session 51): "A `--no-color` flag could be added later if needed (parallel to `--no-adverb`)"
- Added 8 tests in `TestColorFlag` class: `test_color_enabled_default_same_as_before`, `test_color_disabled_still_produces_valid_output`, `test_color_disabled_differs_from_enabled`, `test_color_disabled_deterministic`, `test_color_disabled_no_formatting_artifacts`, `test_color_disabled_flag_exists_via_cli`, `test_color_disabled_works_with_detail_three`, `test_color_disabled_works_with_mood_and_bias`
- Tests increased from 282 to 290 total (18 todo + 272 landscape)

### Current status
Working. All 290 tests pass (18 todo + 272 landscape).

## 2026-07-12

### What was done (Session 55)
- Added **"peaceful" mood** — the 4th mood overlay — to `MOOD_WORDS` in `landscape.py`, with curated word banks across all 8 categories:
  - 8 adjectives (calm, serene, gentle, tranquil, placid, lulling, sleepy, soft)
  - 6 elements (stillness, warmth, soft light, quiet, breeze, lullaby)
  - 6 nouns (glades, shallows, meadows, clearings, reflections, coves)
  - 6 verbs (rest, glide, settle, bloom, ripple, cradle)
  - 6 colors (pale, soft, gentle, mellow, warm, milky)
  - 6 adverbs (gently, softly, peacefully, calmly, tranquilly, serenely)
  - 4 weathers (soft breeze, warm sunlight, still air, light mist)
  - 4 anomalies (harmonious hum, world holds its breath, vivid colors, time like honey)
- Mood blends with existing moods: `--mood peaceful --mood eerie` creates gentle eeriness; `--mood peaceful --mood vibrant` creates luminous calm; `--mood peaceful --mood desolate` creates quiet desolation
- Follows the exact same pattern as the 3 existing moods — zero code changes to the generation pipeline (weighting, bias, dedup, templating all work automatically)
- Added 8 tests in `TestPeacefulMood` class: output validity, word weight boost, category-specific boost, cross-mood blending (3 combos), determinism, word appearance, JSON metadata, and CLI flag existence
- Updated `test_describe_all_contains_all_moods` and `test_describe_all_moods_flag_prints_multiple` to include "peaceful"
- Tests increased from 298 to 306 total (18 todo + 288 landscape)

### Current status
Working. All 306 tests pass (18 todo + 288 landscape).

## 2026-07-12

### What was done (Session 54)
- Added **`--no-anomaly` CLI flag** and `anomaly_enabled` parameter to `generate_landscape()` — users can now conveniently suppress anomaly descriptions alongside the existing `--no-weather`, `--no-middle`, `--no-color`, and `--no-adverb` flags
  - `anomaly_enabled=True` (default) preserves existing behavior
  - `anomaly_enabled=False` skips the entire anomaly generation block regardless of `anomaly_prob` and `anomaly_count` settings
  - Follows the same pattern as the other `--no-*` suppression flags: `--no-dedup` (Session 33), `--no-adverb` (Session 34), `--no-weather` (Session 46), `--no-middle` (Session 48), `--no-color` (Session 53)
  - Anomalies were the last major output component without a dedicated suppression flag; `--anomaly-prob 0` worked but was less discoverable
- Added 8 tests in `TestAnomalyFlag` class: `test_anomaly_enabled_default_same_as_before`, `test_anomaly_disabled_still_produces_valid_output`, `test_anomaly_disabled_differs_from_enabled`, `test_anomaly_disabled_deterministic`, `test_anomaly_disabled_suppresses_all_anomalies`, `test_anomaly_disabled_flag_exists_via_cli`, `test_anomaly_disabled_works_with_detail_three`, `test_anomaly_disabled_works_with_mood_and_bias`
- Tests increased from 290 to 298 total (18 todo + 280 landscape)

### Current status
Working. All 306 tests pass (18 todo + 288 landscape).

## 2026-07-12

### What was done (Session 56)
- Added **`{element}` to all 3 opening templates** and added a **4th poetic em-dash opening template** — the opening now references an element word (mist, light, echo, etc.) for richer, more vivid opening descriptions
  - Templates 0–2: `"... of {element} ..."` — "A vast crystal forest of mist stretches silently before you."
  - Template 3 (new): `"{Element} — the {adj} {display} stretches {adverb} before you."` — "Mist — the crystal forest stretches silently before you."
  - The element is picked once before the opening (like `adj` and `adverb`), consuming a dedup slot
  - `element` and `Element` kwargs are passed to the opening format call; templates that don't use one or the other silently ignore the extra kwarg
- Seed-breaking change: existing seed-based output differs because the random call order changes (one extra `_pick()` before the opening template)
- Added 5 tests: `test_opening_contains_known_element`, `test_opening_em_dash_template_appears_across_seeds`, `test_opening_element_is_deterministic`, `test_opening_element_works_with_detail_zero`, `test_opening_element_works_with_json_format`
- Updated `test_output_starts_with_valid_opening` and `test_template_variety_opening_patterns_differ_across_seeds` to accept em-dash openings
- Tests increased from 306 to 311 total (18 todo + 293 landscape)

### Current status
Working. All 311 tests pass (18 todo + 293 landscape).

## 2026-07-12

### What was done (Session 57)
- Added **`{element}` to weather templates** — the weather slot now references the per-sentence-pair element word, following the same pattern as Session 56 (element in openings) and making weather descriptions richer and more cohesive
  - Template 0: `"{Weather} {adverb} through the {element}."` — "A gentle rain falls softly through the mist."
  - Template 2: `"{Weather}, as if the {display} itself breathes {element} {adverb}."` — "A gentle rain falls, as if the forest itself breathes mist softly."
  - Template 3 (new): `"Through the {element}, {weather} {adverb}."` — "Through the mist, a gentle rain falls softly."
  - Template 1 (`"The air tells its own story: ..."`) is unchanged — no natural insertion point for element
- **Moved element pick outside the `middle_enabled` block** in the detail loop — element is now always picked per-sentence-pair (used by both middle and weather), even when middle sentences are suppressed via `--no-middle`. This is consistent with how the per-sentence-pair adverb is always picked for weather regardless of middle state (Session 37/48 tradeoff).
- `element=element` kwarg passed to weather `_format_tmpl()` call — unmodified templates silently ignore the extra kwarg
- Updated `test_template_variety_weather_has_varied_structure` to check for new "Through the " pattern and fixed the `has_as_if` check (now matches on " itself breathes " instead of " itself breathes.")
- Added 9 tests: element appearance in weather, "Through the" template statistical appearance, works with middle-disabled, determinism, detail=3, JSON format, template count, element placeholder assertion, works with no-adverb
- Tests increased from 311 to 320 total (18 todo + 302 landscape)

## 2026-07-12

### What was done (Session 58)
- Added **`{color}` to weather templates** — the weather slot now references the per-sentence-pair color word, making weather descriptions richer and more cohesive with the landscape's color palette
  - Template 4 (new): `"{Weather} {adverb} in {color} light."` — "A gentle rain falls softly in vivid light."
  - Existing `Weather=weather.capitalize()`, `weather=weather`, `display=display`, `adverb=adverb`, `element=element` kwargs are unchanged
  - `color=color` kwarg passed to weather `_format_tmpl()` call — unmodified templates silently ignore the extra kwarg
- **`color` variable initialized to `""` before the `if middle_enabled:` block** in the detail loop — ensures color is always defined for weather templates even when middle sentences are suppressed. When `middle_enabled=True` and `color_enabled=True`, the picked color word is used; otherwise color stays `""` and `_format_tmpl` cleans up the resulting `" in  light."` → `" in light."` (reads naturally without the color).
- No seed-breaking change: the random sequence is unchanged when `middle_enabled=True` (color is picked at the same position). When `middle_enabled=False`, `color=""` adds no random calls.
- Added 9 tests: color appearance in weather, "in {color} light" template statistical appearance, works with middle-disabled, determinism, detail=3, JSON format, template count, color placeholder assertion, works with no-adverb
- Tests increased from 320 to 329 total (18 todo + 311 landscape)

### Current status
Working. All 329 tests pass (18 todo + 311 landscape).

## 2026-07-12

### What was done (Session 59)
- Added **`{color}` to opening templates 0, 1, and 2** — the opening slot now references a color word (picked from the `colors` category before the opening), making opening descriptions more visually evocative
  - Template 0: `"A vast {adj} {display} of {color} {element} stretches {adverb} before you."` — "A vast crystal forest of vivid mist stretches silently before you."
  - Template 1: `"Before you, a {adj} {display} of {color} {element} comes into view {adverb}."`
  - Template 2: `"The {adj} {display} of {color} {element} lies {adverb} ahead."`
  - Template 3 (em-dash) is unchanged — no natural insertion point for color
- Color is picked before the opening template (if `color_enabled`) in the same block as `adj`, `element`, and `adverb` — a second color pick per sentence pair still happens inside the detail loop for middle/weather templates
- When `color_enabled=False`, `color=""` is passed and `_format_tmpl` collapses the resulting `"of  "` → `"of "` (reads naturally without the color word)
- Seed-breaking change: existing seed-based output differs because the random call order changes (one extra `_pick()` before the opening template). Determinism is preserved.
- Added 4 tests: `test_opening_contains_known_color`, `test_opening_color_works_with_color_disabled`, `test_opening_color_is_deterministic`, `test_opening_color_appears_in_opening_templates`
- Tests increased from 329 to 333 total (18 todo + 315 landscape)

### Current status
Working. All 333 tests pass (18 todo + 315 landscape).

## 2026-07-12

### What was done (Session 60)
- Added **`{color}` to middle templates 1, 2, 4, and 5** — the middle sentence slot now references the per-sentence-pair color word in more templates, making middle descriptions richer:
  - Template 1: `"Among the {adj} {noun}, {color} {element} {verb_conjugated} {adverb}."` — "Among the crystal trees, vivid mist whispers softly."
  - Template 2: `"The {adj} {noun} {verb} {adverb} with {color} {element}."` — "The crystal trees whisper softly with vivid mist."
  - Template 4: `"Beneath the {adj} {noun}, {color} {element} {verb_conjugated} {adverb}."` — "Beneath the crystal trees, vivid mist whispers softly."
  - Template 5: `"Across the {display}, {color} {element} {verb_conjugated} {adverb}."` — "Across the forest, vivid mist whispers softly."
  - Templates 0 and 3 unchanged (sentence-initial `{Element}` would produce leading-space artifacts when color is disabled — same reason Session 59 skipped the em-dash opening template)
- Template-level change only — `color=color` was already passed to the middle format call (since Session 51), `_format_tmpl` handles disabled-color cleanup of `",  "` → `", "` naturally
- Updated `test_color_light_template_exists_in_pool` to expect ≥5 `{color}` templates (was 1)
- Added 4 tests: `test_color_in_middle_templates`, `test_color_middle_works_with_color_disabled`, `test_color_middle_is_deterministic`, `test_color_middle_works_with_no_adverb`
- Tests increased from 333 to 337 total (18 todo + 319 landscape)

## 2026-07-12

### What was done (Session 61)
- Added **`{adverb}` to anomaly framing templates (indices 2 and 3)** — the anomaly slot now uses the per-sentence-pair adverb word, making anomaly descriptions feel more integrated with the landscape's adverbial flavor:
  - Template 2: `"A strange detail catches your eye {adverb}: {anomaly_lower}"` — "A strange detail catches your eye softly: the gravity here feels wrong."
  - Template 3: `"There is a quiet wrongness here {adverb}: {anomaly_lower}"` — "There is a quiet wrongness here silently: the horizon curves upward."
  - Templates 0 and 1 unchanged (no natural insertion point)
  - Adverb kwarg was already passed to anomaly format calls (line 661), so this is a template-level change only
- Added **`{color}` to middle templates 0 and 3** — the last two middle templates that didn't use the per-sentence-pair color word. Now all 7 middle templates use `{color}`:
  - Template 0: `"{Element} {verb_conjugated} {adverb} between the {color} {adj} {noun}."` — "Mist whispers softly between the vivid crystal trees." (was `"...between the {adj} {noun}."`)
  - Template 3: `"{Element} {verb_conjugated} {adverb} through the {color} {adj} {noun}."` — "Mist whispers softly through the vivid crystal trees." (was `"...through the {adj} {noun}."`)
  - `{color}` placed before `{adj}` creates a natural adjective stack ("vivid crystal") — no leading-space artifacts when `color_enabled=False` because `_format_tmpl` collapses `"the  crystal"` → `"the crystal"`
- Improved **`_format_tmpl()`** to clean up space-before-colon artifacts: added `.replace(" :", ":")` to the sanitization chain — a general quality improvement that prevents `"eye  :"` → `"eye :"` from appearing when `adverb_enabled=False`
- Updated 2 existing tests: `test_template_variety_anomaly_has_varied_structure` and `test_anomaly_colon_template_lowercases` — the detection strings no longer assume a colon immediately follows "your eye"/"here" since the adverb now sits between them
- Added 11 tests: `TestAnomalyAdverb` class (8 tests: placeholder presence, output validity, adverb appearance, determinism, no-adverb composition, mood+bias composition, detail=3, JSON format) + `test_color_in_all_middle_templates`, `test_color_middle_template_zero_and_three_have_color`, `test_color_middle_zero_and_three_produce_valid_output`
- Tests increased from 337 to 348 total (18 todo + 330 landscape)

## 2026-07-12

### What was done (Session 62)
- Added **biome-specific color and adverb word pools** to `BIOME_WORDS` — each of the 13 biomes now has its own curated list of 3-4 colors and 3-4 adverbs, making each biome feel more distinctive in its color palette and adverbial flavor
  - Previously, `_pick("colors", ...)` and `_pick("adverbs", ...)` fell back entirely to global pools — every biome shared the same colors and adverbs
  - Now, colors and adverbs are blended the same way as other categories: biome-specific words are concatenated with the global pool, so biomes get thematic flavor without losing global variety
  - Example: forest gets "emerald"/"deep green"/"golden"/"dappled" colors and "softly"/"gently"/"peacefully" adverbs; desert gets "amber"/"golden"/"pale"/"crimson" and "relentlessly"/"harshly"/"patiently"; volcanic field gets "obsidian black"/"crimson"/"molten orange"/"ash-grey" and "violently"/"harshly"/"relentlessly"
- Updated `describe_biome()` to include `"colors"` and `"adverbs"` in its category listing — users inspecting biome word banks via `--describe-biome` now see the new categories
- No code changes to `_pick()` — it already looked up `BIOME_WORDS[biome]["colors"]` and `BIOME_WORDS[biome]["adverbs"]` via the generic `BIOME_WORDS.get(b, {}).get(category, [])` pattern, it just returned empty lists before because the entries didn't exist
- Added 12 tests in `TestBiomeColorsAndAdverbs` class: structural tests (all biomes have non-empty colors/adverbs), statistical tests (biome-specific colors/adverbs appear in output), validity tests (works with combine, color_disabled, determinism, mood+bias, detail levels), and describe_biome inclusion
- Tests increased from 348 to 360 total (18 todo + 342 landscape)

### Current status
Working. All 360 tests pass (18 todo + 342 landscape).

## 2026-07-12

### What was done (Session 63)
- Added **`"fourth"` and `"fifth"` template set modes** to `TEMPLATE_SETS` — users can now force index 3 and index 4 templates via `--template-set fourth` or `--template-set fifth`
  - `"fourth"` maps to index 3: opens the em-dash opening template (`"{Element} — the {adj} {display}..."`), the 4th middle template (`"{Element} {verb_conjugated} {adverb} through the {color} {adj} {noun}."`), the 4th weather template (`"Through the {element}, {weather} {adverb}."`), and the 4th anomaly template (`"There is a quiet wrongness here {adverb}: {anomaly_lower}"`)
  - `"fifth"` maps to index 4: opens the 5th middle template (`"Beneath the {adj} {noun}, {color} {element} {verb_conjugated} {adverb}."`) and the 5th weather template (`"{Weather} {adverb} in {color} light."`); clamps to the last template for slots with ≤4 templates (opening, anomaly)
  - `_pick_template()` handles out-of-range indices via its existing `min(idx, len(templates) - 1)` clamping — no overflow crashes
- Added 7 tests: `test_pick_template_selects_correct_fourth_index`, `test_pick_template_selects_correct_fifth_index`, `test_template_set_fourth_uses_fourth_opening`, `test_template_set_fifth_uses_fifth_opening`, `test_template_set_fourth_is_deterministic`, `test_template_set_fifth_is_deterministic`, `test_template_set_fourth_fifth_produce_valid_output`
- Tests increased from 360 to 367 total (18 todo + 349 landscape)

### Current status
Working. All 367 tests pass (18 todo + 349 landscape).

## 2026-07-12

### What was done (Session 64)
- Added **`"sixth"` and `"seventh"` template set modes** to `TEMPLATE_SETS` — completing coverage for all 7 middle templates and 5 weather templates
  - `"sixth"` maps to index 5: opens middle template 5 (`"Across the {display}, {color} {element} {verb_conjugated} {adverb}."`); opening/weather/anomaly clamp to max index (3/4/3)
  - `"seventh"` maps to index 6: opens middle template 6 (`"The {color} light of {element} {verb_conjugated} {adverb}."`); opening/weather/anomaly clamp to max index
  - Backward compatible — existing `--template-set first` through `--fifth` choices are unchanged
- Added **`--describe-templates` CLI flag** and `describe_templates()` function — users can now inspect all available sentence templates per slot (opening, middle, weather, anomaly) with index numbers, without reading the source code
  - Pure function returns a string with all template strings grouped by slot, annotated with count and index
  - Similar pattern to `describe_biome()`, `describe_mood()`, and `describe_global()` — introspection without landscape generation
  - CLI exits immediately after printing — no landscape generation occurs when `--describe-templates` is used
- Updated `--template-set` help text to list all 8 modes (random + first–seventh)
- Added 7 template set tests and 10 describe_templates tests
- Tests increased from 367 to 384 total (18 todo + 366 landscape)

### What was done (Session 65)
- Fixed `describe_mood()` to include `"colors"` in its category listing — when Session 62 added colors and adverbs to biome word banks, `describe_biome()` was updated to list both new categories, but `describe_mood()` was not similarly updated, so mood introspection silently omitted color words
- Updated `test_describe_known_mood_contains_categories` to assert on `"colors:"` presence (was missing from the test assertion list)
- One-line fix in `describe_mood()`: added `"colors"` to the category iteration list
- Tests: still 384 total (18 todo + 366 landscape) — assertion updated in existing test

### Current status
Working. All 384 tests pass (18 todo + 366 landscape).

## 2026-07-12

### What was done (Session 66)
- Fixed **`ALL_ADVERBS` and `ALL_COLORS` test sets** — when Session 62 added biome-specific color and adverb word pools to `BIOME_WORDS`, the test module's `ALL_ADVERBS` and `ALL_COLORS` sets were not updated to include biome-specific words. Unlike all other `ALL_*` sets (adjectives, elements, nouns, verbs, weathers, anomalies), which include biome-specific words via `{w for bw in BIOME_WORDS.values() for w in bw.get("cat", [])}`, adverbs and colors only contained the global pool. This meant tests checking for adverb/color presence in output (e.g. `test_output_contains_known_adverb`, `test_color_in_middle_templates`) could miss biome-specific words.
- Updated `ALL_ADVERBS` and `ALL_COLORS` definitions to include biome-specific words — consistent with the other 6 `ALL_*` sets.
- Fixed `test_describe_global_includes_colors` to assert against `COLORS` (global pool) instead of `ALL_COLORS` (global + biome-specific) — biome-specific colors are correctly not listed by `describe_global()`, which only shows global word pools.
- Tests increased from 366 to 366 (unchanged — this was a test data fix, not a new feature).

### Current status
Working. All 384 tests pass (18 todo + 366 landscape).

## 2026-07-13

### What was done (Session 67)
- Added **`{color}` to anomaly templates** — color words now appear in anomaly descriptions, closing the last template slot gap (color was used in openings, middle, and weather but not anomalies)
  - Modified template 2: `"A strange {color} detail catches your eye {adverb}: {anomaly_lower}"` — color word naturally modifies "detail" (e.g. "A strange vivid detail catches your eye softly: the gravity here feels wrong.")
  - Added template 4 (new): `"In the {color} light, {anomaly_lower}"` — frames the anomaly in the landscape's light palette (e.g. "In the vivid light, the gravity here feels wrong.")
- Added `color=color` kwarg to the anomaly `_format_tmpl()` call — color was already in scope (last per-sentence-pair color) but was not passed to anomaly templates
- When `color_enabled=False`, `_format_tmpl` handles the empty-string artifacts (`"In the  light,"` → `"In the light,"` and `"A strange  detail"` → `"A strange detail"`)
- Updated 3 existing tests to use new detection strings (anomaly template 2 now has a color word between "strange" and "detail")
- Added 9 tests in `TestAnomalyColor` class: placeholder count, output validity, color appearance, determinism, color-disabled formatting, mood+bias composition, detail=3, JSON format, and "In the {color} light" template statistical appearance
- Tests increased from 384 to 393 total (18 todo + 375 landscape)

### Current status
Working. All 393 tests pass (18 todo + 375 landscape).

## 2026-07-13

### What was done (Session 69)
- Added **`{adj}` to weather templates 0, 1, 2, and 3** — the per-sentence-pair adjective now appears in weather descriptions, making weather sentences richer and more cohesive with the landscape's adjectival palette:
  - Template 0: `"{Weather} {adverb} through the {adj} {element}."` — "A gentle rain falls softly through the crystal mist."
  - Template 1: `"The air tells its own story: {weather} {adverb} through the {adj} {element}."`
  - Template 2: `"{Weather}, as if the {adj} {display} itself breathes {element} {adverb}."` — "A gentle rain falls, as if the crystal forest itself breathes mist softly."
  - Template 3: `"Through the {adj} {element}, {weather} {adverb}."` — "Through the crystal mist, a gentle rain falls softly."
  - Template 4 unchanged (uses `{color}` but no natural adj insertion point)
- **Moved adj pick outside `if middle_enabled:` block** — the per-sentence-pair adjective is now always picked in the detail loop (like `element`), so it's available for weather templates regardless of middle sentence state. When `middle_enabled=False`, one extra `_pick()` per iteration provides the adjective for weather descriptions.
- Template-level change to 4 weather templates plus one code change (moved adj pick) and one kwarg addition (`adj=adj` to weather format call)
- RNG-preserving for `middle_enabled=True` (adj is picked in the same position relative to element/noun/verb as before). Seed-breaking for `middle_enabled=False` (one extra `_pick()` per iteration).
- Added 9 tests in `TestWeatherAdj` class: placeholder presence, output validity, adjective appearance, determinism, middle-disabled compatibility, adverb-disabled formatting, JSON format, detail=3, and mood+bias composition
- Tests increased from 384 to 393 total (18 todo + 375 landscape)

### Current status
Working. All 393 tests pass (18 todo + 375 landscape).

## 2026-07-13

### What was done (Session 68)
- Added **`{element}` to weather template 1** — changed `"The air tells its own story: {weather} {adverb}."` to `"The air tells its own story: {weather} {adverb} through the {element}."` (e.g. "The air tells its own story: a gentle rain falls softly through the mist.")
- Weather template 1 was the only weather template that didn't reference `{element}` — templates 0, 2, and 3 already had it, and template 4 uses `{color}`. This change makes all 5 weather templates use at least one injected word category.
- Template-level change only — `element=element` kwarg was already passed to all weather format calls (since Session 57)
- No new tests needed — existing template and output tests cover the change
- Tests: still 393 total (18 todo + 375 landscape)

## 2026-07-13

### What was done (Session 70)
- Fixed **`test_describe_global_contains_all_categories`** — the test was checking that `describe_global()` includes all 8 global word categories, but the test's category list was missing `"colors"`. This was a test data gap left when the `COLORS` word bank was added (Session 51): the category was correctly listed in the `describe_global()` output, but the corresponding test assertion never added `"colors"` to its expected category list.
- The fix is a one-word addition: `"colors"` added to the expected-categories list in the `for` loop. The previously separate `test_describe_global_includes_colors` in `TestColors` covered the behavioral assertion, but `TestDescribeGlobal.test_describe_global_contains_all_categories` now also correctly enumerates colors as one of the global categories.
- Tests: still 393 total (18 todo + 375 landscape) — updated assertion in existing test.

## 2026-07-13

### What was done (Session 71)
- Added **`{display}` to anomaly template 4** — changed `"In the {color} light, {anomaly_lower}"` to `"In the {color} light of the {display}, {anomaly_lower}"` (e.g. "In the vivid light of the forest, the gravity here feels wrong.")
- Added `display=display` kwarg to the anomaly `_format_tmpl()` call — `display` was in scope but not passed to anomaly templates, so the placeholder would have rendered as literal `{display}` text
- Previously, only middle and weather templates referenced the biome name; now the anomaly slot can also anchor its description in the biome context
- No new tests — existing anomaly template and output tests cover the change (template 4 still renders with `{color}`, still matches the `"In the " ... " light"` pattern in `test_anomaly_color_in_light_template_appears`)

### Current status
Working. All 393 tests pass (18 todo + 375 landscape).

## 2026-07-13

### What was done (Session 73)
- Added **`{adj}` to anomaly template 4** — changed `"In the {color} light of the {display}, {anomaly_lower}"` to `"In the {color} {adj} light of the {display}, {anomaly_lower}"` (e.g. "In the vivid crystal light of the forest, the gravity here feels wrong.")
- Added `adj=adj` kwarg to the anomaly `_format_tmpl()` call — `adj` was already in scope (last per-sentence-pair adjective) but was not passed to anomaly templates, so the placeholder would have rendered as literal `{adj}` text
- Anomaly template 4 was the last template in any slot that didn't reference `{adj}` — now all 20 templates (4 opening, 7 middle, 5 weather, 5 anomaly) that support word-category injection use `{adj}` where grammatically natural
- Template-level change plus one kwarg addition — follows the same pattern as every previous template enrichment (Sessions 38–42, 47, 56–61, 67–69, 72): add a kwarg that existing templates silently ignore, update one template to use it
- No seed-breaking change: no new `_pick()` calls, only the template string and format kwarg changed
- Added 4 tests in `TestAnomalyAdj` class: placeholder presence, output validity, adjective appearance in anomaly output, determinism
- Tests increased from 393 to 397 total (18 todo + 379 landscape)

### Current status
Working. All 397 tests pass (18 todo + 379 landscape).

## 2026-07-13

### What was done (Session 72)
- Added **`{adj}` to weather template 4** — changed `"{Weather} {adverb} in {color} light."` to `"{Weather} {adverb} in {color} {adj} light."` (e.g. "A gentle rain falls softly in vivid crystal light.")
- Weather template 4 was the only weather template that didn't use `{adj}` — templates 0–3 received it in Session 69, leaving template 4 (`"in {color} light"`) as the last template without the per-sentence adjective
- Template-level change only — `adj=adj` was already passed to the weather format call (since Session 69), so no code changes were needed
- Now all 5 weather templates use `{adj}` — complete adjective coverage across the weather slot
- No seed-breaking change: the random call order is unchanged (no new `_pick()` calls), only the template string changed
- No new tests needed (existing `test_weather_templates_use_adj_placeholder` checks `>= 4`, passes with 5/5)
- Tests: still 393 total (18 todo + 375 landscape)

### Current status
Working. All 393 tests pass (18 todo + 375 landscape).

## 2026-07-13

### What was done (Session 74)
- Added **`{color}` to the em-dash opening template (index 3)** — changed `"{Element} — the {adj} {display} stretches {adverb} before you."` to `"{Element} — the {adj} {display} of {color} light stretches {adverb} before you."` (e.g. "Echo — the rusted ruined city of faded light stretches softly before you.")
- The em-dash opening template was the last opening template (and one of the last templates overall) without a color reference — templates 0–2 use `"of {color} {element}"`, but template 3 had no color at all. Using `"of {color} light"` avoids duplicating `{element}` (which already appears sentence-initially as `{Element}`) while keeping the visual richness.
- Template-level change only — `color=color` was already passed to the opening format call (since Session 59), so no code changes were needed
- When `color_enabled=False`, `_format_tmpl` collapses `"of  light"` → `"of light"` — reads naturally without the color word
- Added 3 tests: `test_opening_em_dash_color_contains_color` (statistical — color appears in 300 seeds), `test_opening_em_dash_color_deterministic` (same seed = same output), and `test_opening_em_dash_color_works_with_color_disabled` (no formatting artifacts)
- Tests increased from 397 to 400 total (18 todo + 382 landscape)

### Current status
Working. All 400 tests pass (18 todo + 382 landscape).

## 2026-07-13

### What was done (Session 75)
- Added **`{display}` to anomaly template 1** — changed `"Something is not right — {anomaly}"` to `"Something is not right with the {display} — {anomaly}"` (e.g. "Something is not right with the forest — The gravity here feels wrong.") — grounds the anomaly framing in the biome context
- Anomaly template 1 was one of only two templates (alongside template 0) that didn't reference any injected word category. Adding `{display}` makes it feel connected to the landscape without adding clutter.
- Template-level change only — `display=display` kwarg was already passed to anomaly format calls (since Session 71/73)
- No seed-breaking change: no new `_pick()` calls, only the template string changed
- No new tests — existing anomaly template and output tests cover the change

### Current status
Working. All 414 tests pass (18 todo + 396 landscape).

## 2026-07-13

### What was done (Session 78)
- Added **`--echo` CLI flag** and `echo_enabled` parameter to `generate_landscape()` — users can now append a short atmospheric "echo" phrase to the end of the landscape description, adding a sense of deep time and experiential presence
  - 10 curated echo phrases: "The land remembers.", "This place has been waiting for you.", "Nothing here has changed in a thousand years.", "The echoes of the past linger in the air.", etc.
  - Echo is picked via `rng.choice(ECHOES)` — no dedup slot consumed, independent of all word categories
  - Only fires when `detail >= 1` and `echo_enabled=True` (default: False)
  - Works with all formats (prose, poetic, json)
  - No seed-breaking change for existing outputs (echo_enabled=False by default)
- Added 8 tests in `TestEcho` class: disabled by default, echo appears when enabled, output validity, determinism, poetic format, JSON format, detail=0 suppression, CLI flag existence
- Tests increased from 414 to 422 total (18 todo + 404 landscape)

### What was done (Session 79)
- Added **`--echo-count` CLI flag** and `echo_count` parameter to `generate_landscape()` — users can now control how many echo phrases appear per landscape (0–3, default: 1)
  - `--echo-count 0` suppresses echoes (alternative to not using `--echo`)
  - `--echo-count 2` or `--echo-count 3` generates multiple echoes, each independently picked from the pool
  - Added **echo dedup**: the same phrase will not appear twice in a single landscape, even with `echo_count > 1`
  - When `echo_count > len(ECHOES)`, falls back to the full pool (repeats allowed) — prevents crashes from exhausted pools
  - Follows the same pattern as `--anomaly-count` (Session 29) for multi-instance generation
  - Included in JSON metadata as `echo_count` when `echo_enabled=True`
- Refactored echo block from single `rng.choice(ECHOES)` to a loop with `used_echoes` set — dedup is internal to the echo system (not shared with the `used_words` set from `_pick()`) since echoes are not part of the word-category system
- Added 12 tests in `TestEchoCount` class: default is 1, zero suppression, multi-echo appearance, dedup across repetitions, validity at all counts, determinism, JSON text output, JSON metadata field, CLI flag existence, and pool-exhaustion fallback
- Tests increased from 422 to 433 total (18 todo + 415 landscape)

## 2026-07-13

### What was done (Session 77)
- Added **`{color}` to all 4 remaining weather templates** — weather templates 0, 1, 2, and 3 now reference the per-sentence-pair color word, completing color coverage across all 5 weather templates
  - Template 0: `"{Weather} {adverb} through the {color} {adj} {element}."` — "A gentle rain falls softly through the vivid crystal mist."
  - Template 1: `"The air tells its own story: {weather} {adverb} through the {color} {adj} {element}."`
  - Template 2: `"{Weather}, as if the {adj} {display} itself breathes {color} {element} {adverb}."` — "... itself breathes vivid mist softly."
  - Template 3: `"Through the {color} {adj} {element}, {weather} {adverb}."` — "Through the vivid crystal mist, a gentle rain falls softly."
- Template-level change only — `color=color` was already passed to the weather format call (since Session 58), so no code changes were needed
- Updated `test_weather_color_templates_use_color_placeholder` from `>= 1` to `>= 5`
- Added `test_weather_color_in_all_templates` — explicitly asserts every weather template contains `{color}`
- Tests increased from 404 to 414 total (18 todo + 396 landscape)

## 2026-07-13

### What was done (Session 76)
- Added **`{element}` to anomaly template 2** — changed `"A strange {color} detail catches your eye {adverb}: {anomaly_lower}"` to `"A strange {color} detail catches your eye {adverb} through the {element}: {anomaly_lower}"` (e.g. "A strange vivid detail catches your eye softly through the mist: the gravity here feels wrong.") — grounds anomaly descriptions in the landscape's elemental vocabulary
- Added `element=element` kwarg to the anomaly `_format_tmpl()` call — `element` was already in scope (last per-sentence-pair element) but was not passed to anomaly templates, so the placeholder would have rendered as literal `{element}` text
- `{element}` was the last word category completely missing from the anomaly slot — openings, middle, and weather all used it, but no anomaly template referenced it. This change closes the last category gap in anomaly templates.
- Added 4 tests in `TestAnomalyElement` class: template placeholder presence, output validity, element word appearance in anomaly output, determinism
- Tests increased from 400 to 404 total (18 todo + 386 landscape)
