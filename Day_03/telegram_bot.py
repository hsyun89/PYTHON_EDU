from flask import Flask, render_template, request
import requests
from decouple import config
from pprint import pprint as pp
app=Flask(__name__)

base="https://api.telegram.org"
token = config('TOKEN')

@app.route('/')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    method = 'getUpdates'

    url = f'{base}/bot{token}/{method}'
    res = requests.get(url).json()
    #pp(res)
    # 받아온 응답(json)을 dictionary로 바꿔 첫번째 메세지의 chat_id를 가져온다.
    chat_id = res['result'][0]['message']['chat']['id']

    method = 'sendMessage'
    text = request.args.get('msg')
    url = f'{base}/bot{token}/{method}?chat_id={chat_id}&text={text}'

    requests.get(url)
    return '전송완료'

@app.route(f'/{token}',methods=['POST'])
def webhook():
    #1. webhook을 통해 telegram에 보낸 요청 안에 있는 메시지를 가져와서
    url = f'{base}/bot{token}/setWebhook?url=https://664fb30a.ngrok.io/{token}'
    #
    requests.get(url)
    #2. 그대로 전송
    res = request.get_json()

    if res.get('message'):
        text=res.get('message').get('text')
        if '/로또' in text:
            import random
            text = sorted(random.sample(range(1,45),6))
        elif '/비트코인' in text:
            currency='BTC'
            url=f'https://api.bithumb.com/public/ticker/{currency}'
            response=requests.get(url).json()
            text=response.get('data').get('opening_price')
        elif '/번역 ' == text[0:4]:
            naver_client_id=config('NAVER_CLIENT_ID')
            naver_client_secret = config('NAVER_CLIENT_SECRET')
            url='https://openapi.naver.com/v1/papago/n2mt'
            headers={
                'X-Naver-Client-Id': naver_client_id,
                'X-Naver-Client-Secret': naver_client_secret
            }
            data ={
                'source' : 'ko',
                'target' : 'en',
                'text' : text[4:]
            }
            response=requests.post(url,data=data, headers=headers).json()
            text=response.get('message').get('result').get('translatedText')

        chat_id = res.get('message').get('chat').get('id')
        method = 'sendMessage'
        url = f'{base}/bot{token}/{method}?chat_id={chat_id}&text={text}'
        requests.get(url)
    return '',200
