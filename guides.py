"""The ten guide pages (SEO landing pages) for vietnamese-learning.com.

One page per keyword cluster, no two pages chasing the same query.
Phrase tables come from the app's own content (guides_phrases.json, made by
export_phrases.py), so the site and the app always teach the same Vietnamese.

Body blocks: ('p', text) · ('h2', text) · ('ul', [items]) · ('table', i)
where i indexes the guide's `tables`: (heading, mode, topic, how many).
`youtube`: video id for the page's pillar video, or None until it exists.
"""

GUIDES = [
    {
        'slug': 'learn-vietnamese-for-kids',
        'keyword': 'learn vietnamese for kids',
        'cluster': ['vietnamese for kids', 'teach my child vietnamese',
                    'heritage vietnamese kids', 'vietnamese app for kids'],
        'title': 'Learn Vietnamese for Kids: Talk to Grandma and Grandpa',
        'desc': 'How to help a child growing up abroad speak Vietnamese with '
                'grandparents: first phrases, daily habits and video-call words.',
        'h1': 'Learn Vietnamese for kids: words to say to bà and ông',
        'mode': 'kids',
        'youtube': None,
        'published': '2026-11-23', 'updated': '2026-11-26',
        'related': ['say-hello-to-grandma-in-vietnamese', 'vietnamese-family-terms', 'heritage-vietnamese-learner', 'tet-greetings'],
        'tables': [('First phrases for grandparents', 'kids', 'greetings', 12),
                   ('Words for a video call', 'kids', 'phone_call', 10),
                   ('Saying I love you', 'kids', 'love_words', 8)],
        'body': [
            ('p', 'Many children of Vietnamese families understand some Vietnamese '
                  'but answer in English. That is normal. Understanding comes first; '
                  'speaking comes when a child has a few short phrases they feel safe '
                  'using, and a person they want to use them with. For most kids that '
                  'person is bà (grandma) or ông (grandpa).'),
            ('h2', 'Start with “Dạ”'),
            ('p', '“Dạ” is the polite way a child answers a grown-up: when grandma '
                  'calls, the answer is “Dạ!”. It is one syllable, it makes '
                  'grandparents smile, and it teaches the idea of politeness to elders '
                  'that runs through the whole language. Add “ạ” at the end of a '
                  'sentence and it becomes polite too: “Con cảm ơn ạ.” The first '
                  'greeting, word by word, is in [how to say hello to grandma in '
                  'Vietnamese](say-hello-to-grandma-in-vietnamese).'),
            ('table', 0),
            ('h2', 'Make the video call the lesson'),
            ('p', 'A weekly call with grandparents is the best practice there is. '
                  'Pick two or three phrases before the call, say them together once, '
                  'then let your child try them on the call. Keep it short and happy; '
                  'a call that ends with a laugh is the one they will want to repeat.'),
            ('table', 1),
            ('h2', 'Habits that work at home'),
            ('ul', ['Use the same Vietnamese words for daily routines: meals, bath, bed.',
                    'Five minutes a day beats an hour on Saturday.',
                    'Praise the try, not the accent. Correct by repeating the phrase '
                    'back the right way, not by saying “wrong”.',
                    'Let your child hear the accent your family speaks. If grandma is '
                    'from Saigon, learn Southern words; if she is from Hà Nội, Northern '
                    '([how to choose](northern-vs-southern-vietnamese)).',
                    'Young children do not need to read. Pictures and sound are enough.']),
            ('table', 2),
        ],
    },
    {
        'slug': 'vietnamese-family-terms',
        'keyword': 'vietnamese family terms',
        'cluster': ['vietnamese kinship terms', 'what to call relatives in vietnamese',
                    'vietnamese aunt uncle words', 'ông bà nội ngoại'],
        'title': 'Vietnamese Family Terms: What to Call Every Relative',
        'desc': 'Bác, chú, cô, cậu, dì, nội and ngoại explained. A simple guide to '
                'Vietnamese kinship words, with audio in the Dạ app.',
        'h1': 'Vietnamese family terms: what to call every relative',
        'mode': 'adult',
        'youtube': None,
        'published': '2026-11-23', 'updated': '2026-11-26',
        'related': ['vietnamese-pronouns', 'vietnamese-phrases-for-in-laws', 'say-hello-to-grandma-in-vietnamese', 'meeting-vietnamese-parents'],
        'tables': [('Core family words', 'kids', 'family', 12),
                   ('Aunts, uncles and cousins', 'adult', 'relatives', 12)],
        'body': [
            ('p', 'English has one word for aunt and one for uncle. Vietnamese has a '
                  'different word depending on whose side of the family the person is '
                  'on and whether they are older or younger than your parent. These '
                  'words are not only names: they are also the pronouns you use when '
                  'you talk to that person, and the word you use for yourself changes '
                  'with them.'),
            ('table', 0),
            ('h2', 'Father’s side and mother’s side'),
            ('ul', ['ông bà nội: your father’s parents. ông bà ngoại: your mother’s parents.',
                    'bác: an older sibling of your parent (in the North, on either side).',
                    'chú: your father’s younger brother. cô: your father’s sister.',
                    'cậu: your mother’s brother. dì: your mother’s sister.']),
            ('p', 'Usage differs by region and by family. In the South, for example, '
                  '“cô” and “dì” are often used for a father’s or mother’s sister '
                  'whatever her age. When in doubt, ask: “Con gọi bác ấy là gì ạ?” '
                  '(What should I call him or her?). Families are happy to explain.'),
            ('table', 1),
            ('h2', 'How you call yourself'),
            ('p', 'Talking to your parents’ generation you are “con” or “cháu”; to an '
                  'older brother or sister you are “em”; to a younger one you are '
                  '“anh” (if you are a man) or “chị” (if you are a woman). Getting this '
                  'right matters more to most Vietnamese families than perfect tones. '
                  'The full system, and why “tôi” sounds cold to a grandparent, is in '
                  '[Vietnamese pronouns](vietnamese-pronouns).'),
        ],
    },
    {
        'slug': 'meeting-vietnamese-parents',
        'keyword': 'meeting vietnamese parents',
        'cluster': ['meeting your vietnamese partner’s parents',
                    'what to say to vietnamese parents',
                    'vietnamese girlfriend parents'],
        'title': 'Meeting Your Vietnamese Partner’s Parents: Phrases',
        'desc': 'What to say when you meet your Vietnamese partner’s family: greetings, '
                'polite answers, gifts and how to address each person.',
        'h1': 'Meeting your Vietnamese partner’s parents',
        'mode': 'adult',
        'youtube': None,
        'published': '2026-11-23', 'updated': '2026-11-26',
        'related': ['vietnamese-phrases-for-in-laws', 'vietnamese-family-terms', 'vietnamese-dinner-phrases', 'vietnamese-wedding-toast'],
        'tables': [('Greetings', 'adult', 'greetings', 10),
                   ('The first visit', 'adult', 'meet_family', 12)],
        'body': [
            ('p', 'You do not need fluent Vietnamese to make a good first impression. '
                  'A handful of polite phrases, said with the right words for each '
                  'person, tells the family that you take them seriously. Most parents '
                  'remember the effort far longer than the mistakes.'),
            ('h2', 'Three words that do most of the work'),
            ('ul', ['“Con”: what you call yourself when talking to your partner’s '
                    'parents, the way their own child would.',
                    '“Dạ”: the polite yes. Use it whenever an elder speaks to you.',
                    '“ạ”: put it at the end of a sentence to an elder to make it polite.']),
            ('table', 0),
            ('h2', 'On the day'),
            ('ul', ['Greet the oldest person first, then the parents, then everyone else.',
                    'Bring a small gift (fruit, tea, something from your country) and '
                    'offer it with both hands.',
                    'Wait to be invited to sit, or ask: “Con xin phép ngồi ạ.”',
                    'At the meal, invite the elders to eat before you start '
                    '(see [Vietnamese dinner phrases](vietnamese-dinner-phrases)).']),
            ('table', 1),
            ('p', 'Ask your partner which accent and which words the family uses for '
                  'parents: “bố mẹ” is more Northern, “ba má” more Southern. For the '
                  'words you will use every week after the first visit, see '
                  '[Vietnamese phrases for in-laws](vietnamese-phrases-for-in-laws).'),
        ],
    },
    {
        'slug': 'vietnamese-tones',
        'keyword': 'vietnamese tones',
        'cluster': ['six vietnamese tones', 'how to pronounce vietnamese tones',
                    'vietnamese tone marks', 'ma má mà mả mã mạ'],
        'title': 'Vietnamese Tones Explained: The Six Tones, Simply',
        'desc': 'The six Vietnamese tones, how the marks work, and why the South uses '
                'five. Practise with minimal pairs like ma, má, mà, mả, mã, mạ.',
        'h1': 'Vietnamese tones, explained simply',
        'mode': 'adult',
        'youtube': None,
        'published': '2026-11-23', 'updated': '2026-11-26',
        'related': ['vietnamese-pronunciation-practice', 'northern-vs-southern-vietnamese', 'learn-vietnamese-app-for-beginners', 'heritage-vietnamese-learner'],
        'tables': [('One syllable, six meanings', 'adult', 'tones', 12)],
        'body': [
            ('p', 'Vietnamese is a tonal language: the pitch of a syllable is part of the '
                  'word. “ma” with a falling tone (mà) means “but”; with a rising tone '
                  '(má) it means “cheek”, or “mom” in the South. The good news is that '
                  'the spelling tells you the tone every time.'),
            ('h2', 'The six tones'),
            ('ul', ['ngang (no mark): ma, level and steady.',
                    'huyền (grave accent, à): mà, low and falling gently.',
                    'sắc (acute accent, á): má, rising.',
                    'hỏi (small hook, ả): mả, dipping down then up.',
                    'ngã (tilde, ã): mã, rising with a break in the voice.',
                    'nặng (dot below, ạ): mạ, short, low and heavy.']),
            ('table', 0),
            ('h2', 'North and South'),
            ('p', 'Hà Nội speech keeps all six tones apart. In Saigon and most of the '
                  'South, hỏi and ngã sound almost the same, so you hear five. They are '
                  'still written differently. Learn the accent your family or friends '
                  'speak; both are correct.'),
            ('h2', 'How to practise'),
            ('ul', ['Listen to a pair, say it, record yourself, compare.',
                    'Practise whole phrases, not only single syllables: tones change '
                    'slightly in real speech.',
                    'Ten minutes a day for a few weeks matters more than long sessions.']),
            ('p', 'A step-by-step routine, with the pairs that trip learners up most, is in '
                  '[Vietnamese pronunciation practice](vietnamese-pronunciation-practice).'),
        ],
    },
    {
        'slug': 'northern-vs-southern-vietnamese',
        'keyword': 'northern vs southern vietnamese',
        'cluster': ['hanoi vs saigon accent', 'vietnamese dialects',
                    'which vietnamese accent to learn', 'bố or ba'],
        'title': 'Northern vs Southern Vietnamese: Which to Learn?',
        'desc': 'The main differences between the Hà Nội and Saigon accents, the words '
                'that change, and how to choose the one your family speaks.',
        'h1': 'Northern vs Southern Vietnamese: which accent should you learn?',
        'mode': 'adult',
        'youtube': None,
        'published': '2026-11-23', 'updated': '2026-11-26',
        'related': ['vietnamese-tones', 'vietnamese-pronunciation-practice', 'heritage-vietnamese-learner', 'vietnamese-phrases-for-in-laws'],
        'tables': [('Words that change between regions', 'adult', 'dialects', 12)],
        'body': [
            ('p', 'Vietnamese speakers from Hà Nội and from Saigon understand each other '
                  'without trouble, but the accents sound different and some everyday '
                  'words change. If you are learning to talk to a family, the right '
                  'accent is simply the one they speak.'),
            ('h2', 'What changes'),
            ('ul', ['Tones: the North keeps six distinct tones; the South merges hỏi and ngã.',
                    'Sounds: the North says “d”, “gi” and “r” like a “z”; the South says '
                    '“d” and “gi” closer to an English “y”.',
                    'Words: bố/ba (dad), không/hông (no), quả/trái (fruit), lợn/heo (pig).',
                    'Politeness: “vâng” is a Northern yes; “dạ” is used everywhere, and '
                    'is the usual polite yes in the South.']),
            ('table', 0),
            ('h2', 'How to choose'),
            ('ul', ['Family from the North, or living in Hà Nội: learn Northern.',
                    'Family from the South, or in Saigon, or in most overseas communities '
                    'in the US: Southern is a common choice.',
                    'Not sure? Ask: “Nhà mình nói giọng miền nào ạ?”',
                    'You can switch later. The grammar and spelling are the same.']),
            ('p', 'The tone difference is explained with examples in '
                  '[Vietnamese tones](vietnamese-tones).'),
        ],
    },
    {
        'slug': 'tet-greetings',
        'keyword': 'vietnamese new year greetings',
        'cluster': ['tet greetings', 'chúc mừng năm mới meaning',
                    'lunar new year vietnamese phrases', 'lì xì'],
        'title': 'Vietnamese New Year Greetings: What to Say at Tết',
        'desc': 'Chúc mừng năm mới and the Tết wishes families love to hear, for '
                'parents, grandparents and relatives, plus lucky money etiquette.',
        'h1': 'Vietnamese New Year greetings: what to say at Tết',
        'mode': 'adult',
        'youtube': None,
        'published': '2026-11-23', 'updated': '2026-11-26',
        'related': ['say-hello-to-grandma-in-vietnamese', 'vietnamese-phrases-for-in-laws', 'vietnamese-dinner-phrases', 'learn-vietnamese-for-kids'],
        'tables': [('Tết wishes', 'adult', 'tet', 12)],
        'body': [
            ('p', 'Tết, the Lunar New Year, is the biggest family event of the Vietnamese '
                  'year. Visiting relatives and wishing them a good year is the heart of '
                  'it, and a few well-chosen wishes in Vietnamese go a long way.'),
            ('h2', 'The basics'),
            ('ul', ['“Chúc mừng năm mới!”: Happy New Year. Works with anyone.',
                    'For elders, wish health and long life: “Con chúc ông bà sống lâu '
                    'trăm tuổi ạ.”',
                    'For adults, wish health, peace and success: “An khang thịnh vượng!”',
                    'Start your wish with “Con chúc…” (to parents and grandparents) or '
                    '“Cháu chúc…” (to aunts and uncles). See [Vietnamese family '
                    'terms](vietnamese-family-terms) for who is who.']),
            ('table', 0),
            ('h2', 'Lucky money'),
            ('p', 'Children and unmarried young people receive lucky money in red '
                  'envelopes: “lì xì” in the South, “mừng tuổi” in the North. Receive it '
                  'with both hands and say thank you. Once you are married or working, '
                  'you may be the one giving.'),
            ('h2', 'Good to know'),
            ('ul', ['The first visitor of the year is thought to bring the household’s '
                    'luck, so families often choose who comes first.',
                    'Avoid arguing, sweeping and talking about bad luck on the first days.',
                    'Families often visit the father’s side first, then the mother’s.']),
        ],
    },
    {
        'slug': 'vietnamese-dinner-phrases',
        'keyword': 'vietnamese phrases for dinner',
        'cluster': ['vietnamese table manners', 'mời cơm', 'family meal vietnamese',
                    'how to say delicious in vietnamese', 'ăn cơm chưa meaning'],
        'title': 'Vietnamese Dinner Phrases and Family Table Manners',
        'desc': 'How to invite elders to eat, say “delicious”, ask for more rice and '
                'offer to wash up at a Vietnamese family meal.',
        'h1': 'Vietnamese phrases for a family dinner',
        'mode': 'adult',
        'youtube': None,
        'published': '2026-11-23', 'updated': '2026-11-26',
        'related': ['vietnamese-phrases-for-in-laws', 'meeting-vietnamese-parents', 'tet-greetings', 'learn-vietnamese-for-family'],
        'tables': [('At the table', 'adult', 'family_meal', 12)],
        'body': [
            ('p', 'Family meals are where you will use your Vietnamese most. Dishes are '
                  'shared in the middle, everyone has a bowl of rice, and there is a small '
                  'ritual before anyone starts.'),
            ('h2', 'Invite the elders first'),
            ('p', 'Before eating, younger people invite the older ones: “Con mời bố mẹ '
                  'ăn cơm.” If the table is big, “Con mời cả nhà ăn cơm ạ” covers '
                  'everyone. Then wait for the oldest person to start.'),
            ('h2', '“Ăn cơm chưa?”'),
            ('p', 'Literally “Have you eaten rice yet?”, this is less a question about food '
                  'than a way of saying “I care about you”. Grandparents and parents ask it '
                  'on the phone, at the door and in the family group chat. Answer politely: '
                  '“Dạ, con ăn rồi ạ” (Yes, I have eaten) or “Dạ, con chưa ạ” (Not yet). If '
                  'you say not yet, expect to be fed. You can ask it back too: “Bà ăn cơm '
                  'chưa ạ?”'),
            ('table', 0),
            ('h2', 'Manners that matter'),
            ('ul', ['Take food from the shared dishes a little at a time.',
                    'Do not stand your chopsticks upright in the rice: it is linked to '
                    'offerings for the dead.',
                    'Praise the cook: “Mẹ nấu ăn ngon quá!” is never wrong.',
                    'Expect to be offered more food. Saying “Con ăn no rồi ạ” politely '
                    'tells them you are full.',
                    'Offer to help clear up: “Để con rửa bát cho ạ.”']),
        ],
    },
    {
        'slug': 'vietnamese-wedding-toast',
        'keyword': 'vietnamese wedding toast',
        'cluster': ['vietnamese wedding speech', 'cheers in vietnamese',
                    'một hai ba dô', 'vietnamese wedding phrases'],
        'title': 'Vietnamese Wedding Toast: A Short Speech You Can Give',
        'desc': 'A short, polite Vietnamese wedding speech line by line, from greeting '
                'both families to raising a glass with “Một, hai, ba, dô!”.',
        'h1': 'A Vietnamese wedding toast you can actually give',
        'mode': 'adult',
        'youtube': None,
        'published': '2026-11-23', 'updated': '2026-11-26',
        'related': ['meeting-vietnamese-parents', 'vietnamese-phrases-for-in-laws', 'i-love-you-in-vietnamese', 'tet-greetings'],
        'tables': [('Your toast, line by line', 'adult', 'toast_speech', 12)],
        'body': [
            ('p', 'If you are marrying into a Vietnamese family, you may be asked to say '
                  'a few words at the wedding or at the engagement ceremony. A short '
                  'speech in Vietnamese, even read from a card, is one of the most '
                  'remembered moments of the day.'),
            ('h2', 'The shape of a good toast'),
            ('ul', ['Ask permission to speak.',
                    'Greet both families respectfully: “Kính thưa hai bên gia đình.”',
                    'Thank the parents for welcoming you.',
                    'Apologise, lightly, for your Vietnamese. Everyone will love it.',
                    'Wish health to the elders and happiness to everyone.',
                    'Raise your glass.']),
            ('table', 0),
            ('h2', 'Tips'),
            ('p', 'Keep it under a minute. Practise the greeting and the final cheer the '
                  'most; that is what people hear clearly in a noisy room. “Một, hai, ba, '
                  'dô!” (One, two, three, cheers!) is the cue for everyone to drink.'),
        ],
    },
    {
        'slug': 'i-love-you-in-vietnamese',
        'keyword': 'i love you in vietnamese',
        'cluster': ['anh yêu em', 'em yêu anh', 'yêu vs thương',
                    'romantic vietnamese phrases'],
        'title': 'How to Say I Love You in Vietnamese (Yêu and Thương)',
        'desc': 'Anh yêu em, em yêu anh, con thương mẹ: how to say I love you in '
                'Vietnamese to a partner, parents and grandparents.',
        'h1': 'How to say “I love you” in Vietnamese',
        'mode': 'adult',
        'youtube': None,
        'published': '2026-11-23', 'updated': '2026-11-26',
        'related': ['vietnamese-pronouns', 'vietnamese-wedding-toast', 'vietnamese-phrases-for-in-laws', 'learn-vietnamese-for-kids'],
        'tables': [('To your family', 'adult', 'loving_words', 10),
                   ('Talking about your partner', 'adult', 'partner', 10),
                   ('From a child', 'kids', 'love_words', 8)],
        'body': [
            ('p', 'There is no single “I love you” in Vietnamese, because there is no '
                  'neutral “I” and “you” ([why](vietnamese-pronouns)). The words change '
                  'with who is speaking to whom.'),
            ('h2', 'To a partner'),
            ('ul', ['“Anh yêu em”: said by the man, or the older partner, to the other.',
                    '“Em yêu anh”: said back by the woman, or the younger partner.',
                    'Two women or two men use the same anh/chị/em logic by age.']),
            ('h2', 'Yêu or thương?'),
            ('p', '“Yêu” is romantic love. “Thương” is a warm, caring love that you also '
                  'feel for family; many couples, especially in the South, use it for each '
                  'other too. To parents and grandparents, “thương” sounds natural: '
                  '“Con thương bố mẹ nhiều lắm.”'),
            ('table', 0),
            ('table', 1),
            ('table', 2),
        ],
    },
    {
        'slug': 'vietnamese-phrases-for-travel',
        'keyword': 'vietnamese phrases for travel',
        'cluster': ['basic vietnamese phrases for tourists', 'how to order pho in vietnamese',
                    'vietnamese street food phrases', 'grab bike vietnamese'],
        'title': 'Vietnamese Phrases for Travel: Food, Rides and Prices',
        'desc': 'Order phở and bánh mì, take a ride-app motorbike and ask prices in '
                'Vietnamese. Real phrases with Northern and Southern audio in Dạ.',
        'h1': 'Vietnamese phrases for travel: eat, ride, pay',
        'mode': 'everyday',
        'youtube': None,
        'published': '2026-11-23', 'updated': '2026-11-26',
        'related': ['learn-vietnamese-app-for-beginners', 'vietnamese-tones', 'northern-vs-southern-vietnamese', 'vietnamese-pronunciation-practice'],
        'tables': [('Ordering phở', 'everyday', 'pho_shop', 10),
                   ('Street food', 'everyday', 'street_food', 10),
                   ('Taking a ride-app motorbike', 'everyday', 'ride_app', 10)],
        'body': [
            ('p', 'A few phrases make Vietnam far easier and friendlier: food stalls, '
                  'motorbike rides and markets are where you will use them every day.'),
            ('h2', 'Polite and simple'),
            ('ul', ['“Cho tôi…” (Give me…) is how you order almost anything.',
                    '“Bao nhiêu tiền?” asks the price.',
                    '“Cảm ơn” is thank you; “anh” or “chị” in front of a sentence makes it '
                    'warmer when speaking to someone a bit older.',
                    'Bowl is “bát” in the North and “tô” in the South. More regional '
                    'words are in [Northern vs Southern Vietnamese]'
                    '(northern-vs-southern-vietnamese).']),
            ('table', 0),
            ('table', 1),
            ('table', 2),
        ],
    },
    {
        'slug': 'learn-vietnamese-for-family',
        'keyword': 'learn vietnamese for family',
        'cluster': ['learn vietnamese to talk to family', 'speak vietnamese with family',
                    'learn vietnamese for my partner’s family',
                    'vietnamese for family members'],
        'title': 'Learn Vietnamese for Family: A Starter Guide',
        'desc': 'Learning Vietnamese to talk to grandparents, a partner’s parents or your '
                'own family? What to learn first, and a simple four-week plan.',
        'h1': 'Learn Vietnamese for family: where to start',
        'mode': 'adult',
        'youtube': None,
        'published': '2026-11-26', 'updated': '2026-11-26',
        'related': ['say-hello-to-grandma-in-vietnamese', 'vietnamese-family-terms',
                    'vietnamese-pronouns', 'vietnamese-phrases-for-in-laws'],
        'tables': [('Words for the family group chat', 'adult', 'family_chat', 10)],
        'body': [
            ('p', 'Most people learning Vietnamese outside Vietnam are not learning it for '
                  'an exam. They want to talk to someone: a grandmother on a video call, a '
                  'partner’s parents at Tết, aunts and uncles at a wedding. That changes '
                  'what you should learn first.'),
            ('h2', 'Family Vietnamese is its own thing'),
            ('ul', ['Kinship words come first. Vietnamese has a different word for each '
                    'relative, and that word is also how you say “you”. See [Vietnamese '
                    'family terms](vietnamese-family-terms).',
                    'There is no neutral “I”. With family you call yourself con, cháu or '
                    'em, never “tôi”. See [Vietnamese pronouns](vietnamese-pronouns).',
                    'Politeness to elders is built into the words: “dạ” to answer, “ạ” at '
                    'the end of a sentence.',
                    'The accent matters. Learn the one your family speaks: [Northern vs '
                    'Southern Vietnamese](northern-vs-southern-vietnamese).']),
            ('h2', 'A four-week plan'),
            ('ol', ['Week 1: greetings for the people you will actually see. Start with '
                    '[how to say hello to grandma](say-hello-to-grandma-in-vietnamese).',
                    'Week 2: the six tones, ten minutes a day. [Vietnamese tones explained]'
                    '(vietnamese-tones).',
                    'Week 3: the family table. [Phrases for a family dinner]'
                    '(vietnamese-dinner-phrases), including “Ăn cơm chưa?”.',
                    'Week 4: one real conversation. Pick three phrases, use them on a call, '
                    'and ask the family to correct you.']),
            ('p', 'Married or partnered into a Vietnamese family? Start with [meeting your '
                  'partner’s parents](meeting-vietnamese-parents) and [phrases for in-laws]'
                  '(vietnamese-phrases-for-in-laws). Grew up hearing Vietnamese but never '
                  'speaking it? Read [the heritage learner guide](heritage-vietnamese-learner). '
                  'Teaching a child? See [Vietnamese for kids](learn-vietnamese-for-kids).'),
            ('table', 0),
            ('h2', 'What helps most'),
            ('ul', ['Short daily practice. Fifteen minutes every day beats two hours on Sunday.',
                    'Speak out loud from day one, and record yourself.',
                    'Use the family. Ask “Con nói đúng không ạ?” (Did I say that right?). '
                    'Most relatives are delighted to help.',
                    'Learn whole phrases, not lists of words. A phrase you can say today is '
                    'worth more than fifty words you can only recognise.']),
        ],
    },
    {
        'slug': 'say-hello-to-grandma-in-vietnamese',
        'keyword': 'how to say hello to grandma in vietnamese',
        'cluster': ['hello grandma in vietnamese', 'con chào bà ạ',
                    'what to call grandma in vietnamese', 'bà nội bà ngoại'],
        'title': 'How to Say Hello to Grandma in Vietnamese',
        'desc': '“Con chào bà ạ” word by word: the polite way to greet a Vietnamese '
                'grandmother, bà nội vs bà ngoại, and what to say on a video call.',
        'h1': 'How to say hello to your Vietnamese grandma',
        'mode': 'kids',
        'youtube': None,
        'published': '2026-11-26', 'updated': '2026-11-26',
        'related': ['learn-vietnamese-for-kids', 'vietnamese-pronouns',
                    'vietnamese-family-terms', 'tet-greetings'],
        'tables': [('Greetings from a child', 'kids', 'greetings', 8),
                   ('Talking with grandparents', 'adult', 'grandparents', 12)],
        'body': [
            ('p', 'The phrase is “Con chào bà ạ.” It is usually the first full sentence a '
                  'child learns, and the one that makes a Vietnamese grandmother smile '
                  'every time.'),
            ('h2', 'Word by word'),
            ('ul', ['con: “I”, said by a child to an elder. It literally means “child”.',
                    'chào: to greet. On its own it works as “hello” or “bye”.',
                    'bà: grandma, and also “you” when you are talking to her.',
                    'ạ: a small word at the end that makes the sentence polite. Leaving it '
                    'out to a grandparent sounds a little rude.']),
            ('p', 'So the sentence is literally “Child greets grandma, politely.” There is '
                  'no “I” or “you” in the English sense: you name yourself and her by your '
                  'place in the family. [Vietnamese pronouns](vietnamese-pronouns) explains '
                  'why.'),
            ('h2', 'Con or cháu?'),
            ('p', '“Cháu” is the word for a grandchild, so “Cháu chào bà ạ” is also correct '
                  'and is common with older children and adults. Many families, especially '
                  'with small children, use “con” for grandchildren too. Use whatever your '
                  'family uses; if you are not sure, listen to how your parents talk to bà.'),
            ('table', 0),
            ('h2', 'Bà nội or bà ngoại?'),
            ('p', 'Your father’s mother is bà nội; your mother’s mother is bà ngoại. You use '
                  'these words when talking about her (“Bà nội con ở Huế”). Face to face, '
                  'just “bà” is enough. To get her attention, call “Bà ơi!”. Grandpa works '
                  'the same way: ông nội, ông ngoại, “Ông ơi!”. More in [Vietnamese family '
                  'terms](vietnamese-family-terms).'),
            ('h2', 'On a video call'),
            ('ul', ['Start: “Con chào bà ạ! Bà có khoẻ không ạ?” (Hello grandma! Are you well?)',
                    'If she asks “Ăn cơm chưa?”, answer “Dạ, con ăn rồi ạ.” (Yes, I have eaten.)',
                    'Before you hang up: “Con yêu bà. Con chào bà ạ.” (I love you, grandma. Bye.)',
                    'Bow your head a little as you greet her, even on screen. Grandparents notice.']),
            ('table', 1),
        ],
    },
    {
        'slug': 'vietnamese-phrases-for-in-laws',
        'keyword': 'vietnamese phrases for in-laws',
        'cluster': ['what to call vietnamese in-laws', 'vietnamese mother in law',
                    'bố mẹ chồng bố mẹ vợ', 'living with vietnamese in-laws'],
        'title': 'Vietnamese Phrases for In-Laws: What to Say',
        'desc': 'What to call your Vietnamese in-laws and the everyday phrases to use with '
                'them: thanks, visits, favours and calls, with Northern and Southern forms.',
        'h1': 'Vietnamese phrases for in-laws',
        'mode': 'adult',
        'youtube': None,
        'published': '2026-11-26', 'updated': '2026-11-26',
        'related': ['meeting-vietnamese-parents', 'vietnamese-pronouns',
                    'vietnamese-dinner-phrases', 'tet-greetings'],
        'tables': [('Saying thank you', 'adult', 'thanking_in_laws', 10, {'south': True}),
                   ('When they come to stay', 'adult', 'in_laws_visit', 10, {'south': True}),
                   ('Asking a favour, politely', 'adult', 'polite_requests', 8,
                    {'south': True})],
        'body': [
            ('p', 'In a Vietnamese family, your partner’s parents become your parents in the '
                  'way you talk. You call them what your partner calls them, and you call '
                  'yourself “con”, their child. That one change does more for the '
                  'relationship than any amount of vocabulary.'),
            ('h2', 'What to call them'),
            ('ul', ['To their face: “bố mẹ” (North) or “ba má” (South), the same as your '
                    'partner. Some families use “thầy u”, “cha mẹ” or “ba mẹ”; follow theirs.',
                    'When talking about them: “bố mẹ chồng” (husband’s parents), “bố mẹ vợ” '
                    '(wife’s parents). Never to their face.',
                    'Yourself: “con”. Not “tôi”, which sounds like a stranger. See '
                    '[Vietnamese pronouns](vietnamese-pronouns).',
                    'Your partner’s older siblings are “anh” and “chị” even if they are '
                    'younger than you; their younger siblings are “em”. You take your '
                    'partner’s place in the family order.']),
            ('table', 0),
            ('h2', 'Everyday politeness'),
            ('ul', ['Answer with “dạ” before anything else: “Dạ, con biết rồi ạ.”',
                    'Say where you are going: “Con xin phép ra ngoài một chút ạ.”',
                    'Offer to help in the kitchen and at the end of the meal. More in '
                    '[Vietnamese dinner phrases](vietnamese-dinner-phrases).',
                    'Call or message on their birthdays, at Tết and on death anniversaries '
                    '(đám giỗ). See [Tết greetings](tet-greetings).']),
            ('table', 1),
            ('p', 'Meeting them for the first time? Start with [meeting your partner’s '
                  'parents](meeting-vietnamese-parents).'),
            ('table', 2),
        ],
    },
    {
        'slug': 'heritage-vietnamese-learner',
        'keyword': 'heritage vietnamese learner',
        'cluster': ['i understand vietnamese but can’t speak',
                    'second generation vietnamese learn vietnamese',
                    'relearn vietnamese as an adult', 'heritage speaker vietnamese'],
        'title': 'Heritage Vietnamese: Understand It but Can’t Speak?',
        'desc': 'Grew up hearing Vietnamese but answer in English? Why it happens, what '
                'heritage learners already have, and how to start speaking again.',
        'h1': 'Heritage Vietnamese learners: you understand, now speak',
        'mode': 'adult',
        'youtube': None,
        'published': '2026-11-26', 'updated': '2026-11-26',
        'related': ['vietnamese-pronouns', 'northern-vs-southern-vietnamese',
                    'vietnamese-pronunciation-practice', 'learn-vietnamese-for-family'],
        'tables': [('When you don’t understand', 'adult', 'understanding', 12),
                   ('Talking about your Vietnamese', 'adult', 'my_vietnamese', 10)],
        'body': [
            ('p', 'Your parents spoke Vietnamese to you. You answered in English. Now you '
                  'can follow most of a family dinner, but when an aunt asks you something '
                  'directly, the words do not come. This is extremely common among children '
                  'of Vietnamese families abroad, and it is a much better starting point than '
                  'it feels like.'),
            ('h2', 'What you already have'),
            ('ul', ['An ear for the tones. You hear the difference between bà and bá even if '
                    'you cannot explain it.',
                    'Your family’s accent, North, South or Central, already in your head.',
                    'Home vocabulary: food, family, feelings, the things you heard every day.',
                    'A reason to speak and people to speak with.']),
            ('h2', 'What usually holds people back'),
            ('ul', ['Shyness. Relatives laugh kindly at mistakes, and it still stings. Expect '
                    'it, and keep going.',
                    'Pronouns. Not knowing whether to say con, cháu or em makes people go '
                    'silent. Learn the system once: [Vietnamese pronouns](vietnamese-pronouns).',
                    'Reading. Many heritage speakers never learned the tone marks. Spelling is '
                    'regular, so it takes weeks, not years: [Vietnamese tones](vietnamese-tones).',
                    'Vocabulary outside the home: work, news, feelings in detail.']),
            ('table', 0),
            ('h2', 'How to start speaking'),
            ('ol', ['Say out loud the phrases you already understand. Recognition turns into '
                    'speech by repetition, not by study.',
                    'Record yourself and compare with a model. Your ear is good; let it judge '
                    'your voice. See [pronunciation practice](vietnamese-pronunciation-practice).',
                    'Pick one relative and one routine, such as a weekly call with a parent, '
                    'and speak only Vietnamese for the first five minutes.',
                    'Tell the family what you are doing: “Con đang học lại tiếng Việt, bố mẹ '
                    'sửa giúp con nhé.” Most will slow down and help.',
                    'Keep the accent you grew up with, even if a course teaches a different '
                    'one. [Northern vs Southern](northern-vs-southern-vietnamese).']),
            ('table', 1),
        ],
    },
    {
        'slug': 'vietnamese-pronouns',
        'keyword': 'vietnamese pronouns',
        'cluster': ['how to say i and you in vietnamese', 'when to use tôi',
                    'vietnamese pronouns chart', 'con cháu em anh chị'],
        'title': 'Vietnamese Pronouns: Why Not Say “Tôi” to Grandma',
        'desc': 'Vietnamese uses family words for “I” and “you”. Why “tôi” sounds cold to '
                'family, and a simple chart of what to call yourself with each person.',
        'h1': 'Vietnamese pronouns: why you don’t say “tôi” to grandma',
        'mode': 'adult',
        'youtube': None,
        'published': '2026-11-26', 'updated': '2026-11-26',
        'related': ['vietnamese-family-terms', 'say-hello-to-grandma-in-vietnamese',
                    'vietnamese-phrases-for-in-laws', 'i-love-you-in-vietnamese'],
        'tables': [('The same greeting, different people', 'adult', 'greetings', 6,
                    {'start': 6}),
                   ('Who is who', 'kids', 'my_relatives', 12)],
        'body': [
            ('p', 'Textbooks teach “tôi” for “I” and “bạn” for “you”. They are correct, and '
                  'you will almost never use them with family. Vietnamese mostly uses family '
                  'words as pronouns: you call the other person by their place in the family, '
                  'and you call yourself by yours.'),
            ('h2', 'Why not “tôi”?'),
            ('p', '“Tôi” is neutral and a little distant. It is right in a shop, at work, in '
                  'writing, or with an adult you do not know well. Said to your grandmother it '
                  'sounds as if you are keeping her at arm’s length, like calling your mother '
                  '“madam”. Families notice it at once, and switching to “con” or “cháu” is the '
                  'fastest way to sound like part of the family.'),
            ('h2', 'Who calls whom what'),
            ('ul', ['Grandparents: call them ông / bà, yourself cháu (many families also use con).',
                    'Parents, and your partner’s parents: bố mẹ or ba má; yourself con.',
                    'Aunts and uncles: bác, chú, cô, cậu, dì; yourself cháu. Who is which: '
                    '[Vietnamese family terms](vietnamese-family-terms).',
                    'Older brother or sister, and older cousins: anh / chị; yourself em.',
                    'Younger brother or sister: em; yourself anh (male) or chị (female).',
                    'Partner: usually anh for the man or older partner, em for the woman or '
                    'younger one. See [I love you in Vietnamese](i-love-you-in-vietnamese).',
                    'Strangers: guess the family role by age. A bit older: anh / chị. Your '
                    'parents’ age: cô / chú. Elderly: bác, or ông / bà. Younger: em.',
                    'Friends your own age: mình / bạn; in the North also tớ / cậu.']),
            ('p', 'The other person answers the same way. Grandma calls herself “bà” and '
                  'calls you “cháu” or “con”: “Bà thương cháu” is her “I love you”.'),
            ('table', 0),
            ('h2', 'Small rules that help'),
            ('ul', ['We, to elders: “chúng con” or “chúng cháu”. Your partner and you, '
                    'casually: “tụi con” in the South.',
                    'He or she: add “ấy”: “bà ấy”, “anh ấy”, “chị ấy”.',
                    'Not sure? Ask: “Con gọi bác ấy là gì ạ?” (What should I call him or her?)',
                    'When in doubt, go one step more respectful. Calling someone chị when she '
                    'expected em is flattering; the other way round is not.']),
            ('table', 1),
        ],
    },
    {
        'slug': 'vietnamese-pronunciation-practice',
        'keyword': 'vietnamese pronunciation practice',
        'cluster': ['how to practice vietnamese pronunciation', 'vietnamese tone practice',
                    'vietnamese pronunciation app', 'record and compare vietnamese'],
        'title': 'Vietnamese Pronunciation Practice: Record and Compare',
        'desc': 'A daily routine for Vietnamese pronunciation: listen, shadow, record, '
                'compare your pitch curve with a model, and drill the pairs that matter.',
        'h1': 'Vietnamese pronunciation practice that actually works',
        'mode': 'adult',
        'youtube': None,
        'published': '2026-11-26', 'updated': '2026-11-26',
        'related': ['vietnamese-tones', 'northern-vs-southern-vietnamese',
                    'learn-vietnamese-app-for-beginners', 'say-hello-to-grandma-in-vietnamese'],
        'tables': [('Pairs to drill', 'adult', 'tones', 16, {'start': 6})],
        'body': [
            ('p', 'Reading about the six tones is useful once. After that, pronunciation '
                  'improves only one way: hearing a model, saying it yourself, and finding out '
                  'how close you were. Here is a routine that takes ten minutes a day.'),
            ('h2', 'The ten-minute routine'),
            ('ol', ['Listen three times without speaking. Pay attention to whether the voice '
                    'rises, falls, dips or stays level.',
                    'Shadow: play it again and speak along with it, at the same time.',
                    'Record yourself saying it alone.',
                    'Compare. Play the model, then your recording. Better still, look at the '
                    'pitch: is your line rising where the model rises?',
                    'Repeat with the next phrase. Five phrases done well beat twenty skimmed.']),
            ('h2', 'Watch the pitch curve'),
            ('p', 'Your ear is easily fooled by your own voice; a picture is not. In the Dạ '
                  'app, the tone coach draws the rise and fall of your voice next to the '
                  'model’s line, so you can see when your sắc tone is not rising high enough '
                  'or your nặng tone is not short and low. After a few tries it also adjusts '
                  'for how high or low your voice naturally is.'),
            ('h2', 'What to drill first'),
            ('ul', ['Minimal pairs, words that differ only by tone: bán / bạn, cá / cà, '
                    'sửa / sữa. They are in the table below.',
                    'Tones in phrases, not only single words. “Con chào bà ạ” has four syllables '
                    'and three different tones.',
                    'Final sounds: -c, -t, -p are stopped, not released. “Cát” ends abruptly.',
                    'Your accent’s sounds. In the South hỏi and ngã sound alike and “v” is often '
                    'closer to “y”; see [Northern vs Southern](northern-vs-southern-vietnamese).']),
            ('table', 0),
            ('p', 'New to the tones themselves? Start with [Vietnamese tones explained]'
                  '(vietnamese-tones).'),
        ],
    },
    {
        'slug': 'learn-vietnamese-app-for-beginners',
        'keyword': 'learn vietnamese app for beginners',
        'cluster': ['best app to learn vietnamese', 'vietnamese learning app',
                    'how to start learning vietnamese', 'vietnamese for beginners'],
        'title': 'Learn Vietnamese App for Beginners: What to Look For',
        'desc': 'What a beginner needs from a Vietnamese learning app: real audio in the '
                'right accent, tone feedback, useful phrases, and a first-month plan.',
        'h1': 'Choosing a Vietnamese app as a beginner',
        'mode': 'adult',
        'youtube': None,
        'published': '2026-11-26', 'updated': '2026-11-26',
        'related': ['vietnamese-pronunciation-practice', 'vietnamese-tones',
                    'learn-vietnamese-for-family', 'heritage-vietnamese-learner'],
        'tables': [('Your first phrases', 'adult', 'greetings', 8),
                   ('Phrases that keep a conversation going', 'adult', 'understanding', 8)],
        'body': [
            ('p', 'Vietnamese is not hard to start: the alphabet is Latin, there are no verb '
                  'endings, and spelling follows sound. What makes it hard is listening and '
                  'tones. A good beginner app should spend most of its time there.'),
            ('h2', 'What to look for'),
            ('ul', ['Audio for every phrase, and the choice of a Northern or Southern accent. '
                    'Learning one when your family speaks the other is frustrating. See '
                    '[Northern vs Southern](northern-vs-southern-vietnamese).',
                    'Speaking practice with feedback: record yourself and compare, ideally with '
                    'a view of your pitch. See [pronunciation practice]'
                    '(vietnamese-pronunciation-practice).',
                    'The six tones taught early, with minimal pairs, not saved for later.',
                    'Phrases you will use with real people, not only single words.',
                    'Kinship words and pronouns. Without them you cannot greet anyone '
                    'properly: [Vietnamese pronouns](vietnamese-pronouns).',
                    'A fair price model. Know whether it is a subscription or a single purchase '
                    'before you invest your time.']),
            ('table', 0),
            ('h2', 'Your first month'),
            ('ol', ['Days 1–7: the tones and five greetings. [Vietnamese tones](vietnamese-tones).',
                    'Days 8–14: the people around you: family words and how to address them.',
                    'Days 15–21: one situation you will really be in, such as a family dinner, '
                    'a phone call or ordering food.',
                    'Days 22–30: use it. Three phrases on a real call, or at a restaurant.']),
            ('table', 1),
            ('h2', 'Where Dạ fits'),
            ('p', 'Dạ is built for beginners who are learning Vietnamese for people: '
                  'grandparents, partners, in-laws, friends. It has three modes (Kids, Partner '
                  '& family, Everyday), 200 topics in each, audio in a Northern or Southern '
                  'accent, record-and-compare practice with a tone coach, and culture notes '
                  'that explain why people say what they say. It works offline, has no ads '
                  'and no accounts, and 50 topics in every mode are free. It is not a grammar '
                  'course or exam preparation. If that is your goal, pair it with a textbook '
                  'or a teacher.'),
        ],
    },
]
