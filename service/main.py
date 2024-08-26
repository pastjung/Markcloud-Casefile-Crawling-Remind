import find_path
import crawling
from dotenv import load_dotenv
import os
import asyncio

# .env 파일 로드
load_dotenv()

URL = os.getenv('URL')
BASE_URL = os.getenv('BASE_URL')
POST_API = os.getenv('POST_API')

urls = 'case-file-path.txt'
csv_file = 'case-file.csv'

if __name__ == "__main__":
    # 지정된 URL에서 크롤링할 URL 목록 저장
    asyncio.run(find_path.url_crawling(urls, POST_API))
    
    # 저장한 URL을 통해 case-file을 CSV 파일에 저장
    crawling.make_csv_from_url(urls, BASE_URL, csv_file)