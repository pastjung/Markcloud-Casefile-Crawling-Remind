import find_path

from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

URL = os.getenv('URL')
BASE_URL = os.getenv('BASE_URL')
POST_API = os.getenv('POST_API')

urls='case-file-path.txt'

if __name__ == "__main__":
    # 지정된 URL에서 크롤링할 URL 목록 저장
    find_path.url_crawling(urls, POST_API)