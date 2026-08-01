# Audio course vs. source document — audit report

- **Source:** `original.pdf` — corrected transcription supplied via --source-text (source_corrected.txt)
- **Course:** 4 lessons, 8.5 min of audio
- **Audio transcribed with:** faster-whisper `medium.en` on `cpu/int8` (beam 5, VAD off). Wording below is the transcript, not the authoring text — some oddities are speech-recognition artifacts, and are labelled as such where identifiable.

## 1. Headline numbers

| Measure | Value |
| --- | --- |
| Source statements identified | 30 |
| Fully carried into the audio | 15 (50%) |
| Carried but with detail dropped | 7 (23%) |
| Absent from the audio | 8 (27%) |
| **Content coverage (full + partial)** | **73%** |
| Source length | 349 words |
| Course length | 1177 words |
| Expansion ratio | 3.4x |
| Narrated sentences | 75 (28 teaching scaffold, 47 content) |
| Content sentences with no close source match | 15 |
| Sentences naming something absent from the source | 7 |
| Near-duplicate statement pairs across lessons | 0 |

## 2. Does the audio carry all the context?

**No — 8 statement(s) from the letter never appear in any lesson.**

| # | Missing from the course | Closest thing the audio says |
| --- | --- | --- |
| 0 | 57 Petersham Road Feb. 23, '40. | _The author mentions a person named Newton, who has been away ill, but will be seen on Mond…_ (sim 0.20) |
| 1 | Yours of Feb. 18 to hand this A.M. | _We are so near to the end._ (sim 0.29) |
| 6 | which will be very useful for your vieuz jours (and mine, if I can ever get out there!) I want very much to go over and devlop these. | _Both Smith and Mosses have acquired properties there, which will be very useful for visits…_ (sim 0.22) |
| 15 | I'm in trouble here. | _He writes, I'm worried about the tarot._ (sim 0.24) |
| 18 | Normally, though, I'm quite o.k. personally. | _He says that plainly, it's the biggest work of my whole life._ (sim 0.25) |
| 22 | I shall probably have to be content with a one-page war poem for March 21. | _This session draws on a letter written by Aleister Crowley._ (sim 0.35) |
| 24 | Sorry if this letter seems gloomy. | _Second, the letter shows how connections are used to achieve goals. The author mentions a …_ (sim 0.35) |
| 25 | But I have been rather sick, and still don't feel too gay. | _He even wondered if his worry was simply due to feeling unwell._ (sim 0.28) |

### Carried, but with specifics dropped (7)

| Source statement | What went missing | Where it landed |
| --- | --- | --- |
| Re partners. | — | 02 - Partnerships and Confidentiality |
| But I think all payments to G.M.C. should be credited to your O.T.O. interests esp. in California where both Smith and Mas S. have acquired-properties | `GMC` | 04 - Ambition Conquering Hollywood |
| But they look very promising.) | — | 02 - Partnerships and Confidentiality |
| I see him Monday, I hope. | — | 04 - Ambition Conquering Hollywood |
| So if I can talk him into it, you might be able to explain your proposition to the man on the spot, and start immediately. | — | 04 - Ambition Conquering Hollywood |
| My Trust Fund has got cold feet, so that I can't count on my weekly £2. | `2` | 01 - Foundations Financial Instability |
| I had to put your cheque through in consequence. | — | 01 - Foundations Financial Instability |

## 3. Did the AI invent anything?

### Narrated content with no close match in the source (15)

| Lesson | Sentence | Similarity to nearest source statement |
| --- | --- | --- |
| 01 - Foundations Financial Instability | This meant he could no longer rely on a steady income from that source. | 0.34 |
| 01 - Foundations Financial Instability | These factors combine to create a foundation of financial uncertainty during this period. | 0.26 |
| 02 - Partnerships and Confidentiality | The author then ties this to current OTO interests, particularly in California. | 0.35 |
| 02 - Partnerships and Confidentiality | The author expresses a strong desire to go over and develop these properties. | 0.29 |
| 02 - Partnerships and Confidentiality | With the goal of revitalizing the organization through the author's own efforts and connections, | 0.35 |
| 03 - The Tarot Crowley's Magnum Opus | Yet he was deeply worried about its completion. | 0.30 |
| 03 - The Tarot Crowley's Magnum Opus | He feared that some last minute obstacle, some trick, would prevent the work from being finished. | 0.24 |
| 03 - The Tarot Crowley's Magnum Opus | He even wondered if his worry was simply due to feeling unwell. | 0.31 |
| 03 - The Tarot Crowley's Magnum Opus | But the anxiety was real. | 0.23 |
| 03 - The Tarot Crowley's Magnum Opus | So two concrete needs, a new set of clothes to present himself properly, and a printer to produce the actual deck or book. | 0.37 |
| 04 - Ambition Conquering Hollywood | This is the core of the plan, using his personal charisma and existing network in the creative industries to establish the O.T.O. | 0.28 |
| 04 - Ambition Conquering Hollywood | This illustrates a strategic use of a personal contact to gain access to financial backing. | 0.31 |
| 04 - Ambition Conquering Hollywood | Plan. | 0.27 |
| 04 - Ambition Conquering Hollywood | Funding for it enables the author to act. | 0.31 |
| 04 - Ambition Conquering Hollywood | It also depends on using specific contacts like Newton to reach capitalists and the tarot par major life work, financially interwoven with those O.T.O. ambitions requiring even small contributions to keep both projects moving forward. | 0.38 |

### Names and numbers spoken that are not in the letter (7)

| Lesson | Not in source | Sentence |
| --- | --- | --- |
| 01 - Foundations Financial Instability | `FEBRUARY`, `1940` | The source material comes from a letter dated 23rd February 1940, where he discusses his financial troubles and their impact on his Tarot project. |
| 02 - Partnerships and Confidentiality | `FEBRUARY`, `1940` | This lesson is about partnerships and confidentiality, drawn from a letter written in February 1940. |
| 02 - Partnerships and Confidentiality | `MOSSES` | Both Smith and Mosses have acquired properties there, which will be very useful for visits. |
| 02 - Partnerships and Confidentiality | `MOSSES` | At the same time, the author highlights that in California, partners Smith and Mosses have acquired OTO properties that are intended for visits and development. |
| 03 - The Tarot Crowley's Magnum Opus | `ALEISTER`, `CROWLEY` | This session draws on a letter written by Aleister Crowley. |
| 03 - The Tarot Crowley's Magnum Opus | `CROWLEY` | To recap, the tarot was Crowley's magnum opus, the biggest work of his life. |
| 04 - Ambition Conquering Hollywood | `GMR` | Furthermore, he instructs that all payments to G.M.R. should be credited to your O.T.O. interests, especially in California, tying financial support directly to the O.T.O. expansion. |

_Fuzzy matching is applied before flagging, so mangled-but-recognisable names are not listed here. What remains is either genuinely new information or a transcription error severe enough to change the word._

## 4. Duplication and redundancy

7 of 30 source statements are taught in more than one lesson (23%).

| Source statement | Repeated in |
| --- | --- |
| But in order to push the Tarot I shall have to renew my wardrobe, at least one suit, amd some underclothes. | 01 - Foundations Financial Instability, 03 - The Tarot Crowley's Magnum Opus, 04 - Ambition Conquering Hollywood |
| As soon as I can do so, I can put the O.T.O. really on its feet again | 02 - Partnerships and Confidentiality, 04 - Ambition Conquering Hollywood |
| for my presence and personality and literary & dramatic connexions should enable me to conquer Hollywood. | 02 - Partnerships and Confidentiality, 04 - Ambition Conquering Hollywood |
| This will cost about £30. | 01 - Foundations Financial Instability, 03 - The Tarot Crowley's Magnum Opus |
| Then, of course, the printer. | 01 - Foundations Financial Instability, 03 - The Tarot Crowley's Magnum Opus |
| But please remember that even the smallest cheque makes all the difference between staying idle and dashing about to put business through. | 01 - Foundations Financial Instability, 04 - Ambition Conquering Hollywood |
| and it's the biggest work of my whole life | 01 - Foundations Financial Instability, 03 - The Tarot Crowley's Magnum Opus |

## 5. Is it teachable?

| Lesson | Minutes | Words | Sentences | Scaffold | Source statements touched | Direct quotes |
| --- | --- | --- | --- | --- | --- | --- |
| 01 - Foundations Financial Instability | 2.0 | 290 | 18 | 11 | 6 | 5 |
| 02 - Partnerships and Confidentiality | 1.7 | 228 | 14 | 5 | 5 | 0 |
| 03 - The Tarot Crowley's Magnum Opus | 1.9 | 268 | 22 | 6 | 7 | 3 |
| 04 - Ambition Conquering Hollywood | 2.9 | 391 | 21 | 6 | 7 | 1 |

---

<details><summary>Source statements as parsed</summary>

- [ ] `00` 57 Petersham Road Feb. 23, '40.
- [ ] `01` Yours of Feb. 18 to hand this A.M.
- [~] `02` Re partners.
- [x] `03` Most important never to divulge your business.
- [x] `04` They never understand.
- [~] `05` But I think all payments to G.M.C. should be credited to your O.T.O. interests esp. in California where both Smith and Mas S. have acquired-properties
- [ ] `06` which will be very useful for your vieuz jours (and mine, if I can ever get out there!) I want very much to go over and devlop these.
- [x] `07` As soon as I can do so, I can put the O.T.O. really on its feet again
- [x] `08` for my presence and personality and literary & dramatic connexions should enable me to conquer Hollywood.
- [x] `09` (I can't send photos of the properties because of the censor.
- [~] `10` But they look very promising.)
- [x] `11` Newton has been away ill.
- [~] `12` I see him Monday, I hope.
- [x] `13` He has capitalists in Belgium.
- [~] `14` So if I can talk him into it, you might be able to explain your proposition to the man on the spot, and start immediately.
- [ ] `15` I'm in trouble here.
- [~] `16` My Trust Fund has got cold feet, so that I can't count on my weekly £2.
- [~] `17` I had to put your cheque through in consequence.
- [ ] `18` Normally, though, I'm quite o.k. personally.
- [x] `19` But in order to push the Tarot I shall have to renew my wardrobe, at least one suit, amd some underclothes.
- [x] `20` This will cost about £30.
- [x] `21` Then, of course, the printer.
- [ ] `22` I shall probably have to be content with a one-page war poem for March 21.
- [x] `23` But please remember that even the smallest cheque makes all the difference between staying idle and dashing about to put business through.
- [ ] `24` Sorry if this letter seems gloomy.
- [ ] `25` But I have been rather sick, and still don't feel too gay.
- [x] `26` I'm worried about the Tarot: we are so near to the end
- [x] `27` and it's the biggest work of my whole life
- [x] `28` that I can't help wondering if some 'tuile' isn't going to drop!
- [x] `29` I suppose that's liver too.

</details>

_Generated by `analyze_course.py`. Coverage percentages are computed from sentence-embedding similarity plus entity/number grounding against the parsed source statements shown above; they are a measurement of this parse, not a universal truth._