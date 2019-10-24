import requests
#string interpolation
#문자열에 변수 값 넣기
currency='BTC'
url=f'https://api.bithumb.com/public/ticker/{currency}'
print(url)
#요청결과 json -> dictionary 자료구조로 변환(딕셔너리 = 해시)
response=requests.get(url).json()
print(response['data']['opening_price'])
print(response.get('data').get('opening_price'))