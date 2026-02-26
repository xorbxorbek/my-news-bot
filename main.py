import requests
import feedparser
from datetime import datetime, timedelta

# --- 설정 정보 (나중에 입력) ---
TELEGRAM_TOKEN = "8691397801:AAFJWMPazlZ1yI_T-N5UjetunAuHyrBJp6Q"
CHAT_ID = "7519865650"
KEYWORDS = ["현대로템 ESG", "탄소중립", "환경 규제", "LCA", "탄소발자국", "탄소세", "재생에너지", "넷제"]

def get_google_news(keyword):# 띄어쓰기를 인터넷 주소 형식(%20)으로 변환해줍니다.
    safe_keyword = keyword.replace(" ", "%20")
    rss_url = f"https://news.google.com/rss/search?q={safe_keyword}+when:1d&hl=ko&gl=KR&ceid=KR:ko"
    feed = feedparser.parse(rss_url)
    results = []
    
    for entry in feed.entries:
        # 최근 24시간 이내 기사만 필터링 (필요시 추가 로직)
        results.append(f"📌 {entry.title}\n🔗 {entry.link}")
    
    return results
