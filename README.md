# case-file Crawling

> Initial written at August 24, 2024 <br/>
> last updated at: August 24, 2024

## Current: ver. 1.0.0<br/>

> - case-file 크롤링 후 .csv 파일로 저장 & case-file-path.txt를 통해 진행도 확인 가능

# 1. 프로그램 (프로젝트) 설명

- 본 프로젝트는 웹 페이지에 존재하는 모든 case-file 페이지의 데이터를 크롤링하여 하나의 csv 파일에 저장하는 프로젝트 입니다

# 2. Prerequisite

- 본 프로젝트는 Chromedriver를 사용합니다 ( 최신버전은 Selenium에 Chromedriver가 포함되었지만 구번전의 경우 다운로드가 필요하니 버전에 주의해주세요 ) 
- 본 프로젝트는 Linux OS 환경을 기반으로 동작하는 것을 가정합니다.
    - 따라서 `dockerfile`의 python과 venv 가상환경, selenium, chrome을 모두 Linux 기반으로 설정되어 있습니다.
    - Linux 환경이 아닌 window같은 환경일 경우 특히 chrome, venv가 Linux 환경인지 확인해주세요

# 3. 구동 방법

- `(sudo) docker compose up (--build)` 명령어를 통해서 실행 가능합니다.

- 만약 window에서 동작을 확인해보고 싶다면 아래 순서를 확인해주세요
    1. window용 가상환경 생성 : `python -m venv venv` 
    2. window용 가상환경 실행 : `. venv/Scripts/activate` 
    3. 필요한 라이브러리 설치 : `pip install -r requirements.txt`
    4. 프로젝트 실행 : `python service/main.py`

# 4. 참고 문서