# case-file Crawling

> Initial written at August 24, 2024 <br/>
> last updated at: August 24, 2024

## Current: ver. 1.0.0<br/>

> - case-file 크롤링 후 .csv 파일로 저장 & case-file-path.txt를 통해 진행도 확인 가능

# 1. 프로그램 (프로젝트) 설명

- 본 프로젝트는 웹 페이지에 존재하는 모든 case-file 페이지의 데이터를 크롤링하여 하나의 csv 파일에 저장하는 프로젝트 입니다

# 2. Prerequisite

- 본 프로젝트는 Chromedriver를 사용합니다 ( 최신버전은 Selenium에 Chromedriver가 포함되었지만 구번전의 경우 다운로드가 필요하니 버전에 주의해주세요 ) 

# 3. 구동 방법

- `(sudo) docker compose up (--build)` 명령어를 통해서 실행 가능합니다.

# 4. 참고 문서