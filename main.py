import requests
import feedparser
from datetime import datetime, timedelta

# --- 설정 정보 (나중에 입력) ---
TELEGRAM_TOKEN = "8691397801:AAFJWMPazlZ1yI_T-N5UjetunAuHyrBJp6Q"
CHAT_ID = "7519865650"
KEYWORDS = ["현대로템 ESG", "탄소중립", "환경 규제", "LCA", "탄소발자국", "탄소세", "재생에너지", "넷제"]

def get_google_news(keyword):
    rss_url = f"https://news.google.com/rss/search?q={keyword}+when:1d&hl=ko&gl=KR&ceid=KR:ko"
    feed = feedparser.parse(rss_url)
    results = []
    
    for entry in feed.entries:
        # 최근 24시간 이내 기사만 필터링 (필요시 추가 로직)
        results.append(f"📌 {entry.title}\n🔗 {entry.link}")
    
    return results

def send_telegram_msg(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    params = {"chat_id": CHAT_ID, "text": text}
    requests.get(url, params=params)

# 실행부
for kw in KEYWORDS:
    news_list = get_google_news(kw)
    if news_list:
        send_telegram_msg(f"--- [{kw}] 뉴스 브리핑 ---")
        for news in news_list[:3]: # 키워드당 상위 3개만
            send_telegram_msg(news)
