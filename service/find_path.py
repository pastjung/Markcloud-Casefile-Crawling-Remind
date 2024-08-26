import aiohttp
import aiofiles


async def fetch(session, url, payload):
    async with session.post(url, json=payload) as response:
        response_json = await response.json()
        return response_json

async def url_crawling(urls : str, POST_API: str):
    # 페이지네이션 변수 설정
    page_size = 500 # 한 페이지에서 가져올 항목 수
    start_index = 0 # 검색 결과의 시작 위치
        
    all_case_files = [] # 크롤링한 case-file를 저장
    
    # User-Agent 설정
    headers = {
        'User-Agent' : 'MyApp/1.0 (contact@example.com)'
    }
    
    async with aiohttp.ClientSession() as session:
        while True:
            # 페이로드 정의
            payload = {
                "query": {
                    "bool": {
                        "must": []
                    }
                },
                "_source": {
                    # case_no와 court 필드만 가져옴
                    "includes": ["case_no", "court"],
                    "excludes": ["created_at", "updated_at", "id", "*.created_at", "*.updated_at", "*.id", "patent_id", "patent.abstract", "patent.title", "*.full_text", "dockets"]
                },
                "size": page_size,
                "from": start_index,
                "sort": [{"case_no": "asc"}],
                "track_total_hits": True
            }
            
            # headers를 포함시킨 요청
            async with session.post(POST_API, json=payload, headers=headers) as response:
                response_json = await response.json()
                case_files = response_json.get('hits', {}).get('hits', [])

            # 만약 데이터가 없을 경우 종료
            if not case_files:
                break

            formatted_case_files = [
                f"/{case['_source']['court']}/case/{case['_source']['case_no']}"
                for case in case_files
                if '_source' in case and 'case_no' in case['_source'] and 'court' in case['_source']
            ]

            all_case_files.extend(formatted_case_files)

            # 크롤링한 case-file을 urls에 저장
            async with aiofiles.open(urls, 'a', encoding='utf-8') as file:
                for url in formatted_case_files:
                    await file.write(url + '\n')

            print(f"start_index: {start_index}, end_index: {len(all_case_files) - 1}")

            # 다음 페이지를 요청하기 위해 start_index 값 증가
            start_index += page_size   
                
    print("Data has been written to .txt file")