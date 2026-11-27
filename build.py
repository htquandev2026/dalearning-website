"""Builds the static site for vietnamese-learning.com (GitHub Pages).

All page text lives in TEXT below; run `python build.py` after editing and
commit the generated HTML. No dependencies.
"""
import html
import json
import re
import os
from urllib.parse import quote

from guides import GUIDES

DOMAIN = 'https://vietnamese-learning.com'
CONTACT = 'htquandev2026@gmail.com'
APP_STORE = None   # e.g. 'https://apps.apple.com/app/id...'
GOOGLE_PLAY = None  # e.g. 'https://play.google.com/store/apps/details?id=com.dalearn.app'
OTHER_APPS = [
    ('Animal World', 'https://htquandev2026.github.io/'),
    ('Prehistoric World', 'https://htquandev2026.github.io/prehistoricworld/'),
]
# Official profiles, same name and link everywhere (see marketing/brand.md in
# the app repo). Add each URL once the profile is live; they feed the
# Organization sameAs, the About page and llms.txt.
# Waitlist form while the app is not in both stores. Set WAITLIST_ACTION to a
# form endpoint that takes a POST with an `email` field (Buttondown:
# https://buttondown.com/api/emails/embed-subscribe/<username>, Formspree:
# https://formspree.io/f/<id>). Left as None, the button opens an email to CONTACT.
WAITLIST_ACTION = None
# Google Search Console HTML-tag verification token (the content="..." value),
# only needed if you verify with the meta tag instead of DNS.
GSC_VERIFY = None
# Date of the last real change to the home pages (sitemap lastmod).
SITE_UPDATED = '2026-11-26'
PROFILES = [
    # ('YouTube', 'https://www.youtube.com/@...'),
]
LANGS = [('en', 'English', ''), ('vi', 'Tiếng Việt', 'vi/'),
         ('ko', '한국어', 'ko/'), ('zh', '繁體中文', 'zh/')]

TEXT = {
    'en': {
        'title': 'Dạ: Learn Vietnamese for Family, Love & Travel',
        'desc': 'Learn the Vietnamese your family actually speaks. 200 topics per mode, '
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
            ('📚', '200 topics per mode', 'More than 7,000 phrases, from first '
             'greetings to toasts at a wedding.'),
            ('🗣️', 'North and South', 'Every phrase has audio in a Hanoi or '
             'Saigon accent. Pick the one your family uses.'),
            ('🎙️', 'Speak and compare', 'Record yourself and compare with the '
             'example audio. The tone coach draws your pitch next to the '
             'model and scores each try.'),
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
            ('Pay once', '50 free topics in every mode. One purchase unlocks '
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
        'wl_btn': 'Join the waitlist', 'wl_ph': 'Your email',
        'wl_note': 'One email when Dạ launches. No spam, unsubscribe any time.',
        'wl_subject': 'Dạ waitlist', 'wl_body': 'Please email me when Dạ launches.',
    },
    'vi': {
        'title': 'Dạ: Học tiếng Việt để nói chuyện với gia đình',
        'desc': 'Học tiếng Việt mà gia đình bạn thật sự nói. 200 chủ đề mỗi chế độ, '
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
            ('📚', '200 chủ đề mỗi chế độ', 'Hơn 7.000 câu, từ lời chào đầu '
             'tiên đến lời chúc trong tiệc cưới.'),
            ('🗣️', 'Giọng Bắc và Nam', 'Câu nào cũng có âm thanh giọng Hà Nội '
             'hoặc Sài Gòn. Chọn giọng nhà bạn hay nói.'),
            ('🎙️', 'Nói và so sánh', 'Thu âm giọng mình rồi so với giọng mẫu. '
             'Phần luyện thanh vẽ đường cao độ giọng bạn cạnh giọng mẫu và '
             'chấm điểm từng lần.'),
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
            ('Trả một lần', '50 chủ đề miễn phí mỗi chế độ. Mua một lần là mở '
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
        'wl_btn': 'Đăng ký nhận tin', 'wl_ph': 'Email của bạn',
        'wl_note': 'Một email khi Dạ ra mắt. Không spam, huỷ lúc nào cũng được.',
        'wl_subject': 'Đăng ký chờ Dạ', 'wl_body': 'Hãy báo cho tôi khi Dạ ra mắt.',
    },
    'ko': {
        'title': 'Dạ: 가족과 함께 쓰는 베트남어',
        'desc': '가족이 실제로 쓰는 베트남어를 배우세요. 모드별 200개 주제, '
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
            ('📚', '모드별 200개 주제', '첫인사부터 결혼식 건배사까지 7,000개가 '
             '넘는 표현.'),
            ('🗣️', '북부와 남부', '모든 표현에 하노이 또는 사이공 발음 오디오. '
             '가족이 쓰는 발음을 고르세요.'),
            ('🎙️', '말하고 비교하기', '내 목소리를 녹음해 예시 음성과 '
             '비교해요. 성조 코치가 내 음높이를 예시와 나란히 그려 주고 '
             '매번 점수를 매겨요.'),
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
            ('한 번 결제', '모드마다 50개 주제 무료. 한 번 구매하면 전부 '
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
        'wl_btn': '출시 알림 받기', 'wl_ph': '이메일',
        'wl_note': 'Dạ 출시 때 이메일 한 통만 보내요. 스팸 없음, 언제든 해지 가능.',
        'wl_subject': 'Dạ 출시 알림', 'wl_body': 'Dạ가 출시되면 알려 주세요.',
    },
    'zh': {
        'title': 'Dạ:和家人說越南語',
        'desc': '學會家人真正在說的越南語。每種模式 200 個主題,北部與南部口音,'
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
            ('📚', '每種模式 200 個主題', '超過 7,000 句,從第一句問候到婚禮'
             '致詞。'),
            ('🗣️', '北部與南部', '每一句都有河內或西貢口音的音檔,選家人說'
             '的那一種。'),
            ('🎙️', '說說看、比一比', '錄下自己的聲音和示範音檔比較。聲調教練'
             '會把你的音高曲線畫在示範旁邊,每次都給分數。'),
            ('☎️', '每週通話卡', '下次和家人視訊時可以試試的幾句話。'),
            ('🏮', '文化小筆記', '關於禮節、稱謂和節慶的簡短說明。'),
            ('🔎', '句庫', '不打聲調符號也能搜尋所有句子。'),
        ],
        'trust_h': '為家庭而做',
        'trust': [
            ('無廣告、不追蹤', '不需要帳號,不收集資料。學習進度只存在你的'
             '手機裡。'),
            ('離線使用', '所有課程和音檔都在 App 裡。'),
            ('一次買斷', '每種模式 50 個免費主題。購買一次全部解鎖,沒有'
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
        'wl_btn': '加入等候名單', 'wl_ph': '你的 Email',
        'wl_note': 'Dạ 上架時只寄一封信。不寄垃圾信,可隨時取消。',
        'wl_subject': 'Dạ 等候名單', 'wl_body': 'Dạ 上架時請通知我。',
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
.grid a.card { text-decoration: none; color: var(--ink); }
.grid a.card:hover { border-color: var(--accent); }
.doc.wide { max-width: none; }
.crumbs { font-size: 14px; margin: 0; }
.crumbs a { color: var(--muted); }
.doc h3 { font-size: 18px; margin: 22px 0 8px; }
table.phrases { width: 100%; border-collapse: collapse; background: var(--card);
  border: 2px solid var(--line); border-radius: 16px; overflow: hidden; }
table.phrases th, table.phrases td { text-align: left; padding: 9px 12px; border-top: 1px solid var(--line);
  vertical-align: top; }
table.phrases th { border-top: 0; font-size: 13px; letter-spacing: .5px; color: var(--muted); }
table.phrases td:first-child { color: var(--ink); font-weight: 900; }
table.phrases td:last-child { color: var(--muted); }
.cta { background: var(--soft); border-radius: 20px; padding: 4px 20px 20px; margin-top: 32px; }
.cta h2 { margin-top: 18px; }
.wl { display: flex; flex-wrap: wrap; gap: 8px; margin: 16px 0 6px; max-width: 460px; }
.wl input { flex: 1 1 200px; min-width: 0; padding: 12px 16px; border-radius: 999px; border: 2px solid var(--line);
  background: var(--card); color: var(--ink); font: inherit; }
.wl input:focus { outline: 2px solid var(--accent); outline-offset: 1px; }
.wl button { border: 0; cursor: pointer; font: inherit; }
.wl-note { font-size: 14px; color: var(--muted); margin: 0 0 12px; }
.table-wrap { overflow-x: auto; }
.doc ol li, .doc ul li { margin: 4px 0; }
.video { position: relative; aspect-ratio: 16 / 9; margin: 16px 0; }
.video iframe { position: absolute; inset: 0; width: 100%; height: 100%; border: 0; border-radius: 16px; }
footer { border-top: 2px solid var(--line); margin-top: 48px; padding-top: 20px; color: var(--muted); font-size: 15px; }
"""

e = html.escape


def head(lang, title, desc, path, root, alternates=True, extra='', og_type='website'):
    alt = ''
    if alternates:
        alt = ''.join(
            f'<link rel="alternate" hreflang="{c}" href="{DOMAIN}/{p}">\n'
            for c, _, p in LANGS)
        alt += f'<link rel="alternate" hreflang="x-default" href="{DOMAIN}/">\n'
    gsc = (f'<meta name="google-site-verification" content="{e(GSC_VERIFY)}">\n'
           if GSC_VERIFY and path == '' else '')
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
<meta property="og:type" content="{og_type}">
<link rel="icon" href="{root}icon.png">
<link rel="apple-touch-icon" href="{root}apple-touch-icon.png">
<meta property="og:image" content="{DOMAIN}/og-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Nunito:wght@700;900&display=swap" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@700;900&display=swap"></noscript>
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#FFF8EE">
{gsc}<link rel="stylesheet" href="{root}style.css">
{extra}</head>
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
    <p><a href="{root}guides/">Guides</a> · <a href="{root}about.html">About</a> · <a href="{root}privacy.html">{e(t['privacy'])}</a> · <a href="{root}support.html">{e(t['support'])}</a> · {e(t['contact'])}: <a href="mailto:{CONTACT}">{CONTACT}</a> · {e(t['also'])}: {also}</p>
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


def waitlist(t, source):
    """Email sign-up shown until the app is in both stores."""
    if APP_STORE and GOOGLE_PLAY:
        return ''
    note = f'<p class="wl-note">{e(t["wl_note"])}</p>'
    if WAITLIST_ACTION:
        return (f'<form class="wl" action="{e(WAITLIST_ACTION)}" method="post" target="_blank">'
                f'<input type="email" name="email" required autocomplete="email" '
                f'placeholder="{e(t["wl_ph"])}" aria-label="{e(t["wl_ph"])}">'
                f'<input type="hidden" name="tag" value="{e(source)}">'
                f'<button class="badge" type="submit">{e(t["wl_btn"])}</button></form>{note}')
    href = (f'mailto:{CONTACT}?subject={quote(t["wl_subject"] + " (" + source + ")")}'
            f'&body={quote(t["wl_body"])}')
    return f'<div class="wl"><a class="badge" href="{href}">{e(t["wl_btn"])}</a></div>{note}'


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
    extra = jsonld(org_ld(), website_ld()) if code == 'en' else ''
    guides_block = ''
    if code == 'en':
        guides_block = ('  <h2>Free guides</h2>\n  <div class="grid">\n'
                        + guide_cards(root, 9) + '\n  </div>\n'
                        + f'  <p><a href="{root}guides/">All guides</a></p>\n\n')
    return head(code, t['title'], t['desc'], path, root, extra=extra) + header(root, code) + f"""
  <section class="hero">
    <div>
      <h1>{e(t['h1'])}</h1>
      <p>{e(t['lead'])}</p>
      {waitlist(t, 'home-' + code)}
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

""" + guides_block + footer(t, root)


# ---- structured data, guides, about, llms.txt -------------------------------

def jsonld(*objs):
    return ''.join('<script type="application/ld+json">'
                   + json.dumps(o, ensure_ascii=False, separators=(',', ':'))
                   + '</script>\n' for o in objs)


def org_ld():
    o = {'@context': 'https://schema.org', '@type': 'Organization',
         '@id': f'{DOMAIN}/#org', 'name': 'Dạ: Learn Vietnamese',
         'alternateName': 'Dạ', 'url': DOMAIN, 'logo': f'{DOMAIN}/og-icon.png',
         'email': CONTACT}
    if PROFILES:
        o['sameAs'] = [u for _, u in PROFILES]
    return o


def website_ld():
    return {'@context': 'https://schema.org', '@type': 'WebSite',
            'url': f'{DOMAIN}/', 'name': 'Dạ: Learn Vietnamese',
            'publisher': {'@id': f'{DOMAIN}/#org'}}


def load_phrases():
    with open('guides_phrases.json', encoding='utf8') as f:
        return json.load(f)


def guide_cards(root, limit=None):
    by_slug = {g['slug']: g for g in GUIDES}
    order = [by_slug[s] for _, ss in GROUPS for s in ss][:limit]
    return '\n'.join(
        f'    <a class="card guide" href="{root}guides/{g["slug"]}/"><h3>{e(g["h1"])}</h3>'
        f'<p>{e(g["desc"])}</p></a>' for g in order)


MODE_NAME = {'kids': 'Kids', 'adult': 'Partner & family', 'everyday': 'Everyday'}
SLUGS = {g['slug'] for g in GUIDES}
LINK = re.compile(r'\[([^\]]+)\]\(([a-z0-9-]+)\)')


def rich(text, root):
    """Escapes text and turns [words](guide-slug) into a link to that guide."""
    def link(m):
        if m.group(2) not in SLUGS:
            raise SystemExit(f'unknown guide link: {m.group(2)}')
        return f'<a href="{root}guides/{m.group(2)}/">{m.group(1)}</a>'
    return LINK.sub(link, e(text))


def phrase_table(spec, phrases):
    h, mode, topic, n = spec[:4]
    opt = spec[4] if len(spec) > 4 else {}
    start = opt.get('start', 0)
    items = phrases[f'{mode}/{topic}'][start:start + n]
    south = opt.get('south') and any('south' in x for x in items)
    head_ = ('<th>Vietnamese</th>' + ('<th>In the South</th>' if south else '')
             + '<th>English</th>')
    rows = ''.join(
        f'<tr><td lang="vi">{e(x["vi"])}</td>'
        + (f'<td lang="vi">{e(x.get("south", "(same)"))}</td>' if south else '')
        + f'<td>{e(x["en"])}</td></tr>' for x in items)
    return (f'    <h3>{e(h)}</h3>\n    <div class="table-wrap"><table class="phrases"><thead><tr>'
            f'{head_}</tr></thead><tbody>{rows}</tbody></table></div>')


def guide_page(g, phrases):
    root = '../../'
    path = f'guides/{g["slug"]}/'
    out = []
    for kind, val in g['body']:
        if kind == 'p':
            out.append(f'    <p>{rich(val, root)}</p>')
        elif kind == 'h2':
            out.append(f'    <h2>{e(val)}</h2>')
        elif kind in ('ul', 'ol'):
            out.append(f'    <{kind}>' + ''.join(f'<li>{rich(x, root)}</li>' for x in val)
                       + f'</{kind}>')
        elif kind == 'table':
            out.append(phrase_table(g['tables'][val], phrases))
    video = ''
    ld = [{'@context': 'https://schema.org', '@type': 'Article',
           'headline': g['title'], 'description': g['desc'],
           'url': f'{DOMAIN}/{path}', 'inLanguage': 'en',
           'datePublished': g['published'], 'dateModified': g['updated'],
           'image': f'{DOMAIN}/og-icon.png',
           'author': {'@id': f'{DOMAIN}/#org'}, 'publisher': {'@id': f'{DOMAIN}/#org'}},
          {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
              {'@type': 'ListItem', 'position': 1, 'name': 'Dạ', 'item': f'{DOMAIN}/'},
              {'@type': 'ListItem', 'position': 2, 'name': 'Guides', 'item': f'{DOMAIN}/guides/'},
              {'@type': 'ListItem', 'position': 3, 'name': g['h1']}]}]
    y = g.get('youtube')
    if y:  # {'id':..., 'title':..., 'upload_date': 'YYYY-MM-DD'}
        video = (f'    <div class="video"><iframe src="https://www.youtube-nocookie.com/embed/{y["id"]}" '
                 f'title="{e(y["title"])}" loading="lazy" allowfullscreen></iframe></div>\n')
        ld.append({'@context': 'https://schema.org', '@type': 'VideoObject',
                   'name': y['title'], 'description': g['desc'],
                   'uploadDate': y['upload_date'],
                   'thumbnailUrl': f'https://i.ytimg.com/vi/{y["id"]}/hqdefault.jpg',
                   'embedUrl': f'https://www.youtube.com/embed/{y["id"]}'})
    by_slug = {x['slug']: x for x in GUIDES}
    related = ''.join(f'<li><a href="{root}guides/{s}/">{e(by_slug[s]["h1"])}</a></li>'
                      for s in g['related'])
    mode = MODE_NAME[g['mode']]
    t = TEXT['en']
    return (head('en', g['title'], g['desc'], path, root, alternates=False,
                 extra=jsonld(*ld), og_type='article')
            + header(root)
            + f'  <article class="doc guide-page">\n'
              f'    <p class="crumbs"><a href="{root}">Dạ</a> / <a href="{root}guides/">Guides</a></p>\n'
              f'    <h1>{e(g["h1"])}</h1>\n{video}'
            + '\n'.join(out)
            + f'\n    <div class="cta"><h2>Hear every phrase</h2><p>All the phrases on this page '
              f'are in the {e(mode)} mode of Dạ, with audio in a Northern or Southern accent. '
              f'Record yourself and compare. 50 topics free in every mode, works offline, no ads.</p>'
              f'{waitlist(t, g["slug"])}'
              f'<div class="badges">{badges(t)}</div></div>\n'
              f'    <h2>Keep reading</h2>\n    <ul>{related}</ul>\n'
              f'    <p class="wl-note">Updated {g["updated"]}. Phrases come straight from the Dạ app. '
              f'<a href="{root}about.html">About Dạ</a></p>\n'
              f'  </article>\n'
            + footer(t, root))


GROUPS = [('Start here', ['learn-vietnamese-for-family', 'learn-vietnamese-app-for-beginners',
                          'heritage-vietnamese-learner']),
          ('Family and kinship', ['say-hello-to-grandma-in-vietnamese', 'vietnamese-family-terms',
                                  'vietnamese-pronouns', 'vietnamese-phrases-for-in-laws',
                                  'meeting-vietnamese-parents', 'learn-vietnamese-for-kids']),
          ('Sounds and accents', ['vietnamese-tones', 'vietnamese-pronunciation-practice',
                                  'northern-vs-southern-vietnamese']),
          ('Family occasions', ['vietnamese-dinner-phrases', 'tet-greetings',
                                'vietnamese-wedding-toast', 'i-love-you-in-vietnamese']),
          ('Travel', ['vietnamese-phrases-for-travel'])]


def guides_index():
    root = '../'
    by_slug = {g['slug']: g for g in GUIDES}
    listed = [s for _, ss in GROUPS for s in ss]
    assert sorted(listed) == sorted(by_slug), 'GROUPS must list every guide once'
    card = lambda g: (f'    <a class="card guide" href="{root}guides/{g["slug"]}/"><h3>{e(g["h1"])}</h3>'
                      f'<p>{e(g["desc"])}</p></a>')
    body = ''.join(f'  <h2>{e(h)}</h2>\n  <div class="grid">\n'
                   + '\n'.join(card(by_slug[s]) for s in ss) + '\n  </div>\n'
                   for h, ss in GROUPS)
    return (head('en', 'Free Vietnamese Guides for Families · Dạ',
                 'Free guides to the Vietnamese families speak: greetings for grandparents, '
                 'family terms, pronouns, tones, accents, in-laws, Tết and meals.', 'guides/', root,
                 alternates=False)
            + header(root)
            + '  <article class="doc wide">\n    <h1>Free guides</h1>\n'
              '    <p>Short, practical guides to the Vietnamese real families speak, '
              'with phrases from the Dạ app.</p>\n  </article>\n'
            + body
            + footer(TEXT['en'], root))


def about_page():
    guides = ''.join(f'<li><a href="guides/{g["slug"]}/">{e(g["h1"])}</a></li>' for g in GUIDES)
    if PROFILES:
        find = '<ul>' + ''.join(f'<li><a href="{u}" rel="me">{e(n)}</a></li>'
                                for n, u in PROFILES) + '</ul>'
    else:
        find = '<p>Our official channels are on the way.</p>'
    body = f"""
  <article class="doc">
    <h1>About Dạ</h1>
    <p>Dạ: Learn Vietnamese is an app for people who want to speak Vietnamese with family: children growing up abroad who want to talk to their grandparents, partners and in-laws of Vietnamese families, and anyone living, working or travelling in Vietnam.</p>
    <p>The name comes from “dạ”, the polite way Vietnamese people answer an elder. It is often the first word a child says to bà and ông, and the first word a new partner says to the family.</p>
    <h2>What we believe</h2>
    <ul>
      <li>Family Vietnamese is different from textbook Vietnamese: the right word for each relative matters more than grammar tables.</li>
      <li>Learners should hear the accent their family speaks, Northern or Southern.</li>
      <li>A learning app for families should not track anyone. Dạ has no accounts, no ads and no analytics.</li>
    </ul>
    <h2>Guides</h2>
    <ul>{guides}</ul>
    <h2>Find us on</h2>
    {find}
    <h2>Contact</h2>
    <p><a href="mailto:{CONTACT}">{CONTACT}</a></p>
  </article>
"""
    return (head('en', 'About Dạ: Learn Vietnamese', 'Who makes Dạ, why, and where to '
                 'find us.', 'about.html', '', alternates=False,
                 extra=jsonld(org_ld()))
            + header('') + body + footer(TEXT['en'], ''))


def llms_txt():
    lines = ['# Dạ: Learn Vietnamese', '',
             '> A mobile app (iOS and Android) for learning the Vietnamese families '
             'speak, with three modes: Kids (heritage children talking to grandparents), '
             'Partner & family (partners and in-laws of Vietnamese families) and Everyday '
             '(travel, work, friends). Audio in Northern and Southern accents, offline, '
             'no ads, no tracking, one-time purchase.', '',
             f'Website: {DOMAIN}/', f'Contact: {CONTACT}', '', '## Guides', '']
    lines += [f'- [{g["title"]}]({DOMAIN}/guides/{g["slug"]}/): {g["desc"]}' for g in GUIDES]
    lines += ['', '## Pages', '',
              f'- [About]({DOMAIN}/about.html)', f'- [Privacy policy]({DOMAIN}/privacy.html)',
              f'- [Support]({DOMAIN}/support.html)']
    if PROFILES:
        lines += ['', '## Official profiles', ''] + [f'- [{n}]({u})' for n, u in PROFILES]
    return '\n'.join(lines) + '\n'


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
    phrases = load_phrases()
    for g in GUIDES:
        write(f'guides/{g["slug"]}/index.html', guide_page(g, phrases))
    write('guides/index.html', guides_index())
    write('about.html', about_page())
    write('llms.txt', llms_txt())
    write('style.css', CSS.lstrip())
    write('CNAME', 'vietnamese-learning.com\n')
    write('.nojekyll', '')
    write('robots.txt', f'User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n')
    latest = max(g['updated'] for g in GUIDES)
    urls = ([(p, SITE_UPDATED) for _, _, p in LANGS] + [('guides/', latest)]
            + [(f'guides/{g["slug"]}/', g['updated']) for g in GUIDES]
            + [('about.html', latest), ('privacy.html', '2026-11-21'),
               ('support.html', '2026-11-21')])
    write('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + ''.join(f'  <url><loc>{DOMAIN}/{u}</loc><lastmod>{d}</lastmod></url>\n'
                    for u, d in urls)
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
