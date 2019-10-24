#0. 요청을 보내는 라이브러리 
import requests
from bs4 import BeautifulSoup
#1. url로 요청을 보낸다.
url = 'https://finance.naver.com/sise/'
response=requests.get(url)
#print(response.text)
#2. 받은 문서에서 검색한다.
#2.1. string -> HTML 구조로 변환 (bs4 - BeautifulSoup)
soup=BeautifulSoup(response.text,'html.parser')
#print(soup)
#2.2. Selector를 통해서 문서내 탐색
kospi=soup.select_one('#KOSPI_now')
#2.3. 내용 출력
print(kospi.text)