from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import csv
import os

def read_urls(urls: str, BASE_URL: str):
    file_paths = []
    
    try:
        with open(urls, 'r', encoding='utf-8') as files:
            for file in files:
                file_paths.append(BASE_URL + file.strip())
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    
    return file_paths

def write_csv_file_from_txt(file_paths: str, BASE_URL: str, csv_file_name: str):    
    # CSV 파일에 데이터 저장
    for file_path in file_paths:
        # 파일 이름 가져오기
        file_name = file_path.split('/')[-1]
    
        # URL로부터 데이터 크롤링
        data = get_data(file_path)
        
        if data is not None:
            # 크롤링한 데이터 csv 파일에 저장
            write_csv(data, csv_file_name)
            print(f"{file_name}: Text has been written to case-file.csv")
        else:
            print(f"{file_name}: None Data")
        
    print("All Text has been written to case-file.csv")


def get_data(file_path: str):
    # Chrome 드라이버 옵션 설정
    chrome_options = Options()
    chrome_options.add_argument("--headless")               # 헤드리스 모드 : 크롬 창 숨기는 옵션
    chrome_options.add_argument("--no-sandbox")             # 샌드박스 기능 비활성화 : 브라우저의 프로세스를 격리 
    chrome_options.add_argument("--disable-dev-shm-usage")  # dev/shm ( 리눅스의 공유 메모리 파일 시스템을 제공하는 디렉토리 ) 디렉토리 사용 X -> 디스크 기반의 임시 파일 시스템 사용
    
    try:
        # 웹 드라이버 설정
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(file_path)
        
        # 페이지가 로드될 때까지 대기
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div/main/div/div/div/div[1]/div[2]/div/div[1]/div[1]/div[1]/h4'))
        )

        # 태그 경로
        detail_data_path = '//*[@id="root"]/div/div[2]/div/main/div/div/div/div[1]/div[2]/div/div[1]'
        dockets_text_path = '//*[@id="root"]/div/div[2]/div/main/div/div/div/div[2]/div[2]/div/div/div/div/div/div/table/tbody'
        
        # 태그 데이터 찾기
        detail_data = driver.find_element(By.XPATH, detail_data_path)
        
        # 텍스트 추출
        detail_data_text = detail_data.text.strip()
            
        # 텍스트를 줄 단위로 나누기
        lines = detail_data_text.split('\n')
        
        # 마지막 두 줄 제거 : 필요 없는 데이터
        lines = lines[:-2]
        
        # Dockets 찾기
        dockets_data = driver.find_element(By.XPATH, dockets_text_path)
        
        # Dockets의 Text 데이터 추출
        dockets_text = dockets_data.text.strip()
        dockets = [dockets_text]
        lines.append(dockets)
        lines.append(dockets)

        # 필요한 데이터만 추출
        data = [lines[i] for i in range(1, len(lines), 2)]
        driver.quit()
        return data

    except Exception as e:
        print("An error occurred:", e)
    
def write_csv(data: list, csv_file_name: str):
    # 파일이 존재하는지 확인
    file_exists = os.path.isfile(csv_file_name)

    # CSV 파일 생성
    with open(csv_file_name, 'a', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
            
        # 첫 번째 행: 헤더 추가
        if not file_exists:
            header = [
                "Case Number", "Current Status", "Cause of Action", "Related Case(s)",
                "Plaintiff(s)", "Defendant(s)", "Court", "Judge",
                "Filing Date", "Termination Date", "Text"
            ]
            csv_writer.writerow(header)
        
        # 두번째 행부터 데이터 추가
        csv_writer.writerow(data)
    
def make_csv_from_url(urls: str, BASE_URL: str, csv_file: str):
    # txt 파일에서 URL을 불러와 리스트에 저장
    file_paths = read_urls(urls, BASE_URL)
    
    # 리스트에 저장된 URL의 데이터를 크롤링하여 csv 파일에 저장
    write_csv_file_from_txt(file_paths, BASE_URL, csv_file)