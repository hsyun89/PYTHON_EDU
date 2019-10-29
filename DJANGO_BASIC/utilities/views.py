from django.shortcuts import render
from decouple import config
# import os
# import sys
# import urllib.request
import requests

def index(request):
    return render(request,'utilities/index.html')

# def translate(request, message):
#     # client_id=config('NAVER_CLIENT_ID')
#     # client_secret = config('NAVER_CLIENT_SECRET')
#     # encText = urllib.parse.quote(message)
#     # data = "source=ko&target=en&text=" + encText
#     # url = "https://openapi.naver.com/v1/papago/n2mt"
#     # request = urllib.request.Request(url)
#     # request.add_header("X-Naver-Client-Id",client_id)
#     # request.add_header("X-Naver-Client-Secret",client_secret)
#     # response = urllib.request.urlopen(request, data=data.encode("utf-8"))
#     # rescode = response.getcode()
#     # if(rescode==200):
#     #     response_body = response.read()
#     #     print(response_body.decode('utf-8'))
#     # else:
#     #     print("Error Code:" + rescode)
#             naver_client_id=config('NAVER_CLIENT_ID')
#             naver_client_secret = config('NAVER_CLIENT_SECRET')
#             url='https://openapi.naver.com/v1/papago/n2mt'
#             headers={
#                 'X-Naver-Client-Id': naver_client_id,
#                 'X-Naver-Client-Secret': naver_client_secret
#             }
#             response=requests.post(url,headers=headers).json()
#             text=response.get('message').get('result').get('translatedText')
#             print(text)
#     return render(request,'utilities/translate.html')

def papago(request):
        return render(request,'utilities/papago.html')

def translated(request):
    # 1. 사용자가 입력한 번역을 하고싶은 한국어 텍스트
    korean = request.GET.get('text')

    # 2. 네이버에(POST)번역 요청을 위해서 필요한
    naver_client_id = config('NAVER_CLIENT_ID')
    naver_client_secret = config('NAVER_CLIENT_SECRET')

    # 3.요청을 보낼 url
    papago_url='https://openapi.naver.com/v1/papago/n2mt'

    # 4.헤더정보구성
    headers = {
        'X-Naver-Client-Id': naver_client_id,
        'X-Naver-Client-Secret': naver_client_secret,
    }
    # 5. 우리가 요청할 데이터   
    data={
        "source":"ko",
        "target":"en",
        "text":korean,
    }
    # 6. 네이버로 요청보내기
    papago_response = requests.post(
        papago_url, headers=headers, data=data
    ).json() # .json()을 통해서 요청의 결과를 dict로 변환한다.

    # 7. 응답 결과
    english = papago_response['message']['result']['translatedText']

    context = {'korean':korean,'english':english}
    return render(request,'utilities/translated.html',context)