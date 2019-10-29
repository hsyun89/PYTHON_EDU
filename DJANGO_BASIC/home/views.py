from django.shortcuts import render, HttpResponse
import random
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def index(request):
    # return HttpResponse('welcome')
    return render(request, 'home/index.html')

def hola(request):
    # return HttpResponse('hello, my name is hyunsu')
    return render(request, 'home/hola.html')

def dinner(request):
    menus = ['피자','치킨','족발','라면']
    dinner = random.choice(menus)
    # return HttpResponse(f'오늘의 저녁메뉴는 {dinner}입니다.')
    return render(request, 'home/dinner.html', {'menus':menus,'dinner':dinner})

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
    # return render(request, 'home/lotto.html', {'cnt':cnt})
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
    return render(request, 'home/lotto.html',{'cnt':cnt, 'winner':winner,'my_lotto':my_lotto})


def hello(request, name):
    return render(request, 'home/hello.html',{'name':name})

def introduce(request, name, age):
    return render(request, 'home/introduce.html',{'name':name,'age':age})

def square(request, x, y):
    result = int(x)*int(y)
    return render(request, 'home/square.html',{'x':x,'y':y,'result':result})

def template_language(request):
    menus = ['아메리카노','카페라떼','마끼아또','루이보스', '프라푸치노']
    cafes = ['starbucks','coffeebean','hollys','eduya']
    my_sentence = 'Life is short, you need Python'
    datetimenow = datetime.now()
    empty_list=[]
    context = {
        'menus':menus,
        'cafes':cafes,
        'my_sentence':my_sentence,
        'empty_list':empty_list,
        'datetimenow':datetimenow,
    }
    return render(request,'home/template_language.html',context)

def image(request):
    return render(request, 'home/image.html')

def isbirth(request):
    today = datetime.now()
    if today.month == 6 and today.day == 27:
        result = True
    else:
        result=False
    return render(request, 'home/isbirth.html',{'result':result})

def ispal(request, word):
    # if word == ''.join(reversed(word)):
    if word == word[::-1]:
        result = True
    else:
        result = False
    return render(request, 'home/ispal.html',{'result':result,'word':word})

# GET / POST

def throw(request):
    return render(request,'home/throw.html')

def catch(request):
    message = request.GET.get('message')
    message2 = request.GET.get('message2')
    return render(request,'home/catch.html',{'message':message,'message2':message2})

def user_new(request):
    return render(request,'home/user_new.html')

def user_create(request):
    user_name = request.POST.get('name')
    user_password = request.POST.get('pwd')
    return render(request,'home/user_create.html',{'user_name':user_name,'user_password':user_password})

def static_example(request):
    return render(request,'home/static_example.html')

