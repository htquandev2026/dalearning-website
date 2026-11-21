"""Builds the static site for vietnamese-learning.com (GitHub Pages).

All page text lives in TEXT below; run `python build.py` after editing and
commit the generated HTML. No dependencies.
"""
import html
import os

DOMAIN = 'https://vietnamese-learning.com'
CONTACT = 'htquandev2026@gmail.com'
APP_STORE = None   # e.g. 'https://apps.apple.com/app/id...'
GOOGLE_PLAY = None  # e.g. 'https://play.google.com/store/apps/details?id=com.dalearn.app'
OTHER_APPS = [
    ('Animal World', 'https://htquandev2026.github.io/'),
    ('Prehistoric World', 'https://htquandev2026.github.io/prehistoricworld/'),
]
LANGS = [('en', 'English', ''), ('vi', 'Tiếng Việt', 'vi/'),
         ('ko', '한국어', 'ko/'), ('zh', '繁體中文', 'zh/')]

TEXT = {
    'en': {
        'title': 'Dạ: Learn Vietnamese for Family, Love & Travel',
        'desc': 'Learn the Vietnamese your family actually speaks. 150 topics per mode, '
                'audio in Northern and Southern accents, works offline, no ads.',
        'h1': 'Speak Vietnamese with the people you love.',
        'lead': 'Dạ teaches the everyday Vietnamese of real families: greeting '
                'grandparents, chatting at dinner, calling home at Tết. '
                'Short lessons, real phrases and both accents.',
        'store_ios': 'App Store', 'store_android': 'Google Play',
        'soon': 'Coming soon on',
        'get': 'Download on the',
        'modes_h': 'Three ways to learn',
        'modes': [
            ('🧒', 'Kids', 'For children growing up between two languages. '
             'Picture games, stickers and phrases to say to bà and ông, '
             'with no reading needed.'),
            ('💞', 'Partner & family', 'For anyone with a Vietnamese partner '
             'or in-laws. The right words for each relative, what to say at '
             'family meals, weddings and Tết, and why.'),
            ('🛵', 'Everyday', 'For travel, work and friends in Vietnam. '
             'Ordering phở, taking a xe ôm, renting a flat, making friends.'),
        ],
        'feat_h': 'What is inside',
        'feats': [
            ('📚', '150 topics per mode', 'More than 5,400 phrases, from first '
             'greetings to toasts at a wedding.'),
            ('🗣️', 'North and South', 'Every phrase has audio in a Hanoi or '
             'Saigon accent. Pick the one your family uses.'),
            ('🎙️', 'Speak and compare', 'Record yourself and compare with the '
             'model. Tone drills help with the six tones.'),
            ('☎️', 'Weekly call cards', 'A few phrases to try on your next '
             'video call with family.'),
            ('🏮', 'Culture notes', 'Short notes on manners, kinship words and '
             'festivals, so you know why people say what they say.'),
            ('🔎', 'Phrasebook', 'Search every phrase, even without typing '
             'the accents.'),
        ],
        'trust_h': 'Made for families',
        'trust': [
            ('No ads, no tracking', 'No accounts and no data collection. '
             'Your progress stays on your phone.'),
            ('Works offline', 'All lessons and audio are inside the app, so '
             'no internet is needed.'),
            ('Pay once', '10 free topics in every mode. One purchase unlocks '
             'everything, with no subscription.'),
            ('Your language', 'The app speaks English, Vietnamese, Korean and '
             'Traditional Chinese.'),
        ],
        'phone_today': "TODAY'S LESSON", 'phone_topic': 'Visiting grandma',
        'phone_lines': [('Con chào bà ạ!', 'Hello, Grandma!'),
                        ('Bà có khoẻ không ạ?', 'How are you, Grandma?'),
                        ('Con nhớ bà lắm.', 'I miss you so much.')],
        'privacy': 'Privacy policy', 'support': 'Support',
        'contact': 'Contact', 'also': 'Also by us',
        'footer_note': 'We want every phrase to sound natural. '
                       'Found a mistake? Please tell us.',
    },
    'vi': {
        'title': 'Dạ: Học tiếng Việt để nói chuyện với gia đình',
        'desc': 'Học tiếng Việt mà gia đình bạn thật sự nói. 150 chủ đề mỗi chế độ, '
                'âm giọng Bắc và Nam, dùng không cần mạng, không quảng cáo.',
        'h1': 'Nói tiếng Việt với những người bạn thương.',
        'lead': 'Dạ dạy tiếng Việt đời thường của các gia đình thật: chào ông bà, '
                'trò chuyện trong bữa cơm, gọi điện về nhà dịp Tết. Bài ngắn, '
                'câu thật, đủ cả giọng Bắc lẫn giọng Nam.',
        'store_ios': 'App Store', 'store_android': 'Google Play',
        'soon': 'Sắp có trên', 'get': 'Tải trên',
        'modes_h': 'Ba cách học',
        'modes': [
            ('🧒', 'Trẻ em', 'Cho các bé lớn lên giữa hai ngôn ngữ. Trò chơi '
             'bằng hình, sticker và những câu để nói với ông bà. Bé chưa biết '
             'đọc vẫn học được.'),
            ('💞', 'Vợ chồng & gia đình', 'Cho người có vợ, chồng hoặc người '
             'yêu là người Việt. Biết gọi từng người trong nhà cho đúng, nói gì '
             'trong bữa cơm, đám cưới, ngày Tết, và vì sao.'),
            ('🛵', 'Giao tiếp hằng ngày', 'Cho du lịch, công việc và bạn bè ở '
             'Việt Nam: gọi phở, đi xe ôm, thuê nhà, kết bạn.'),
        ],
        'feat_h': 'Có gì trong app',
        'feats': [
            ('📚', '150 chủ đề mỗi chế độ', 'Hơn 5.400 câu, từ lời chào đầu '
             'tiên đến lời chúc trong tiệc cưới.'),
            ('🗣️', 'Giọng Bắc và Nam', 'Câu nào cũng có âm thanh giọng Hà Nội '
             'hoặc Sài Gòn. Chọn giọng nhà bạn hay nói.'),
            ('🎙️', 'Nói và so sánh', 'Thu âm giọng mình rồi so với giọng mẫu. '
             'Bài luyện thanh điệu giúp nói đúng sáu thanh.'),
            ('☎️', 'Thẻ gọi điện hằng tuần', 'Vài câu để thử trong lần gọi '
             'video tới với gia đình.'),
            ('🏮', 'Ghi chú văn hoá', 'Giải thích ngắn về lễ nghĩa, cách xưng '
             'hô và lễ Tết, để hiểu vì sao người ta nói như vậy.'),
            ('🔎', 'Sổ câu', 'Tìm mọi câu đã có, gõ không dấu cũng được.'),
        ],
        'trust_h': 'Làm cho gia đình',
        'trust': [
            ('Không quảng cáo, không theo dõi', 'Không cần tài khoản, không '
             'thu thập dữ liệu. Tiến độ học nằm trên máy bạn.'),
            ('Dùng không cần mạng', 'Toàn bộ bài học và âm thanh có sẵn trong '
             'app.'),
            ('Trả một lần', '10 chủ đề miễn phí mỗi chế độ. Mua một lần là mở '
             'hết, không thuê bao.'),
            ('Ngôn ngữ của bạn', 'App có giao diện tiếng Anh, Việt, Hàn và '
             'Hoa phồn thể.'),
        ],
        'phone_today': 'BÀI HÔM NAY', 'phone_topic': 'Về thăm bà',
        'phone_lines': [('Con chào bà ạ!', 'Hello, Grandma!'),
                        ('Bà có khoẻ không ạ?', 'How are you, Grandma?'),
                        ('Con nhớ bà lắm.', 'I miss you so much.')],
        'privacy': 'Chính sách quyền riêng tư', 'support': 'Hỗ trợ',
        'contact': 'Liên hệ', 'also': 'App khác của chúng tôi',
        'footer_note': 'Chúng tôi muốn câu nào cũng tự nhiên như người Việt nói. '
                       'Bạn thấy chỗ nào chưa đúng? Hãy báo cho chúng tôi.',
    },
    'ko': {
        'title': 'Dạ: 가족과 함께 쓰는 베트남어',
        'desc': '가족이 실제로 쓰는 베트남어를 배우세요. 모드별 150개 주제, '
                '북부·남부 발음, 오프라인 사용, 광고 없음.',
        'h1': '사랑하는 사람과 베트남어로 이야기하세요.',
        'lead': 'Dạ는 실제 가족이 쓰는 생활 베트남어를 가르쳐요. 조부모님께 '
                '인사하기, 저녁 식탁 대화, 설날 안부 전화까지. 짧은 수업, '
                '실제 표현, 북부와 남부 발음 모두.',
        'store_ios': 'App Store', 'store_android': 'Google Play',
        'soon': '곧 출시:', 'get': '다운로드:',
        'modes_h': '세 가지 학습 모드',
        'modes': [
            ('🧒', '어린이', '두 언어 사이에서 자라는 아이들을 위해. 그림 '
             '게임, 스티커, 할머니·할아버지께 드릴 말. 글을 몰라도 배울 수 '
             '있어요.'),
            ('💞', '배우자와 가족', '베트남인 배우자나 시댁·처가가 있는 분을 '
             '위해. 친척마다 맞는 호칭, 가족 식사·결혼식·설날에 할 말과 그 '
             '이유까지.'),
            ('🛵', '일상 회화', '베트남 여행, 일, 친구를 위해. 쌀국수 주문, '
             '쎄옴 타기, 집 구하기, 친구 사귀기.'),
        ],
        'feat_h': '앱에 담긴 것',
        'feats': [
            ('📚', '모드별 150개 주제', '첫인사부터 결혼식 건배사까지 5,400개가 '
             '넘는 표현.'),
            ('🗣️', '북부와 남부', '모든 표현에 하노이 또는 사이공 발음 오디오. '
             '가족이 쓰는 발음을 고르세요.'),
            ('🎙️', '말하고 비교하기', '내 목소리를 녹음해 원어민 발음과 '
             '비교하고, 성조 연습으로 6개 성조를 익혀요.'),
            ('☎️', '주간 통화 카드', '다음 가족 영상통화에서 써 볼 몇 마디.'),
            ('🏮', '문화 노트', '예절, 호칭, 명절에 대한 짧은 설명.'),
            ('🔎', '표현집', '성조 부호 없이 입력해도 모든 표현을 검색할 수 '
             '있어요.'),
        ],
        'trust_h': '가족을 위해 만들었어요',
        'trust': [
            ('광고·추적 없음', '계정도, 데이터 수집도 없어요. 학습 기록은 내 '
             '휴대폰에만 저장돼요.'),
            ('오프라인 사용', '모든 수업과 오디오가 앱 안에 있어요.'),
            ('한 번 결제', '모드마다 10개 주제 무료. 한 번 구매하면 전부 '
             '열리고 구독은 없어요.'),
            ('내 언어로', '영어, 베트남어, 한국어, 번체 중국어 화면을 '
             '지원해요.'),
        ],
        'phone_today': '오늘의 수업', 'phone_topic': '할머니 댁 방문',
        'phone_lines': [('Con chào bà ạ!', '할머니, 안녕하세요!'),
                        ('Bà có khoẻ không ạ?', '할머니, 잘 지내셨어요?'),
                        ('Con nhớ bà lắm.', '할머니가 너무 보고 싶었어요.')],
        'privacy': '개인정보 처리방침', 'support': '지원',
        'contact': '문의', 'also': '다른 앱',
        'footer_note': '자연스러운 생활 베트남어를 목표로 합니다. 틀린 곳이 '
                       '있으면 알려 주세요.',
    },
    'zh': {
        'title': 'Dạ:和家人說越南語',
        'desc': '學會家人真正在說的越南語。每種模式 150 個主題,北部與南部口音,'
                '可離線使用,無廣告。',
        'h1': '用越南語和你愛的人聊天。',
        'lead': 'Dạ 教的是真實家庭的日常越南語:問候爺爺奶奶、晚餐聊天、'
                '過年打電話回家。課程簡短、句子實用,北部和南部口音都有。',
        'store_ios': 'App Store', 'store_android': 'Google Play',
        'soon': '即將登上', 'get': '下載:',
        'modes_h': '三種學習模式',
        'modes': [
            ('🧒', '兒童', '給在兩種語言之間長大的孩子。圖片遊戲、貼紙,'
             '還有對外公外婆說的話,不識字也能學。'),
            ('💞', '伴侶與家人', '給有越南伴侶或姻親的人。學會怎麼稱呼每位'
             '親戚,家庭聚餐、婚禮、過年該說什麼,以及為什麼。'),
            ('🛵', '日常會話', '給在越南旅行、工作、交朋友的人。點河粉、'
             '搭摩托計程車、租房、交朋友。'),
        ],
        'feat_h': 'App 裡有什麼',
        'feats': [
            ('📚', '每種模式 150 個主題', '超過 5,400 句,從第一句問候到婚禮'
             '致詞。'),
            ('🗣️', '北部與南部', '每一句都有河內或西貢口音的音檔,選家人說'
             '的那一種。'),
            ('🎙️', '說說看、比一比', '錄下自己的聲音和示範比較,聲調練習幫你'
             '掌握六個聲調。'),
            ('☎️', '每週通話卡', '下次和家人視訊時可以試試的幾句話。'),
            ('🏮', '文化小筆記', '關於禮節、稱謂和節慶的簡短說明。'),
            ('🔎', '句庫', '不打聲調符號也能搜尋所有句子。'),
        ],
        'trust_h': '為家庭而做',
        'trust': [
            ('無廣告、不追蹤', '不需要帳號,不收集資料。學習進度只存在你的'
             '手機裡。'),
            ('離線使用', '所有課程和音檔都在 App 裡。'),
            ('一次買斷', '每種模式 10 個免費主題。購買一次全部解鎖,沒有'
             '訂閱。'),
            ('你的語言', '介面支援英文、越南文、韓文和繁體中文。'),
        ],
        'phone_today': '今日課程', 'phone_topic': '去看奶奶',
        'phone_lines': [('Con chào bà ạ!', '奶奶好!'),
                        ('Bà có khoẻ không ạ?', '奶奶身體好嗎?'),
                        ('Con nhớ bà lắm.', '我好想奶奶。')],
        'privacy': '隱私權政策', 'support': '支援',
        'contact': '聯絡我們', 'also': '我們的其他 App',
        'footer_note': '內容力求自然、道地的日常越南語。發現錯誤?請告訴我們。',
    },
}

CSS = """
:root {
  --bg: #FFF8EE; --ink: #2B2140; --muted: #6B5E55; --card: #FFFFFF;
  --accent: #E8553F; --accent-ink: #FFFFFF; --line: #F0E0C8; --soft: #FFEBDD;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #1E1A17; --ink: #F5EDE4; --muted: #BFB2A6; --card: #2A2420;
    --accent: #FF7A62; --accent-ink: #1E1A17; --line: #3A322C; --soft: #3A2A24;
  }
}
:root[data-theme="dark"] {
  --bg: #1E1A17; --ink: #F5EDE4; --muted: #BFB2A6; --card: #2A2420;
  --accent: #FF7A62; --accent-ink: #1E1A17; --line: #3A322C; --soft: #3A2A24;
}
* { box-sizing: border-box; }
body { margin: 0; background: var(--bg); color: var(--ink);
  font-family: Nunito, system-ui, sans-serif; font-weight: 700; line-height: 1.5; }
:lang(ko) body, :lang(ko) h1 { word-break: keep-all; }
main { max-width: 960px; margin: 0 auto; padding: 0 16px 48px; }
header { display: flex; align-items: center; gap: 12px; padding: 20px 0; flex-wrap: wrap; }
header .logo { width: 48px; height: 48px; border-radius: 12px; }
header .name { font-size: 22px; font-weight: 900; margin-right: auto; }
nav.langs { display: flex; gap: 4px; flex-wrap: wrap; }
nav.langs a { padding: 6px 10px; border-radius: 999px; color: var(--muted);
  text-decoration: none; font-size: 14px; }
nav.langs a[aria-current] { background: var(--card); color: var(--ink); border: 2px solid var(--line); }
.hero { display: grid; gap: 32px; grid-template-columns: 1fr; align-items: center; padding: 16px 0 32px; }
@media (min-width: 760px) { .hero { grid-template-columns: 1.2fr 1fr; } }
.hero h1 { font-size: clamp(32px, 6vw, 52px); line-height: 1.1; margin: 0 0 12px; font-weight: 900; }
.hero p { font-size: 19px; color: var(--muted); margin: 0 0 20px; }
.badges { display: flex; flex-wrap: wrap; gap: 10px; }
.badge { display: inline-block; padding: 12px 20px; border-radius: 999px; text-decoration: none;
  background: var(--accent); color: var(--accent-ink); font-weight: 900; }
.badge.soon { background: var(--card); color: var(--muted); border: 2px solid var(--line); }
.phone { justify-self: center; width: min(300px, 100%); background: var(--ink); border-radius: 40px;
  padding: 14px; box-shadow: 0 14px 40px rgba(0,0,0,.18); }
.screen { background: var(--bg); border-radius: 28px; padding: 18px 16px 22px; }
.today { background: #2B2140; color: #FFF8EE; border-radius: 20px; padding: 16px; margin-bottom: 14px; }
.today small { letter-spacing: 1px; opacity: .75; font-size: 11px; }
.today b { display: block; font-size: 20px; font-weight: 900; margin-top: 4px; }
.bar { height: 6px; border-radius: 9px; background: #4A3F5C; margin-top: 12px; overflow: hidden; }
.bar i { display: block; width: 40%; height: 100%; background: #F97316; }
.line { display: flex; align-items: center; gap: 10px; background: var(--card); border: 2px solid var(--line);
  border-radius: 16px; padding: 10px 12px; margin-top: 8px; }
.line div { flex: 1; min-width: 0; }
.line b { display: block; font-size: 16px; }
.line span { color: var(--muted); font-size: 13px; }
.play { width: 34px; height: 34px; border-radius: 50%; background: var(--accent); color: var(--accent-ink);
  display: grid; place-items: center; font-size: 13px; flex: none; }
.grid { display: grid; gap: 16px; grid-template-columns: repeat(auto-fit, minmax(min(220px, 100%), 1fr)); }
.card { background: var(--card); border-radius: 20px; padding: 20px; border: 2px solid var(--line); }
.card .ic { font-size: 30px; line-height: 1; margin-bottom: 8px; }
.card h3 { margin: 0 0 6px; font-size: 19px; font-weight: 900; }
.card p { margin: 0; color: var(--muted); }
.mode { background: var(--soft); border-color: transparent; }
h2 { font-size: 28px; font-weight: 900; margin: 40px 0 16px; }
.doc { max-width: 720px; }
.doc h1 { font-size: 34px; font-weight: 900; margin: 8px 0 4px; }
.doc h2 { font-size: 21px; margin: 28px 0 8px; }
.doc p, .doc li { color: var(--muted); }
.doc a, footer a { color: var(--ink); }
footer { border-top: 2px solid var(--line); margin-top: 48px; padding-top: 20px; color: var(--muted); font-size: 15px; }
"""

e = html.escape


def head(lang, title, desc, path, root, alternates=True):
    alt = ''
    if alternates:
        alt = ''.join(
            f'<link rel="alternate" hreflang="{c}" href="{DOMAIN}/{p}">\n'
            for c, _, p in LANGS)
        alt += f'<link rel="alternate" hreflang="x-default" href="{DOMAIN}/">\n'
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{DOMAIN}/{path}">
{alt}<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{DOMAIN}/{path}">
<meta property="og:type" content="website">
<link rel="icon" href="{root}icon.png">
<link rel="apple-touch-icon" href="{root}apple-touch-icon.png">
<meta property="og:image" content="{DOMAIN}/og-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}style.css">
</head>
<body>
<main>
"""


def header(root, current=None):
    langs = ''
    if current is not None:
        langs = '<nav class="langs" aria-label="Language">' + ''.join(
            f'<a href="{root}{p}" hreflang="{c}"'
            f'{" aria-current=\"page\"" if c == current else ""}>{n}</a>'
            for c, n, p in LANGS) + '</nav>'
    return (f'  <header>\n    <a href="{root or './'}"><img class="logo" src="{root}icon.png" alt=""></a>\n'
            f'    <span class="name">Dạ</span>\n    {langs}\n  </header>\n')


def footer(t, root):
    also = ' · '.join(f'<a href="{u}">{e(n)}</a>' for n, u in OTHER_APPS)
    return f"""  <footer>
    <p>{e(t['footer_note'])}</p>
    <p><a href="{root}privacy.html">{e(t['privacy'])}</a> · <a href="{root}support.html">{e(t['support'])}</a> · {e(t['contact'])}: <a href="mailto:{CONTACT}">{CONTACT}</a> · {e(t['also'])}: {also}</p>
  </footer>
</main>
</body>
</html>
"""


def badges(t):
    out = []
    for url, name in [(APP_STORE, t['store_ios']), (GOOGLE_PLAY, t['store_android'])]:
        if url:
            out.append(f'<a class="badge" href="{url}">{e(t["get"])} {name}</a>')
        else:
            out.append(f'<span class="badge soon">{e(t["soon"])} {name}</span>')
    return '\n        '.join(out)


def landing(code, path):
    t = TEXT[code]
    root = '../' if path else ''
    cards = lambda items, cls='': '\n'.join(
        f'    <div class="card {cls}"><div class="ic">{ic}</div><h3>{e(h)}</h3><p>{e(p)}</p></div>'
        for ic, h, p in items)
    lines = '\n'.join(
        f'          <div class="line"><div><b>{e(vi)}</b><span>{e(m)}</span></div>'
        f'<span class="play" aria-hidden="true">▶</span></div>'
        for vi, m in t['phone_lines'])
    trust = '\n'.join(
        f'    <div class="card"><h3>{e(h)}</h3><p>{e(p)}</p></div>' for h, p in t['trust'])
    return head(code, t['title'], t['desc'], path, root) + header(root, code) + f"""
  <section class="hero">
    <div>
      <h1>{e(t['h1'])}</h1>
      <p>{e(t['lead'])}</p>
      <div class="badges">
        {badges(t)}
      </div>
    </div>
    <div class="phone" role="img" aria-label="{e(t['phone_topic'])}">
      <div class="screen">
        <div class="today"><small>{e(t['phone_today'])}</small><b>{e(t['phone_topic'])}</b><div class="bar"><i></i></div></div>
{lines}
      </div>
    </div>
  </section>

  <h2>{e(t['modes_h'])}</h2>
  <div class="grid">
{cards(t['modes'], 'mode')}
  </div>

  <h2>{e(t['feat_h'])}</h2>
  <div class="grid">
{cards(t['feats'])}
  </div>

  <h2>{e(t['trust_h'])}</h2>
  <div class="grid">
{trust}
  </div>

""" + footer(t, root)


PRIVACY = f"""
  <article class="doc">
    <h1>Privacy policy</h1>
    <p>Dạ: Learn Vietnamese · Effective 21 November 2026</p>

    <h2>The short version</h2>
    <p>Dạ does not collect, store or share any personal information. There are no accounts, no ads, no analytics and no tracking. Everything you do in the app stays on your device.</p>

    <h2>What stays on your device</h2>
    <ul>
      <li>Your learning progress, streak, stickers, settings and the name you type during set-up.</li>
      <li>Voice recordings you make to practise speaking, and any family voice clips you add. These are saved inside the app on your device only and are never uploaded.</li>
    </ul>
    <p>Deleting the app deletes all of this. We cannot see it or recover it.</p>

    <h2>Microphone</h2>
    <p>The app asks for microphone access only so you can record yourself and compare with the example audio. Recordings never leave your device.</p>

    <h2>Purchases</h2>
    <p>Purchases and optional tips are handled by Apple (App Store) or Google (Google Play). We never receive your name, email or card details. The store only tells the app that a purchase was completed.</p>

    <h2>Children</h2>
    <p>Kids mode is designed for children and collects nothing. Purchases and settings sit behind a grown-up check. We do not show ads or use third-party analytics in any mode.</p>

    <h2>Changes</h2>
    <p>If this policy changes, we will update this page and the date above.</p>

    <h2>Contact</h2>
    <p>Questions about privacy: <a href="mailto:{CONTACT}">{CONTACT}</a></p>
  </article>
"""

SUPPORT = f"""
  <article class="doc">
    <h1>Support</h1>
    <p>Need help with Dạ? Email <a href="mailto:{CONTACT}">{CONTACT}</a> and we will reply as soon as we can. Please include your phone model and what you were doing.</p>

    <h2>Restore a purchase</h2>
    <p>Open Settings (in Kids mode, the grown-ups area) and tap <b>Restore purchases</b>. Use the same Apple ID or Google account you bought with. One purchase unlocks every mode.</p>

    <h2>No sound</h2>
    <p>Check the volume and that the phone is not on silent. All audio is inside the app, so no internet is needed.</p>

    <h2>North or South accent</h2>
    <p>You can switch accents at any time in Settings. Every phrase has audio in both.</p>

    <h2>Found a mistake in the Vietnamese?</h2>
    <p>We want every phrase to sound natural. Tell us the topic and the phrase and we will fix it in the next update.</p>
  </article>
"""


def doc(title, path, body):
    return (head('en', f'{title} · Dạ', f'{title} for Dạ: Learn Vietnamese.',
                 path, '', alternates=False)
            + header('') + body + footer(TEXT['en'], ''))


def write(path, text):
    os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
    with open(path, 'w', encoding='utf8', newline='\n') as f:
        f.write(text)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    os.chdir(here)
    for code, _, path in LANGS:
        write(os.path.join(path, 'index.html'), landing(code, path))
    write('privacy.html', doc('Privacy policy', 'privacy.html', PRIVACY))
    write('support.html', doc('Support', 'support.html', SUPPORT))
    write('style.css', CSS.lstrip())
    write('CNAME', 'vietnamese-learning.com\n')
    write('.nojekyll', '')
    write('robots.txt', f'User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n')
    urls = [p for _, _, p in LANGS] + ['privacy.html', 'support.html']
    write('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + ''.join(f'  <url><loc>{DOMAIN}/{u}</loc></url>\n' for u in urls)
          + '</urlset>\n')
    write('404.html', head('en', 'Page not found · Dạ', 'Page not found.', '', '/', False)
          + header('/') + '  <article class="doc"><h1>Page not found</h1>'
          '<p><a href="/">Back to Dạ</a></p></article>\n' + footer(TEXT['en'], '/'))
    write('README.md', '# vietnamese-learning.com\n\nStatic site for the Dạ app, '
          'served by GitHub Pages.\nEdit `build.py`, run `python build.py`, '
          'commit the output.\n')
    print('built')


if __name__ == '__main__':
    main()
