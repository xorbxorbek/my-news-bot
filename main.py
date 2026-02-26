import requests
import feedparser
from datetime import datetime, timedelta

# --- 설정 정보 ---
TELEGRAM_TOKEN = "8691397801:AAFJWMPazlZ1yI_T-N5UjetunAuHyrBJp6Q"
CHAT_ID = "7519865650"
KEYWORDS = ["현대로템 ESG", "탄소중립", "환경 규제", "LCA", "탄소발자국", "탄소세", "재생에너지", "넷제로"] # '넷제' 오타를 '넷제로'로 임의 수정했습니다.

def get_google_news(keyword):
    # 띄어쓰기를 인터넷 주소 형식(%20)으로 변환해줍니다.
    safe_keyword = keyword.replace(" ", "%20")
    rss_url = f"https://news.google.com/rss/search?q={safe_keyword}+when:1d&hl=ko&gl=KR&ceid=KR:ko"
    feed = feedparser.parse(rss_url)
    results = []
    
    for entry in feed.entries:
        # 최근 24시간 이내 기사만 필터링
        results.append(f"📌 {entry.title}\n🔗 {entry.link}")
    
    return results

# --- 1. 추가된 부분: 텔레그램 메시지 전송 함수 ---
def send_telegram_msg(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    # 텔레그램 서버로 요청 보내기
    requests.post(url, data=payload)

# --- 2. 추가된 부분: 실제 실행 로직 ---
if __name__ == "__main__":
    for keyword in KEYWORDS:
        news_list = get_google_news(keyword)
        
        # 해당 키워드의 뉴스가 있을 경우에만 전송
        if news_list:
            # 기사가 너무 많으면 텔레그램 메시지가 잘리거나 도배될 수 있으므로
            # 상위 3개만 묶어서 전송하도록 설정했습니다. (필요시 수정 가능)
            message_text = f"[{keyword}] 관련 최신 뉴스입니다.\n\n" + "\n\n".join(news_list[:3])
            send_telegram_msg(message_text)
            print(f"[{keyword}] 뉴스 전송 완료!")
        else:
            print(f"[{keyword}] 관련 새로운 기사가 없습니다.")
