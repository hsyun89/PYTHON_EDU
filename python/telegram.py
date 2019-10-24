import requests
#url
token='909866102:AAFrFgNXrVLzFhsQVxWFzGG0YMNuA3ySLEU'
base_url=f'https://api.telegram.org/bot{token}'
#요청 내용
chat_id=803482390
text='안녕하세요?'
url=f'{base_url}/sendMessage?chat_id={chat_id}&text={text}'
#요청 보내기
requests.get(url)