from django.shortcuts import render, HttpResponse
import random
import requests
from bs4 import BeautifulSoup

def index(request):
    # return HttpResponse('welcome')
    return render(request, 'index.html')

def hola(request):
    # return HttpResponse('hello, my name is hyunsu')
    return render(request, 'hola.html')

def dinner(request):
    menus = ['피자','치킨','족발','라면']
    dinner = random.choice(menus)
    # return HttpResponse(f'오늘의 저녁메뉴는 {dinner}입니다.')
    return render(request, 'dinner.html', {'menus':menus,'dinner':dinner})

def lotto(request):
    numbers=range(1,46)
    my_lotto = random.sample(numbers,6)
    # return HttpResponse(f'오늘의 로또 추천번호는{my_lotto}입니다')
    # url = 'https://www.dhlottery.co.kr/gameResult.do?method=byWin&drwNo=882'
    # html = requests.get(url).text
    # soup = BeautifulSoup(html,'html.parser')
    # selector = '#article > div:nth-child(2) > div > div.win_result > div > div.num.win > p'
    # # print(soup.select(selector))
    # lotto_882 = soup.select(selector)[0].text.strip()
    # list_lotto = lotto_882.split()
    # list_lotto = list(map(int, list_lotto))
    # set1 = set(my_lotto)
    # set2 = set(list_lotto)
    # result = set1 & set2
    # my_result = len(result)
    # cnt = 1
    # while my_result < 6:
    #     my_lotto = random.sample(numbers,6)
    #     set1 = set(my_lotto)
    #     set2 = set(list_lotto)
    #     result = set1 & set2
    #     my_result = len(result)
    #     cnt+=1
    # print(f'반복횟수는{cnt}')
    # return render(request, 'lotto.html', {'cnt':cnt})
# #################################################################
    url = 'https://dhlottery.co.kr/common.do?method=main'
    res = requests.get(url)
    data = res.json()

    winner = []
    for i in range(1,7):
        winner.append(data[f'drwtNo{i}'])

    match = set(my_lotto) & set(winner)
    rank = len(match)
    cnt= 0

    while rank < 5:
        cnt += 1
        my_lotto = random.sample(range(1,46),6)
        match = set(my_lotto) & set(winner)
        rank = len(match)
    return render(request, 'lotto.html',{'cnt':cnt, 'winner':winner,'my_lotto':my_lotto})


def hello(request, name):
    return render(request, 'hello.html',{'name':name})

def introduce(request, name, age):
    return render(request, 'introduce.html',{'name':name,'age':age})

def square(request, x, y):
    result = int(x)*int(y)
    return render(request, 'square.html',{'x':x,'y':y,'result':result})