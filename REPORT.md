# Audio course vs. source document — audit report

- **Source:** `original.pdf` — corrected transcription supplied via --source-text (source_from_pdf.txt)
- **Course:** 8 lessons, 86.4 min of audio
- **Audio transcribed with:** faster-whisper `medium.en` on `cuda/float16` (beam 5, VAD off). Wording below is the transcript, not the authoring text — some oddities are speech-recognition artifacts, and are labelled as such where identifiable.

## 1. Headline numbers

| Measure | Value |
| --- | --- |
| Source statements identified | 562 |
| Fully carried into the audio | 507 (90%) |
| Carried but with detail dropped | 53 (9%) |
| Absent from the audio | 2 (0%) |
| **Content coverage (full + partial)** | **100%** |
| Source length | 10886 words |
| Course length | 12172 words |
| Expansion ratio | 1.1x |
| Narrated sentences | 923 (7 teaching scaffold, 916 content) |
| Content sentences with no close source match | 32 |
| Sentences naming something absent from the source | 30 |
| Near-duplicate statement pairs across lessons | 38 |
| **Narration lifted word-for-word from the source** | **46%** |

Read the last two rows together. Coverage should be high and lifted should be low; a course that reads the source aloud scores well on the first *because* it scores badly on the second. An expansion ratio near 1.0x is the same warning from the other direction — teaching adds words, copying does not.

<details><summary>3 statement(s) excluded as front matter, not scored</summary>

Attribution, title and copyright boilerplate. A course that omits these has not failed the listener, so they are held out of the coverage numbers above. Score them like any other statement with `--keep-front-matter`.

- `01` HARRY B JOSEPH (REVIVAL OF WISDOM) WORK TITLE: "THE BOOK OF WISDOM" IS REGISTERED WITH UK COPYRIGHT SERVICE.
- `02` MARKETING, RE-SALE, AND CLAIMING "THE BOOK OF WISDOM" WITHOUT CONSENT WILL RESULT IN VIOLATING THE LEGAL PROTECTION RIGHT, WHICH CAN RESULT IN LEGAL ACTION TOWARDS THE INDIVIDUAL.
- `12` EVERY IMAGE THE BOOK INCLUDES HAS BEEN CHANGED AND IS NOW CLASSED AS "ARTWORK" UNDER THE COPYRIGHT OF THE AUTHOR OF THE BOOK OF WISDOM.

</details>

> **Claude's independent read of coverage: 80%** — Near-total surface coverage of the document's sentences, but a meaningful share of it does not actually transfer, because this source is a caption-and-diagram book and the narration frequently recites labels without explaining the picture they label. A listener gets the doctrine (Christ oil, chakras, planes, hemispheres, flat-earth firmament cosmology) but not the visual arguments, several correspondence tables, and a few small text items.

> **Is this taught or recited? mixed** — Roughly 46% of the narration sits inside runs of eight or more words lifted verbatim, and the longest runs are not scripture — the 143-word passage on the left brain's analytic purpose, the 109-word hand-chakra axis passage, the 106-word mind-as-frequency-tuner passage and the 72-word toe-grounding passage are all straight transcription of the document's prose. Lessons 4 through 8 are largely that: the source's caption text spoken in page order with connective phrases added. Against that, Lessons 2 and 3 do real authorial work — reassembling the oil process into numbered steps from marginalia, and closing with a synthesis ("So the whole story from the Garden to the Crucifixion is written on the body itself") that appears nowhere in the source. The course therefore sits between the two poles, with the balance tipping toward recitation as the lessons progress.

## 2. Does the audio carry all the context?

**No — 2 statement(s) from the source never appear in any lesson.**

| # | Missing from the course | Closest thing the audio says |
| --- | --- | --- |
| 0 | BOOK OF WISDOM AUTHOR | _There is a quote from Walter Russell Lee, Universal One._ (sim 0.38) |
| 92 | THALAMUS 2. | _The spine contains 33 vertebrae, and once the oil passes all 33 and reaches the optic pell…_ (sim 0.35) |

### Carried, but with specifics dropped (53)

| Source statement | What went missing | Where it landed |
| --- | --- | --- |
| AUTHOR: REVIVAL OF WISDOM REVIVALOFWSIDOM REVIVALOFWISDOM3 REVIVALOFWISDOM INTRODUCTION THE BOOK OF WISDOM IS A BOOK CONTAINING ESOTERICISM, OCCULTISM, SYMBOLISM, AND MOST IMPORTANTLY, SYNCRETISM. | — | 04 - Pineal Gland, Holy Grail, and the Planes |
| ALL OF THE IMAGES IN THIS BOOK HAVE BEEN EDITED, MANIPULATED, AND ATIFICIALLY GENERATED TO AVOID ANY COPYRIGHT CLAIMS. | — | 08 - One Reality, Element Symbols, and Seven Heavens |
| NOT ONE OF THE IMAGES USED IN THIS BOOK IS BEING USED IN ITS ORIGINAL FORM. | — | 08 - One Reality, Element Symbols, and Seven Heavens |
| OIL PROCESS: 1-THE CLAUSTRUM (CLAUS=SANTA CLAUSE) PRODUCES THE PSYCHO-PHYSICAL THE BRAIN in the bible is: FLUID WHICH THEN GOES TO THE PINEAL AND PITUITARY GLAND IDA PINGALA -THE UPPER ROOM WHERE JESUS 2-THE PINEAL GLAND ELECTRICALLY CHARGES THE FLUID (MALE/ JOSEPH) MEETS THE 12 DISCIPLES/12 CRANIAL NERVES 3-THE PITUITARY GLAND MAGNETICALLY CHARGES THE FLUID (FEMALE/ MARY) -THE HOLY LAND 4-THEN THE FLUID WILL TRAVEL DOWN THE TWO NERVES, THE IDA WHICH IS -the LAND FLOWING WITH MILK AND HONEY CONNECTED TO THE PITUITARY, AND THEN THE PINGALA WHICH IS CONNECTED -promise land of israel TO THE PINEAL GLAND. | `1`, `4` | 02 - Christ Oil, Brain Anatomy, and Kundalini |
| MEDICAL SYMBOL -CONSUMING AN ALKALINE DIET -NO CONSUMPTION OF ACIDIC FOODS/FLUIDS THE PINGALA (MASCULINE) CHANNLE IS CONNECTED -NO CONSUMING ALCHOHOL TO THE PINEAL GLAND. -KHUNDALINI MEDITATION -BALANCE ALL CHAKARAS -KEEPING YOUR TOUNGE ON THE TOP OF SUSHUMNA YOUR MOUTH -PROPER BREATHING PSALMS 137:6 MY MY TOUNGE CLING TO THE ROOF OF MY MOUTH IF I DO NOT REMEMBER YOU, IF I DO NOT CONSIDER JERUSALEM MY HIGHEST JOY PINGALA IDA HEAVEN JESUS (THE OIL) IS IN NAZARETH (THE HEAD) WITH JOSEPH AND MARY (THE PINEAL AND PITUITARY RIVER JORDAN= SPINAL CORD GLAND) AND KING HAROD WANTS TO KILL HIM. | — | 02 - Christ Oil, Brain Anatomy, and Kundalini |
| IT'S NOT A COINCIDENCE THAT THE VERSE jOHN 3:3 IS TALKIG ABOUT BEING REBORN AGAIN. | — | 02 - Christ Oil, Brain Anatomy, and Kundalini |
| PINGALA IDA PINEAL PITUAITARY MASONIC ART FEMANINE MASCULINE RIGHT BRAIN LEFT BRIAN SNAKE=KHUNDALINI TREE=SPINE (IDA PINGALA) TREE LEAVES=BRAIN MALE=PINGALA CHANNLE=PINEAL=SUN=ELECTRIC FEMALE=IDA= CHANNLE=PITUITARY=MOON=MAGNETIC SERPENT KHUNDALINI CHANNLES "THREE WISE MEN FROM THE EAST" "THREE WISE MEN FROM THALAMUS THE EAST" 1. | — | 03 - Born Again, the Serpent, and the Tree of Life |
| HUMAN OUT OF BODY ABILLITIES. | — | 03 - Born Again, the Serpent, and the Tree of Life |
| AND EXPLORE OTHER REALITIES. | — | 08 - One Reality, Element Symbols, and Seven Heavens |
| THE MIND AND SOUL COME FROM ETERNAL BLISS, AND THE THE CENTRE OF EVERY TORUS FIELD IS MAGNETISM. | — | 03 - Born Again, the Serpent, and the Tree of Life |
| IT IS THE RADIATION GAIN THE KNOWLEDGE OF DUALISM. | — | 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THE HEART IS 5000X STRONGER MAGICALLY THAN THE BRAIN | `5000` | 03 - Born Again, the Serpent, and the Tree of Life |
| THE ANCIENT TEXTS AND INFORMATION OF OUR TRUE POWERS. | — | 04 - Pineal Gland, Holy Grail, and the Planes |
| IT THE TWO MASONIC PILLERS HAS NO BEGINNING OR END, ITS ETERNAL. | — | 05 - Astral Plane, Chakras, and the True Self |
| MOON SPIRIT SPIRITUALITY CONNECTION GOLD INTUITION MERCURY spirit PHYCIC ABILITY COMMUNICATION VENUS SELF-EXPRESSION LOVE SUN air INNER PEACE POWER MARS fire SELF LOVE SEXUALITY JUPITER water CREATIVITY LEAD GROUNDING SATURN earth SURVIVAL MATTER "144,000 go to heaven" 144,000 A THERE ARE ACTUALLY 7 VOULS, AND EACH VOUL CORRESPONDS WITH ONE OF THE CHAKARAS. | — | 07 - Ether, Moon, and the Light Projection |
| FREQUENCIES TO HELP BALANCE EACH CHAKARA. 4+6+10+12=48 | — | 05 - Astral Plane, Chakras, and the True Self |
| crown=1000 petals U PHYSICAL PLANE = MATTER THE ETHER IS THE 5TH ELEMENT, ALSO | — | 05 - Astral Plane, Chakras, and the True Self |
| ITS A SUBSTANCE 1000x144=144,000hz JAHOVAS WITNESS BELIEVE EXACTLY 144,000 FAITHFUL CHRISTIAN WILL Y THAT HAS ONE FOOT IN THE ASTRAL PLANE AND IN THE PHYSICAL PLANE. | — | 05 - Astral Plane, Chakras, and the True Self |
| CHAKARAS I KNOW HOW TO KNOW YOUR PASSING THROUGH CHAKARAS I SEE ROOT = YOU WILL NO LONGER FEAR AND FEEL STABLE SACREL= NO LONGER HAVE LUST/DESIRE FOR SEX I SPEAK SOLAR = NO LONGER DESIRE FOR FOOD HEART = NO LONGER HATE ANYTHING/ANYONE I LOVE THROAT = NO LONGER HOLD YOURSELF BACK TO EXPRESS YOURSELF I DO THIRDEYE = HAVE THE ABILLTY TO READ PEOPLES ENERGY, INTUITION AND ASTRAL PROJECTION. | — | 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THE HIGHER 3 CHAKRAS ARE THE HIGHER STATES OF CONSCIOUSNESS WHERE YOUR DEUTERONOMY 20:17 MIND IS NO LONGER MANIFESTING "Completely destroy them—the Hittites, Amorites, Canaanites, WHATEVER THE LOWER SELF DESIRES. | `20`, `COMPLETELY` | 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| NATURE AND TURNING TO YOUR HIGHER/SPIRIT SELF. | — | 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| WHENEVER THE STOMACH RUMBLES, -FOR EXAMPLE, IF YOU ARE OVERSEXUAL, YOU ABUSE YOUR RELEASING SEXUAL FLUIDS WHENEVER YOU SACREL CHAKARA, WHICH IS WEAKENING YOUR FIELD. | — | 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| FEEL LIKE IT, ETC. | — | 05 - Astral Plane, Chakras, and the True Self |
| LOW FREQUENCY CHAKARAS PAGE 243 FIGURE 11:11 FROM THE BOOK "BECOMING SUPERNATURAL"-AUTHORED BY DOCTOR JOE DISPENZA SEVEN UP IS TRUTH IN PLANE SITE. from thought to energy matter WHOLENESS BLISS FREEDOM LOVE JOY NOTICE HOW LUST IS THE LOWEST APPRECIATION VIBRATIONAL EMOTION. | `11`, `243` | 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| They manifest in the following associations: Manipura (solar plexus)= thumb. | `MANIPURA` | 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| Sahasrara (crown) = PALM Ajna Chakra (third eye) = WRIST POINT This arrangement results in a harmonious balance on the hand, where the ring and little fingers embody feminine qualities, while the thumb and index finger exude masculine attributes. | `AJNA` | 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| Additionally, a central axis extends from the wrist point, passing through the center of the palm and reaching up to the middle finger, symbolizing the Spirit Element. | `ADDITIONALLY` | 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| In contrast to the feet | — | 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| FOOT AND CHAKARAS: Manipura (solar plexus) = big toe. | `MANIPURA` | 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| Ajna (THIRD EYE) = fourth toe. | `AJNA` | 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THE SOLFEGGIO SCALE 3+9+6=18=9 4+1+7=12=3 5+2+8=15=6 THE TWO ANGLES COVERING THE COVENENT ARE THE TWO 7+4+1=12=3 HEMISPHERES OF THE BRAIN COVERING (PROTECTING) THE SACRED CENTRE OF THE BRAIN. | — | 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| I am the YOURSELF INTO THE LOWER PLANES OF all. | — | 04 - Pineal Gland, Holy Grail, and the Planes |
| EXISTNECE BY IGNORANCE OF TRUTH AND KNOWLEDGE. | — | 01 - Syncretism and the Lightwave Universe |
| MASCULINE THE MOST MAGICAL POINT IN THE FIELD. | — | 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| WHICH ARE THE 7 LANDS, CREATING THE SEASON OF WINTER. | — | 07 - Ether, Moon, and the Light Projection |
| GO TO THE SATURN PAGES BELOW TO LEARN MORE. | — | 07 - Ether, Moon, and the Light Projection |
| A Persian miniature depicting Seven Heavens THE 7 PLANETS COME FROM THE 7 COLOURS OF THE ELECTROMAGNETIC COLOUR SPECTRUM. from The History of EACH PLANET GIVE OFF CERTAIN FREQUENCY OF Mohammed, Bibliothèque LIGHT WHICH INFLUENCE THE MIND UNTIL WE nationale de France, Paris. | `FRANCE`, `HISTORY`, `MOHAMMED`, `PERSIAN` | 07 - Ether, Moon, and the Light Projection |
| THE LORD OF EARTH THE RINGS THE WORD PLANET HAS A PLAN WITHIN IT, AND PLAN QUARAN 65:12 MEANS PLANE. | `12`, `65` | 07 - Ether, Moon, and the Light Projection |
| and let it divide the waters WAVES. | — | 07 - Ether, Moon, and the Light Projection |
| THE FIRMAMENT IS SYMBOLIZED BY THE YOU HAVE TO BALANCE ALL FAMOUS LL SEEING EYE WITH LIGHT BEING THE SUN IS ELECTRIC/MALE. | — | 07 - Ether, Moon, and the Light Projection |
| BRIAN, BALANCE THE CHAKRAS isiah 40:22 EVEN=BALANCE. | `22`, `40` | 02 - Christ Oil, Brain Anatomy, and Kundalini |
| and its people are like grasshoppers. | — | 07 - Ether, Moon, and the Light Projection |
| EACH CHAKARA IS ONE NEGATIVE ETC... | — | 05 - Astral Plane, Chakras, and the True Self |
| Greed, Quran 15:19 POLES. | — | 08 - One Reality, Element Symbols, and Seven Heavens |
| You out (like a carpet) | — | 05 - Astral Plane, Chakras, and the True Self |
| Quran 71:19 chronicles 16:30 "And Allah has made the earth for you as a carpet (spread out)." "Tremble before him, all the earth! | `16`, `19`, `30`, `71` | 08 - One Reality, Element Symbols, and Seven Heavens |
| The world GENESIS 1:14 is firmly established | `14` | 08 - One Reality, Element Symbols, and Seven Heavens |
| and let them be Talaaq 65:12 for signs | — | 07 - Ether, Moon, and the Light Projection |
| and years" Pslams 104:5 "It is Allah Who has created seven heavens and of the earth the like "He set the earth on its foundations | `104`, `5` | 08 - One Reality, Element Symbols, and Seven Heavens |
| Revelation 7:1 THE FIRMIMENT IS A FIRM ARCH/ SKY FAULT. | — | 07 - Ether, Moon, and the Light Projection |
| COSMOLOGY @Revivalofwisdom ELEMENT SYBOLS SUN FIRE EARTH AIR MOON EARTH WATER BLACK SUN MASONIC COMPASS SUN MOON AS ABOVE SO BELOW LUNAR SOLAR BLACK SUN ISLAND=EYELAND PLANET=PLAN=PLANE MAYAN UNIVERSE THE ANCIENTS SAID WE LIVE IN GUARD, WHICH IS A BALANCED REALM CONTAINING BOTH GOOD AND EVIL. | `REVIVALOFWISDOM` | 08 - One Reality, Element Symbols, and Seven Heavens |
| ALCHEMICAL SYMBOL FOR EARTH 1500S-1600S NORTH POLE MAP LUCKY HEARTH UNITED NATIONS LOGO FLAT EARTH MAP HITLER USING 2 FLAT EARTH MAPS IMAGE SOURCE | `1500`, `1600` | 08 - One Reality, Element Symbols, and Seven Heavens |
| BIBLE=GENISIS 1:6-8 BIBLE JOB 37:18 QUARAN 65:12 THE 7 HEAVENS ARE THE 7 LAYERS OF THE FIRMAMENT | `12`, `18`, `37`, `6`, `65` | 08 - One Reality, Element Symbols, and Seven Heavens |

## 3. Did the AI invent anything?

### Narrated content with no close match in the source (32)

| Lesson | Sentence | Similarity to nearest source statement |
| --- | --- | --- |
| 01 - Syncretism and the Lightwave Universe | Split it as ilel-lent. | 0.29 |
| 01 - Syncretism and the Lightwave Universe | Split it as h, u, man. | 0.35 |
| 02 - Christ Oil, Brain Anatomy, and Kundalini | You do not consume alcohol. | 0.34 |
| 02 - Christ Oil, Brain Anatomy, and Kundalini | The Aida channel is feminine and connects to the pituitary gland. | 0.38 |
| 02 - Christ Oil, Brain Anatomy, and Kundalini | King Herod wants to kill him. | 0.25 |
| 03 - Born Again, the Serpent, and the Tree of Life | Let them pick up where we left off. | 0.27 |
| 03 - Born Again, the Serpent, and the Tree of Life | That's not a coincidence. | 0.32 |
| 03 - Born Again, the Serpent, and the Tree of Life | That 10. | 0.36 |
| 03 - Born Again, the Serpent, and the Tree of Life | Now consider the word play. | 0.32 |
| 03 - Born Again, the Serpent, and the Tree of Life | You are all knowing and directly from the source. | 0.35 |
| 04 - Pineal Gland, Holy Grail, and the Planes | I either support Manchester, United, or Liverpool. | 0.36 |
| 05 - Astral Plane, Chakras, and the True Self | Breathe deep in through the nose and slowly out the mouth. | 0.33 |
| 05 - Astral Plane, Chakras, and the True Self | Ninety-six plus forty-eight equals one hundred and forty-four. | 0.32 |
| 06 - Chakra Balance, Head as Heaven, and Hemispheres | Let them pick up where we left off. | 0.27 |
| 06 - Chakra Balance, Head as Heaven, and Hemispheres | I love the throat. | 0.33 |
| 06 - Chakra Balance, Head as Heaven, and Hemispheres | I, know. | 0.26 |
| 06 - Chakra Balance, Head as Heaven, and Hemispheres | So what do those nations represent? | 0.35 |
| 06 - Chakra Balance, Head as Heaven, and Hemispheres | That. | 0.25 |
| 06 - Chakra Balance, Head as Heaven, and Hemispheres | There in a well-known chart from Dr. | 0.31 |
| 06 - Chakra Balance, Head as Heaven, and Hemispheres | Hell. | 0.37 |
| 06 - Chakra Balance, Head as Heaven, and Hemispheres | For example, 396 adds to 18, which reduces to 9. 417 adds to 12, which reduces to 3. 528 adds to 15, which reduces to 6. | 0.36 |
| 06 - Chakra Balance, Head as Heaven, and Hemispheres | And 741 adds to 12, which reduces to 3. | 0.31 |
| 06 - Chakra Balance, Head as Heaven, and Hemispheres | Know thyself. | 0.36 |
| 06 - Chakra Balance, Head as Heaven, and Hemispheres | The Merkaba is the vehicle of ascension. | 0.37 |
| 06 - Chakra Balance, Head as Heaven, and Hemispheres | That and done intentionally to keep us left. | 0.36 |
| 06 - Chakra Balance, Head as Heaven, and Hemispheres | Heia. | 0.36 |
| 06 - Chakra Balance, Head as Heaven, and Hemispheres | It is speechless. | 0.35 |
| 07 - Ether, Moon, and the Light Projection | The neutral. | 0.36 |
| 07 - Ether, Moon, and the Light Projection | It infeminine? | 0.32 |
| 07 - Ether, Moon, and the Light Projection | Good and bad. | 0.31 |
| 07 - Ether, Moon, and the Light Projection | And it was so. | 0.29 |
| 08 - One Reality, Element Symbols, and Seven Heavens | Notice the word play. | 0.35 |

### Names and numbers spoken that are not in the source (30)

| Lesson | Not in source | Sentence |
| --- | --- | --- |
| 01 - Syncretism and the Lightwave Universe | `BEN` | In Genesis 1 to 3, it says, Ben, let there be light. |
| 01 - Syncretism and the Lightwave Universe | `LEE`, `RUSSELL` | There is a quote from Walter Russell Lee, Universal One. |
| 02 - Christ Oil, Brain Anatomy, and Kundalini | `PROMISED` | The Promised Land of Israel, the quaestrum is Santa Claus. |
| 02 - Christ Oil, Brain Anatomy, and Kundalini | `HEROD` | King Herod wants to kill him. |
| 03 - Born Again, the Serpent, and the Tree of Life | `ABBAS` | Matthew 6 22 says, Abbas the light of the body is the eye, therefore if thine eye be single, the whole body shall be full of light. |
| 03 - Born Again, the Serpent, and the Tree of Life | `TAURUS` | The heart is the center of the body-electrope-inactive field, and at the center of every Taurus field is magnetism. |
| 03 - Born Again, the Serpent, and the Tree of Life | `CRUCIFIXION` | So the whole story from the Garden to the Crucifixion is written on the body itself. |
| 04 - Pineal Gland, Holy Grail, and the Planes | `SUMERIANS` | The Sumerians depicted a god holding a pine cone, which symbolizes the pineal gland. |
| 05 - Astral Plane, Chakras, and the True Self | `DIAMON` | If you entertain negative thought forms for long periods, the emotional power you give that thought can manifest into a Diamon. |
| 05 - Astral Plane, Chakras, and the True Self | `DIAMON` | Every single mental addiction you have is some Diamon you created within the astral plane. |
| 05 - Astral Plane, Chakras, and the True Self | `DIAMON` | The word Diamon has the letters M-O-N in it, which means moon. |
| 05 - Astral Plane, Chakras, and the True Self | `SANSKRIT` | The word chakra in Sanskrit means wheel. |
| 05 - Astral Plane, Chakras, and the True Self | `WITNESSES` | Jehovah Witnesses believe exactly 144,000 faithful Christians will go to heaven. |
| 05 - Astral Plane, Chakras, and the True Self | `44` | Ninety-six plus forty-eight equals one hundred and forty-four. |
| 05 - Astral Plane, Chakras, and the True Self | `44` | The crown has ten hundred petals, ten hundred times one hundred and forty-four equals one hundred forty-four thousand hertz. |
| 06 - Chakra Balance, Head as Heaven, and Hemispheres | `2017` | This idea of destroying your lower nature shows up in scripture and it demends symbolically in Deuteronomy 2017. |
| 06 - Chakra Balance, Head as Heaven, and Hemispheres | `AMEL` | And note that Amel means God, so the name itself carries that divine reference. |
| 06 - Chakra Balance, Head as Heaven, and Hemispheres | `CAUDO`, `DISBENZA`, `1111` | Joe Disbenza to book, Caudo, Becoming Supernatural, figure 1111, that lays out the vibrational emotions. |
| 06 - Chakra Balance, Head as Heaven, and Hemispheres | `ROCKEFELLER` | The Rockefeller Foundation, in the 1950 seconds, changed the standard music tuning from 432 hertz to 440 hertz. |
| 06 - Chakra Balance, Head as Heaven, and Hemispheres | `396`, `417` | For example, 396 adds to 18, which reduces to 9. 417 adds to 12, which reduces to 3. 528 adds to 15, which reduces to 6. |
| 06 - Chakra Balance, Head as Heaven, and Hemispheres | `741` | And 741 adds to 12, which reduces to 3. |
| 06 - Chakra Balance, Head as Heaven, and Hemispheres | `JEDPILA` | The Egyptian Jedpila represents the central nervous system, the spine. |
| 06 - Chakra Balance, Head as Heaven, and Hemispheres | `SAUL` | Horus is the sun and sun is Saul, which is soul. |
| 06 - Chakra Balance, Head as Heaven, and Hemispheres | `TAURUS` | That and why the Egyptians stated, all is a two, meaning all is Adam, the Taurus field. |
| 06 - Chakra Balance, Head as Heaven, and Hemispheres | `TOLLOS` | Neo Tollos from The Matrix woke up and started to use his higher critical thinking mind, which is the neocortex, that tan, the whole point. |
| 07 - Ether, Moon, and the Light Projection | `CAPRICOURT` | After this it spirals outward towards the Tropic of Capricourt which is further away from the northern lands creating winter. |
| 07 - Ether, Moon, and the Light Projection | `BON` | Now Genesis 1 to 3 says Bon, let there be light. |
| 07 - Ether, Moon, and the Light Projection | `SUNDAY` | There are seven stars that symbolize the seven planets, also known as the seven wanderers or the seven layers of heaven, Saturn, Jupiter, Mars, Sunday, Venus, Mercury, Moon. |
| 08 - One Reality, Element Symbols, and Seven Heavens | `ELAND` | Island is Eland, and planet is Plan, which is plain. |
| 08 - One Reality, Element Symbols, and Seven Heavens | `500`, `600` | There are also historical maps from the 1,500 seconds and 1,600 seconds, showing the North Pole and flat earth maps. |

_Fuzzy matching is applied before flagging, so mangled-but-recognisable names are not listed here. What remains is either genuinely new information or a transcription error severe enough to change the word._

### Adjudicated findings

- **misreading** — _06 - Chakra Balance, Head as Heaven, and Hemispheres_: “The head corresponds to the mind, the heart to the body, and the heel to the soul.”
  The source table reads HEAVEN/HEAD = MENTAL = MIND = GOD; EARTH/HEART = EMOTIONAL = SOUL = JESUS; HELL/HEEL = PHYSICAL = BODY = SATAN. The narration swaps soul and body, inverting the source's own scheme — and it does so one sentence before correctly saying "These map onto God, Jesus, and Satan," leaving the listener with a self-contradictory mapping.
- **invented fact** — _06 - Chakra Balance, Head as Heaven, and Hemispheres_: “Each chakra has a corresponding statement of identity... Those are the feminine and masculine poles of your being. And when they mount of whack, your whole frequency drops.”
  The source lists I KNOW / I SEE / I SPEAK / I LOVE / I DO / I FEEL / I AM beside the chakra column. Nothing in the source describes these statements as feminine and masculine poles, nor says that unbalanced I-statements drop your frequency. The narration also scrambles the pairings ("The root is, but I. The sacral is. I feel the solar plexus. I do the heart, idzu."), so the one list the listener gets is both invented in framing and misaligned in content.
- **unsupported inference** — _06 - Chakra Balance, Head as Heaven, and Hemispheres_: “The head is associated with concentration and meditation, the masculine Solar Yang principle. The heel is associated with contemplation. The Feminine Lunar Yin principle.”
  The source page carries only the loose labels "concentration contemplation meditation / HEAD HEAVEN / masculine femanine solar lunar yang yin / HEEL HELL". The course assigns two of the three practices to the head and the third to the heel, and pairs yang with the head and yin with the heel. No such assignment exists in the document.
- **unsupported inference** — _04 - Pineal Gland, Holy Grail, and the Planes_: “Consciousness is referenced in Chronicles 3 10, and the 33 vertebrae appear again in this context.”
  In the source, "33 VERDABREA" is a stray page label sitting near the Chronicles 3:10 note; the source makes no connection between the Chronicles passage (most holy place = pineal, two cherubim = hemispheres) and the vertebrae. The narration manufactures a link and then asserts it as if the source drew it.
- **outside knowledge** — _04 - Pineal Gland, Holy Grail, and the Planes_: “The gland connects to the body through specific pathways, the retino-hypothalamic tract, the suprachiasmatic nucleus, the superior cervical ganglion... These are the physical roots by which light information reaches the gland.”
  The source only reproduces these terms as scattered labels on an unexplained anatomical diagram (alongside "PINEAL GLAND INHIBITION" and "MELATONIN"). The explanatory sentence — that these constitute the pathway by which light information reaches the gland — is imported physiology, not something the document states.
- **unsupported inference** — _06 - Chakra Balance, Head as Heaven, and Hemispheres_: “And note that Amel means God, so the name itself carries that divine reference.”
  The source prints only "EL=GOD" beside the Baphomet page. The narration turns a bare gloss into a claim that the Baphomet's name carries a divine reference, which the source never argues. (The word "Amel" itself is a likely transcription slip for "EL".)
- **likely transcription artifact** — _01, 03, 06_: “There is a quote from Walter Russell Lee, Universal One... In Genesis 1 to 3, it says, Ben, let there be light... Matthew 6 22 says, Abbas the light of the body is the eye... Neo Tollos from The Matrix... all is a two, meaning all is Adam, the Taurus field... The Egyptian Jedpila represents the central nervous system.”
  These garbles (Russell's 'Universal One'; the interjections before verses; 'all is Atum, meaning all is atom, the torus field'; the Djed pillar) all track the source sentence-for-sentence and are speech-to-text noise rather than authoring errors — but the 'Atum/atom/torus' pun and the 'Djed pillar' reference are destroyed for the listener, since 'a two / Adam / Taurus' and 'Jedpila' convey nothing.

## 4. Is it taught, or is it read out?

**45.9% of narrated words sit inside a run of 8+ consecutive words copied from the source** (5,580 of 12,155 words, 345 runs).

| Lesson | Words | Lifted | Longest unbroken run |
| --- | --- | --- | --- |
| 01 - Syncretism and the Lightwave Universe | 739 | 54% | 106 words |
| 02 - Christ Oil, Brain Anatomy, and Kundalini | 907 | 32% | 30 words |
| 03 - Born Again, the Serpent, and the Tree of Life | 1,467 | 47% | 40 words |
| 04 - Pineal Gland, Holy Grail, and the Planes | 1,721 | 60% | 66 words |
| 05 - Astral Plane, Chakras, and the True Self | 1,378 | 48% | 51 words |
| 06 - Chakra Balance, Head as Heaven, and Hemispheres | 3,403 | 43% | 143 words |
| 07 - Ether, Moon, and the Light Projection | 2,024 | 42% | 37 words |
| 08 - One Reality, Element Symbols, and Seven Heavens | 516 | 35% | 31 words |

### Longest passages carried over word-for-word

- **143 words** — _06 - Chakra Balance, Head as Heaven, and Hemispheres_
  > purpose is to analyze and break down the unified whole presented by the right brain this process is done by the left hemisphere so that we can have distinct singular fragments of reality so that it can manipulate manage and control it both hemispheres are needed for us to function within this creation however we must balance these two aspects of the brain so that we don't become left or right brai…
- **109 words** — _06 - Chakra Balance, Head as Heaven, and Hemispheres_
  > up to the middle finger symbolizing the spirit element this central axis serves as a reconciling force for the contrasting gender principles hand chakras serve as a vital interface between the physical and energetic dimensions allowing us to engage with the world on both levels the fingers function as sensitive receptors while the palms act as conduits for channeling healing energy your dominant h…
- **106 words** — _01 - Syncretism and the Lightwave Universe_
  > world would cease to exist the mind is spirit the mind is the intellect that manipulates the physical body and the world around us the mind is like a frequency tuner tuning itself into different frequencies the mind exists within the mental plane which is shared between all the minds of the universe thoughts are not created by the individual they are received based on what frequency our mind is se…
- **72 words** — _06 - Chakra Balance, Head as Heaven, and Hemispheres_
  > one of the primary functions of the toes is to release and discharge any surplus energy that accumulates within the major chakras through our everyday activities and bodily functions this excess energy is channeled into the earth facilitating a grounding of our consciousness when the minor chakras in the feet operate harmoniously and are in alignment with the major chakras it establishes a continu…
- **66 words** — _04 - Pineal Gland, Holy Grail, and the Planes_
  > entities that live amongst us like goblins gnomes and trolls they are entities that have the ability to materialize or stay in the astral body at their will they can choose whether to be physical or non physical this is where we get the myths of trolls fairies gnomes and goblins from they are very secretive beings and do not like to be seen by humans
- **51 words** — _05 - Astral Plane, Chakras, and the True Self_
  > etheric body being awakened now imagine yourself pulling a rope up into the sky you may feel yourself being lifted out of the body do not be scared keep doing this exercise until you gain the ability to leave the whole body and discover the astral plane if you do astral
- **45 words** — _04 - Pineal Gland, Holy Grail, and the Planes_
  > external teachings this is done purposely to keep the pyramid scheme up and running meanwhile the people in power get taught the esoteric meaning the internal teachings about the body consciousness and the metaphysical aspects of reality the bible is written in such a way
- **45 words** — _04 - Pineal Gland, Holy Grail, and the Planes_
  > the mental plane is shared between all the minds that exist it is the world of thoughts thoughts are not created they are received based upon what frequency our mind is set to this is why we call it a mindset each thought topic and
- **45 words** — _06 - Chakra Balance, Head as Heaven, and Hemispheres_
  > the body to do so actions of the body are under the command of the centering soul the body is an electrical machine that takes commands from the omnipotent cosmic intelligence to think is to create we create with light nothing is not light the
- **43 words** — _04 - Pineal Gland, Holy Grail, and the Planes_
  > when we astral project we are using our mind to project the soul into the astral plane you will only see and encounter beings that are on a similar frequency as you if you operate on a low frequency you will come across
- **41 words** — _04 - Pineal Gland, Holy Grail, and the Planes_
  > 20 or do you not know that your body is a temple of the holy spirit within you whom you have from god you are not your own for you were bought with a price so glorify god in your body
- **41 words** — _05 - Astral Plane, Chakras, and the True Self_
  > astral projecting when jesus teaches peter to walk on water he is teaching him not to be scared or else you will fall back into the water this is symbolic of when you are astral projecting when you start to fear
- **40 words** — _03 - Born Again, the Serpent, and the Tree of Life_
  > the story of jesus is symbolic of the alchemical process that occurs monthly within the human body jesus falls from heaven and incarnates on the earth which is symbolic of the christ oil traveling down the spine from your brain
- **40 words** — _04 - Pineal Gland, Holy Grail, and the Planes_
  > the root cause there is no point in looking down here because the physical plane is the world of effect whatever you see and experience is the effect of your mind so look up at the cause change your mind
- **40 words** — _06 - Chakra Balance, Head as Heaven, and Hemispheres_
  > both hemispheres participate and contribute to all activities however they do the activity in different ways in other words both brains carry out the same functions but function in two distinct and different ways both brains have separate views and

_Scripture is the honest exception: where the source quotes a verse and the course quotes the same verse, the run above is shared quotation of a third text, not the source's own prose. Check long runs against that before treating them as copying._

## 5. Duplication and redundancy

263 of 562 source statements are taught in more than one lesson (47%).

| Source statement | Repeated in |
| --- | --- |
| THE MIND IS SPIRIT. | 01 - Syncretism and the Lightwave Universe, 03 - Born Again, the Serpent, and the Tree of Life, 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| THE MIND IS THE INTERLECT THAT CONNECTS soul THE SOUL TO THE BODY | 01 - Syncretism and the Lightwave Universe, 03 - Born Again, the Serpent, and the Tree of Life, 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| MIDDLE ASTRAL WHEN WE ASTRAL PROJECT, WE ARE USING OUR MIND TO PROJECT THE SOUL INTO THE ASTRAL PLANE. | 01 - Syncretism and the Lightwave Universe, 03 - Born Again, the Serpent, and the Tree of Life, 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| THE HEAD IS HEAVEN BECAUSE IT IS THE PLACE OF CONSCIOUSNESS IN THE CENTRE OF THE BRAIN. | 03 - Born Again, the Serpent, and the Tree of Life, 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection, 08 - One Reality, Element Symbols, and Seven Heavens |
| THE ONE SUBSTANCE OF THINKING MIND IS ALL THAT EXISTS." "MIND IS EXPRESSED IN LIGHT". | 01 - Syncretism and the Lightwave Universe, 03 - Born Again, the Serpent, and the Tree of Life, 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THE MIND EXISTS WITHIN THE MENTAL PLANE, WHICH IS SHARED BETWEEN ALL THE MINDS OF THE UNIVERSE. | 01 - Syncretism and the Lightwave Universe, 03 - Born Again, the Serpent, and the Tree of Life, 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THEREFORE, OUR MIND IS MANIFESTING COLOURS WITHIN THE ASTRAL PLANE BASED UPON WHAT FREQUENCY OUR MIND IS GENERALLY OPERATING OFF. | 01 - Syncretism and the Lightwave Universe, 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| LEAVING ACTIVATION OF THE PINEAL GLAND GIVES THE BODY GIVES YOU ACCESS TO WORLDS YOU THE ABILLITIES TO LEAVE THE BODY BEYONG TIME AND SPACE. | 02 - Christ Oil, Brain Anatomy, and Kundalini, 03 - Born Again, the Serpent, and the Tree of Life, 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| CONSCIOUSNESS IS GOD AND WE ARE ALL THAT SAME SPARK OF CONSCIOUSNESS IN THE CNETRE OF THE BRAIN. | 01 - Syncretism and the Lightwave Universe, 03 - Born Again, the Serpent, and the Tree of Life, 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| HEAD IS HEAVEN THE 3 BRAINS CONTROL THE 3 SECTIONS OF THE BODY HIGHER BRAIN HEAVEN/HEAD MENTAL MIND GOD MAMEL EARTH/HEART EMOTIONAL SOUL JESUS HELL/HEEL PHYSICAL BODY SATAN REPTILLIAN NOTICE HOW THE LANDSCAPE OF THE EXTERNAL WORLD MATCHES UP WITH THE CHAKRA SYSTEM. | 03 - Born Again, the Serpent, and the Tree of Life, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection, 08 - One Reality, Element Symbols, and Seven Heavens |
| PLATOS ASPECT FIRE=SHARPNESS,THINNESS,MOVEMENT EARTH=DULLNESS,THICKNESS,REST AIR=THINNESS,MOVEMENT,DULLNESS WATER=DULLNESS,THICKNESS,MOVEMENT FEMALE MALE WATER FIRE EARTH AIR PASSIVE ACTIVE SPIRIT THE ELEMENTS ARE ALWAYS IN THIS ORDER BECAUSE IT STARTS WITH THE DENSEST (EARTH), THEN ON TOP OF THE FIRE=LIGHT EARTH LIES WATER, THEN ON TOP OF WATER IS THE AIR, AND ON TOP OF THE AIR IS FIRE (HEAT RISES), THEN ON TOP AIR=BREATH OF FIRE IS SPIRIT/ETHER. | 03 - Born Again, the Serpent, and the Tree of Life, 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 07 - Ether, Moon, and the Light Projection, 08 - One Reality, Element Symbols, and Seven Heavens |
| ELECTRICAL IMPULSES BACK TO THE PINEAL GLAND TO DECODE THE EXTERNAL WORLD. | 02 - Christ Oil, Brain Anatomy, and Kundalini, 03 - Born Again, the Serpent, and the Tree of Life, 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| This is why your head is heaven. | 03 - Born Again, the Serpent, and the Tree of Life, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection, 08 - One Reality, Element Symbols, and Seven Heavens |
| THE MIND IS THE INTELLECT THAT MANIPULATES THE PHYSICAL BODY AND THE WORLD AROUND US. | 01 - Syncretism and the Lightwave Universe, 03 - Born Again, the Serpent, and the Tree of Life, 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self |
| THE MIND IS LIKE A FREQUENCY TUNER, TUNING ITSELF INTO DIFFERENT FREQUENCIES. | 01 - Syncretism and the Lightwave Universe, 03 - Born Again, the Serpent, and the Tree of Life, 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THOUGHTS ARE NOT CREATED BY THE INDIVIDUAL | 01 - Syncretism and the Lightwave Universe, 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| WE ARE LIGHT BEINGS MANFESTED INTO PHYSICAL FORM. | 01 - Syncretism and the Lightwave Universe, 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| BY AWAKENING THE SEVEN CHAKRAS AND RAISING THE KUNDALINI TO THE CROWN CHAKARA, NEW ENERGY PATHWAYS OPEN UP WITHIN THE BRAIN, WHICH FEELS LIKE YOUR HEAD BECOMES HOLLOW ON THE INSIDE. | 02 - Christ Oil, Brain Anatomy, and Kundalini, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| THE PINEAL GLAND WHICH IS THE SEAT OF CONSCIOUSNESS (THRONE OF GOD). | 03 - Born Again, the Serpent, and the Tree of Life, 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| PINEAL GLAND 3. | 02 - Christ Oil, Brain Anatomy, and Kundalini, 03 - Born Again, the Serpent, and the Tree of Life, 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THE RIGHT HEMISPHERE IS TO DO WITH CREATIVITY, INTUITION AND INSIGHT WHICH IS CONNECTED TO THE CEREBRUM (THE HIGHER BRAIN) chronicles 3:10 THE MOST HOLY PLACE = THE PINEAL GLAND/CENTRE OF THE BRAIN, TWO CHERUBIM = THE TWO HEMISPHEARS OF THE BRAIN. | 01 - Syncretism and the Lightwave Universe, 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| MENTAL PLANE THE MENTAL PLANE IS THE DIMENSION OF THE MIND. | 01 - Syncretism and the Lightwave Universe, 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THE MIND IS A PART OF THE UNIVERSAL MIND. | 01 - Syncretism and the Lightwave Universe, 03 - Born Again, the Serpent, and the Tree of Life, 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THEREFORE, THE MENTAL PLANE IS SHARED BETWEEN ALL THE MINDS THAT EXIST. | 01 - Syncretism and the Lightwave Universe, 03 - Born Again, the Serpent, and the Tree of Life, 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self |
| THOUGHTS ARE NOT CREATED | 01 - Syncretism and the Lightwave Universe, 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| EACH THOUGHT, TOPIC, AND MENTAL SUBJECT IS A FREQUENCY, AND WHEN YOU SET YOUR MIND TO THESE TOPICS, YOU GAIN THE THOUGHTS THAT ARE ON THAT SIMILAR FREQUENCY. | 01 - Syncretism and the Lightwave Universe, 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| IT IS THE MOST FLUIDIC PLANE ASTRAL PLANE THE ASTRAL PLANE IS WHERE THOUGHTS MANIFEST INTO FORMS. | 01 - Syncretism and the Lightwave Universe, 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| FOR EXAMPLE, THE MENTAL PLANE IS THE THOUGHT OF THE CHAIR, AND THE ASTRAL PLANE IS THE IMAGINATION OF THAT CHAIR. | 01 - Syncretism and the Lightwave Universe, 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| HIGHER ASTRAL THE ASTRAL PLANE IS CREATED OUT OF THOUGHTS MANIFESTING, AND EACH THOUGHT HAS A VIBRATIONAL FREQUENCY. | 01 - Syncretism and the Lightwave Universe, 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| FOR EXAMPLE, THERE ARE SPIRITS OF FIRE, WATER, EARTH, AND AIR. | 03 - Born Again, the Serpent, and the Tree of Life, 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 07 - Ether, Moon, and the Light Projection |
| IT IS THE MIRRORING OF REALITIES WITHIN THE THE MENTALISM PLANES OF EXISTENCE. | 01 - Syncretism and the Lightwave Universe, 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| WHATEVER YOU DO IN THE ASTRAL THE STARS ARE NOT PHYSICAL PLACES THEY ASTRAL PLANE WILL MANIFEST ARE PORTALS TO THE ASTRAL PLANE. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| IT'S THE UNSEEN OF WHAT WE SEE IT IS WHERE THOUGHT FORMS EXIST (MENTAL IMAGES) IT CAN BE SEEN ONLY BY OUR MIND'S EYE YOU WILL EXPERIENCE BEINGS AND ENTITIES THAT MATCH YOUR FREQUENCY, SO MAKE SURE YOU ARE VIBRATING AS HIGH AS POSSIBLE BEFORE TRYING TO PROJECT. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| WHEN YOU ASTRAL PROJECT, YOU ARE USING YOUR MIND TO PROJECT THE SOUL OUT OF THE PHYSICAL BODY (PHYSICAL WORLD) INTO THE ASTRAL PLANE WHERE THERE ARE NO LIMITATIONS OF TIME AND SPACE. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| THIS IS SYMBOLIC OF WHEN YOU ARE ASTRAL PROJECTING. | 01 - Syncretism and the Lightwave Universe, 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THE CHAKRAS ARE LIKE MINI-BRAINS CONTROLLING ALL THE CELLS AND ORGANS WITHIN THAT section of the body OF THE BODY. | 02 - Christ Oil, Brain Anatomy, and Kundalini, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| KNOWN AS SPIRIT. | 01 - Syncretism and the Lightwave Universe, 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 07 - Ether, Moon, and the Light Projection |
| THE CHAKRAS ARE GO TO HEAVEN. | 02 - Christ Oil, Brain Anatomy, and Kundalini, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| OUR CONSCIOUSNESS IS GENDERLESS, MEANING WE ARE A SPARK OF GOD | 01 - Syncretism and the Lightwave Universe, 03 - Born Again, the Serpent, and the Tree of Life, 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| GOD IS CONSCIOUSNESS. | 01 - Syncretism and the Lightwave Universe, 03 - Born Again, the Serpent, and the Tree of Life, 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| Hand Chakras serve as a vital interface between the physical and energetic dimensions, allowing us to engage with the world on both levels. | 02 - Christ Oil, Brain Anatomy, and Kundalini, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| These Minor Chakras play a HUGE role in facilitating A WIDE range of energy inflOW into THE HUMAN BODY AND CONSIOUSNESS. | 02 - Christ Oil, Brain Anatomy, and Kundalini, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| THIS RESULTS IN LACK OF AWARENESS OF THERE OWN CONSCIOUSNESS WHICH THEN CREATES A SOCIETY OPERATING THERE LIFES OUR OF THE LOWER CHAKARAS HEAD IS HEAVEN EL EL=GOD IS CONSCIOUSNESS RA NO ENDER MASCULINE FEMANINE FIRE WATER O SOL MON CONSCIOUS SUB-CONSCIOUS LEFT BRAIN RIGHT BRAIN -IN THE BIBLE THE HEAD IS REFERED TO AS THE UPPER ROOM WHERE JESUS MET THE 12 DISCIPLES. | 02 - Christ Oil, Brain Anatomy, and Kundalini, 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 08 - One Reality, Element Symbols, and Seven Heavens |
| FOR EXAMPLE, THIS SIDE OF THE BRAIN VIEWING HUMANS AS ONE UNITED CONSCIOUSNESS. | 01 - Syncretism and the Lightwave Universe, 03 - Born Again, the Serpent, and the Tree of Life, 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| We create with light | 01 - Syncretism and the Lightwave Universe, 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| THE EARTH IS THE HEART OF THE SOUL SYSTEM. | 03 - Born Again, the Serpent, and the Tree of Life, 04 - Pineal Gland, Holy Grail, and the Planes, 07 - Ether, Moon, and the Light Projection, 08 - One Reality, Element Symbols, and Seven Heavens |
| YOUR HEAD IS HEAVEN BECAUSE IT IS THE PLACE OF THYNE CONSCIOUSNESS/TRUE FORM. | 03 - Born Again, the Serpent, and the Tree of Life, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection, 08 - One Reality, Element Symbols, and Seven Heavens |
| SOUL SYSTEM -EARTH IS THE HEART OF THE SOUL SYSTEM AS IT IS IN THE MIDDLE OF THE SYSTEM. | 03 - Born Again, the Serpent, and the Tree of Life, 04 - Pineal Gland, Holy Grail, and the Planes, 07 - Ether, Moon, and the Light Projection, 08 - One Reality, Element Symbols, and Seven Heavens |
| The head is the place of consciousness, and it has the ability to see the other worlds. | 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection, 08 - One Reality, Element Symbols, and Seven Heavens |
| THE LEFT HEMISPHERE OF THE BRAIN BREAKS DOWN AND ANYLIZES THE RIGHT HEMIPHEARS UNITED PERCEPTION OF REALITY INTO SEPERATE FRAGMENTS SO THAT WE CAN MANIPULATE AND UNDERSTAND THINGS LOGICALLY. | 01 - Syncretism and the Lightwave Universe, 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| LIGHT GENESIS 1:3 "LET THERE BE LIGHT" WE LIVE INSIDE OF A LIGHTWAVE UNIVERSE WHERE ALL THINGS ARE CREATED OUT OF LIGHT. | 01 - Syncretism and the Lightwave Universe, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| THE SUBSTANCE OR BODY OF GOD IS LIGHT". | 01 - Syncretism and the Lightwave Universe, 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THE SUBSTANCE OF ALL CREATED THINGS IS LIGHT. | 01 - Syncretism and the Lightwave Universe, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| THEY ARE RECEIVED BASED ON WHAT FREQUENCY OUR MIND IS SET TO. | 01 - Syncretism and the Lightwave Universe, 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| EVERY FREQUENCY IS A COLOUR. | 01 - Syncretism and the Lightwave Universe, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| Our sexual energy/fluids must be retained if we wish to raise this psycho-physical oil back to our brain (heaven). | 02 - Christ Oil, Brain Anatomy, and Kundalini, 03 - Born Again, the Serpent, and the Tree of Life, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| By opening our chakras, preserving our sexual energy | 02 - Christ Oil, Brain Anatomy, and Kundalini, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| and maintaining the Christ oil, we can use the Power behind the sexual energy (kundalini) to raise it PINEAL GLAND up from the base of the spine back to the crown chakra in the brain. | 02 - Christ Oil, Brain Anatomy, and Kundalini, 03 - Born Again, the Serpent, and the Tree of Life, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THE KUNDALINI, OVER TIME, BECOMES A SELF-SUSTAINING ENERGY CIRCUIT FUELED BY FOOD AND WATER THAT GROWS AND GETS STRONGER. | 02 - Christ Oil, Brain Anatomy, and Kundalini, 03 - Born Again, the Serpent, and the Tree of Life, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THE SUN AND MOON CREATE THE SACRED FLUIDS WITHIN THE CLAUSTRUM IN THE BRAIN. | 02 - Christ Oil, Brain Anatomy, and Kundalini, 03 - Born Again, the Serpent, and the Tree of Life, 04 - Pineal Gland, Holy Grail, and the Planes |
| THE TWO SACRED FLUIDS ARE REFERRED TO IN THE BIBLE AS THE MILK AND HONEY. | 02 - Christ Oil, Brain Anatomy, and Kundalini, 03 - Born Again, the Serpent, and the Tree of Life, 04 - Pineal Gland, Holy Grail, and the Planes |
| BIRDS SYMBOLIZE THE HOLY SPIRIT/SOUL. vISHNU THE MIND IS THE SERPENT BECAUSE SERPENTS SYBOLIZE BRAHMA SHIVA KNOWLEDGE. | 03 - Born Again, the Serpent, and the Tree of Life, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| THIS IS WHY THE MIND IS IN THE MIDDLE | 01 - Syncretism and the Lightwave Universe, 03 - Born Again, the Serpent, and the Tree of Life, 04 - Pineal Gland, Holy Grail, and the Planes |
| CONSCIOUSNESS IS PRETTY MUCH EXPERIENCING A PROGRAM PLAYED OUT BY THE CENTRAL NERVOUS SYSTEM. | 03 - Born Again, the Serpent, and the Tree of Life, 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| PINeal THE PINEAL GLAND IS A CONED SHAPED BODY, 6mm HIGH AND 4mm IN DIAMETER gland -THE MIND ENHABITS THE PINEAL GLAND. -ITS THE ORGAN THROUGH WHICH THE ELECTRICAL FORCES OF THE BODY PLAY -IT'S WHAT THE UNIVERSAL ESSENCE/SOUL/CONSCIOUSNESS DEPOSITED -IT IS THE LIGHT OF THE BODY THAT GIVES LIFE TO THE WHOLE TEMPLE. -THE PINEAL IS THE MALE SPIRITUAL ORGAN. -THE PINEAL GLAND OPENS WHEN THE TWO EYES ARE CLOSED FOR PERIODS. -THE MORE SPIRITUAL WORK YOU DO THE MORE ACTIVE THE PINEAL GLAND BECOMES -THE PINEAL GLAND IS COVERED IN MICROCRYSTALS. | 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| THE VATICAN SUPPRESSED THE INFORMATION the pineal GLAND IS THE SEAT OF consciousness, also known as the ON THE PINEAL GLANDS' MYSTICAL POWERS. seat of the soul/throne of god. the pineal gland is an empty THE VATICAN (CATHOLIC CHURCH) TOOK OVER chamber that holds the universal essence which is invisable to the EUROPE AND DESTROYED/STOLE ALL THE naked eye. our true self is within the pineal gland and from this KNOWLEDGE AND LIBRARIES CONTAINING ALL centre we control the physical body. | 03 - Born Again, the Serpent, and the Tree of Life, 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THE CENTRE OF THE BRAIN IS THE PINEAL GLAND, WHICH WE REFER TO AS "I. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THIS BODY IS THE VEHICLE FOR OUR SOUL/ENTITY TO OPERATE WITHIN THIS PHYSICAL WORLD OF TIME AND SPACE. 33 VERDABREA THE THRONE OF GOD IS IN THE CENTRE OF THE BRAIN. | 03 - Born Again, the Serpent, and the Tree of Life, 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THE RIGHT HAND OF GOD IS THE RIGHT HEMISPHERE OF THE BRAIN. | 01 - Syncretism and the Lightwave Universe, 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THE CUP IS YOUR HEAD AND NECK, AND THE SUN IS YOUR CONSCIOUSNESS IN THE CENTRE OF THE BRAIN ON TOP OF YOUR NECK. | 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 08 - One Reality, Element Symbols, and Seven Heavens |
| THE BIRD IS AN AIR ANIMAL THAT SYMBOLIZES THE HIGHER NATURE OF MAN. | 03 - Born Again, the Serpent, and the Tree of Life, 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| MASONIC ART THIS MASONIC ART SYMBOLIZES THE SUN AND MOON CREATING THE "MILK AND HONEY" IN THE BRAIN. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 08 - One Reality, Element Symbols, and Seven Heavens |
| THE HONEY IS THE FLUID CREATED BY THE SUN. magnetic electric PITUITARY PINEAL MILK HONEY MOON SUN FEMALE MALE MAGNETIC ELECTRIC - + holy grail Corinthians 6:19-20 "Or do you not know that your body is a temple of the Holy Spirit within you, whom you have from God? | 02 - Christ Oil, Brain Anatomy, and Kundalini, 03 - Born Again, the Serpent, and the Tree of Life, 04 - Pineal Gland, Holy Grail, and the Planes |
| YOUR REALITY IS YOUR LEVEL OF REALI-ZATION. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 07 - Ether, Moon, and the Light Projection |
| PLANES OF EXISTENCE THERE ARE DIFFERENT LEVELS OF REALITY. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| IT IS THE WORLD OF THOUGHTS. | 01 - Syncretism and the Lightwave Universe, 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self |
| THEY ARE RECEIVED BASED UPON WHAT FREQUENCY OUR MIND IS SET TO. | 01 - Syncretism and the Lightwave Universe, 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| ITS BASICALLY THE WORLD OF IMAGINATION AND MENTAL PICTURES. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| WE CREATE WITH OUR THOUGHTS | 01 - Syncretism and the Lightwave Universe, 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THIS IS WHY THOUGHTS ARE THINGS. | 01 - Syncretism and the Lightwave Universe, 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self |
| THE HIGHER PLANES WILL EMBODY HIGH VIBRATIONAL THOUGHTS LIKE LOVE AND JOY, AND THE LOWER PLANES WILL BE DEMONIC THOUGHTS LIKE HATE, MURDER, AND LUST. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| DAEMONS, ANGELS, SPIRITS, AND JINS ARE LIVING WITHIN THE ASTRAL PLANE. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| ELEMENTALS ARE SPIRITS OF THE 4 ELEMENTS | 04 - Pineal Gland, Holy Grail, and the Planes, 07 - Ether, Moon, and the Light Projection, 08 - One Reality, Element Symbols, and Seven Heavens |
| LOWER ASTRAL ETHERIC PLANE THE ETHERIC PLANE IS THE WORLD OF ENERGY, ELECTRICITY AND MAGNETISM. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| IT IS THE 5TH ELEMENT, ALSO KNOWN AS SPIRIT OR AETHER. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 07 - Ether, Moon, and the Light Projection |
| THE ETHER IS A SUBSTANCE THAT HAS ONE FOOT IN THE PHYSICAL WORLD AND ONE FOOT IN THE ASTRAL WORLD. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 07 - Ether, Moon, and the Light Projection |
| ETHER IS WHERE WE GET THE WORD EITHER FROM. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 07 - Ether, Moon, and the Light Projection |
| THE WORD TOGETHER HAS THE WORD ETHER WITHIN IT. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 07 - Ether, Moon, and the Light Projection |
| YOU CHANGE THE PHYSICAL PLANES. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| WHATEVER YOU SEE AND EXPERIENCE IS THE EFFECT OF YOUR MIND. | 01 - Syncretism and the Lightwave Universe, 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self |
| THE INTO THE PHYSICAL WORLD | 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| EVERYTHING YOU THINK OF WILL MANIFEST INSTANTLY IN THE ASTRAL PLANE (4TH DIMENSION) YOUR VISION IN THE ASTRAL PLANE WILL NOT BE VERY CLEAR WHEN YOU FIRST ASTRAL PROJECT. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| HOW ASTRAL PROJECTION WORKS YOUR MIND IS THE PROJECTOR OF YOUR SOUL. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| YOUR SOUL IS THE EXPERIENCER (OBSERVER). | 03 - Born Again, the Serpent, and the Tree of Life, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| PRACTICES FOR ASTRAL PROJECTION LIE DOWN FLAT WITH NO BODY PARTS TOUCHING REST EVERY SINGLE MUSCLE AND BE AS STILL AS POSSIBLE CLOSE YOUR EYES BREATH DEEP IN THROUGH THE NOSE AND SLOWLY OUT THE MOUTH MEDITATE UNTIL YOU HAVE LOST ALL DESIRES AND THE MIND IS EMPTY OF THOUGHTS THEN FOCUS YOUR ATTENTION ON THE MIDDLE OF YOUR BRAIN (PINEAL GLAND) DO THIS UNTIL YOU START TO FEEL TINGLING SENSATION ALL OVER THE BODY THE TINGLING SENSATION IS YOUR ENERGY BODY (ETHERIC BODY) BEING AWAKENED NOW IMAGINE YOURSELF PULLING A ROPE UP INTO THE SKY YOU MAY FEEL YOURSELF BEING LIFTED OUT OF THE BODY | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THE WATER IS THE ETHERAL PLANE, WHICH IS THE VEIL BETWEEN THE PHYSICAL WORLD AND THE ASTRAL WORLD. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 07 - Ether, Moon, and the Light Projection |
| WE DESCENDED FROM SPIRIT INTO MATTER | 01 - Syncretism and the Lightwave Universe, 05 - Astral Plane, Chakras, and the True Self, 07 - Ether, Moon, and the Light Projection |
| O MENTAL PLANE = THOUGHTS ASTRAL PLANE = IMAGINATION 48x2=96 ETHERIC PLANE = ENERGY 96+48=144 | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THE MIND IS MANIFESTING WHAT THE SOUL -SO THIS IS SYMBOLIC FORDESTORYING YOUR LOWER/ANIMAL WILLS TO DO. | 01 - Syncretism and the Lightwave Universe, 03 - Born Again, the Serpent, and the Tree of Life, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| WE COME FROM THE ONE, AND WE INCARNATE INTO DUALITY TO GAIN THE KNOWLEDGE OF GOOD AND EVIL. | 03 - Born Again, the Serpent, and the Tree of Life, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| THE MINDS THAT OPERATE ON THEIR LOWER FREQUENCIES WILL BE ATTRACTED TO THE COLOURS OF THEIR LOWER FREQUENCIES. | 01 - Syncretism and the Lightwave Universe, 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| EACH ONE OF US OPERATES WITHIN A FREQUENCY, AND THAT FREQUENCY IS A COLOUR WITHIN THE ELECTROMAGNETIC LIGHT SPECTRUM. | 01 - Syncretism and the Lightwave Universe, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| THIS IS WHY WE CALL IT A MINDSET YOUR MIND SETS ITSELF TO VARIOUS FREQUENCIES. | 01 - Syncretism and the Lightwave Universe, 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| Consequently, the Hand Chakras wield significant influence over the information that enters our consciousness. there exists a network of energy centers known as Minor Chakras in the feet (AS ABOVE SO BELOW). | 02 - Christ Oil, Brain Anatomy, and Kundalini, 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| RIGHT BRAIN THE RIGHT BRAIN IS THE FEMANINE ASPECT OF THE BRAIN. | 01 - Syncretism and the Lightwave Universe, 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| IT CREATES A WHOLISTIC PERCEPTION OF REALITY WHERE ALL THINGS ARFE UNITED AND ONENESS. | 01 - Syncretism and the Lightwave Universe, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 08 - One Reality, Element Symbols, and Seven Heavens |
| LEFT BRAIN THE LEFT HEMISPHERE IS THE ANALYTIC SIDE OF THE BRAIN. | 01 - Syncretism and the Lightwave Universe, 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THE CENTRE OF THE BRAIN IS THE "MOST IF YOU ADD ANY OF THE SOLFEGGIO HOLY HOUSED" IN THE BIBLE. | 02 - Christ Oil, Brain Anatomy, and Kundalini, 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THIS PLACE IS THE THRONE OF GOD/CONSCIOUSNESS WITHIN THE PINEAL GLAND. | 03 - Born Again, the Serpent, and the Tree of Life, 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THE PINEAL GLAND IS THE PLACE OF THYNE CONSCIOUSNESS, AND IT HAS ACCESS TO THE ASTRAL PLANE. concentration contemplation meditation HEAD HEAVEN masculine femanine solar lunar yang yin HEEL HELL early christian artwork HEAD IS HEAVEN OBSERVER/INNER BEING/CONCIOUSNESS OBSERVER/INNER left hemisphear right hemisphear BEING/CONCIOUSNESS left hemisphear right hemisphear EGYPTIAN FALCON OF HORUS EGYPTIAN DJED PILLAR holy grail central nervous system two hemispheres soul/conciousness spine KNOW THYSELF merkaba CELESTIAL SPHERE TO PORTRAY DIFFERENT PLANES OF REALITY MER=LIGHT KA=SPIRIT BA=BODY eye of horus VEHICLE OF ASCENSION HORUS IS THE SUN SUN=SOL=SOUL NEUTRALIZING THE DUALITY OF SELF BY COMBINING THE UPPER AND LOWER SELF. | 03 - Born Again, the Serpent, and the Tree of Life, 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| Jesus said, "Man will never see death, for there is no death to see or know." The body manifests PHYSICAL dveil the spirit | 02 - Christ Oil, Brain Anatomy, and Kundalini, 03 - Born Again, the Serpent, and the Tree of Life, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| nothing is not light. | 01 - Syncretism and the Lightwave Universe, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| THE RIGHT BRAIN PRESENTS REALITY AS A UNIFIED WHOLE, WHICH EXPLAINS WHY THE PEOPLE IN POWER HAVE SPLIT UP ALL THE FIELDS OF KNOWLEDGE INTO DIFFERENT CATEGORIES WHEN IT IS ALL ACTUALLY ONE UNIFIED SCIENCE, WHICH IS DONE INTENTIONALLY TO KEEP US LEFT-BRAIN DOMINANT. | 01 - Syncretism and the Lightwave Universe, 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| HOWEVER, WE MUST BALANCE THESE TWO ASPECTS OF THE BRAIN SO THAT WE DON'T BECOME LEFT OR RIGHT-BRAIN DOMINANT. | 01 - Syncretism and the Lightwave Universe, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| IT HAS ONE FOOT IN THE PHYSICAL WORLD AND IN THE ASTRAL PLANE, IT'S ON EITHER SIDE. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 07 - Ether, Moon, and the Light Projection |
| THE WORD ETHER IS EITHER. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 07 - Ether, Moon, and the Light Projection |
| THEY ARE COMPOSED OF EACH OTHER BY TRANSMUTATION. -ALL OF THE ELEMENTS ARE BORN FROM THE 1ST ELEMENT ETHER (SPIRIT). -THE 4 PHYSICAL ELEMENTS ARE THE 4 VIBRATIONAL STATES OF THE ETHER. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 07 - Ether, Moon, and the Light Projection |
| THE NEUTRAL, ZERO PLANE OF EVERY ELECTROMAGNETIC FIELD IS THE BIRTH OF PHYSICAL MATTER. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 07 - Ether, Moon, and the Light Projection |
| HORUS SYMBOLISES THE SUN, AND SET SYMBOLISES THE MOON, AND THEY ARE BEING SPUN BY THE CENTRE POLE. | 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection, 08 - One Reality, Element Symbols, and Seven Heavens |
| THE HEART IS THE MIDDLE OF THE EARTH=HEART BODY. | 03 - Born Again, the Serpent, and the Tree of Life, 07 - Ether, Moon, and the Light Projection, 08 - One Reality, Element Symbols, and Seven Heavens |
| IT ALSO SYMBOLIZES SPIRIT (LIGHT) AND MATTER (BLACK) (YIN AND YANG). | 03 - Born Again, the Serpent, and the Tree of Life, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| THE EARTH IS THE HEART, MEANING THE MIDDLE. | 03 - Born Again, the Serpent, and the Tree of Life, 07 - Ether, Moon, and the Light Projection, 08 - One Reality, Element Symbols, and Seven Heavens |
| THE MIDDLE OF THE ELECTROMAGNETIC COLOUR SPECTRUM IS GREEN. | 01 - Syncretism and the Lightwave Universe, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| WHEN WE ASTRAL PROJECT OURSELF OUTSIDE OF THE PHYSICAL BODY, WE ARE INDEED LEAVING THE PHYSICAL PLANE WE CALL EARTH AND ENTERING THE ASTRAL PLANE. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 07 - Ether, Moon, and the Light Projection |
| HEAVEN IS ABOVE EARTH, THROUGH THE BLUE SKY. | 03 - Born Again, the Serpent, and the Tree of Life, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| HEAD AND HEAVEN ARE THE SAEM ROOT WORDS. | 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection, 08 - One Reality, Element Symbols, and Seven Heavens |
| SPIRIT IS ALSO ETHER. | 01 - Syncretism and the Lightwave Universe, 05 - Astral Plane, Chakras, and the True Self, 07 - Ether, Moon, and the Light Projection |
| ETHER IS THE SUBSTANCE THAT ETHERIAL WORLDS BEYOND THIS WORLD. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 07 - Ether, Moon, and the Light Projection |
| IF CONNECTS THE PHYSICAL WORLD TO THE YOU LOOK AT STARS WITH A TELESCOPE SPIRITUAL WORLD (ASTRAL). | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 07 - Ether, Moon, and the Light Projection |
| EARTH IS AN ANAGRAM FOR THE HEART. | 03 - Born Again, the Serpent, and the Tree of Life, 07 - Ether, Moon, and the Light Projection, 08 - One Reality, Element Symbols, and Seven Heavens |
| THE HEART IS THE BALANCE POINT BETWEEN TWO OPPOSING the world it falls due to heavy attachments to the mind. | 03 - Born Again, the Serpent, and the Tree of Life, 07 - Ether, Moon, and the Light Projection, 08 - One Reality, Element Symbols, and Seven Heavens |
| THE WORLDS BELOW. external world to become lighter and at peace with all. then and and produced therein all kinds only then shall the soul pass upward to the light. of things in due balance." the word reality is similar to realize. your level of realization is your level of reality. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self, 07 - Ether, Moon, and the Light Projection |
| You can only experience one reality at a time. | 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres, 08 - One Reality, Element Symbols, and Seven Heavens |
| ALL THINGS COME FROM THE ONE, THEREFORE ALL THINGS ARE ONE. | 01 - Syncretism and the Lightwave Universe, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| TO GAIN A FULL UNDERSTANDING OF THE INFORMATION THIS BOOK PRESENTS, YOU MUST FIRST FREE YOUR MIND FROM THE INDOCTRINATIONS GIVEN BY THE EDUCATIONAL SYSTEMS WE WERE FORCED TO ATTEND TO AND, SECONDLY, TRY AND PERCEIVE REALITY AS ONE UNITED AND WHOLISTIC CREATION. | 01 - Syncretism and the Lightwave Universe, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| HUMAN HUE MAN AS A HUE MAN, WE ARE AN ATTRIBUTE OF A COLOUR THAT PERMITS THEM TO BE CLASSED THAT SPECIFIC COLOUR. | 01 - Syncretism and the Lightwave Universe, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| EACH INDIVIDUAL IS THE MIND, NOT THE PHYSICAL BODY. | 01 - Syncretism and the Lightwave Universe, 03 - Born Again, the Serpent, and the Tree of Life |
| IF WE SET OUR MIND TO A SPECIFIC TOPIC, LIKE GENERATING WEALTH, FOR EXAMPLE, WE TUNE INTO THAT FREQUENCY IN THE MENTAL PLANE, AND WE WILL RECEIVE THOUGHTS ON HOW TO GENERATE WEALTH. | 01 - Syncretism and the Lightwave Universe, 04 - Pineal Gland, Holy Grail, and the Planes |
| OUR MID IS GENERALLY OPERATING OFF ONE SPECIFIC FREQUENCY BASED UPON OUR DAILY THINKING PATTERNS. | 01 - Syncretism and the Lightwave Universe, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THIS IS WHY THE WORD HUMAN MEANS AN ATTRIBUTE OF A COLOUR. | 01 - Syncretism and the Lightwave Universe, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THE ELEMENTS ONLY EXIST WITHIN THE ELEMENT MIND. | 01 - Syncretism and the Lightwave Universe, 07 - Ether, Moon, and the Light Projection |
| GOD IS THINKING ALL THINGS INTO EXISTANCE. | 01 - Syncretism and the Lightwave Universe, 04 - Pineal Gland, Holy Grail, and the Planes |
| OIL PROCESS: 1-THE CLAUSTRUM (CLAUS=SANTA CLAUSE) PRODUCES THE PSYCHO-PHYSICAL THE BRAIN in the bible is: FLUID WHICH THEN GOES TO THE PINEAL AND PITUITARY GLAND IDA PINGALA -THE UPPER ROOM WHERE JESUS 2-THE PINEAL GLAND ELECTRICALLY CHARGES THE FLUID (MALE/ JOSEPH) MEETS THE 12 DISCIPLES/12 CRANIAL NERVES 3-THE PITUITARY GLAND MAGNETICALLY CHARGES THE FLUID (FEMALE/ MARY) -THE HOLY LAND 4-THEN THE FLUID WILL TRAVEL DOWN THE TWO NERVES, THE IDA WHICH IS -the LAND FLOWING WITH MILK AND HONEY CONNECTED TO THE PITUITARY, AND THEN THE PINGALA WHICH IS CONNECTED -promise land of israel TO THE PINEAL GLAND. | 02 - Christ Oil, Brain Anatomy, and Kundalini, 03 - Born Again, the Serpent, and the Tree of Life |
| THEN IT BECAME CHRIST 7-THIS WILL THEN PASS TO THE PINEAL GLAND AND THEN TO THE CEREBRUM WHICH WILL REBIRTH/RESURRECT ALL BRAIN CELLS, ACTIVATE THE PINEAL GLAND, CORINTHIANS 13:5 AND REGENERATE ALL THE CELLS IN THE BODY "DO YOU NOT KNOW THAT JESUS THIS PROCESS IS SYMBOLISED AS BEING "BORN AGAIN" CHRIST IS WITHIN YOU?" SUSHUMNA HOW TO RAISE THE OIL THE IDA (FEMANINE) CHANNLE IS CONNECTED TO THE -RETAIN YOUR SEXUAL FLUIDS PITUITARY GLAND. | 02 - Christ Oil, Brain Anatomy, and Kundalini, 03 - Born Again, the Serpent, and the Tree of Life |
| JESUS (THE OIL) GOES DOWN THE RIVER JORDAN (THE SPINE) TO BETHLEHEM NEXT TO THE DEAD SEA (SACRUM BONE). | 02 - Christ Oil, Brain Anatomy, and Kundalini, 03 - Born Again, the Serpent, and the Tree of Life |
| JOSEPH AND MARY (PINEAL AND PITUITARY GLAND) ARE WAITING FOR JESUS (THE OIL) TO RETURN. | 02 - Christ Oil, Brain Anatomy, and Kundalini, 03 - Born Again, the Serpent, and the Tree of Life |
| THE PROCESS OF THE OIL COMING DOWN FROM THE HEAD SYMBOLIZES JESUS COMING DOWN FROM HEAVEN INTO PHYSICAL FORM. | 02 - Christ Oil, Brain Anatomy, and Kundalini, 03 - Born Again, the Serpent, and the Tree of Life |
| JESUS DYING FOR 3 DAYS AND THEN BEING RESURRECTED TO BE CRUCIFIED AT 33 IS A METAPHORICAL STORY ABOUT THE CHRIST OIL PROCESS WITHIN THE BODY WHICH ACTIVATES 100% OF THE BRAIN. | 02 - Christ Oil, Brain Anatomy, and Kundalini, 03 - Born Again, the Serpent, and the Tree of Life |
| JORDAN RIVER The story of Jesus is metaphorical for the journey of the sacred oil the brain produces. | 02 - Christ Oil, Brain Anatomy, and Kundalini, 03 - Born Again, the Serpent, and the Tree of Life |
| The oil coming down from the brain is god descending from heaven to earth. jesus dying for 3 days in the cave is symbolic of the sacred fluid staying in the sacrum bone at the base of the spine (the cave) for some time. | 02 - Christ Oil, Brain Anatomy, and Kundalini, 03 - Born Again, the Serpent, and the Tree of Life |
| Then once the oil is resurrected, meaning ACTIVATING THE KHUNDALINI TO RIASE THE OIL BACK UP THE SPINE, it travels passed all of the 33 vertebras on the back of the spine and crosses the vagus nerve. the SACRED SACRUM oil crossing the vagus nerve is Jesus being crucified at 33 years of age because there are /CAVE WHERE JESUS 33 vertebras on the BACK OF THE spine. the death of Jesus symbolizes being born again WAS DEAD FOR 3 DAYS and turning spirit matter in spirit. | 02 - Christ Oil, Brain Anatomy, and Kundalini, 03 - Born Again, the Serpent, and the Tree of Life |
| THE CEREBROSPINAL SYSTEM IS THE DEAD SEA= SACRUM BONE/ AN EXTENTION OF THE BRAIN SOLAR PLEXUS CHRIST OIL THE CHRIST OIL PASSES THE 33 VERTEBRAS OF THE SPINE AND THEN PASSES THE VAGUS NERVE WHICH CROSSES OVER SPINAL CORD JESUS WAS CRUCIFIED AT 33 BECAUSE IT WAS THE CRUCIFICTION OF THE CHRIST OIL PASSING THE 33 VERDABREAS AND CROSSING THE VAGUS NERVE. | 02 - Christ Oil, Brain Anatomy, and Kundalini, 03 - Born Again, the Serpent, and the Tree of Life |
| VAGUS NERVE 33 VERDABREAS FOR THE 33 YEARS OF CHRIST/CHRIST OIL. | 02 - Christ Oil, Brain Anatomy, and Kundalini, 03 - Born Again, the Serpent, and the Tree of Life |
| JESUS DYING AT 33 ALSO SYMBOLIZES TURNING MATTER INTO SPIRIT WHEN MOVING THE OIL PAST THE 33 VERDABREAS. | 02 - Christ Oil, Brain Anatomy, and Kundalini, 03 - Born Again, the Serpent, and the Tree of Life |
| HE THEN SAW A LADDER THAT REACHED HEAVEN, WHICH IS THE SPINAL CORD LEADING UP TO THE BRAIN (HEAVEN). | 03 - Born Again, the Serpent, and the Tree of Life, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THE SUN IS POSITIVE, MALE & ELECTRIC. | 03 - Born Again, the Serpent, and the Tree of Life, 07 - Ether, Moon, and the Light Projection |
| THE THE MOON IS NEGATIVE, FEMALE, MAGNETIC. | 03 - Born Again, the Serpent, and the Tree of Life, 07 - Ether, Moon, and the Light Projection |
| THE LAND FLOWING WITH MILK AND HONEY IS THE BRAIN. | 02 - Christ Oil, Brain Anatomy, and Kundalini, 03 - Born Again, the Serpent, and the Tree of Life |
| SUSHUMNA MASONIC ART CROWN CHAKARA (TOP OF THE HEAD) MOON/MAGNETIC /FEMALE SUN/ELECTRIC/MALE TWO SERPENTS TO SYMBOLIZE THE TWO KHUNDALINI CHANNELS WRAPED AROUND THE SPINE "LORD" = HIGHER SELF/INNER YOU/OBSERVER/CHRIST MILK=MOON=PITUITARY GLAND HONEY=SUN=PINEAL GLAND THE FIRE AT THE BOTTOM OF THE MEDICAL SYMBOL ARTWORK SYMBOLIZES KUNDALINI ENERGY AT YOUR SPINE'S BASE. | 03 - Born Again, the Serpent, and the Tree of Life, 04 - Pineal Gland, Holy Grail, and the Planes |
| ACTIVATION OF THE KUNDALINI ENERGY AT THE SPINE BASE IS THE FORCE USED TO PUSH THE CEREBROSPINAL FLUID UP THE SPINE TO REACH THE PINEAL GLAND. | 02 - Christ Oil, Brain Anatomy, and Kundalini, 03 - Born Again, the Serpent, and the Tree of Life |
| THE STORY OF JESUS IS SYMBOLIC OF THE ALCHEMICAL PROCESS THAT OCCURS MONTHLY WITHIN THE HUMAN BODY. | 02 - Christ Oil, Brain Anatomy, and Kundalini, 03 - Born Again, the Serpent, and the Tree of Life |
| JESUS FALLS FROM HEAVEN AND INCARNATES ON THE EARTH, WHICH IS SYMBOLIC OF THE CHRIST OIL TRAVELING DOWN THE SPINE FROM YOUR BRAIN (HEAVEN). | 02 - Christ Oil, Brain Anatomy, and Kundalini, 03 - Born Again, the Serpent, and the Tree of Life |
| THE SACRED OIL STAYS STILL WITHIN THE SACRUM BONE FOR 3 DAYS, WHICH IS JESUS BEING DEAD IN THE CAVE FOR THREE DAYS. | 02 - Christ Oil, Brain Anatomy, and Kundalini, 03 - Born Again, the Serpent, and the Tree of Life |
| ONCE JESUS RESURRECTS (THE OIL RSING UP THE SPINE) HE GETS CRUCIFIED AT 33 YEARS OF AGE. | 02 - Christ Oil, Brain Anatomy, and Kundalini, 03 - Born Again, the Serpent, and the Tree of Life |
| THE SPINE CONTAINS 33 VERDABREAS, AND ONCE THE OIL PASSES ALL 33 VERDABREAS AND REACHES THE OPTIC THALAMUS, IT GETS CRUCIFED ON THE CROSS BECAUSE THE THALAMUS LOOKS LIKE A CROSS. | 02 - Christ Oil, Brain Anatomy, and Kundalini, 03 - Born Again, the Serpent, and the Tree of Life |
| THE DEATH OF JESUS SYMBOLIZES TURNING MATTER INTO SPIRIT AS THE RETURN OF THE OIL GIVES THE HUMAN SUPERNATURAL ABILITIES LIKE ASTRAL TRAVEL. | 02 - Christ Oil, Brain Anatomy, and Kundalini, 03 - Born Again, the Serpent, and the Tree of Life |
| IT PROJECTS THE SOUL INTO THE REALITY WE CHOOSE TO EXPERIENCE. body mind THE SOUL (BRAHMA) HAS MULTIPLE FACES, SYMBOLISING THE SOUL TAKING ON DIFFERENT BODIES | 03 - Born Again, the Serpent, and the Tree of Life, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| All of this is the GENISIS 2:10 expression of the one universal breath of life. body EARTH=BODY MOON=MIND SUN=SOUL THE 4 RIVERS FLOWING IN THE GARDEN OF EDEN ARE THE 4 HOLY FLUIDS IN THE BODY WHICH ARE: 1) BLOOD 2) SELIVER mind soul 3) CHRIST OIL body mind soul 4) SEMEN/VAGINAL FLUID THE TEMPLE OF SOLOMON IS YOU SPIRIT head EARTH AIR Sol=SOUL THE BODY IS THE TEMPLE MON=MIND hea heaven OF THE SOUL AND MIIND WATER FIRE YOU ARE A STAR STER=STAR A AND E ARE INTERCHANGABLE MISTER MINISTER, SISTER, MONSTER, SUPER STAR, MASTER, FRAUSTER, SINISTER. you are a qantom photon (a star) in a physical body. you are all knowing and directly from the source, in other words you are god/godess experiencing THE PROGRAM BEING RAN BY THE CENTRAL NERVOUS SYSTEM. while we are incarnated here we are divided from source and absent of the knowledge of our true divine heel insight. hell THE PINEAL GLAND THE PINEAL GLAND | 03 - Born Again, the Serpent, and the Tree of Life, 04 - Pineal Gland, Holy Grail, and the Planes |
| THE GROUND ANIMALS SYMBOLISE THE LOWER NATURE OF MAN. | 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THE MILK IS THE FLUID CREATED BY THE MOON. | 03 - Born Again, the Serpent, and the Tree of Life, 04 - Pineal Gland, Holy Grail, and the Planes |
| IN OTHER WORDS, EACH PLANE IS A PRODUCT OF THE PLANE THAT IS ABOVE. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self |
| THE HIGHER THE PLANE, THE MORE FLUID/FORMLESS IT BECOMES | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self |
| THIS IS WHY WE CALL IT A MINDSET. | 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THE WORLD OF THOUGHT IS COMPLETELY FORMLESS. | 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THE SCREEN WE SEE IN OUR MIND WHEN WE IMAGINE SOMETHING IS THE ASTRL PLANE. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self |
| DEPENDING ON THE VIBRATIONAL FREQUENCY OF THE THOUGHT, MANIFESTING WILL RESULT IN THE THOUGHT FORM MANIFESTING ON THE HIGHER MIDDLE OR LOWER ATRAL PLANES. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self |
| YOU WILL ONLY SEE AND ENCOUNTER BEINGS THAT ARE ON A SIMILAR FREQUENCY AS YOU. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self |
| THEY ARE ENTITIES THAT HAVE THE ABILITY TO MATERIALIZE OR STAY IN THE ASTRAL BODY AT THEIR WILL. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self |
| PHYSICAL PLANE THE PHYSICAL PLANE IS THE WORLD OF MATTER. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self |
| IT IS THE PHYSICAL WORLD OF EFFECT. | 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THIS IS WHERE WE GET THE SAYING ABOVE, SO BELOW. | 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| MAGICIANS AND OCCULTISTS DO HAVE METHODS TO HAVE CONTACT WITH THESE ASTRAL AND ETHERIC ENTITIES, WHICH THEN HAVE THE ABILITY TO MANIPULATE THE PHYSICAL PLANE. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self |
| THERE IS NO POINT IN LOOKING DOWN HERE BECAUSE THE PHYSICAL PLANE IS THE WORLD OF EFFECT | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self |
| THE ETHEREAL PLANE IS IN CONSTANT ROTATION WITH THE PHYSICAL PLANE THROUGH RHYME, KARMA, POLARITY, AND GENDER. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self |
| STARS ARE THE START OF THE SOUL SYSTEM. | 04 - Pineal Gland, Holy Grail, and the Planes, 07 - Ether, Moon, and the Light Projection |
| YOU CREATE DEAMONS THE IDEAS WE MENTALLY ENTERTAIN CAN TAKE FORM IN THE 4TH DIMENSIONAL PLANE. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self |
| EVERY SINGLE MENTAL ADDICTION YOU HAVE IS SOME DEAMON YOU CREATED WITHIN THE ASTRAL PLANE. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self |
| IT GROWS THE MORE EMOTION (ENERGY IN MOTION) YOU GIVE IT. | 03 - Born Again, the Serpent, and the Tree of Life, 05 - Astral Plane, Chakras, and the True Self |
| MOON IS MIND, WE CREATE DEAMONS WITH OUR MINDS. | 03 - Born Again, the Serpent, and the Tree of Life, 05 - Astral Plane, Chakras, and the True Self |
| IT IS SYMBOLIC FOR LEAVING THE PHYSICAL BODY. | 03 - Born Again, the Serpent, and the Tree of Life, 05 - Astral Plane, Chakras, and the True Self |
| THE CHAKARAS ARE 7 WHEELS OF ENERGY THAT ARE A PART OF THE ELECTROMAGNETIC FIELD WE CALL OUR AURA. | 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THE CHAKARAS ARE A PART OF THE ETHERIC BODY AS THEY ARE 7 SEALS THAT BIND YOUR SOUL/SPIRIT TO THE PHYSICAL BODY. | 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THE CROWN CHAKARA IS LOCATED JUST ABOVE THE HEAD, OUT OF THE BODY BECAUSE ITS PURE SPIRIT. | 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| OUR TRUE GOD SELF IS HIDDEN BEHIND THE 7 CHAKRAS, AS THE CHAKRAS CAN BE ABUSED OR BALANCED. | 05 - Astral Plane, Chakras, and the True Self, 07 - Ether, Moon, and the Light Projection |
| WHEN THE MIND & BODY MANIFEST THE SOUL/HIGHER SELF IDEAS 24/7, WE BECOME OUR TRUE GOD SELF, AND THERE ARE NO MENTAL OR ETHERIC BLOCKAGES WITHIN OUR DIFFERENT BODIES OF CONSCIOUSNESS. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self |
| third eye=2 petals | 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| ETHER IS THE WORD EITHER BECAUSE ITS ON EITHER SIDE. | 04 - Pineal Gland, Holy Grail, and the Planes, 05 - Astral Plane, Chakras, and the True Self |
| THIS IS A ON THE ETHERIC PLANE, AND WHEN WE FREQUENCY YOU NEED TO ACHIEVE IN ORDER TO GO FROM THE ROOT TO THE CROWN CHAKRA (HEAD=HEAVEN) M UNLOCK THESE CENTRES, WE UNLOCK OUR TRUE SPIRIT FORM. | 05 - Astral Plane, Chakras, and the True Self, 07 - Ether, Moon, and the Light Projection |
| THE HIGHER 3 CHAKRAS ARE THE HIGHER STATES OF CONSCIOUSNESS WHERE YOUR DEUTERONOMY 20:17 MIND IS NO LONGER MANIFESTING "Completely destroy them—the Hittites, Amorites, Canaanites, WHATEVER THE LOWER SELF DESIRES. | 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THIS STATE OF CONSCIOUSNESS IS MANIFESTING HELL. | 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| IT SYMBOLIZES AN INDIVIDUAL'S MINDSET. | 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| THIS IS BECAUSE THEY UNDERSTAND THAT 80% OF PEOPLE'S MINDS MANIFEST THE DESIRES OF THE LOWER 3 CHAKRAS. | 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THE WORD HUMAN COMES FROM THE WORD HUE, WHICH MEANS AN ATTRIBUTE OF A COLOUR. | 01 - Syncretism and the Lightwave Universe, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| WE ARE AN ATTRIBUTE OF A SPECIFIC COLOUR BASED ON WHAT OUR MIND IS SETTING OUR FREQUENCY TO. | 01 - Syncretism and the Lightwave Universe, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| When the Minor Chakras in the feet operate harmoniously and are in alignment with the Major Chakras, it establishes a continuous connection and a flow of communication between the Earth's energy grids and our own energies. | 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| ROOT CHAKARA CORRESPONDS WITH THE EARTH ELEMENT AS ITS THE MOST PHYSICAL/METERIALISTIC CHAKRA. | 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THE SKY IS BLUE AND CAN TURN PURPLE AT NIGHT, WHICH SYNCS IN WITH THE HIGHER THREE CHAKARAS. | 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| THE EARTH IS GREEN, AND THE HEART CHAKARA IS GREEN, AS ABOVE AND BELOW. | 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| SET HORUS GROUND ANIMAL-OX AIR ANIMAL-BIRD LOWER SELF HIGHER SELF THE DEVIL HAS GROUND ANIMAL FEATURES SYMBOLIZING THE LOWER SELF. | 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THE 12 DISCIPLES ARE THE 12 CRANIAL NERVES IN THE BRAIN WHICH ARE THE 12 ZODIAC SIGNS. -MOSES CROSSING THE RED SEA IS MOVING YOUR PERCEPTION/AWARENESS INTO THE RIGHT HEMISPHERE OF THE BRAIN. | 02 - Christ Oil, Brain Anatomy, and Kundalini, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THE RIGHT HEMISPHERE SHOWS THE UNIFIED PERCEPTION OF REALITY. | 01 - Syncretism and the Lightwave Universe, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| IT IS ALSO THE PLACE OF OUR INTUITION, CREATIVITY, AND INSIGHT. | 03 - Born Again, the Serpent, and the Tree of Life, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| IT BREAKS DOWN THE UNITED PERCEPTION OF THE RIGHT HEMISPHERE INTO SINGULAR SEGMENTS. | 01 - Syncretism and the Lightwave Universe, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THE LEFT BRAIN SEES HUMANITY AS INDIVIDUALS AND NOT UNIFIED LIKE THE RIGHT BRAIN. | 01 - Syncretism and the Lightwave Universe, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| SCALE FREQUENCIES UP THEY ALL ADD TO 3,6 OR 6 HEAD IS HEAVEN head=hea=heaven God (higher self) is reaching/ stretching over to TRY to CONNECT WITH Adam (lower self) | 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| ALL YOU HAVE TO DO IS FOLLOW THE COMMANDS OF THE HIGHER SELF (HIGHER MIND/THOUGHTS). | 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| YOU ARE A SOUL THAT YOU ARE AN ETERNAL EXPERIENCES DIFFERENT REALITIES WITHIN THE SUN/SOUL MULTI-VERSE. | 05 - Astral Plane, Chakras, and the True Self, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| IN EACH PLANE YOU TAKE ON THE SINGLE EYE IS THE DIFFERENT BODIES. | 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| YOUR AIM IS TO BECOME A SYMBOL OF THE SOUL MULTI-DIMENSIONAL CREATURE AND NOT TO BE EYE OF THE SOUL BOUND TO JUST ONE REALITY. 5 SENSES OF THE SOUL MENTAL devil consciousness The body does not live. | 03 - Born Again, the Serpent, and the Tree of Life, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| It is only maintained by the ASTRAL veils ETHERIC spirit/consciousness within. | 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| Actions of the body are under the command of the centering soul. | 03 - Born Again, the Serpent, and the Tree of Life, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| The body is an electrical machine that takes commands from the omnipotent cosmic intelligence. | 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| To think is to create. | 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| All else are electrically acting based ANOTHER VEIL ON TOP OF YOUR TRUE SOUL upon instinct. | 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| Corinthians 3:16-17 16 Know ye not that ye are the temple of God | 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| and that the Spirit of God = dwelleth in you? 17 If any man defile the temple of God, SYMBOL FOR SPIRIT him shall God destroy | 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| for the temple SPIRIT IS IN THE HEAD of God is holy, which temple ye are. | 04 - Pineal Gland, Holy Grail, and the Planes, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| BOTH BRAINS HAVE SEPARATE VIEWS AND PERCEPTION OF THE WORLD. | 01 - Syncretism and the Lightwave Universe, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| ALL THINGS COME FROM THE ONE THEREFORE ALL IS ONE. | 01 - Syncretism and the Lightwave Universe, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THE LEFT BRAIN'S PURPOSE IS TO ANALYZE AND BREAK DOWN THE UNIFIED WHOLE PRESENTED BY THE RIGHT BRAIN. | 01 - Syncretism and the Lightwave Universe, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THIS PROCESS IS DONE BY THE LEFT HEMISPHERE SO THAT WE CAN HAVE DISTINCT SINGULAR FRAGMENTS OF REALITY SO THAT IT CAN MANIPULATE, MANAGE AND CONTROL IT. | 01 - Syncretism and the Lightwave Universe, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THE LEFT BRAIN MAINTAINS A SENSE OF DETACHMENT FROM THE DIRECT EXPERIENCE TO EXERT CONTROL OVER IT, WHILE THE RIGHT BRAIN STAYS IN THE PRESENT MOMENT AND WHOLEHEARTEDLY EXPERIENCES IT. | 01 - Syncretism and the Lightwave Universe, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THE RIGHT BRAIN RELIES ON THE LEFT BRAIN BECAUSE ITS HOLISTIC PERCEPTION WHILE CAPTURING THE ESSENCE OF THE WHOLE MAY LACK PRECISION AND CLARITY. | 01 - Syncretism and the Lightwave Universe, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| THE LEFT BRAIN REQUIRES THE RIGHT BRAIN BECAUSE ALTHOUGH IT PRODUCES MENTAL CLARITY, IT CAN LOSE SITE OF THE CONNECTION BETWEEN ALL THINGS AND TRAP THE INDIVIDUAL IN A FRAGMENTED WORLDVIEW. | 01 - Syncretism and the Lightwave Universe, 06 - Chakra Balance, Head as Heaven, and Hemispheres |
| HEAD IS HEAVEN, SAME ROOT WORD=HEA REPTILLIAN=INSTINCTUAL LIMBICK=EMOTIONAL NEOCORTEX=CRITICAL THINKING NEO FROM THE MATRIX WOKE UP AND STARTED TO USE HIS HIGHER, CRITIAL THINKING MIND WHICH IS THE NEO CORTEX ELEMENTS THE BASE OF ALL PHYSICAL MATTER IS THE EATHER, ALSO KNOWN AS SPIRIT OR AETHER. | 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| THE AETHER IS THE HIDDEN ENERGY THAT VIBRATES TO CREATE THE "PHYSICAL WORLD WE SEE AND KNOW. | 04 - Pineal Gland, Holy Grail, and the Planes, 07 - Ether, Moon, and the Light Projection |
| THE 4 ELEMENTS ARE THE 4 VIBRATIONAL STATES OF THE ETHER. -NONE OF THE ELEMENTS ARE PURE | 04 - Pineal Gland, Holy Grail, and the Planes, 07 - Ether, Moon, and the Light Projection |
| THE PLANE OF INIRTIA IS WHERE WE GET THE PHRASE "PLANET EARTH" FROM. | 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| AT THE CENTRE OF THE EARTH IS THE CENTRE OF THE EARTH'S MAGNETIC FIELD. | 03 - Born Again, the Serpent, and the Tree of Life, 07 - Ether, Moon, and the Light Projection |
| SUN=ELECTRIC AND POSITIVLY CHARGED. | 03 - Born Again, the Serpent, and the Tree of Life, 07 - Ether, Moon, and the Light Projection |
| THE START OF THE SOUL SYSTEM FEMANINE TROPIC OF CAPRICORN STAR=START STAIR=STARS EQUATOR THE STAIRWAY TO HEAVEN IS THE STARWAY TO HEAVEN. | 04 - Pineal Gland, Holy Grail, and the Planes, 07 - Ether, Moon, and the Light Projection |
| HEARTH EARTH IS AN ANAGRAM FOR HEART MOVE THE H TO THE BEGINNING AND EARTH BECOMES HEART. | 07 - Ether, Moon, and the Light Projection, 08 - One Reality, Element Symbols, and Seven Heavens |
| HEART MEANS MIDDLE. | 03 - Born Again, the Serpent, and the Tree of Life, 07 - Ether, Moon, and the Light Projection |
| IT IS THE BALANCED REALM BETWEEN GOOD AND EVIL. | 07 - Ether, Moon, and the Light Projection, 08 - One Reality, Element Symbols, and Seven Heavens |
| THIS IS WHY WE HAVE DUALISM HERE (GOOD AND EVIL). | 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| THE EARTH IS GREEN, AND THEN ABOVE THE GREEN EARTH IS THE BLUE SKY. | 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| OUTGROW MATTER AND TURN TO SPIRIT (GROW TO EACH PLANET HAS ITS LAYER THE HIGHEST STATE OF CONSCIOUSNESS). | 05 - Astral Plane, Chakras, and the True Self, 07 - Ether, Moon, and the Light Projection |
| FREEMASONIC COSMOLOGY GENESIS 1:3 GENESIS 1:16 "LET THERE BE LIGHT" ""And God made two great lights | 01 - Syncretism and the Lightwave Universe, 07 - Ether, Moon, and the Light Projection |
| the greater light to rule the day and the GENESIS 1:6 EVERYTHING IS MADE OUT OF LIGHT | 01 - Syncretism and the Lightwave Universe, 07 - Ether, Moon, and the Light Projection |
| THE lesser light to rule the night" "Let there be a firmament in the midst of UNIVERSE IS CREATED OUT OF LIGHT IN OTHER WORDS GOD CREATED THE SUN the waters | 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| THE MOON IS MASONIC ROYAL ARCH. | 04 - Pineal Gland, Holy Grail, and the Planes, 07 - Ether, Moon, and the Light Projection |
| MAGNETIC/FEMALE. | 03 - Born Again, the Serpent, and the Tree of Life, 07 - Ether, Moon, and the Light Projection |
| THE FIRMAMENT IS ALSO CALLED HEAVEN. | 07 - Ether, Moon, and the Light Projection, 08 - One Reality, Element Symbols, and Seven Heavens |
| TWO HEMISPHERES OF THE HEAVEN HAS THE WORD EVEN WITHIN IT. | 06 - Chakra Balance, Head as Heaven, and Hemispheres, 07 - Ether, Moon, and the Light Projection |
| and spreads 7 STARS them out like a tent to live in. =THESE STARS SYMBOLIZE THE 7 PLANETS, ALSO KNOWN AS THE 7 WONDERERS OR THE 7 LAYERS OF HEAVEN: SATURN, JUPITER, MARS, SUN, VENUS, MURCERY, MOON. | 07 - Ether, Moon, and the Light Projection, 08 - One Reality, Element Symbols, and Seven Heavens |
| EACH 'pLANET' HAS ITS OWN LAYER OF THE FIRMAMENT PLANET=PLAN=PLANE 5 POINTED STAR GENESIS 1:14 THIS SYMBOL IS CALLED A PENTICLE. | 07 - Ether, Moon, and the Light Projection, 08 - One Reality, Element Symbols, and Seven Heavens |
| THE ETHER IS THE BASE OF ALL PHYSICAL THE BOAT ON WATER SYMBOLIZES THE MATTER. | 05 - Astral Plane, Chakras, and the True Self, 07 - Ether, Moon, and the Light Projection |
| THE STARS ARE ARE THE E 5 WAYS THE BODY REPORTS LIGHT SHINING THROUGH THE ETHER ABOVE. | 04 - Pineal Gland, Holy Grail, and the Planes, 07 - Ether, Moon, and the Light Projection |
| HEART IS THE MIDDLE OF THINGS SUCH AS the lighter something is the higher it rises. it's the same with the journey of the soul. the more materialistic the soul gets, the lower THE BODY FOR EXAMPLE. | 03 - Born Again, the Serpent, and the Tree of Life, 07 - Ether, Moon, and the Light Projection |
| The world GENESIS 1:14 is firmly established | 07 - Ether, Moon, and the Light Projection, 08 - One Reality, Element Symbols, and Seven Heavens |
| it cannot be moved" "And God said, Let there be lights in the firmament of the heaven to divide the day from the night | 07 - Ether, Moon, and the Light Projection, 08 - One Reality, Element Symbols, and Seven Heavens |
| THIS COULD BE WHY EARTH IS AN ANAGRAM FOR THE HEART, AS IT WOULD BE THE SYSTEM'S HEART. | 07 - Ether, Moon, and the Light Projection, 08 - One Reality, Element Symbols, and Seven Heavens |
| FOR THOUSANDS OF YEARS, PEOPLE BELIEVED IN HEAVEN AND HELL, WHICH COULD BE THE REALMS ABOVE AND BELOW US. | 07 - Ether, Moon, and the Light Projection, 08 - One Reality, Element Symbols, and Seven Heavens |

### Near-identical narrated sentences (38 pairs)

| Sim | A | B |
| --- | --- | --- |
| 1.00 | _01 - Syncretism and the Lightwave Universe_<br>They are received based on what frequency our mind is set to. | _04 - Pineal Gland, Holy Grail, and the Planes_<br>They are received based upon what frequency our mind is set to. |
| 0.99 | _06 - Chakra Balance, Head as Heaven, and Hemispheres_<br>It controls the right side of the body. | _06 - Chakra Balance, Head as Heaven, and Hemispheres_<br>It controls the left side of the body. |
| 0.95 | _07 - Ether, Moon, and the Light Projection_<br>The solar system is actually the soul system. | _07 - Ether, Moon, and the Light Projection_<br>It are a soul system, not a solar system. |
| 0.95 | _06 - Chakra Balance, Head as Heaven, and Hemispheres_<br>Head is heaven, same root word. | _07 - Ether, Moon, and the Light Projection_<br>Head and heaven are the same root words. |
| 0.94 | _06 - Chakra Balance, Head as Heaven, and Hemispheres_<br>The head is heaven, the heart is earth, and the heel is hell. | _06 - Chakra Balance, Head as Heaven, and Hemispheres_<br>The head is heaven and the heel is hell. |
| 0.93 | _04 - Pineal Gland, Holy Grail, and the Planes_<br>The stars are the start of the soul system. | _07 - Ether, Moon, and the Light Projection_<br>The start is the stars as they are the start of the soul system. |
| 0.92 | _04 - Pineal Gland, Holy Grail, and the Planes_<br>Aether is where we get the word either. | _07 - Ether, Moon, and the Light Projection_<br>In fact, the word aether is literally the word either. |
| 0.92 | _06 - Chakra Balance, Head as Heaven, and Hemispheres_<br>The head is heaven because it is the place of consciousness in the center of the brain. | _07 - Ether, Moon, and the Light Projection_<br>Your head is heaven because it is the place of your consciousness and true form. |
| 0.90 | _06 - Chakra Balance, Head as Heaven, and Hemispheres_<br>The heart chakra, anahata, corresponds to the index finger. | _06 - Chakra Balance, Head as Heaven, and Hemispheres_<br>The heart chakra, anahata, is the index toe. |
| 0.89 | _01 - Syncretism and the Lightwave Universe_<br>The mind is the intellect that manipulates the physical body and the world around us. | _03 - Born Again, the Serpent, and the Tree of Life_<br>The mind is the intellect that connects the soul to the body. |
| 0.88 | _04 - Pineal Gland, Holy Grail, and the Planes_<br>When we astral project, we are using our mind to project the soul into the astral plane. | _05 - Astral Plane, Chakras, and the True Self_<br>When you astral project, you are using your mind to project the soul out of the physical body, out of the physical world, into the astral plane where there are no limitations of time and space. |
| 0.87 | _01 - Syncretism and the Lightwave Universe_<br>The mind exists within the mental plane which is shared between all the minds of the universe. | _04 - Pineal Gland, Holy Grail, and the Planes_<br>So the mental plane is shared between all the minds that exist. |
| 0.87 | _06 - Chakra Balance, Head as Heaven, and Hemispheres_<br>The word itself tells you, head hey, heaven, same root word. | _07 - Ether, Moon, and the Light Projection_<br>Head and heaven are the same root words. |
| 0.86 | _06 - Chakra Balance, Head as Heaven, and Hemispheres_<br>The word itself tells you, head hey, heaven, same root word. | _06 - Chakra Balance, Head as Heaven, and Hemispheres_<br>Head is heaven, same root word. |
| 0.86 | _05 - Astral Plane, Chakras, and the True Self_<br>Whatever you do in the astral plane will manifest into the physical world. | _05 - Astral Plane, Chakras, and the True Self_<br>Everything you think of will manifest instantly in the astral plane. |
| 0.86 | _04 - Pineal Gland, Holy Grail, and the Planes_<br>The right hand of God is the right hemisphere of the brain, which has to do with creativity, intuition and insight, and it is connected to the cerebrum, the higher brain. | _06 - Chakra Balance, Head as Heaven, and Hemispheres_<br>The right hand of God is the right hemisphere. |
| 0.86 | _03 - Born Again, the Serpent, and the Tree of Life_<br>Honey is the sun and the pineal gland. | _04 - Pineal Gland, Holy Grail, and the Planes_<br>The pineal gland is associated with the honey, the sun, the male, and the electric. |
| 0.86 | _02 - Christ Oil, Brain Anatomy, and Kundalini_<br>The oil travels past all thirty-three. on the back of the spine, and crosses the vagus nerve, that crossing is Jesus being crucified at thirty-three years of age. | _03 - Born Again, the Serpent, and the Tree of Life_<br>The Christ oil is named for the 33 years of Christ and the spine has 33 vertebrae, so when the oil passes all 33 vertebrae and then crosses the vagus nerve that's in the crucifixion, Jesus was crucified at 33 because it was the crucifixion of the Christ oil, passing the 33 vertebrae and crossing the vagus nerve. |
| 0.86 | _03 - Born Again, the Serpent, and the Tree of Life_<br>Milk is the moon and the pituitary gland. | _04 - Pineal Gland, Holy Grail, and the Planes_<br>The pituitary gland is associated with the milk, the moon, the female, and the magnetic. |
| 0.85 | _01 - Syncretism and the Lightwave Universe_<br>The mind is like a frequency tuner tuning itself into different frequencies. | _06 - Chakra Balance, Head as Heaven, and Hemispheres_<br>Your mind sets itself to various frequencies. |
| 0.85 | _02 - Christ Oil, Brain Anatomy, and Kundalini_<br>Then Jesus dies for three days in the cave that symbolizes the sacred fluid resting in the sacrum bone at the base of the spine, ha-cave. | _02 - Christ Oil, Brain Anatomy, and Kundalini_<br>The sacrum is the cave where Jesus was dead for three days. |
| 0.85 | _06 - Chakra Balance, Head as Heaven, and Hemispheres_<br>The right brain relies on the left brain because its holistic perception while capturing the essence of the whole may lack precision and clarity. | _06 - Chakra Balance, Head as Heaven, and Hemispheres_<br>The left brain requires the right brain because although it produces mental clarity, it can lose sight of the connection between all things and trap the individual in a fragmented world. |
| 0.84 | _05 - Astral Plane, Chakras, and the True Self_<br>The chakras are a part of the etheric body, as they are seven seals that bind your soul and spirit to the physical body. | _06 - Chakra Balance, Head as Heaven, and Hemispheres_<br>We've already worked through what the chakras are, how they relate to the etheric body, and how they function as the seven seals. |
| 0.84 | _04 - Pineal Gland, Holy Grail, and the Planes_<br>The astral plane is where thoughts manifest into forms. | _04 - Pineal Gland, Holy Grail, and the Planes_<br>The manifesting thought form will appear on the higher, middle, or lower astral plane. |
| 0.84 | _01 - Syncretism and the Lightwave Universe_<br>This is why the word human means an attribute of a color. | _06 - Chakra Balance, Head as Heaven, and Hemispheres_<br>Human comes from the word hue, which means an attribute of a color. |
| 0.84 | _04 - Pineal Gland, Holy Grail, and the Planes_<br>The astral plane is where thoughts manifest into forms. | _04 - Pineal Gland, Holy Grail, and the Planes_<br>The astral plane is created out of thoughts manifesting, and each thought has a vibrational frequency. |
| 0.84 | _04 - Pineal Gland, Holy Grail, and the Planes_<br>The mind inhabits the pineal gland. | _06 - Chakra Balance, Head as Heaven, and Hemispheres_<br>The pineal gland is the place of your consciousness. |
| 0.83 | _02 - Christ Oil, Brain Anatomy, and Kundalini_<br>The oil travels past all thirty-three. on the back of the spine, and crosses the vagus nerve, that crossing is Jesus being crucified at thirty-three years of age. | _03 - Born Again, the Serpent, and the Tree of Life_<br>Once Jesus resurrects the oil rising up the spine, he gets crucified at 33 years of age. |
| 0.83 | _03 - Born Again, the Serpent, and the Tree of Life_<br>The sun is positive, male and electric. | _07 - Ether, Moon, and the Light Projection_<br>The sun is electric and positively charged. |
| 0.83 | _06 - Chakra Balance, Head as Heaven, and Hemispheres_<br>The body divides into three sections, each controlled by one of three brains. | _06 - Chakra Balance, Head as Heaven, and Hemispheres_<br>The three brains control these three sections. |
| 0.83 | _06 - Chakra Balance, Head as Heaven, and Hemispheres_<br>The head is heaven, because in the bible the head is referred to as the upper room where Jesus met the twelve disciples. | _06 - Chakra Balance, Head as Heaven, and Hemispheres_<br>The head is heaven because it is the place of consciousness in the center of the brain. |
| 0.83 | _07 - Ether, Moon, and the Light Projection_<br>Earth is called heart because it din the heart, meaning the middle of the soul system. | _07 - Ether, Moon, and the Light Projection_<br>The earth is the heart of the soul system. |
| 0.83 | _01 - Syncretism and the Lightwave Universe_<br>We live inside of a light wave universe where all things are created out of light. | _07 - Ether, Moon, and the Light Projection_<br>The universe is created out of light, waves. |
| 0.83 | _07 - Ether, Moon, and the Light Projection_<br>Earth is called heart because it din the heart, meaning the middle of the soul system. | _07 - Ether, Moon, and the Light Projection_<br>The earth is the heart, meaning the middle. |
| 0.83 | _08 - One Reality, Element Symbols, and Seven Heavens_<br>Polaris is the eight-pointed star. | _08 - One Reality, Element Symbols, and Seven Heavens_<br>Polaris is the center and highest star. |
| 0.83 | _04 - Pineal Gland, Holy Grail, and the Planes_<br>The astral plane is where thoughts manifest into forms. | _04 - Pineal Gland, Holy Grail, and the Planes_<br>For example, the mental plane is the thought of a chair, and the astral plane is the imagination of that chair. |
| 0.83 | _03 - Born Again, the Serpent, and the Tree of Life_<br>And Jesus, dying at 33, also symbolizes turning matter into spirit. | _03 - Born Again, the Serpent, and the Tree of Life_<br>The death of Jesus symbolizes turning matter into spirit. |
| 0.82 | _04 - Pineal Gland, Holy Grail, and the Planes_<br>It is the fifth element, also known as spirit or aether. | _05 - Astral Plane, Chakras, and the True Self_<br>The ether is the fifth element, also known as spirit. |

### Adjudicated redundancy

- **The full Christ-oil crucifixion narrative: oil descends, rests three days on the sacrum (the cave), kundalini raises it past the 33 vertebrae, crosses the vagus nerve = crucifixion at 33, matter turned into spirit.** (02 (twice within the lesson), 03 (twice within the lesson — once as the John 3:3 exposition and again as "the alchemical process that occurs monthly")) — **not justified**. Four essentially complete retellings. The source itself repeats this passage on several pages, and the course simply narrates each occurrence rather than consolidating. The second telling in Lesson 3 does add one new element (the thalamus looking like a cross), but the rest is restatement.
- **"Head is heaven, same root word HEA" / "Head and heaven are the same root words" / "the head is heaven because it is the place of consciousness in the centre of the brain"** (03, 06 (three times), 07, 08) — **not justified**. Five or six utterances of the same etymology-plus-claim. Once as a thesis and once as a reprise would be earned; the rest is the course tracking the source's page-by-page repetition.
- **The mental plane is shared by all minds; thoughts are not created but received according to the frequency your mind is set to; hence "mindset"** (01, 04) — justified. Lesson 1 introduces it as part of the mind-as-tuner idea; Lesson 4 restates it in its proper place in the ladder of planes. The near-verbatim identity of the two passages is unnecessary, but the second occurrence does structural work.
- **Ether = either = the fifth element with one foot in the physical and one in the astral** (04, 05, 07) — **not justified**. Stated three times in nearly identical words, including the Manchester United/Liverpool illustration in Lesson 4 and a bare restatement in Lesson 5. Nothing new is added on the second or third pass.
- **Astral projection mechanics: the mind projects the soul, you meet only entities matching your frequency, low frequency means demons** (04, 05) — **not justified**. Lesson 4 delivers this in full, then Lesson 5 opens by delivering it again before adding the practice instructions. Lesson 5 should have carried it alone; the lesson split between 'planes' and 'astral plane' forced the duplication.
- **Earth is an anagram for heart; earth is the heart/middle of the soul system; the checkered board symbolises duality** (07 (twice), 08) — **not justified**. The source repeats these lines across several cosmology pages and the course repeats them along with it.
- **Milk = moon = pituitary = female = magnetic; honey = sun = pineal = male = electric** (02, 03, 04) — justified. This is the central polarity of the whole oil doctrine and each occurrence sits in a different frame (the process steps, the sun/moon principles, the Holy Grail). Reinforcement here is defensible.

## 6. Is it teachable?

| Lesson | Minutes | Words | Sentences | Scaffold | Source statements touched | Direct quotes |
| --- | --- | --- | --- | --- | --- | --- |
| 01 - Syncretism and the Lightwave Universe | 5.5 | 740 | 59 | 0 | 95 | 0 |
| 02 - Christ Oil, Brain Anatomy, and Kundalini | 6.5 | 908 | 60 | 2 | 45 | 0 |
| 03 - Born Again, the Serpent, and the Tree of Life | 11.0 | 1469 | 114 | 1 | 118 | 0 |
| 04 - Pineal Gland, Holy Grail, and the Planes | 12.0 | 1722 | 128 | 0 | 177 | 0 |
| 05 - Astral Plane, Chakras, and the True Self | 9.0 | 1379 | 107 | 1 | 123 | 0 |
| 06 - Chakra Balance, Head as Heaven, and Hemispheres | 24.7 | 3410 | 249 | 2 | 226 | 0 |
| 07 - Ether, Moon, and the Light Projection | 14.3 | 2027 | 167 | 1 | 162 | 0 |
| 08 - One Reality, Element Symbols, and Seven Heavens | 3.4 | 517 | 39 | 0 | 41 | 0 |

**Verdict:** Mixed. The first half is genuinely organised and would teach; the second half degrades into caption reading, and the final lesson transfers almost nothing.

Strengths:
- Lesson 2 performs the single most valuable editorial act in the course: it takes the source's oil material, which is physically scattered across a page as marginal notes interleaved mid-sentence with unrelated captions, and delivers it as a clean seven-step sequence — "First the claustrum... Second, the pineal gland electrically charges the fluid... Third, the pituitary gland magnetically charges the fluid..." A reader of the raw page has to reconstruct that order themselves.
- Lessons use explicit forward and backward references ("We already talked about the Christ oil as the sacred brain oil and how raising it through the spine awakens the chakras"), giving the material a spine the document lacks.
- Lesson 3 ends with a genuine synthesis in the course's own voice: "The spine is the ladder. The brain is heaven. The heart is the tree of life and the nervous system is the tree of knowledge. You are the temple." That is teaching, not transcription.
- The Dispenza emotional scale is re-ordered upward from lust to wholeness, which is easier to follow aloud than the source's downward column.

Weaknesses:
- Lesson 8 is almost pure caption recital of an image gallery and teaches nothing: "There are also historical maps from the 1,500 seconds and 1,600 seconds, showing the North Pole and flat earth maps. Hitler used two flat earth maps... the Mayan cosmos, the Hebrew cosmos, and the United Nations. There are all carry this same imagery." A listener cannot see the maps and is told nothing about what they allegedly show.
- Image-dependent claims are read out without being described. "The sigil of Lucifer is showing you the visual field of the eyes" (L1) and "Notice the lamb is looking up at a cup with the sun on the top" (L4) are faithful to the words and useless without the picture — the whole point of the sigil argument is a visual resemblance that is never described.
- Lesson 6 is a grab bag roughly the length of three ordinary lessons, running from unbalanced chakras through Deuteronomy, Baphomet, fast-food logos, the Dispenza chart, hand chakras, foot chakras, the three brains, Egyptian symbols, Merkaba, Corinthians, and the full left/right hemisphere table. There is no organising thread after the first third.
- Table-shaped content is read as flat lists and dissolves: "the metals and planets are listed alongside them, gold, lead, moon, sun, Mars, Jupiter, Saturn, Venus, and Mercury" and "The planes also map onto this. The mental plane is thoughts..." convey no correspondences at all.
- Transcription damage lands on precisely the parts that are hardest to recover aurally — the I AM chakra statements, "all is a two, meaning all is Adam," "Diamon" for daemon, "the optic pellamus" — so the listener gets noise where the source had a mapping.
- The 144,000 arithmetic is narrated exactly as the source miscomputes it ("Add those first five. Four plus six plus ten plus twelve equals forty-eight" — only four numbers are added), which is unfollowable read aloud and never flagged.

## 7. What a listener will never learn

- **"THREE WISE MEN FROM THE EAST" = 1. THALAMUS 2. PINEAL GLAND 3. PITUITARY GLAND** — One of the source's named biblical-to-brain decodings, in the same family as the 12 disciples = 12 cranial nerves that the course does teach. It is never mentioned in any lesson, so the listener loses a complete decoding.
- **"SIN IN LATIN IS SINISTER MEANS LEFT / RIGHT = RIGHTIOUS"** — The source's etymological justification for why the left hemisphere is coded as sin and the right as righteousness. Lesson 6 only emits the fragment "In Latin, and right is righteous", dropping the sinister/left half, so the argument collapses into an unexplained assertion.
- **The chakra correspondence table: crown=Moon/spirit/spirituality, third eye=Mercury/intuition, throat=Venus/communication, heart=Sun/love, solar=Mars/power, sacral=Jupiter/creativity, root=Saturn/earth/survival, plus gold and lead as the metal poles** — Lesson 5 gives the qualities correctly but then dumps the rest as an unordered heap — "the metals and planets are listed alongside them, gold, lead, moon, sun, Mars, Jupiter, Saturn, Venus, and Mercury" — which transfers no mapping at all. The planet-per-chakra link is load-bearing for the later claim that "each chakra is one of the seven planets."
- **"ASTRONOMY / ASTRO=ASTRAL / SPACE IS FAKE" and the marginal Hermetic-principle labels "CORRESPONDANCE / MENTALISM / ENERGY"** — The astro=astral etymology is the source's bridge between its astronomy and astral-plane material, and "space is fake" is the explicit cosmological claim that the flat-earth section rests on. Neither is spoken anywhere.
- **The Hindu trinity mapping: Vishnu / Brahma / Shiva laid out against soul / mind / body, with "THE MIND IS THE SERPENT BECAUSE SERPENTS SYMBOLIZE KNOWLEDGE"** — Lesson 3 keeps the serpent-mind idea and "the soul, which is Brahma, has multiple faces," but drops the three-deity-to-three-part-self diagram, so the listener hears an isolated Brahma reference with no framework around it.
- **"SEVEN UP IS TRUTH IN PLANE SITE" and the "from thought to energy matter" caption attached to the Dispenza figure** — Minor, but it is the source's stated reading of why that emotional-scale figure belongs in a book about planes descending from thought to matter.

## Bottom line

A listener would come away with nearly all of the document's verbal doctrine and, thanks to Lesson 2's restructuring, a clearer grasp of the Christ-oil sequence than the raw page offers. What they would not get is anything the source teaches through pictures — the sigil, the Masonic and Egyptian artwork, the flat-earth maps, the chakra-planet-metal table, the pineal anatomy diagram — which the narration recites as labels and abandons. Add a handful of real errors (head/heart/heel mapped to mind/body/soul instead of mind/soul/body; invented 'feminine and masculine poles' framing for the I AM statements; a fabricated Chronicles-to-33-vertebrae link) and a few genuine omissions (the three wise men as thalamus/pineal/pituitary, sin=sinister=left, astro=astral/space is fake). Call it about 80% teaching-equivalent, with the last lesson contributing close to nothing and the middle lessons carrying almost all the value.

---

<details><summary>Source statements as parsed</summary>

- [ ] `00` BOOK OF WISDOM AUTHOR
- [~] `03` AUTHOR: REVIVAL OF WISDOM REVIVALOFWSIDOM REVIVALOFWISDOM3 REVIVALOFWISDOM INTRODUCTION THE BOOK OF WISDOM IS A BOOK CONTAINING ESOTERICISM, OCCULTISM, SYMBOLISM, AND MOST IMPORTANTLY, SYNCRETISM.
- [x] `04` SYNCRETISM IS THE METHOD THAT I, REVIVAL OF WISDOM, HAVE USED TO SYNC/COMBINE ALL FIELDS OF KNOWLEDGE.
- [x] `05` SYNCRETSIM UNITES ALL SUBECTS OF MATTER INTO ONE HOLY SCIENCE.
- [x] `06` ALL THINGS COME FROM THE ONE, THEREFORE ALL THINGS ARE ONE.
- [x] `07` THE WORLD WE LIVE IN IS A FRACTIONAL WORLD WHERE ALL THINGS CONTAIN ALL THINGS FROM A MICRO AND MACRO PERSPECTIVE.
- [x] `08` THE AVERAGE INDIVIDUAL OF TODAY'S DAY AND AGE IS LIVING THEIR LIFE LEFT HEMISPHER DOMINANT.
- [x] `09` THE LEFT HEMISPHERE OF THE BRAIN BREAKS DOWN AND ANYLIZES THE RIGHT HEMIPHEARS UNITED PERCEPTION OF REALITY INTO SEPERATE FRAGMENTS SO THAT WE CAN MANIPULATE AND UNDERSTAND THINGS LOGICALLY.
- [x] `10` TO GAIN A FULL UNDERSTANDING OF THE INFORMATION THIS BOOK PRESENTS, YOU MUST FIRST FREE YOUR MIND FROM THE INDOCTRINATIONS GIVEN BY THE EDUCATIONAL SYSTEMS WE WERE FORCED TO ATTEND TO AND, SECONDLY, TRY AND PERCEIVE REALITY AS ONE UNITED AND WHOLISTIC CREATION.
- [~] `11` ALL OF THE IMAGES IN THIS BOOK HAVE BEEN EDITED, MANIPULATED, AND ATIFICIALLY GENERATED TO AVOID ANY COPYRIGHT CLAIMS.
- [~] `13` NOT ONE OF THE IMAGES USED IN THIS BOOK IS BEING USED IN ITS ORIGINAL FORM.
- [x] `14` LIGHT GENESIS 1:3 "LET THERE BE LIGHT" WE LIVE INSIDE OF A LIGHTWAVE UNIVERSE WHERE ALL THINGS ARE CREATED OUT OF LIGHT.
- [x] `15` LOWVIBRATING LIGHT TURNS INTO MATTER, HIGH-VIBRATING MATTER TURNS BACK INTO LIGHT.
- [x] `16` UNIVERSAL ONE BY WALTER RUSSEL: "GOD IS THINKING MIND.
- [x] `17` THE SUBSTANCE OR BODY OF GOD IS LIGHT".
- [x] `18` "THE ONE UNIVERSAL SUBSTANCE, A THINKING SUBSTANCE, COMPREHENSIVE AND DESCRIBIBABLE AND POSSESSED OF PRINCIPLES WHICH ARE FAMILIAR TO MAN THROUGH MANS OBSERVATION OF THE ONE UNIVERSAL SUBSTANCE IN CREATED THINGS.
- [x] `19` THE SUBSTANCE OF ALL CREATED THINGS IS LIGHT.
- [x] `20` THE ONE SUBSTANCE OF THINKING MIND IS ALL THAT EXISTS." "MIND IS EXPRESSED IN LIGHT".
- [x] `21` HUMAN HUE MAN AS A HUE MAN, WE ARE AN ATTRIBUTE OF A COLOUR THAT PERMITS THEM TO BE CLASSED THAT SPECIFIC COLOUR.
- [x] `22` EACH INDIVIDUAL IS THE MIND, NOT THE PHYSICAL BODY.
- [x] `23` WITHOUT THE MIND THE PHYSICAL BODY/WORLD WOULD CEASE TO EXIST.
- [x] `24` THE MIND IS SPIRIT.
- [x] `25` THE MIND IS THE INTELLECT THAT MANIPULATES THE PHYSICAL BODY AND THE WORLD AROUND US.
- [x] `26` THE MIND IS LIKE A FREQUENCY TUNER, TUNING ITSELF INTO DIFFERENT FREQUENCIES.
- [x] `27` THE MIND EXISTS WITHIN THE MENTAL PLANE, WHICH IS SHARED BETWEEN ALL THE MINDS OF THE UNIVERSE.
- [x] `28` THOUGHTS ARE NOT CREATED BY THE INDIVIDUAL
- [x] `29` THEY ARE RECEIVED BASED ON WHAT FREQUENCY OUR MIND IS SET TO.
- [x] `30` IF WE SET OUR MIND TO A SPECIFIC TOPIC, LIKE GENERATING WEALTH, FOR EXAMPLE, WE TUNE INTO THAT FREQUENCY IN THE MENTAL PLANE, AND WE WILL RECEIVE THOUGHTS ON HOW TO GENERATE WEALTH.
- [x] `31` OUR MID IS GENERALLY OPERATING OFF ONE SPECIFIC FREQUENCY BASED UPON OUR DAILY THINKING PATTERNS.
- [x] `32` EVERY FREQUENCY IS A COLOUR.
- [x] `33` THEREFORE, OUR MIND IS MANIFESTING COLOURS WITHIN THE ASTRAL PLANE BASED UPON WHAT FREQUENCY OUR MIND IS GENERALLY OPERATING OFF.
- [x] `34` IF WE ARE CARRYING HATE IN OUR MIND, WE WILL BE GENERATING REDDISH COLOURS.
- [x] `35` THIS IS WHY THE WORD HUMAN MEANS AN ATTRIBUTE OF A COLOUR.
- [x] `36` WE SHOULD AIM TO BECOME VIOLET, THE HIGHEST VIBRATIONAL COLOUR WITHIN THE LIGHT SPECTRUM.
- [x] `37` WE ARE LIGHT BEINGS MANFESTED INTO PHYSICAL FORM.
- [x] `38` YOU DO NOT SEE INTO REALITY SIGIL OF LUCIFER VISUAL CORTEX LIGHT ENTERS RETNAS EGYPTIAN SCULPTURE VISUAL FIELD WE DO NOT SEE INTO THE EXTERNAL WORLD.
- [x] `39` LIGHT WAVES ENTER THE RETINAS, AND THEN LUCIFER THE LIGHT BEARER THE IMAGE WE SEE IS PRODUCED IN THE VISUAL CORTEX LOCATED AT THE BACK END OF LUCIFER=LUCI OUR BRAINS.
- [x] `40` LUCI IN LATIN MEANS LIGHT THE SIGIL OF LUCIFER IS SHOWING YOU THE VISUAL .The visual cortex is the primary cortical region of the brain that receives, FIELD OF THE EYES. integrates
- [x] `41` and processes visual information relayed from the retinas THE ANCIENT KEMETICS (EGYPTIANS) HAD A DEEP UNDERSTANDING OF THE FUNCTION OF REALITY AND THE BRAIN
- [x] `42` THIS IS WHY IT IS REFLECTED IN THEIR SCULPTURES AS SHOWN ABOVE.
- [x] `43` THE ELEMENTS ONLY EXIST WITHIN THE ELEMENT MIND.
- [x] `44` HUMANS ARE GOD MADE FLESH.
- [x] `45` WE ELE MENT ARE THE GOD IN SEPERATE BODIES.
- [x] `46` GOD IS MENT=MIND MIND AND ALL THINGS EXIST IN THE ELECTROMAGNETIC SPECTRUM UNIVERSAL MIND.
- [x] `47` GOD IS THINKING ALL THINGS INTO EXISTANCE.
- [x] `48` EL=GOD ELEMENT=GODMIND CHRIST OIL WHEN THE MOON ENTERS YOUR SUN SIGN (YOUR BIRTH ZODIAC SIGN), a psychophysical OIL IS RELEASED from the brain DOWN THE SPINE TO THE SACRUM CLAUSTRUM=santa clause BONE.
- [x] `49` This sacred fluid must be cared for and not destroyed by acidic foods and liquids.
- [x] `50` Our sexual energy/fluids must be retained if we wish to raise this psycho-physical oil back to our brain (heaven).
- [x] `51` By opening our chakras, preserving our sexual energy
- [x] `52` and maintaining the Christ oil, we can use the Power behind the sexual energy (kundalini) to raise it PINEAL GLAND up from the base of the spine back to the crown chakra in the brain.
- [x] `53` BY AWAKENING THE SEVEN CHAKRAS AND RAISING THE KUNDALINI TO THE CROWN CHAKARA, NEW ENERGY PATHWAYS OPEN UP WITHIN THE BRAIN, WHICH FEELS LIKE YOUR HEAD BECOMES HOLLOW ON THE INSIDE.
- [x] `54` THE BRAIN UNDERGOES A REMODELLING PROCESS, EXPANDING ITS CAPACITY FROM M ROUGHLY 10% OF PITUITARY GLAND USAGE TO THE COMPLETE 100%.
- [x] `55` DORNMENT AREAS OF THE BRAIN ARE UNLOCKED, SIGNALLING NEW WAYS OF BRAIN FUNCTIONING AND EXPERIENCING THE WORLD.
- [x] `56` THE KUNDALINI, OVER TIME, BECOMES A SELF-SUSTAINING ENERGY CIRCUIT FUELED BY FOOD AND WATER THAT GROWS AND GETS STRONGER.
- [~] `57` OIL PROCESS: 1-THE CLAUSTRUM (CLAUS=SANTA CLAUSE) PRODUCES THE PSYCHO-PHYSICAL THE BRAIN in the bible is: FLUID WHICH THEN GOES TO THE PINEAL AND PITUITARY GLAND IDA PINGALA -THE UPPER ROOM WHERE JESUS 2-THE PINEAL GLAND ELECTRICALLY CHARGES THE FLUID (MALE/ JOSEPH) MEETS THE 12 DISCIPLES/12 CRANIAL NERVES 3-THE PITUITARY GLAND MAGNETICALLY CHARGES THE FLUID (FEMALE/ MARY) -THE HOLY LAND 4-THEN THE FLUID WILL TRAVEL DOWN THE TWO NERVES, THE IDA WHICH IS -the LAND FLOWING WITH MILK AND HONEY CONNECTED TO THE PITUITARY, AND THEN THE PINGALA WHICH IS CONNECTED -promise land of israel TO THE PINEAL GLAND.
- [x] `58` MILK=PITUITARY GLAND 5-THE OIL THEN RESTS FOR 2/3 DAYS ON THE SACRUM BONE/SOLAR PLEXUS HONEY=PINEAL GLAND 6-IF THE OIL IS SAVED AND NOT DESTROYED THE OIL WILL ACTIVATE THE KHUNDALINI ENERGY WHICH WILL TURN THE OIL INTO A GAS AND RISE BACK UP CHRISTOS=GREEK FOR OIL THE 33 VERDABREAS TO THE MEDULLA OBLONGATA.
- [x] `59` THEN IT BECAME CHRIST 7-THIS WILL THEN PASS TO THE PINEAL GLAND AND THEN TO THE CEREBRUM WHICH WILL REBIRTH/RESURRECT ALL BRAIN CELLS, ACTIVATE THE PINEAL GLAND, CORINTHIANS 13:5 AND REGENERATE ALL THE CELLS IN THE BODY "DO YOU NOT KNOW THAT JESUS THIS PROCESS IS SYMBOLISED AS BEING "BORN AGAIN" CHRIST IS WITHIN YOU?" SUSHUMNA HOW TO RAISE THE OIL THE IDA (FEMANINE) CHANNLE IS CONNECTED TO THE -RETAIN YOUR SEXUAL FLUIDS PITUITARY GLAND.
- [~] `60` MEDICAL SYMBOL -CONSUMING AN ALKALINE DIET -NO CONSUMPTION OF ACIDIC FOODS/FLUIDS THE PINGALA (MASCULINE) CHANNLE IS CONNECTED -NO CONSUMING ALCHOHOL TO THE PINEAL GLAND. -KHUNDALINI MEDITATION -BALANCE ALL CHAKARAS -KEEPING YOUR TOUNGE ON THE TOP OF SUSHUMNA YOUR MOUTH -PROPER BREATHING PSALMS 137:6 MY MY TOUNGE CLING TO THE ROOF OF MY MOUTH IF I DO NOT REMEMBER YOU, IF I DO NOT CONSIDER JERUSALEM MY HIGHEST JOY PINGALA IDA HEAVEN JESUS (THE OIL) IS IN NAZARETH (THE HEAD) WITH JOSEPH AND MARY (THE PINEAL AND PITUITARY RIVER JORDAN= SPINAL CORD GLAND) AND KING HAROD WANTS TO KILL HIM.
- [x] `61` JESUS (THE OIL) GOES DOWN THE RIVER JORDAN (THE SPINE) TO BETHLEHEM NEXT TO THE DEAD SEA (SACRUM BONE).
- [x] `62` JOSEPH AND MARY (PINEAL AND PITUITARY GLAND) ARE WAITING FOR JESUS (THE OIL) TO RETURN.
- [x] `63` THE PROCESS OF THE OIL COMING DOWN FROM THE HEAD SYMBOLIZES JESUS COMING DOWN FROM HEAVEN INTO PHYSICAL FORM.
- [x] `64` JESUS DYING FOR 3 DAYS AND THEN BEING RESURRECTED TO BE CRUCIFIED AT 33 IS A METAPHORICAL STORY ABOUT THE CHRIST OIL PROCESS WITHIN THE BODY WHICH ACTIVATES 100% OF THE BRAIN.
- [x] `65` JORDAN RIVER The story of Jesus is metaphorical for the journey of the sacred oil the brain produces.
- [x] `66` The oil coming down from the brain is god descending from heaven to earth. jesus dying for 3 days in the cave is symbolic of the sacred fluid staying in the sacrum bone at the base of the spine (the cave) for some time.
- [x] `67` Then once the oil is resurrected, meaning ACTIVATING THE KHUNDALINI TO RIASE THE OIL BACK UP THE SPINE, it travels passed all of the 33 vertebras on the back of the spine and crosses the vagus nerve. the SACRED SACRUM oil crossing the vagus nerve is Jesus being crucified at 33 years of age because there are /CAVE WHERE JESUS 33 vertebras on the BACK OF THE spine. the death of Jesus symbolizes being born again WAS DEAD FOR 3 DAYS and turning spirit matter in spirit.
- [x] `68` THE CEREBROSPINAL SYSTEM IS THE DEAD SEA= SACRUM BONE/ AN EXTENTION OF THE BRAIN SOLAR PLEXUS CHRIST OIL THE CHRIST OIL PASSES THE 33 VERTEBRAS OF THE SPINE AND THEN PASSES THE VAGUS NERVE WHICH CROSSES OVER SPINAL CORD JESUS WAS CRUCIFIED AT 33 BECAUSE IT WAS THE CRUCIFICTION OF THE CHRIST OIL PASSING THE 33 VERDABREAS AND CROSSING THE VAGUS NERVE.
- [x] `69` VAGUS NERVE 33 VERDABREAS FOR THE 33 YEARS OF CHRIST/CHRIST OIL.
- [x] `70` JESUS DYING AT 33 ALSO SYMBOLIZES TURNING MATTER INTO SPIRIT WHEN MOVING THE OIL PAST THE 33 VERDABREAS.
- [x] `71` AS HE HAS SACRIFICED HIS FLESH NATURE/PERSONALITY AND HAS NOW MANIFESTED HIS TRUE GOD SELF jOHN 3:3 "UNLESS YOU ARE BORN AGAIN, YOU CANNOT SEE THE KINGDOM OF GOD".
- [~] `72` IT'S NOT A COINCIDENCE THAT THE VERSE jOHN 3:3 IS TALKIG ABOUT BEING REBORN AGAIN.
- [x] `73` YOU ARE REBORN AGAIN WHEN THE OIL RIASES BACK UP PASSED THE 33 VERDABREAS.
- [x] `74` MATTHEW 6:22 GENISIS 32:30 "THE LIGHT OF THE BODY IS THE "JACBOB NAMES THE PLACE PENEIL, FOR HE SAID, EYE
- [x] `75` THEREFOR IS THINE EYE BE I HAVE SEEN GOD FACE TO FACE" PENIEL IS THE 3 3 SINGLE, THE WHOLE BODY SHALL BE FULL OF LIGHT".
- [x] `76` THE PINEAL GLAND WHICH IS THE SEAT OF CONSCIOUSNESS (THRONE OF GOD).
- [x] `77` "The Kingdom of God is Within You" is the key phrase in Luke 17:21 JACOB SYMBOLIZES THE OIL IN THIS JACOBS LADDER PARABLE.
- [x] `78` THE ROCK HE FELL ASLEEP ON IS THE SACRUM BONE, WHERE THE OIL FALLS AND STAYS FOR SOME TIME.
- [x] `79` HE THEN SAW A LADDER THAT REACHED HEAVEN, WHICH IS THE SPINAL CORD LEADING UP TO THE BRAIN (HEAVEN).
- [x] `80` THE SPINAL CORD IS THE STAIRWAY TO THE LADDER YOUR HEAD (HEAVEN).
- [x] `81` THE ROCK FREEMASONS SYMBOLIZE THE SPINAL CORD WITH A LADDER OR STAIRCASE S P IN E SPIN E CHRIST OIL & SYMBOLOGY THE SUN AND MOON ARE THE TWO MALE AND FEMALE PRINCIPLES THAT CORRESPOND WITH ALL IDA PINGALA THINGS IN THIS CREATION.
- [x] `82` THE SUN IS POSITIVE, MALE & ELECTRIC.
- [x] `83` THE THE MOON IS NEGATIVE, FEMALE, MAGNETIC.
- [x] `84` THE SUN AND MOON CREATE THE SACRED FLUIDS WITHIN THE CLAUSTRUM IN THE BRAIN.
- [x] `85` THE TWO SACRED FLUIDS ARE REFERRED TO IN THE BIBLE AS THE MILK AND HONEY.
- [x] `86` THE LAND FLOWING WITH MILK AND HONEY IS THE BRAIN.
- [x] `87` SUSHUMNA MASONIC ART CROWN CHAKARA (TOP OF THE HEAD) MOON/MAGNETIC /FEMALE SUN/ELECTRIC/MALE TWO SERPENTS TO SYMBOLIZE THE TWO KHUNDALINI CHANNELS WRAPED AROUND THE SPINE "LORD" = HIGHER SELF/INNER YOU/OBSERVER/CHRIST MILK=MOON=PITUITARY GLAND HONEY=SUN=PINEAL GLAND THE FIRE AT THE BOTTOM OF THE MEDICAL SYMBOL ARTWORK SYMBOLIZES KUNDALINI ENERGY AT YOUR SPINE'S BASE.
- [x] `88` ACTIVATION OF THE KUNDALINI ENERGY AT THE SPINE BASE IS THE FORCE USED TO PUSH THE CEREBROSPINAL FLUID UP THE SPINE TO REACH THE PINEAL GLAND.
- [x] `89` THE MEDICAL INDUSTRY USES THIS SYMBOL BEAUSE WHEN KUNDALINI ENERGY RAISES CHRISM OIL TO THR BRAIN IT hAS HEALING ABILITIES.
- [x] `90` IT IS SAID THAT RAISING THE SECRETION ACTIVATES ALL THE DORNMENT BRAIN CELLS IN THE BRAIN, REGULATES BLOOD PRESSURE AND REGENERATES THE BODY.
- [~] `91` PINGALA IDA PINEAL PITUAITARY MASONIC ART FEMANINE MASCULINE RIGHT BRAIN LEFT BRIAN SNAKE=KHUNDALINI TREE=SPINE (IDA PINGALA) TREE LEAVES=BRAIN MALE=PINGALA CHANNLE=PINEAL=SUN=ELECTRIC FEMALE=IDA= CHANNLE=PITUITARY=MOON=MAGNETIC SERPENT KHUNDALINI CHANNLES "THREE WISE MEN FROM THE EAST" "THREE WISE MEN FROM THALAMUS THE EAST" 1.
- [ ] `92` THALAMUS 2.
- [x] `93` PINEAL GLAND 3.
- [x] `94` PITUITARY GLAND LADDER=SPINE PINEAL GLAND PITUITARY GLAND John 3:14 Just as Moses lifted up the snake in the wilderness
- [x] `95` so the Son of Man must be lifted up SNAKE=SERPENT=KHUNDALINI LIFTING UP THE SERPENT IS LIFTING UP THE KHUNDALINI ENERGY "SON OF MAN MUST BE LIFTED UP" MOSES WAS TEACHING PEOPLE TO RAISE SON=SUN=SOL=SOUL THERE KHUNDALINI ENERGY TO ACTIVATE THE SOUL OF MAN MUST BE LIFTED THROUGH PINEAL GLAND WHICH WOULD THEN GIVE THE KHUNDALINI ACTIVATING THE PINEAL GLAND.
- [~] `96` HUMAN OUT OF BODY ABILLITIES.
- [x] `97` LEAVING ACTIVATION OF THE PINEAL GLAND GIVES THE BODY GIVES YOU ACCESS TO WORLDS YOU THE ABILLITIES TO LEAVE THE BODY BEYONG TIME AND SPACE.
- [~] `98` AND EXPLORE OTHER REALITIES.
- [x] `99` THE STORY OF JESUS IS SYMBOLIC OF THE ALCHEMICAL PROCESS THAT OCCURS MONTHLY WITHIN THE HUMAN BODY.
- [x] `100` JESUS FALLS FROM HEAVEN AND INCARNATES ON THE EARTH, WHICH IS SYMBOLIC OF THE CHRIST OIL TRAVELING DOWN THE SPINE FROM YOUR BRAIN (HEAVEN).
- [x] `101` THE SACRED OIL STAYS STILL WITHIN THE SACRUM BONE FOR 3 DAYS, WHICH IS JESUS BEING DEAD IN THE CAVE FOR THREE DAYS.
- [x] `102` ONCE JESUS RESURRECTS (THE OIL RSING UP THE SPINE) HE GETS CRUCIFIED AT 33 YEARS OF AGE.
- [x] `103` THE SPINE CONTAINS 33 VERDABREAS, AND ONCE THE OIL PASSES ALL 33 VERDABREAS AND REACHES THE OPTIC THALAMUS, IT GETS CRUCIFED ON THE CROSS BECAUSE THE THALAMUS LOOKS LIKE A CROSS.
- [x] `104` THE DEATH OF JESUS SYMBOLIZES TURNING MATTER INTO SPIRIT AS THE RETURN OF THE OIL GIVES THE HUMAN SUPERNATURAL ABILITIES LIKE ASTRAL TRAVEL.
- [x] `105` BIRDS SYMBOLIZE THE HOLY SPIRIT/SOUL. vISHNU THE MIND IS THE SERPENT BECAUSE SERPENTS SYBOLIZE BRAHMA SHIVA KNOWLEDGE.
- [x] `106` THE MIND IS THE INTERLECT THAT CONNECTS soul THE SOUL TO THE BODY
- [x] `107` THIS IS WHY THE MIND IS IN THE MIDDLE
- [x] `108` IT PROJECTS THE SOUL INTO THE REALITY WE CHOOSE TO EXPERIENCE. body mind THE SOUL (BRAHMA) HAS MULTIPLE FACES, SYMBOLISING THE SOUL TAKING ON DIFFERENT BODIES
- [x] `109` JESUS CHRIST JESUS=BODY CHRIST=CHRIST CONCIOUSNESS SOUL MIND BODY FREEMASONS DO NOT SAY JESUS CHRIST THEY SAY CHRIST JESUS.
- [x] `110` THEY DO THIS TO SAY CONCIOUSNESS COMES FIRST.
- [x] `111` CHRIST OVER THE BODY.
- [x] `112` AS WITHIN SO WITHOUT GENISIS 2:9 THE TREE OF LIFE=CARDIVASCULAR SYSTEM THE TREE OF LIFE WAS ALSO IN THE MIDST OF THE GARDEN, AND THE TREE OF KNOWLEDGE OF GOOD AND EVIL.
- [x] `113` THE TREE OF KNOWLEDGE OF GOOD AND EVIL=THE NERVOUS SYSTEM THE CARDIVASCULAR SYSTEM IS THE TREE OF LIFE BECAUSE IT PROVIDES LIFE TO THE PHYSICAL BODY.
- [x] `114` GEN 2:9: "THE TREE OF LIFE WAS IN THE MIDST OF THE GARDEN." THE GARDEN IS YOUR BODY, AND THE MIDST IS THE MIDDLE, WHICH IS THE HEART.
- [x] `115` THE TREE OF KNOWLEDGE OF GOOD AND EVIL IS THE NERVOUS SYSTEM BECAUSE IT GIVES OUR MIND KNOWLEDGE OF GOOD AND THE HEART IS THE CENTRE OF THE BODY'S ELECTROMAGNETIC FIELD, AND AT EVIL.
- [~] `116` THE MIND AND SOUL COME FROM ETERNAL BLISS, AND THE THE CENTRE OF EVERY TORUS FIELD IS MAGNETISM.
- [x] `117` MAGNETISM MIND PROJECTS THE SOUL INTO THIS DUALISTIC SIMULATION TO PULSES/RADIATES
- [~] `118` IT IS THE RADIATION GAIN THE KNOWLEDGE OF DUALISM.
- [x] `119` OF MAGNETISM THAT CREATES THE BEATING OF YOUR HEART.
- [~] `120` THE HEART IS 5000X STRONGER MAGICALLY THAN THE BRAIN
- [x] `121` IT IS THE MOST MAGNETIC THE NERVOUS SYSTEM DECODES ELECTRICAL IMPULSES GIVEN TO IT ORGAN WITHIN THE BODY.
- [x] `122` THE HEART IS THE PLACE OF THYNE EMOTIONS
- [x] `123` BY THE EXTERNAL WORLD AND REPORTS BACK TO THE BRAIN.
- [x] `124` OUR EMOTION IS THE LANGUAGE OF THE UNIVERSE.
- [x] `125` CONSCIOUSNESS IS PRETTY MUCH EXPERIENCING A PROGRAM PLAYED OUT BY THE CENTRAL NERVOUS SYSTEM.
- [x] `126` THE MAGNETIC PULSE OF THE HEART IS WHAT GIVES LIFE TO THE BODY.
- [x] `127` ALL THINGS THAT LIVE HAVE TO HAVE A PULSE
- [x] `128` it's the universal "breath" of 4 RIVERS IN THE GARDEN OF EDEN life.
- [x] `129` We breathe, pulse, blink, sleep, live, and die.
- [x] `130` All of this is the GENISIS 2:10 expression of the one universal breath of life. body EARTH=BODY MOON=MIND SUN=SOUL THE 4 RIVERS FLOWING IN THE GARDEN OF EDEN ARE THE 4 HOLY FLUIDS IN THE BODY WHICH ARE: 1) BLOOD 2) SELIVER mind soul 3) CHRIST OIL body mind soul 4) SEMEN/VAGINAL FLUID THE TEMPLE OF SOLOMON IS YOU SPIRIT head EARTH AIR Sol=SOUL THE BODY IS THE TEMPLE MON=MIND hea heaven OF THE SOUL AND MIIND WATER FIRE YOU ARE A STAR STER=STAR A AND E ARE INTERCHANGABLE MISTER MINISTER, SISTER, MONSTER, SUPER STAR, MASTER, FRAUSTER, SINISTER. you are a qantom photon (a star) in a physical body. you are all knowing and directly from the source, in other words you are god/godess experiencing THE PROGRAM BEING RAN BY THE CENTRAL NERVOUS SYSTEM. while we are incarnated here we are divided from source and absent of the knowledge of our true divine heel insight. hell THE PINEAL GLAND THE PINEAL GLAND
- [x] `131` PINeal THE PINEAL GLAND IS A CONED SHAPED BODY, 6mm HIGH AND 4mm IN DIAMETER gland -THE MIND ENHABITS THE PINEAL GLAND. -ITS THE ORGAN THROUGH WHICH THE ELECTRICAL FORCES OF THE BODY PLAY -IT'S WHAT THE UNIVERSAL ESSENCE/SOUL/CONSCIOUSNESS DEPOSITED -IT IS THE LIGHT OF THE BODY THAT GIVES LIFE TO THE WHOLE TEMPLE. -THE PINEAL IS THE MALE SPIRITUAL ORGAN. -THE PINEAL GLAND OPENS WHEN THE TWO EYES ARE CLOSED FOR PERIODS. -THE MORE SPIRITUAL WORK YOU DO THE MORE ACTIVE THE PINEAL GLAND BECOMES -THE PINEAL GLAND IS COVERED IN MICROCRYSTALS.
- [x] `132` CRYSTALS HAVE THE MELATONIN ABILITY TO RECEIVE AND EMIT FREQUENCIES.
- [x] `133` CRYSTALS ON PINEAL GLAND THE PINEAL GLAND HAS PIZOLUMINESCENT CELLS WHICH ARE CRYSTALILINE JAGGED PINEAL GLAND SHAPED.
- [x] `134` INHIBITION -THE RETINA OF THE TWO EYES ALSO HAS THESE CELLS RETINOHYPOTHALAMIC -THE PINEAL HAS THEM BECAUSE IT TAKES TRACT IN LIGHT AND REFLECTS, REFRACTS AND SUPRACHIAMATIC EMITES LIGHT.
- [x] `135` NUCLEUS -THE PINEAL GLAND EMITS LIGHT THIS IS SUPERIRIOR CERVICAL GANGLION WHY WE SAY ENLIGHTENMENT.
- [x] `136` THE VATICAN SUPPRESSED THE INFORMATION the pineal GLAND IS THE SEAT OF consciousness, also known as the ON THE PINEAL GLANDS' MYSTICAL POWERS. seat of the soul/throne of god. the pineal gland is an empty THE VATICAN (CATHOLIC CHURCH) TOOK OVER chamber that holds the universal essence which is invisable to the EUROPE AND DESTROYED/STOLE ALL THE naked eye. our true self is within the pineal gland and from this KNOWLEDGE AND LIBRARIES CONTAINING ALL centre we control the physical body.
- [~] `137` THE ANCIENT TEXTS AND INFORMATION OF OUR TRUE POWERS.
- [x] `138` THEY THEN CREATED AN ENCODED HOLY BIBLE TO KEEP PEOPLE EYE OF Ra EYE OF HORUS LOOKING OUTSIDE OF THEMSELVES FOR GOD. the vatican symbolizing the pineal gland pine cone SUMARIAN GOD HOLDING PINE CONE SYMBOLIZING PINEAL GLAND.
- [x] `139` THE ANCIENT EGYPTIANS KNEW ABOUT THE PINEAL GLAND THE PINEAL GLAND EVERYTHING IN THE BODY LEADS BACK TO ONE SOURCE POINT, WHICH IS THE CENTRE OF THE BRIAN.
- [x] `140` THE CENTRE OF THE BRAIN IS THE PINEAL GLAND, WHICH WE REFER TO AS "I.
- [x] `141` "WHEN WE SAY "I" WE ARE REFERRING TO THE INNER BEING/ OBSERVER/ENTITY THAT IS CONTROLLING THE BODY.
- [x] `142` IF WE SAY "MY BODY," THEN IF IT IS MINE, IT IS NOT ME.
- [x] `143` THIS BODY IS THE VEHICLE FOR OUR SOUL/ENTITY TO OPERATE WITHIN THIS PHYSICAL WORLD OF TIME AND SPACE. 33 VERDABREA THE THRONE OF GOD IS IN THE CENTRE OF THE BRAIN.
- [x] `144` CONSCIOUSNESS IS GOD AND WE ARE ALL THAT SAME SPARK OF CONSCIOUSNESS IN THE CNETRE OF THE BRAIN.
- [x] `145` THE RIGHT HAND OF GOD IS THE RIGHT HEMISPHERE OF THE BRAIN.
- [x] `146` THE RIGHT HEMISPHERE IS TO DO WITH CREATIVITY, INTUITION AND INSIGHT WHICH IS CONNECTED TO THE CEREBRUM (THE HIGHER BRAIN) chronicles 3:10 THE MOST HOLY PLACE = THE PINEAL GLAND/CENTRE OF THE BRAIN, TWO CHERUBIM = THE TWO HEMISPHEARS OF THE BRAIN.
- [x] `147` THE SWORD IN THE LAMB SYMBOLIZES KILLING THE LOWER NATURE OF YOUR CONSCIOUSNESS MASONIC ART SUMARIAN ART AND MOVING UP THE SPINE TO THE HIGHER MIND/HIGHER SELF.
- [x] `148` NOTICE THE LAMB IS LOOKING UP AT THE CUP WITH THE SUN ON THE TOP.
- [x] `149` THE CUP IS YOUR HEAD AND NECK, AND THE SUN IS YOUR CONSCIOUSNESS IN THE CENTRE OF THE BRAIN ON TOP OF YOUR NECK.
- [x] `150` THE BIRD IS AN AIR ANIMAL THAT SYMBOLIZES THE HIGHER NATURE OF MAN.
- [x] `151` THE GROUND ANIMALS SYMBOLISE THE LOWER NATURE OF MAN.
- [x] `152` THE TREE STUMP SYMBOLIZES YOUR SPINE THE HOLY GRAIL holy grail=neck and skull THE REASON WHY THE HOLY GRAIL IS A CUP IS BECAUSE THE SUN AND MOON CREATE THE HOLY FLUID (CHRIST OIL) AND FILL IT UP EVERY MONTH.
- [x] `153` MASONIC ART THIS MASONIC ART SYMBOLIZES THE SUN AND MOON CREATING THE "MILK AND HONEY" IN THE BRAIN.
- [x] `154` THE MILK IS THE FLUID CREATED BY THE MOON.
- [x] `155` THE HONEY IS THE FLUID CREATED BY THE SUN. magnetic electric PITUITARY PINEAL MILK HONEY MOON SUN FEMALE MALE MAGNETIC ELECTRIC - + holy grail Corinthians 6:19-20 "Or do you not know that your body is a temple of the Holy Spirit within you, whom you have from God?
- [x] `156` You are not your own, for you were bought with a price.
- [x] `157` So glorify God in your body." GLORIFY GOD IN YOUR BODY IS RAISING THE CHRISM/CHRIST OIL UP THE SPINE AND LOOKING AFTER THE BODY.
- [x] `158` THE ELITES IN POWER HAVE EXTERNALIZED ALL OF THE SACRED THINGS LIKE THE HOLY GRAIL, TEMPLE OF SOLOMON, ETC.
- [x] `159` THIS IS DONE TO KEEP YOU FROM FINDING OUT THE FACT THAT YOU ARE THE ULTIMATE OF ALL THINGS.
- [x] `160` MAN IS TRULY CREATED IN THE IMAGE OF GOD.
- [x] `161` THE CHURCH AND OTHER RELIGIONS ARE TEACHING THE MASSES THE EXOTERIC, MEANING EXTERNAL TEACHINGS.
- [x] `162` THIS IS DONE PURPOSELY TO KEEP THE PYRAMID SCHEME UP AND RUNNING.
- [x] `163` MEANWHILE, THE PEOPLE IN POWER GET TAUGHT THE ESOTERIC, MEANING THE INTERNAL TEACHINGS ABOUT THE BODY, CONSCIOUSNESS, AND THE METAPHYSICAL ASPECTS OF REALITY.
- [x] `164` THE BIBLE IS WRITTEN IN SUCH A WAY IT WILL RESONATE WITH YOUR LEVEL OF UNDERSTANDING.
- [x] `165` YOU CAN PERCEIVE THE BIBLE PHYSICALLY, HISTORICALLY, AND METAPHORICALLY DEPENDING ON HOW WIDE YOU HAVE EXPANDED YOUR MIND.
- [x] `166` YOUR REALITY IS YOUR LEVEL OF REALI-ZATION.
- [x] `167` PLANES OF EXISTENCE THERE ARE DIFFERENT LEVELS OF REALITY.
- [x] `168` THEY MELT INTO THE PLANE THAT IS ABOVE AND BELOW
- [x] `169` IN OTHER WORDS, EACH PLANE IS A PRODUCT OF THE PLANE THAT IS ABOVE.
- [x] `170` THE HIGHER THE PLANE, THE MORE FLUID/FORMLESS IT BECOMES
- [x] `171` THE LOWER THE PLANE, THE MORE MATERIAL AND SOLID IT BECOMES.
- [x] `172` MENTAL PLANE THE MENTAL PLANE IS THE DIMENSION OF THE MIND.
- [x] `173` THE MIND IS A PART OF THE UNIVERSAL MIND.
- [x] `174` THEREFORE, THE MENTAL PLANE IS SHARED BETWEEN ALL THE MINDS THAT EXIST.
- [x] `175` IT IS THE WORLD OF THOUGHTS.
- [x] `176` THOUGHTS ARE NOT CREATED
- [x] `177` THEY ARE RECEIVED BASED UPON WHAT FREQUENCY OUR MIND IS SET TO.
- [x] `178` THIS IS WHY WE CALL IT A MINDSET.
- [x] `179` EACH THOUGHT, TOPIC, AND MENTAL SUBJECT IS A FREQUENCY, AND WHEN YOU SET YOUR MIND TO THESE TOPICS, YOU GAIN THE THOUGHTS THAT ARE ON THAT SIMILAR FREQUENCY.
- [x] `180` THE WORLD OF THOUGHT IS COMPLETELY FORMLESS.
- [x] `181` IT IS THE MOST FLUIDIC PLANE ASTRAL PLANE THE ASTRAL PLANE IS WHERE THOUGHTS MANIFEST INTO FORMS.
- [x] `182` FOR EXAMPLE, THE MENTAL PLANE IS THE THOUGHT OF THE CHAIR, AND THE ASTRAL PLANE IS THE IMAGINATION OF THAT CHAIR.
- [x] `183` ITS BASICALLY THE WORLD OF IMAGINATION AND MENTAL PICTURES.
- [x] `184` THE SCREEN WE SEE IN OUR MIND WHEN WE IMAGINE SOMETHING IS THE ASTRL PLANE.
- [x] `185` WE CREATE WITH OUR THOUGHTS
- [x] `186` THIS IS WHY THOUGHTS ARE THINGS.
- [x] `187` HIGHER ASTRAL THE ASTRAL PLANE IS CREATED OUT OF THOUGHTS MANIFESTING, AND EACH THOUGHT HAS A VIBRATIONAL FREQUENCY.
- [x] `188` THIS RESULTS IN GENERATING 3 MAIN LEVELS TO IT: HIGHER, MIDDLE, AND LOWER.
- [x] `189` DEPENDING ON THE VIBRATIONAL FREQUENCY OF THE THOUGHT, MANIFESTING WILL RESULT IN THE THOUGHT FORM MANIFESTING ON THE HIGHER MIDDLE OR LOWER ATRAL PLANES.
- [x] `190` THE HIGHER PLANES WILL EMBODY HIGH VIBRATIONAL THOUGHTS LIKE LOVE AND JOY, AND THE LOWER PLANES WILL BE DEMONIC THOUGHTS LIKE HATE, MURDER, AND LUST.
- [x] `191` MIDDLE ASTRAL WHEN WE ASTRAL PROJECT, WE ARE USING OUR MIND TO PROJECT THE SOUL INTO THE ASTRAL PLANE.
- [x] `192` YOU WILL ONLY SEE AND ENCOUNTER BEINGS THAT ARE ON A SIMILAR FREQUENCY AS YOU.
- [x] `193` IF YOU OPERATE ON A LOW FREQUENCY, YOU WILL COME ACROSS DEAMONS AND NEGATIVE ENTITIES.
- [x] `194` DAEMONS, ANGELS, SPIRITS, AND JINS ARE LIVING WITHIN THE ASTRAL PLANE.
- [x] `195` THEY ARE BASICALLY ENTITIES THAT HAVE NO PHYSICAL BODY.
- [x] `196` ELEMENTALS ARE SPIRITS OF THE 4 ELEMENTS
- [x] `197` FOR EXAMPLE, THERE ARE SPIRITS OF FIRE, WATER, EARTH, AND AIR.
- [x] `198` LOWER ASTRAL ETHERIC PLANE THE ETHERIC PLANE IS THE WORLD OF ENERGY, ELECTRICITY AND MAGNETISM.
- [x] `199` IT IS THE 5TH ELEMENT, ALSO KNOWN AS SPIRIT OR AETHER.
- [x] `200` THE ETHER IS A SUBSTANCE THAT HAS ONE FOOT IN THE PHYSICAL WORLD AND ONE FOOT IN THE ASTRAL WORLD.
- [x] `201` ETHER IS WHERE WE GET THE WORD EITHER FROM.
- [x] `202` EITHER IS CONNECTING TWO SCENARIOS IN LANGUAGE, FOR EXAMPLE, "I EITHER SUPPORT MANCHESTER UNITED OR LIVERPOOL" THE ETHER IS THE SAME THING, CONNECTING TWO TWO PLANES TOGETHER.
- [x] `203` THE WORD TOGETHER HAS THE WORD ETHER WITHIN IT.
- [x] `204` ITS JOINING TWO PLANES.
- [x] `205` ETHERIC THERE ARE ALSO ETHERIC ENTITIES THAT LIVE AMONGST US, LIKE GOBLINS, GNOMES, AND TROLLS.
- [x] `206` THEY ARE ENTITIES THAT HAVE THE ABILITY TO MATERIALIZE OR STAY IN THE ASTRAL BODY AT THEIR WILL.
- [x] `207` THEY CAN CHOOSE WHETHER TO BE PHYSICAL OR NON-PHYSICAL.
- [x] `208` THIS IS WHERE WE GET THE MYTHS OF TROLLS, FAIRIES, GNOMES AND GOBLINS FROM.
- [x] `209` THEY ARE VERY SECRETIVE BEINGS AND DO NOT LIKE TO BE SEEN BY HUMANS.
- [x] `210` PHYSICAL PLANE THE PHYSICAL PLANE IS THE WORLD OF MATTER.
- [x] `211` IT IS THE WORLD GOVERNED BY THE 5 ELEMENTS.
- [x] `212` IT IS THE PHYSICAL WORLD OF EFFECT.
- [x] `213` EVERYTHING WE EXPERIENCE AND VISUALLY SEE WITH THE TWO EYES IS THE EFFECT OF THE HIGHER PLANES ABOVE.
- [x] `214` THIS IS WHERE WE GET THE SAYING ABOVE, SO BELOW.
- [x] `215` YOU CHANGE THE HIGHER PLANES OF EXISTENCE
- [x] `216` YOU CHANGE THE PHYSICAL PLANES.
- [x] `217` THIS IS WHY MAGIC IS INDEED REAL.
- [x] `218` MAGICIANS AND OCCULTISTS DO HAVE METHODS TO HAVE CONTACT WITH THESE ASTRAL AND ETHERIC ENTITIES, WHICH THEN HAVE THE ABILITY TO MANIPULATE THE PHYSICAL PLANE.
- [x] `219` LEONARDO DA VINCI IS SYMBOLISING AS ABOVE SO PHYSICAL PLANE ETHEREAL PLANE ETNERNAL PLANE BELOW.
- [x] `220` LOOK UP BECAUSE THAT THE ROOT CAUSE.
- [x] `221` THERE IS NO POINT IN LOOKING DOWN HERE BECAUSE THE PHYSICAL PLANE IS THE WORLD OF EFFECT
- [x] `222` WHATEVER YOU SEE AND EXPERIENCE IS THE EFFECT OF YOUR MIND.
- [x] `223` SO LOOK UP AT THE CAUSE.
- [x] `224` CHANGE YOUR MIND YOU CHANGE YOUR REALITY.
- [x] `225` AS WITHIN SO WITHOUT.
- [x] `226` THE ETHEREAL PLANE IS IN CONSTANT ROTATION WITH THE PHYSICAL PLANE THROUGH RHYME, KARMA, POLARITY, AND GENDER.
- [x] `227` THE CIRCLE IS NEVER ENDING
- [~] `228` IT THE TWO MASONIC PILLERS HAS NO BEGINNING OR END, ITS ETERNAL.
- [x] `229` IT IS THE EXPANSIVENESS OF ALL THINGS.
- [x] `230` SYMBOLIZE THE NUMBER 11.
- [x] `231` IT IS THE MIRRORING OF REALITIES WITHIN THE THE MENTALISM PLANES OF EXISTENCE.
- [x] `232` WHATEVER YOU DO IN THE ASTRAL THE STARS ARE NOT PHYSICAL PLACES THEY ASTRAL PLANE WILL MANIFEST ARE PORTALS TO THE ASTRAL PLANE.
- [x] `233` THE INTO THE PHYSICAL WORLD
- [x] `234` STARS ARE THE START OF THE SOUL SYSTEM.
- [x] `235` ARE A STAR WRAPPED IN FLESH ( FALLEN STAR WE ITS LIKE A MIRROR.
- [x] `236` THIS IS ETHEREAL PLANE WHY YOU ALWAYS SEE TWO ANGLE OF LIGHT (FALLEN ANGEL)).
- [x] `237` PILLERS IN THE MASONIC ARTWORK.
- [x] `238` ASTRONOMY CORRESPONDANCE ENERGY ASTRO=ASTRAL SPACE IS FAKE ASTRAL PROJECTION AND ASTRAL PLANE ADDITIONAL INFO BEFORE YOU ASTRAL PROJECT THE ASTRAL PLANE IS THE 4TH DIMENSION
- [x] `239` IT'S THE UNSEEN OF WHAT WE SEE IT IS WHERE THOUGHT FORMS EXIST (MENTAL IMAGES) IT CAN BE SEEN ONLY BY OUR MIND'S EYE YOU WILL EXPERIENCE BEINGS AND ENTITIES THAT MATCH YOUR FREQUENCY, SO MAKE SURE YOU ARE VIBRATING AS HIGH AS POSSIBLE BEFORE TRYING TO PROJECT.
- [x] `240` EVERYTHING YOU THINK OF WILL MANIFEST INSTANTLY IN THE ASTRAL PLANE (4TH DIMENSION) YOUR VISION IN THE ASTRAL PLANE WILL NOT BE VERY CLEAR WHEN YOU FIRST ASTRAL PROJECT.
- [x] `241` YOU HAVE TO WORK ON STRENGTHENING IT.
- [x] `242` YOU CREATE DEAMONS THE IDEAS WE MENTALLY ENTERTAIN CAN TAKE FORM IN THE 4TH DIMENSIONAL PLANE.
- [x] `243` BY ENTERTAINING NEGATIVE THOUGHT FORMS FOR LONG PERIODS, THE EMOTIONAL POWER WE GIVE THIS THOUGHT CAN MANIFEST INTO A DEAMON.
- [x] `244` EVERY SINGLE MENTAL ADDICTION YOU HAVE IS SOME DEAMON YOU CREATED WITHIN THE ASTRAL PLANE.
- [x] `245` IT GROWS THE MORE EMOTION (ENERGY IN MOTION) YOU GIVE IT.
- [x] `246` THE WORD DEAMON HAS MON IN IT, WHICH MEANS MOON.
- [x] `247` MOON IS MIND, WE CREATE DEAMONS WITH OUR MINDS.
- [x] `248` HOW ASTRAL PROJECTION WORKS YOUR MIND IS THE PROJECTOR OF YOUR SOUL.
- [x] `249` YOUR SOUL IS THE EXPERIENCER (OBSERVER).
- [x] `250` WHEN YOU ASTRAL PROJECT, YOU ARE USING YOUR MIND TO PROJECT THE SOUL OUT OF THE PHYSICAL BODY (PHYSICAL WORLD) INTO THE ASTRAL PLANE WHERE THERE ARE NO LIMITATIONS OF TIME AND SPACE.
- [x] `251` WHEN YOU "DREAM," YOUR MIND IS PROJECTING THE SOUL INTO ANOTHER REALITY WHILE THE PHYSICAL BODY IS RESTING.
- [x] `252` PRACTICES FOR ASTRAL PROJECTION LIE DOWN FLAT WITH NO BODY PARTS TOUCHING REST EVERY SINGLE MUSCLE AND BE AS STILL AS POSSIBLE CLOSE YOUR EYES BREATH DEEP IN THROUGH THE NOSE AND SLOWLY OUT THE MOUTH MEDITATE UNTIL YOU HAVE LOST ALL DESIRES AND THE MIND IS EMPTY OF THOUGHTS THEN FOCUS YOUR ATTENTION ON THE MIDDLE OF YOUR BRAIN (PINEAL GLAND) DO THIS UNTIL YOU START TO FEEL TINGLING SENSATION ALL OVER THE BODY THE TINGLING SENSATION IS YOUR ENERGY BODY (ETHERIC BODY) BEING AWAKENED NOW IMAGINE YOURSELF PULLING A ROPE UP INTO THE SKY YOU MAY FEEL YOURSELF BEING LIFTED OUT OF THE BODY
- [x] `253` DO NOT BE SCARED KEEP DOING THIS EXERCISE UNTIL YOU GAIN THE ABILITY TO LEAVE THE WHOLE BODY AND DISCOVER THE ASTRAL PLANE IF YOU DO ASTRAL PROJECT SUCCESSFULLY AND YOU FEEL AS IF YOU WANT TO ENTER BACK INTO YOUR PHYSICAL BODY, ALL YOU HAVE TO DO IS THINK ABOUT GOING TO YOUR BODY, AND YOU WILL BE SHOT BACK INTO YOUR BODY.
- [x] `254` JESUS NEVER WALKED ON WATER.
- [x] `255` IT IS SYMBOLIC FOR LEAVING THE PHYSICAL BODY.
- [x] `256` THE WATER IS THE ETHERAL PLANE, WHICH IS THE VEIL BETWEEN THE PHYSICAL WORLD AND THE ASTRAL WORLD.
- [x] `257` JESUS WAS WALKING ON TOP OF THE VEIL OF THE ETHER (ASTRAL PROJECTING).
- [x] `258` WHEN JESUS TEACHES PETER TO "WALK ON WATER," HE IS TEACHING HIM NOT TO BE SCARED OR ELSE YOU WILL FALL BACK INTO THE WATER.
- [x] `259` THIS IS SYMBOLIC OF WHEN YOU ARE ASTRAL PROJECTING.
- [x] `260` WHEN YOU START TO FEAR WHEN YOU'RE PROJECTING, YOU WILL BE SUCKED BACK INTO YOUR BODY.
- [x] `261` MATHEW 14:29 "he was afraid and, beginning to sink, cried out, "Lord, save me!" CHAKARAS Chakara in sanscript means wheel.
- [x] `262` THE CHAKARAS ARE 7 WHEELS OF ENERGY THAT ARE A PART OF THE ELECTROMAGNETIC FIELD WE CALL OUR AURA.
- [x] `263` THE CHAKRAS ARE LIKE MINI-BRAINS CONTROLLING ALL THE CELLS AND ORGANS WITHIN THAT section of the body OF THE BODY.
- [x] `264` THE 7 CHAKARAS ARE THE 7 SEALS IN THE BIBLE.
- [x] `265` THE CHAKARAS ARE A PART OF THE ETHERIC BODY AS THEY ARE 7 SEALS THAT BIND YOUR SOUL/SPIRIT TO THE PHYSICAL BODY.
- [x] `266` THE LOWEST CHAKARA (ROOT CHAKARA) IS THE MOST DENSE/PHYSICAL, AND THE HIGHEST (CROWN CHAKARA) IS SPIRIT/FORMLESS.
- [x] `267` WE DESCENDED FROM SPIRIT INTO MATTER
- [x] `268` NOW WE HAVE TO RETURN TO OUR SPIRIT SELF IN THE CROWN CHAKARA.
- [x] `269` THE CROWN CHAKARA IS LOCATED JUST ABOVE THE HEAD, OUT OF THE BODY BECAUSE ITS PURE SPIRIT.
- [x] `270` OUR TRUE GOD SELF IS HIDDEN BEHIND THE 7 CHAKRAS, AS THE CHAKRAS CAN BE ABUSED OR BALANCED.
- [x] `271` WHEN WE BALANCE THE VICES OF THE CHAKARAS, WE BUILD A STRONG MIND AND SOUL CONNECTION, WHICH THEN MANIFESTS INTO OUR EXTERNAL WORLD.
- [x] `272` WHEN THE MIND & BODY MANIFEST THE SOUL/HIGHER SELF IDEAS 24/7, WE BECOME OUR TRUE GOD SELF, AND THERE ARE NO MENTAL OR ETHERIC BLOCKAGES WITHIN OUR DIFFERENT BODIES OF CONSCIOUSNESS.
- [~] `273` MOON SPIRIT SPIRITUALITY CONNECTION GOLD INTUITION MERCURY spirit PHYCIC ABILITY COMMUNICATION VENUS SELF-EXPRESSION LOVE SUN air INNER PEACE POWER MARS fire SELF LOVE SEXUALITY JUPITER water CREATIVITY LEAD GROUNDING SATURN earth SURVIVAL MATTER "144,000 go to heaven" 144,000 A THERE ARE ACTUALLY 7 VOULS, AND EACH VOUL CORRESPONDS WITH ONE OF THE CHAKARAS.
- [x] `274` WHEN CHANTING THE ADD FIRST 5 PETALS VOULS CORRECTLY, IT CREATES THE E PHONETIC SOUND OF "OHM".
- [x] `275` OHM is root=4 known as THE SOUND OF CREATION, sacrel=6 AND WHEN WE SAY it, WE ARE ALIGNING solar=10 THE 7 CREATIONAL ENERGIES WITHIN OUR ETHERIC BODY.
- [x] `276` EACH CHAKARAS heart=12 I VIBRATES ON A DIFFERENT FREQUENCY, throat=16 AND YOU CAN LISTEN TO THESE
- [~] `277` FREQUENCIES TO HELP BALANCE EACH CHAKARA. 4+6+10+12=48
- [x] `278` third eye=2 petals
- [x] `279` O MENTAL PLANE = THOUGHTS ASTRAL PLANE = IMAGINATION 48x2=96 ETHERIC PLANE = ENERGY 96+48=144
- [~] `280` crown=1000 petals U PHYSICAL PLANE = MATTER THE ETHER IS THE 5TH ELEMENT, ALSO
- [x] `281` KNOWN AS SPIRIT.
- [~] `282` ITS A SUBSTANCE 1000x144=144,000hz JAHOVAS WITNESS BELIEVE EXACTLY 144,000 FAITHFUL CHRISTIAN WILL Y THAT HAS ONE FOOT IN THE ASTRAL PLANE AND IN THE PHYSICAL PLANE.
- [x] `283` ETHER IS THE WORD EITHER BECAUSE ITS ON EITHER SIDE.
- [x] `284` THE CHAKRAS ARE GO TO HEAVEN.
- [x] `285` THIS IS A ON THE ETHERIC PLANE, AND WHEN WE FREQUENCY YOU NEED TO ACHIEVE IN ORDER TO GO FROM THE ROOT TO THE CROWN CHAKRA (HEAD=HEAVEN) M UNLOCK THESE CENTRES, WE UNLOCK OUR TRUE SPIRIT FORM.
- [~] `286` CHAKARAS I KNOW HOW TO KNOW YOUR PASSING THROUGH CHAKARAS I SEE ROOT = YOU WILL NO LONGER FEAR AND FEEL STABLE SACREL= NO LONGER HAVE LUST/DESIRE FOR SEX I SPEAK SOLAR = NO LONGER DESIRE FOR FOOD HEART = NO LONGER HATE ANYTHING/ANYONE I LOVE THROAT = NO LONGER HOLD YOURSELF BACK TO EXPRESS YOURSELF I DO THIRDEYE = HAVE THE ABILLTY TO READ PEOPLES ENERGY, INTUITION AND ASTRAL PROJECTION.
- [x] `287` I FEEL CROWN = AT ONE WITH EVERYTHING, NO NEGATIVE TRATES, NO EGO, NO HATE, NO DESIRE FOR METERIAL THINGS, NO ATTATCHMENT TO I AM ANYTHING.
- [~] `288` THE HIGHER 3 CHAKRAS ARE THE HIGHER STATES OF CONSCIOUSNESS WHERE YOUR DEUTERONOMY 20:17 MIND IS NO LONGER MANIFESTING "Completely destroy them—the Hittites, Amorites, Canaanites, WHATEVER THE LOWER SELF DESIRES.
- [x] `289` THE Perizzites, Hivites and Jebusites—as the LORD your God has MIND HAS BECOME DISCIPLINED AND commanded you" CARRIES OUT MORE SPIRITUAL DESIRES LIKE FASTING, MEDITATION, ASTRAL PROJECTION, -GOD SUPPOSEDLY ORERED FOR THE CANANITES, AMORRITES AND ENERGY HEALING, AWAKENING THE THIRD HITTITIES TO BE "DESTROYED" BUT AS WE KNOW THAT WOULD BE EYE & SAVING SEXUAL ENERGY TO ACTIVATE MURDER WHICH GOD DOES NOT CONDEM ONTO ANY MAN.
- [x] `290` THE SOUL AND THE MIND -CANANITES, AMORRITES AND HITTITIES SYMBOLISE MANS LOWER HAVE GAINED A STRONG CONNECTION, AND NATURE AS THEY WERE CANIBALS AND MURDERES.
- [x] `291` THE MIND IS MANIFESTING WHAT THE SOUL -SO THIS IS SYMBOLIC FORDESTORYING YOUR LOWER/ANIMAL WILLS TO DO.
- [~] `292` NATURE AND TURNING TO YOUR HIGHER/SPIRIT SELF.
- [x] `293` THE LOWER 3 CHAKARAS ARE THE LOWEST UNBALANCED CHAKARAS STATES OF CONCIOUNESS WHERE YOU -OVERUSING OR INCORRECT USAGE OF THE ENERGY CENTRES IDENTIFY AS THE PHYSICAL BODY (MATTER OVER MIND).
- [x] `294` THE MIND AND BODY ARE WILL RESULT IN UNBLALNCED CHAKARAS, WHICH BLOCK THE OPERATING IN SURVIVAL MODE, MEANING FLOW OF ENERGY WITHIN THE ELECTROMAGNETIC FIELD OF YOU ARE DOING WHATEVER THE BODY THE BODY.
- [x] `295` THIS RESULTS IN A LOWER FREQUENCY AS YOU DESIRES.
- [x] `296` AN EXAMPLE OF THIS IS EATING ARE PULLING TOO MUCH ENERGY OUT OF YOUR FIELD.
- [~] `297` WHENEVER THE STOMACH RUMBLES, -FOR EXAMPLE, IF YOU ARE OVERSEXUAL, YOU ABUSE YOUR RELEASING SEXUAL FLUIDS WHENEVER YOU SACREL CHAKARA, WHICH IS WEAKENING YOUR FIELD.
- [~] `298` FEEL LIKE IT, ETC.
- [x] `299` THIS STATE OF CONSCIOUSNESS IS MANIFESTING HELL.
- [x] `300` BAPHOMET SYMBOLOGY THE BAPHOMET/DEVIL HAS A GOAT HEAD TO SYMBOLIZE THE ANIMAL NATURE OF MAN.
- [x] `301` The Baphomet is holding the RIGHT HAND UP FOR THE RIGHT-HAND PATH (ascension) and the left hand down for descension.
- [x] `302` THE BAPHOMAT IS NOT A REAL ENTITY
- [x] `303` IT SYMBOLIZES AN INDIVIDUAL'S MINDSET.
- [x] `304` THE BAPHOMAT IS femanine BOTH MALE AND FEMALE, SYMBOLIZING DIVISION AND INVERSION OF GOD'S CREATION. masculin EL=GOD GOD IS ONENESS, MEANING HE IS GENDERLESS.
- [x] `305` OUR CONSCIOUSNESS IS GENDERLESS, MEANING WE ARE A SPARK OF GOD
- [x] `306` GOD IS CONSCIOUSNESS.
- [x] `307` WE COME FROM THE ONE, AND WE INCARNATE INTO DUALITY TO GAIN THE KNOWLEDGE OF GOOD AND EVIL.
- [x] `308` THE CROWN CHAKARA IS THE ONLY CHAKARA LOCATED OUT OF THE PHYSICAL BODY.
- [x] `309` THIS IS DUE TO IT BEING PURE SPIRIT, MEANING IT IS NOT A PART OF THE DUALISTIC/ PHYSICAL WORLD
- [x] `310` HIGH FREQUENCY NOTICE HOW THE MAJORITY OF FAST-FOOD RESTAURANT SYMBOLS ARE RED, ORANGE, OR YELLOW.
- [x] `311` THIS IS BECAUSE THEY UNDERSTAND THAT 80% OF PEOPLE'S MINDS MANIFEST THE DESIRES OF THE LOWER 3 CHAKRAS.
- [x] `312` THE MINDS THAT OPERATE ON THEIR LOWER FREQUENCIES WILL BE ATTRACTED TO THE COLOURS OF THEIR LOWER FREQUENCIES.
- [x] `313` PLUS, THE SO-CALLED "FOOD" THE RESTAURANTS SUPPLY IS KEEPING THEM STUCK IN THE LOWER 3 CHAKARAS (SURVIVAL MODE).
- [x] `314` THE WORD HUMAN COMES FROM THE WORD HUE, WHICH MEANS AN ATTRIBUTE OF A COLOUR.
- [x] `315` EACH ONE OF US OPERATES WITHIN A FREQUENCY, AND THAT FREQUENCY IS A COLOUR WITHIN THE ELECTROMAGNETIC LIGHT SPECTRUM.
- [x] `316` WE ARE AN ATTRIBUTE OF A SPECIFIC COLOUR BASED ON WHAT OUR MIND IS SETTING OUR FREQUENCY TO.
- [x] `317` THIS IS WHY WE CALL IT A MINDSET YOUR MIND SETS ITSELF TO VARIOUS FREQUENCIES.
- [~] `318` LOW FREQUENCY CHAKARAS PAGE 243 FIGURE 11:11 FROM THE BOOK "BECOMING SUPERNATURAL"-AUTHORED BY DOCTOR JOE DISPENZA SEVEN UP IS TRUTH IN PLANE SITE. from thought to energy matter WHOLENESS BLISS FREEDOM LOVE JOY NOTICE HOW LUST IS THE LOWEST APPRECIATION VIBRATIONAL EMOTION.
- [x] `319` THIS IS WHY LUST GRATITUDE FOR SEX IS PUSHED UPON US BY THE MUSIC INDUSTRY, ESPECIALLY RAP MUSIC.
- [x] `320` ANYTHING THAT IS FREE, YOU ARE THE WILL PRODUCT
- [x] `321` THIS IS WHY PORN IS FREE POWER BECAUSE IT WASTES YOUR SEED, KEEPING YOU IN THE LOWEST VIBRATIONAL STATE CONTROL OF LUST.
- [x] `322` ANGER FEAR GUILT SHAME SUFFERING VICTIMIZATION PAIN LUST HAND & FEET CHAKARAS The 7 Chakras are not limited to the spine but extend their influence to the hands.
- [~] `323` They manifest in the following associations: Manipura (solar plexus)= thumb.
- [x] `324` Anahata (heart) = index finger.
- [x] `325` Vishuddhi (throat) = middle finger.
- [x] `326` Muladhara (root) = ring finger.
- [x] `327` Swadhisthana (sacral) = finger.
- [~] `328` Sahasrara (crown) = PALM Ajna Chakra (third eye) = WRIST POINT This arrangement results in a harmonious balance on the hand, where the ring and little fingers embody feminine qualities, while the thumb and index finger exude masculine attributes.
- [~] `329` Additionally, a central axis extends from the wrist point, passing through the center of the palm and reaching up to the middle finger, symbolizing the Spirit Element.
- [x] `330` This central axis serves as a reconciling force for the contrasting gender principles.
- [x] `331` Hand Chakras serve as a vital interface between the physical and energetic dimensions, allowing us to engage with the world on both levels.
- [x] `332` The fingers function as sensitive receptors, while the palms act as conduits for channeling healing energy.
- [x] `333` Your dominant hand serves as the source of energy emission, while the non-dominant hand acts as the recipient.
- [~] `334` In contrast to the feet
- [x] `335` which are associated with the Earth Element and the physical body, the hands correspond to the Air Element and the realm of the mind, as they are suspended in the air before us.
- [x] `336` Consequently, the Hand Chakras wield significant influence over the information that enters our consciousness. there exists a network of energy centers known as Minor Chakras in the feet (AS ABOVE SO BELOW).
- [x] `337` These Minor Chakras play a HUGE role in facilitating A WIDE range of energy inflOW into THE HUMAN BODY AND CONSIOUSNESS.
- [~] `338` FOOT AND CHAKARAS: Manipura (solar plexus) = big toe.
- [x] `339` Anahata (HEART) = index toe.
- [x] `340` Vishuddhi (THROAT) = middle toe.
- [~] `341` Ajna (THIRD EYE) = fourth toe.
- [x] `342` Swadhisthana (SACREL) finds resonance in the little toe.
- [x] `343` Sahasrara (CROWN) = middle of the sole.
- [x] `344` Muladhara (root) = back of the heel.
- [x] `345` One of the primary functions of the toes is to release and discharge any surplus energy that accumulates within the Major Chakras through our everyday activities and bodily functions.
- [x] `346` This excess energy is channeled into the Earth, facilitating a grounding of our consciousness.
- [x] `347` When the Minor Chakras in the feet operate harmoniously and are in alignment with the Major Chakras, it establishes a continuous connection and a flow of communication between the Earth's energy grids and our own energies.
- [x] `348` ROOT CHAKARA CORRESPONDS WITH THE EARTH ELEMENT AS ITS THE MOST PHYSICAL/METERIALISTIC CHAKRA.
- [x] `349` THIS IS WHY HEEL IS HELL BECAUSE WHEN OUR MIND OPERATES OFF THE ROOT CHAKARA, WE DESIRE, FEAR, AND LACK INSECURITY.
- [x] `350` IN OTHER WORDS, WE MANIFEST HELL.
- [x] `351` HEAD IS HEAVEN THE 3 BRAINS CONTROL THE 3 SECTIONS OF THE BODY HIGHER BRAIN HEAVEN/HEAD MENTAL MIND GOD MAMEL EARTH/HEART EMOTIONAL SOUL JESUS HELL/HEEL PHYSICAL BODY SATAN REPTILLIAN NOTICE HOW THE LANDSCAPE OF THE EXTERNAL WORLD MATCHES UP WITH THE CHAKRA SYSTEM.
- [x] `352` LAVA IS UNDER GROUND WHICH IS RED AND CORRESPONDS WITH THE ROOT CHAKARA (HELL).
- [x] `353` THE SKY IS BLUE AND CAN TURN PURPLE AT NIGHT, WHICH SYNCS IN WITH THE HIGHER THREE CHAKARAS.
- [x] `354` THE EARTH IS GREEN, AND THE HEART CHAKARA IS GREEN, AS ABOVE AND BELOW.
- [x] `355` SET HORUS GROUND ANIMAL-OX AIR ANIMAL-BIRD LOWER SELF HIGHER SELF THE DEVIL HAS GROUND ANIMAL FEATURES SYMBOLIZING THE LOWER SELF.
- [x] `356` THE ANGEL HAS WINGS WHICH ARE BIRD FEATURES SYMBOLIZING HIGHER SLEF.
- [x] `357` THE ELITES IN CONTROL HAVE EXTERNALIZED THIS METAPHYSICAL CONCEPT TO JESUS AND SATAN TO MAKE PEOPLE LOOK OUTSIDE OF THEMSELVES.
- [x] `358` THIS RESULTS IN LACK OF AWARENESS OF THERE OWN CONSCIOUSNESS WHICH THEN CREATES A SOCIETY OPERATING THERE LIFES OUR OF THE LOWER CHAKARAS HEAD IS HEAVEN EL EL=GOD IS CONSCIOUSNESS RA NO ENDER MASCULINE FEMANINE FIRE WATER O SOL MON CONSCIOUS SUB-CONSCIOUS LEFT BRAIN RIGHT BRAIN -IN THE BIBLE THE HEAD IS REFERED TO AS THE UPPER ROOM WHERE JESUS MET THE 12 DISCIPLES.
- [x] `359` THE 12 DISCIPLES ARE THE 12 CRANIAL NERVES IN THE BRAIN WHICH ARE THE 12 ZODIAC SIGNS. -MOSES CROSSING THE RED SEA IS MOVING YOUR PERCEPTION/AWARENESS INTO THE RIGHT HEMISPHERE OF THE BRAIN.
- [x] `360` THE RED SEA IS THE CORPOS COLLOSUM, WHICH CONNECTS THE TWI HEMISPHEARS OF THE BRAIN.
- [x] `361` THE RIGHT HEMISPHERE SHOWS THE UNIFIED PERCEPTION OF REALITY.
- [x] `362` IT IS THE PLACE OF YOUR HIGHER SELF.
- [x] `363` RIGHT BRAIN THE RIGHT BRAIN IS THE FEMANINE ASPECT OF THE BRAIN.
- [x] `364` IT CREATES A WHOLISTIC PERCEPTION OF REALITY WHERE ALL THINGS ARFE UNITED AND ONENESS.
- [x] `365` IT IS ALSO THE PLACE OF OUR INTUITION, CREATIVITY, AND INSIGHT.
- [x] `366` FOR EXAMPLE, THIS SIDE OF THE BRAIN VIEWING HUMANS AS ONE UNITED CONSCIOUSNESS.
- [x] `367` LEFT BRAIN THE LEFT HEMISPHERE IS THE ANALYTIC SIDE OF THE BRAIN.
- [x] `368` IT BREAKS DOWN THE UNITED PERCEPTION OF THE RIGHT HEMISPHERE INTO SINGULAR SEGMENTS.
- [x] `369` THIS IS IMPORTANT AS IT GIVES US THE ABILITY TO BREAK THINGS DOWN AND MANIPULATE THEM.
- [x] `370` THE LEFT BRAIN IS THE MASCULINE SIDE, AND IT IS THE PLACE OF THE EGO.
- [x] `371` THE LEFT BRAIN SEES HUMANITY AS INDIVIDUALS AND NOT UNIFIED LIKE THE RIGHT BRAIN.
- [x] `372` SIN IN LATIN IS SINISTER MEANS LEFT RIGHT = RIGHTIOUS THE ARK OF THE COVENENT=TWO HEMISPHEARS OF THE BRAIN SPOTIFY, RADIO, APPLE MUSIC, AND ALL MAJOR PLATFORMS ARE TUNED TO 440HZ. 440HZ SHUTS OFF THE RIGHT SIDE OF THE BRAIN, RESULTING IN YOU BEING LEFT-BRAIN DOMINANT.
- [x] `373` THEY DO NOT WANT YOU to be balanced or right brain dominant DUE TO IT BEING THE CREATIVE, INTUITIVE, and unified part of the brain.
- [x] `374` THE ROCKERFELLA FOUNDATION IN THE 1950s changed the standard music tuning from 432hz to a440hz.
- [x] `375` THIS IS TO KEEP YOU THINKING LOGICALLY INSTEAD OF CRITICALLY.
- [x] `376` FREQUENCY IS THE ONLY THING THAT ENTERS YOUR TEMPLE WITHOUT CONSENT, AFFECTING YOU NO MATTER WHAT.
- [x] `377` THIS IS WHY MUSIC IS ONE OF THEIR MOST POWERFUL TOOLS INSTEAD, YOU WANT TO LISTEN TO MUSIC/FREQUENCIES IN 432HZ/528HZ/963HZ OR ANY OF THE SOLFEGIO SCALE FREQUENCIES.
- [~] `378` THE SOLFEGGIO SCALE 3+9+6=18=9 4+1+7=12=3 5+2+8=15=6 THE TWO ANGLES COVERING THE COVENENT ARE THE TWO 7+4+1=12=3 HEMISPHERES OF THE BRAIN COVERING (PROTECTING) THE SACRED CENTRE OF THE BRAIN.
- [x] `379` THE CENTRE OF THE BRAIN IS THE "MOST IF YOU ADD ANY OF THE SOLFEGGIO HOLY HOUSED" IN THE BIBLE.
- [x] `380` THIS PLACE IS THE THRONE OF GOD/CONSCIOUSNESS WITHIN THE PINEAL GLAND.
- [x] `381` SCALE FREQUENCIES UP THEY ALL ADD TO 3,6 OR 6 HEAD IS HEAVEN head=hea=heaven God (higher self) is reaching/ stretching over to TRY to CONNECT WITH Adam (lower self)
- [x] `382` and Adam is relaxed, SHOWING NO EFFORT.
- [x] `383` THIS PAINTING IS SHOWING ALL YOU HAVE TO DO MOVE UP TO THE HIGHER MIND TO REACH YOUR HIGHER SELF.
- [x] `384` THE HIGHER SELF IS ALWAYS SPEAKING AND GIVING COMMANDS, BUT THE LOWER SELF DOMINATES.
- [x] `385` ALL YOU HAVE TO DO IS FOLLOW THE COMMANDS OF THE HIGHER SELF (HIGHER MIND/THOUGHTS).
- [x] `386` THE HEAD IS HEAVEN BECAUSE IT IS THE PLACE OF CONSCIOUSNESS IN THE CENTRE OF THE BRAIN.
- [x] `387` THE PINEAL GLAND IS THE PLACE OF THYNE CONSCIOUSNESS, AND IT HAS ACCESS TO THE ASTRAL PLANE. concentration contemplation meditation HEAD HEAVEN masculine femanine solar lunar yang yin HEEL HELL early christian artwork HEAD IS HEAVEN OBSERVER/INNER BEING/CONCIOUSNESS OBSERVER/INNER left hemisphear right hemisphear BEING/CONCIOUSNESS left hemisphear right hemisphear EGYPTIAN FALCON OF HORUS EGYPTIAN DJED PILLAR holy grail central nervous system two hemispheres soul/conciousness spine KNOW THYSELF merkaba CELESTIAL SPHERE TO PORTRAY DIFFERENT PLANES OF REALITY MER=LIGHT KA=SPIRIT BA=BODY eye of horus VEHICLE OF ASCENSION HORUS IS THE SUN SUN=SOL=SOUL NEUTRALIZING THE DUALITY OF SELF BY COMBINING THE UPPER AND LOWER SELF.
- [x] `388` YOU ARE A SOUL THAT YOU ARE AN ETERNAL EXPERIENCES DIFFERENT REALITIES WITHIN THE SUN/SOUL MULTI-VERSE.
- [x] `389` IN EACH PLANE YOU TAKE ON THE SINGLE EYE IS THE DIFFERENT BODIES.
- [x] `390` YOUR AIM IS TO BECOME A SYMBOL OF THE SOUL MULTI-DIMENSIONAL CREATURE AND NOT TO BE EYE OF THE SOUL BOUND TO JUST ONE REALITY. 5 SENSES OF THE SOUL MENTAL devil consciousness The body does not live.
- [x] `391` It is only maintained by the ASTRAL veils ETHERIC spirit/consciousness within.
- [x] `392` Jesus said, "Man will never see death, for there is no death to see or know." The body manifests PHYSICAL dveil the spirit
- [x] `393` that which we think of and will to do manifests the body to do so.
- [x] `394` Actions of the body are under the command of the centering soul.
- [x] `395` The body is an electrical machine that takes commands from the omnipotent cosmic intelligence.
- [x] `396` To think is to create.
- [x] `397` We create with light
- [x] `398` nothing is not light.
- [x] `399` THE DEVIL IS ACTUALLY YOU DE-VEILING The form is born in the image of thinking.
- [x] `400` I alone exist
- [~] `401` I am the YOURSELF INTO THE LOWER PLANES OF all.
- [~] `402` EXISTNECE BY IGNORANCE OF TRUTH AND KNOWLEDGE.
- [x] `403` WHEN YOU DIE UNDER A FALSE Man is the only unit of creation that is self-aware of the IDENTITY OF SELF YOU HAVE NOW ADDED cosmic light within him.
- [x] `404` All else are electrically acting based ANOTHER VEIL ON TOP OF YOUR TRUE SOUL upon instinct.
- [x] `405` Corinthians 3:16-17 16 Know ye not that ye are the temple of God
- [x] `406` and that the Spirit of God = dwelleth in you? 17 If any man defile the temple of God, SYMBOL FOR SPIRIT him shall God destroy
- [x] `407` for the temple SPIRIT IS IN THE HEAD of God is holy, which temple ye are.
- [x] `408` KOPH=K SKULL HENCE WHY THE HEAD IS AN OVAL/CIRCLE Psalm 82:6 I have said, Ye are gods
- [x] `409` And all of you are children of the most High. 22 HEBREW LETTERS=22 BONES IN THE SKULL LEFT AND RIGHT BRAINS LEFT HEMISPEAR RIGHT HEMISPHEAR SCIENTIST ARTIST CONTROLS RIGHT SIDE OF THE BODY CONTROLS LEFT SIDE OF THE BODY LANGUAGE CREATIVITY THE PLACE OF THE EGO HOLISTIC PERCEPTION LOGICAL THINKING UNIFICATION SEQUENCING NON VERBAL CUES FACTS INTUAITION METERIALISTIC FEELINGS LETTERS VISUALIZATION ANALYTIC PATTERNS PERCIEVES REALITY IN USEFULNESS SPEACHLESS DETAILS METAPHORES SYMBOLS ACCEPTS REALITY AS IT IS CONTEXT BOTH HEMISPHERES PARTICIPATE AND CONTRIBUTE TO ALL ACTIVITIES
- [x] `410` HOWEVER, THEY DO THE ACTIVITY IN DIFFERENT WAYS.
- [x] `411` IN OTHER WORDS, BOTH BRAINS CARRY OUT THE SAME FUNCTIONS BUT FUNCTION IN TWO DISTINCT AND DIFFERENT WAYS.
- [x] `412` BOTH BRAINS HAVE SEPARATE VIEWS AND PERCEPTION OF THE WORLD.
- [x] `413` THE RIGHT BRAIN PRESENTS REALITY AS A UNIFIED WHOLE, WHICH EXPLAINS WHY THE PEOPLE IN POWER HAVE SPLIT UP ALL THE FIELDS OF KNOWLEDGE INTO DIFFERENT CATEGORIES WHEN IT IS ALL ACTUALLY ONE UNIFIED SCIENCE, WHICH IS DONE INTENTIONALLY TO KEEP US LEFT-BRAIN DOMINANT.
- [x] `414` ALL THINGS COME FROM THE ONE THEREFORE ALL IS ONE.
- [x] `415` THIS IS WHY THE EGYPTIANS STATED "ALL IS ATUM," MEANING ALL IS ATOM, THE TORUS FIELD.
- [x] `416` FOR EXAMPLE, THE RIGHT BRAIN WOULD SEE A JUNGLE AS A UNIFIED ENTITY, BUT THE LEFT BRAIN WILL SEE THE JUNGLE TREES AS SEPARATE BEINGS.
- [x] `417` THE LEFT BRAIN'S PURPOSE IS TO ANALYZE AND BREAK DOWN THE UNIFIED WHOLE PRESENTED BY THE RIGHT BRAIN.
- [x] `418` THIS PROCESS IS DONE BY THE LEFT HEMISPHERE SO THAT WE CAN HAVE DISTINCT SINGULAR FRAGMENTS OF REALITY SO THAT IT CAN MANIPULATE, MANAGE AND CONTROL IT.
- [x] `419` BOTH HEMISPHERES ARE NEEDED FOR US TO FUNCTION WITHIN THIS CREATION
- [x] `420` HOWEVER, WE MUST BALANCE THESE TWO ASPECTS OF THE BRAIN SO THAT WE DON'T BECOME LEFT OR RIGHT-BRAIN DOMINANT.
- [x] `421` THE LEFT BRAIN MAINTAINS A SENSE OF DETACHMENT FROM THE DIRECT EXPERIENCE TO EXERT CONTROL OVER IT, WHILE THE RIGHT BRAIN STAYS IN THE PRESENT MOMENT AND WHOLEHEARTEDLY EXPERIENCES IT.
- [x] `422` THE RIGHT BRAIN RELIES ON THE LEFT BRAIN BECAUSE ITS HOLISTIC PERCEPTION WHILE CAPTURING THE ESSENCE OF THE WHOLE MAY LACK PRECISION AND CLARITY.
- [x] `423` THE LEFT BRAIN REQUIRES THE RIGHT BRAIN BECAUSE ALTHOUGH IT PRODUCES MENTAL CLARITY, IT CAN LOSE SITE OF THE CONNECTION BETWEEN ALL THINGS AND TRAP THE INDIVIDUAL IN A FRAGMENTED WORLDVIEW.
- [x] `424` JOHN 21:6 "Cast the net on the right-hand side of the boat
- [x] `425` and you will find fish." MOVE INTO THE RIGHT HEMISPHERE OF THE BRAIN AND YOU WILL FIND GOD/ UNIFICATION/ HIGHERSLEF.
- [x] `426` MARK 16:19 "So then after the Lord had spoken unto them, he was received up into heaven, and sat on the right hand of God" RIGHT HAND OF GOD IS THE RIGHT HEMISPERE.
- [x] `427` HEAD IS HEAVEN, SAME ROOT WORD=HEA REPTILLIAN=INSTINCTUAL LIMBICK=EMOTIONAL NEOCORTEX=CRITICAL THINKING NEO FROM THE MATRIX WOKE UP AND STARTED TO USE HIS HIGHER, CRITIAL THINKING MIND WHICH IS THE NEO CORTEX ELEMENTS THE BASE OF ALL PHYSICAL MATTER IS THE EATHER, ALSO KNOWN AS SPIRIT OR AETHER.
- [x] `428` IT IS A SUBSTANCE THAT IS EVERYWHERE BUT NOWHERE AT THE SAME TIME.
- [x] `429` IT HAS ONE FOOT IN THE PHYSICAL WORLD AND IN THE ASTRAL PLANE, IT'S ON EITHER SIDE.
- [x] `430` THE WORD ETHER IS EITHER.
- [x] `431` THE ETHER IS INFINITE POTENTIAL THAT CONSTANTLY MANIFESTS AND UNMANIFESTS ITSELF CYCLICALLY.
- [x] `432` THE AETHER IS THE HIDDEN ENERGY THAT VIBRATES TO CREATE THE "PHYSICAL WORLD WE SEE AND KNOW.
- [x] `433` WE ARE LIKE FISHES IN AN OCEAN, SURROUNDED BY AN ENERGETIC FLUID SUBSTANCE THAT WE CAN SEE OR TOUCH.
- [x] `434` ALL THINGS ARE FEEDING OFF THE ENERGY OF THE INFINITE ETHER.
- [x] `435` THE 4 ELEMENTS ARE THE 4 VIBRATIONAL STATES OF THE ETHER. -NONE OF THE ELEMENTS ARE PURE
- [x] `436` THEY ARE COMPOSED OF EACH OTHER BY TRANSMUTATION. -ALL OF THE ELEMENTS ARE BORN FROM THE 1ST ELEMENT ETHER (SPIRIT). -THE 4 PHYSICAL ELEMENTS ARE THE 4 VIBRATIONAL STATES OF THE ETHER.
- [x] `437` EARTH HAS THE SLOWEST VIBRATION, AND FIRE IS THE QUICKEST. -EACH ELEMENT SHARES ONE CHARACTERISTIC WITH THE ONE NEXT TO IT.
- [x] `438` PLATOS ASPECT FIRE=SHARPNESS,THINNESS,MOVEMENT EARTH=DULLNESS,THICKNESS,REST AIR=THINNESS,MOVEMENT,DULLNESS WATER=DULLNESS,THICKNESS,MOVEMENT FEMALE MALE WATER FIRE EARTH AIR PASSIVE ACTIVE SPIRIT THE ELEMENTS ARE ALWAYS IN THIS ORDER BECAUSE IT STARTS WITH THE DENSEST (EARTH), THEN ON TOP OF THE FIRE=LIGHT EARTH LIES WATER, THEN ON TOP OF WATER IS THE AIR, AND ON TOP OF THE AIR IS FIRE (HEAT RISES), THEN ON TOP AIR=BREATH OF FIRE IS SPIRIT/ETHER.
- [x] `439` WATER=LIQUID EARTH=BOTTOM OF JAW FLAT HEARTH ELECTROMAGNETIC FIELDS ARE RESPONSIBLE FOR ALL OF THE CREATION.
- [x] `440` THE NEUTRAL, ZERO PLANE OF EVERY ELECTROMAGNETIC FIELD IS THE BIRTH OF PHYSICAL MATTER.
- [x] `441` MATTER IS A RESULT OF TWO OPPOSING FORCES EQUALIZED ON THE PLANE OF INERTIA (NEUTRAL POINT OF THE FIELD).
- [x] `442` THE EARTH IS THE PLANE OF INERTIA OF ITS GIANT ELECTROMAGNETIC TORODIAL FIELD.
- [x] `443` THE PLANE OF INIRTIA IS WHERE WE GET THE PHRASE "PLANET EARTH" FROM.
- [x] `444` THE AT THE CENTRE OF EVERY ELECTROMAGNETIC FIELD IS MAGNETIC WHITE LIGHT.
- [x] `445` THIS IS THE MOST MAGNETIC POINT WITHIN THE FIELD.
- [x] `446` AT THE CENTRE OF THE EARTH IS THE CENTRE OF THE EARTH'S MAGNETIC FIELD.
- [x] `447` THIS IS WHERE ALL OF THE ENERGY IS BEING DRAWN BACK TO AND SPAT BACK OUT.
- [x] `448` THIS MIDDLE POINT OF A TORUS FIELD IS CALLED A HYPERBOLOID.
- [x] `449` THE SUN, MOON, STARS, AND PLANETS ARE STIRED BY THE ROTATING, RECIPROATING HYPERBOLOID AT THE CENTRE OF EARTH'S MAGNETIC FIELD (THE NORTH POLE).
- [x] `450` THIS IS WHAT MAKING THIS MOTION OF THE DAILY CYCLE.
- [x] `451` HYPERBOLOID MACROCOSM-CENTRE OF EARTH ENERGY OUT MICROCOSM-CENTRE OF BODY (HEART) =NORTHPOLE =EARTH =MOON =SUN ENERGY BACK IN HYPERBOLOIDS ARE AN INVERSE OF A SPHEAR.
- [x] `452` SUN=ELECTRIC AND POSITIVLY CHARGED.
- [x] `453` THE MAGNETIC NORTH POLE IS THE CENTRE OF THIS FIELD.
- [~] `454` MASCULINE THE MOST MAGICAL POINT IN THE FIELD.
- [x] `455` THIS IS WHERE THE ETHER IS GETTING STIRED AND CREATING THE 4 ELEMENTS FROM OUT OF COUNTER- MOON=MAGNETIC IS MAGNETIC IT SPACE.
- [x] `456` IS NEGATIVELY CHARGED MAKING THE START IS THE STARS AS THEY ARE YOU GO TO SLEEP.
- [x] `457` THE START OF THE SOUL SYSTEM FEMANINE TROPIC OF CAPRICORN STAR=START STAIR=STARS EQUATOR THE STAIRWAY TO HEAVEN IS THE STARWAY TO HEAVEN.
- [x] `458` TROPIC OF CANCER EARTH=HEART BECAUSE ITS THE HEART (MIDDLE) OF THE SOUL THE SUN CREATES THE 4 SEASONS BY SPINNING INWARD TO THE TROPIC SYSTEM OF CANCER, WHICH IS SUMMER FOR THE NORTHERN LANDS.
- [x] `459` AFTER THIS, IT WILL THEN START TO SPIRAL OUTWARDS TOWARDS THE TROPIC OF THE 7 LAYERS OF HEAVEN ARE THE 7 CAPRICORN, WHICH WILL THEN BE FURTHER AWAY FROM THE NORTHERN PLNETARY COSMIC ENERGIES KNOWN AS THE 7 ELOHIM.
- [~] `460` WHICH ARE THE 7 LANDS, CREATING THE SEASON OF WINTER.
- [x] `461` LAYERS OF THE SELF THERE ARE LAYERS TO THE FIRMAMENT, AND EACH OF THE PLANETS IS ON THE LAYER.
- [x] `462` THIS EXPLAINS WHY THEY ALL HAVE DIFFERENT SPEEDS OF MOTION AND ALSO EXPLAINS WHY THE ANCIENTS CALLED THE PLANETS THE "7 WONDERERING STARS" AS THEY ARE NOT FIXED TO THE LIKE THE STARS.
- [x] `463` SET HORUS HERE YOU SEE HORUS AND SET PLACING THERE FEET INSIDE OF THE DOME.
- [x] `464` THE POLE THEY HAVE ROPE ATTACHED TO IS THE MAGNETIC NORTH POLE, WHICH THEY ARE BOTH PULLING, WHICH SYMOLIZES THE SPINNNING OF THE NORTH POLE.
- [x] `465` HORUS SYMBOLISES THE SUN, AND SET SYMBOLISES THE MOON, AND THEY ARE BEING SPUN BY THE CENTRE POLE.
- [x] `466` HEARTH EARTH IS AN ANAGRAM FOR HEART MOVE THE H TO THE BEGINNING AND EARTH BECOMES HEART.
- [x] `467` THE HEART IS THE MIDDLE OF THE EARTH=HEART BODY.
- [x] `468` HEART MEANS MIDDLE.
- [x] `469` THE EARTH IS THE HEART OF THE SOUL SYSTEM.
- [x] `470` IT IS THE BALANCED REALM BETWEEN GOOD AND EVIL.
- [x] `471` THIS IS WHY WE HAVE DUALISM HERE (GOOD AND EVIL).
- [x] `472` FREEMASONS STAND ON THE BLACK AND WHITE CHECKERD BOARD, SYMBOLIZING DUALITY (GOOD AND EVIL).
- [x] `473` IT ALSO SYMBOLIZES SPIRIT (LIGHT) AND MATTER (BLACK) (YIN AND YANG).
- [x] `474` THEY ARE STANDING IN THE REALM OF GOOD AND EVIL, HOT AND COLD, DAY AND NIGHT, ETC...
- [x] `475` EARTH SPIRIT=WHITE MATTER=BLACK HENCE THE CUBE OF SATURN IS ALWAYS BLACK, SYMBOLIZING THE PHYSICAL 3D WORLD OF MATTER.
- [x] `476` ALL THINGS IN THIS WORLD ARE CUBES AND HAVE 6 SIDES.
- [~] `477` GO TO THE SATURN PAGES BELOW TO LEARN MORE.
- [x] `478` EVERYTHING IS MADE OUT OF ELECTROMAGNETIC TORUS FIELDS.
- [x] `479` ITS AN ELECTROMAGNETIC WORLD.
- [x] `480` THE EARTH IS THE HEART, MEANING THE MIDDLE.
- [x] `481` THE MIDDLE OF THE ELECTROMAGNETIC COLOUR SPECTRUM IS GREEN.
- [x] `482` THE EARTH IS GREEN, AND THEN ABOVE THE GREEN EARTH IS THE BLUE SKY.
- [x] `483` BLUE COMES AFTER GREEN ON THE LIGHT SPECTRUM.
- [x] `484` THE WORLD WE SEE AROUND US IS ACTUALLY WITHIN US.
- [x] `485` WHEN WE ASTRAL PROJECT OURSELF OUTSIDE OF THE PHYSICAL BODY, WE ARE INDEED LEAVING THE PHYSICAL PLANE WE CALL EARTH AND ENTERING THE ASTRAL PLANE.
- [x] `486` HEAVEN IS ABOVE EARTH, THROUGH THE BLUE SKY.
- [x] `487` THIS CORRESPONDS WITH THE 7 MAJOR CHAKARAS WITHIN US.
- [x] `488` IN ORDER TO GO TO HEAVEN THROUGH THE BLUE SKY, WE GO THROUGH THE BLUE CHAKARA TO OUR HEAD.
- [x] `489` HEAD AND HEAVEN ARE THE SAEM ROOT WORDS.
- [x] `490` YOUR HEAD IS HEAVEN BECAUSE IT IS THE PLACE OF THYNE CONSCIOUSNESS/TRUE FORM.
- [x] `491` HIGH FREQUENCY HIGH FREQUENCY LOW RANGE LOW RANGE + + -SKY IS BLUE -BLUE COMES AFTER GREEN -EARTH=HEART=CENTRE. -EARTH/NATURE IS GREEN WHICH IS THE HEART OF THE COLOUR SPECTRUM -EARTH IS THE BALANCE POINT THATS WHY ITS DUALISTIC (GOOD & BAD) LOW FREQUENCY HIGH RANGE LOW FREQUENCY HIGH RANGE SOLAR SYSTEM IS - - -ITS A SOUL SYSTEM NOT A SOLAR SYSTEM.
- [x] `492` SOUL SYSTEM -EARTH IS THE HEART OF THE SOUL SYSTEM AS IT IS IN THE MIDDLE OF THE SYSTEM.
- [~] `493` A Persian miniature depicting Seven Heavens THE 7 PLANETS COME FROM THE 7 COLOURS OF THE ELECTROMAGNETIC COLOUR SPECTRUM. from The History of EACH PLANET GIVE OFF CERTAIN FREQUENCY OF Mohammed, Bibliothèque LIGHT WHICH INFLUENCE THE MIND UNTIL WE nationale de France, Paris.
- [x] `494` OUTGROW MATTER AND TURN TO SPIRIT (GROW TO EACH PLANET HAS ITS LAYER THE HIGHEST STATE OF CONSCIOUSNESS).
- [x] `495` OF THE SOUL SYSTEM, WHICH COULD BE A WHOLE OTHER SATURN=SATAN REALITY.
- [~] `496` THE LORD OF EARTH THE RINGS THE WORD PLANET HAS A PLAN WITHIN IT, AND PLAN QUARAN 65:12 MEANS PLANE.
- [x] `497` ITS A FLAT PLANE JUST LIKE THE EARTH.
- [x] `498` EACH PLANET HAS THEIR LAYER OF THE FIRMAMENT WHICH EXPLAINS THE VARIOUS SPEEDS OF THE CELESTIAL BODYS DOING THEIR CYCLE.
- [x] `499` FREEMASONIC COSMOLOGY GENESIS 1:3 GENESIS 1:16 "LET THERE BE LIGHT" ""And God made two great lights
- [x] `500` the greater light to rule the day and the GENESIS 1:6 EVERYTHING IS MADE OUT OF LIGHT
- [x] `501` THE lesser light to rule the night" "Let there be a firmament in the midst of UNIVERSE IS CREATED OUT OF LIGHT IN OTHER WORDS GOD CREATED THE SUN the waters
- [~] `502` and let it divide the waters WAVES.
- [x] `503` THE TORUS FIELD IS ONE UNIT OF AND THE MOON.
- [x] `504` THE MOON EMITS ITS OWN from the waters." LIGHT.
- [x] `505` THE LIGHT PROJECTING THIS LIGHT SOURCE, IT IS NOT REFLECTING THE REALITY IS POLIRIS, SYMBOLISED AS THE SUNS LIGHT.
- [~] `506` THE FIRMAMENT IS SYMBOLIZED BY THE YOU HAVE TO BALANCE ALL FAMOUS LL SEEING EYE WITH LIGHT BEING THE SUN IS ELECTRIC/MALE.
- [x] `507` THE MOON IS MASONIC ROYAL ARCH.
- [x] `508` ASPECTS OF LIFE, BALANCE THE PROJECTED AROUND IT.
- [x] `509` MAGNETIC/FEMALE.
- [x] `510` THE FIRMAMENT IS ALSO CALLED HEAVEN.
- [x] `511` TWO HEMISPHERES OF THE HEAVEN HAS THE WORD EVEN WITHIN IT.
- [~] `512` BRIAN, BALANCE THE CHAKRAS isiah 40:22 EVEN=BALANCE.
- [x] `513` THE FIRMAMENT IS THE EVEN POINT BETWEEN THIS WORLD AND THE AND YOU WILL GO TO HEAVEN (HEAD/HIGHER MIND/HIGHER He sits enthroned above the circle of WORLD ABOVE SLEF) the earth
- [~] `514` and its people are like grasshoppers.
- [x] `515` He stretches out the heavens like a canopy
- [x] `516` and spreads 7 STARS them out like a tent to live in. =THESE STARS SYMBOLIZE THE 7 PLANETS, ALSO KNOWN AS THE 7 WONDERERS OR THE 7 LAYERS OF HEAVEN: SATURN, JUPITER, MARS, SUN, VENUS, MURCERY, MOON.
- [x] `517` EACH 'pLANET' HAS ITS OWN LAYER OF THE FIRMAMENT PLANET=PLAN=PLANE 5 POINTED STAR GENESIS 1:14 THIS SYMBOL IS CALLED A PENTICLE.
- [x] `518` IT IS A "God made the firmament, and divided 5-POINTED STAR THAT SYMBOLIZES THE 5 the waters which were under the ELEMENTS WITHIN THIS CREATION.
- [x] `519` SPIRIT ON firmament from the waters which were THE TOP POINT BECAUSE ITS THE MOST above the firmament: and it was so" IMPORTANT ELEMENT.
- [x] `520` SPIRIT IS ALSO ETHER.
- [x] `521` THE ETHER IS THE BASE OF ALL PHYSICAL THE BOAT ON WATER SYMBOLIZES THE MATTER.
- [x] `522` ETHER IS THE SUBSTANCE THAT ETHERIAL WORLDS BEYOND THIS WORLD.
- [x] `523` IF CONNECTS THE PHYSICAL WORLD TO THE YOU LOOK AT STARS WITH A TELESCOPE SPIRITUAL WORLD (ASTRAL).
- [x] `524` YOU CAN SEE THEM TWINKLE AS IF ITS LIGHT IT ALSO SYMBOLIZES THE 5 SENSES, WHICH SHINING THROUGH WATER.
- [x] `525` THE STARS ARE ARE THE E 5 WAYS THE BODY REPORTS LIGHT SHINING THROUGH THE ETHER ABOVE.
- [x] `526` ELECTRICAL IMPULSES BACK TO THE PINEAL GLAND TO DECODE THE EXTERNAL WORLD.
- [x] `527` STAIRS CHECKERED BORED 6 STAIRS, THE 7TH IS THE EARTH THE BLACK AND WHITE CHECKERD GROUND.
- [x] `528` ALL TOGETHER THOSE 7 STEPS.
- [x] `529` SYMBOLIZES ALL DUALITIES WITHIN THIS THERE ARE 7 STEPS WE HAVE TO STEP UP DUALISTIC REALITY: SPIRIT (LIGHT) AND TO REACH OUR HIGHER SELF, WHICH IS MATTER, REST AND MOTION, POSITIVE AND THE 7 CHAKRAS.
- [~] `530` EACH CHAKARA IS ONE NEGATIVE ETC...
- [x] `531` OF THE 7 "PLANETS".
- [x] `532` EARTH IS AN ANAGRAM FOR THE HEART.
- [x] `533` HEART IS THE MIDDLE OF THINGS SUCH AS the lighter something is the higher it rises. it's the same with the journey of the soul. the more materialistic the soul gets, the lower THE BODY FOR EXAMPLE.
- [x] `534` THE HEART IS THE BALANCE POINT BETWEEN TWO OPPOSING the world it falls due to heavy attachments to the mind.
- [~] `535` Greed, Quran 15:19 POLES.
- [x] `536` EARTH IS THE WORLD BETWEEN envy, lust, and the other seven deadly sins are internal states that "And the earth We have spread HEAVEN AND HELL.
- [x] `537` HEAVEN BEING THE make your soul more heavy and bound to the earth and body.
- [~] `538` You out (like a carpet)
- [x] `539` set thereon HIGHER WORLDS BEYOND THIS, HELL BEING must quell all the chaos of the emotions and detach from the mountains firm and immovable
- [x] `540` THE WORLDS BELOW. external world to become lighter and at peace with all. then and and produced therein all kinds only then shall the soul pass upward to the light. of things in due balance." the word reality is similar to realize. your level of realization is your level of reality.
- [x] `541` You can only experience one reality at a time.
- [~] `542` Quran 71:19 chronicles 16:30 "And Allah has made the earth for you as a carpet (spread out)." "Tremble before him, all the earth!
- [~] `543` The world GENESIS 1:14 is firmly established
- [x] `544` it cannot be moved" "And God said, Let there be lights in the firmament of the heaven to divide the day from the night
- [~] `545` and let them be Talaaq 65:12 for signs
- [~] `546` and years" Pslams 104:5 "It is Allah Who has created seven heavens and of the earth the like "He set the earth on its foundations
- [x] `547` it can THE PHRASE 'LET THEM BE FOR SIGNS' IS TALKING ABOUT THE thereof" never be moved".
- [x] `548` THE STARS ARE SIGNS FOR WHAT IS TO COME.
- [x] `549` FIRMAMENT COMES FROM THE LATIN WORD 'FIRUMS' MEANING FIRM.
- [~] `550` Revelation 7:1 THE FIRMIMENT IS A FIRM ARCH/ SKY FAULT.
- [x] `551` "After this I saw four angels standing at the four corners of the earth, holding back the four winds of the earth to prevent any wind from blowing on the land or on the sea or on any tree." notice how his head is peaking through the ethereal barriers of the earth.
- [x] `552` The head is the place of consciousness, and it has the ability to see the other worlds.
- [x] `553` This is why your head is heaven.
- [~] `554` COSMOLOGY @Revivalofwisdom ELEMENT SYBOLS SUN FIRE EARTH AIR MOON EARTH WATER BLACK SUN MASONIC COMPASS SUN MOON AS ABOVE SO BELOW LUNAR SOLAR BLACK SUN ISLAND=EYELAND PLANET=PLAN=PLANE MAYAN UNIVERSE THE ANCIENTS SAID WE LIVE IN GUARD, WHICH IS A BALANCED REALM CONTAINING BOTH GOOD AND EVIL.
- [x] `555` THIS COULD BE WHY EARTH IS AN ANAGRAM FOR THE HEART, AS IT WOULD BE THE SYSTEM'S HEART.
- [x] `556` FOR THOUSANDS OF YEARS, PEOPLE BELIEVED IN HEAVEN AND HELL, WHICH COULD BE THE REALMS ABOVE AND BELOW US.
- [~] `557` ALCHEMICAL SYMBOL FOR EARTH 1500S-1600S NORTH POLE MAP LUCKY HEARTH UNITED NATIONS LOGO FLAT EARTH MAP HITLER USING 2 FLAT EARTH MAPS IMAGE SOURCE
- [x] `558` https://www.un.org/en/ (THIS IMAGE WAS NOT CREATED BY REVIVALOFWISDOM NOR DO I OWN THIS IMAGE) ADOLF HITLER FLAT EARTH MAP COMPASS POLARIS SYMBOL POLARIS IS THE 8-POINTED STAR BECAUSE WE ARE INSIDE THE WORLD OF SPACE AND TIME.
- [x] `559` THERE ARE 8 POINTS OF SPACE AND TIME.
- [x] `560` POLARIS THE THE CENTRE AND HIGHEST STAR.
- [x] `561` WE SYMBOLIZE THIS TODAY WITH THE STAR ON TOP OF THE CHRISTMAS TREE.
- [x] `562` THE COMPASS IS THE 8 POINTED STAR BECAUSE IT POINTS YOU TO THE 8 POINTED STAR (THE CENTRE OF THE EARTH) STARS WITH NO LIGHT POLUTION EGYPTIAN SKY GOD NUT FREEMASONIC ROYAL ARCH MAYAN COSMOS HEBREW COSMOS THE EGYPTIN SKY GOD NUT IS SYMBOLIZING THE STAR CIELING ABOVE OUR HEADS.
- [x] `563` THIS WAS THEN LATER TURNED INTO THE ROYA ARCH IN FREEMASONRY.
- [~] `564` BIBLE=GENISIS 1:6-8 BIBLE JOB 37:18 QUARAN 65:12 THE 7 HEAVENS ARE THE 7 LAYERS OF THE FIRMAMENT

</details>

_Generated by `analyze_course.py`. Coverage percentages are computed from sentence-embedding similarity plus entity/number grounding against the parsed source statements shown above; they are a measurement of this parse, not a universal truth._