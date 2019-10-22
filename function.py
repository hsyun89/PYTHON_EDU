#함수의 종류
#1. 인자 & 리턴 0
# def sum_ex(a,b):
#     result = a+b
#     return result
# print(sum_ex(2,5))
# sum_result = sum_ex(2,5)
# print(sum_result)

# #2. 리턴만
# def say():
#     return 'hi'

#3. 인자만
# def say(name, age):
#     print(f'제 이름은 {name}이고, 나이는 {age}입니다.')
# say('juan',20)

##함수의 인자
## 1. 위치 인자(positional Argument)

#2. 기본값 인자(default argument)
# def greeting(name='juan'):
#     print(f'{name}님 안녕하세요.')

# greeting()
# greeting('bob')

# def my_sum(a,b=2):
#     return a+b
# print(my_sum(2))
# print(my_sum(2,4))
#3. 키워드 인자
# def greeting(age, name='juan'):
#     print(f'{name}은 {age}살 입니다.')

# # greeting(19)
# greeting(name='john',age=33)

# #4. 가변인자
# def my_func(*args):
#     print(args)
#     print(type(args))
#     return args
# my_func(1,2,3)
# my_func([1,2,3])

#5. 정의되지 않은 인자(키워드 인자)
# def my_dict(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
# my_dict(한국어='안녕',영어='hi',독일어='Guten tag')

# my_dict={
#     '서울':'02'
# }
# my_dict2={}
# my_dict2['경기도']='031'

# jumin1='900101-1020201'
# jumin2='910203-2030020'

# def male_female(number):
#     if number[7] == '1':
#         print('남자입니다')
#     else:
#         print('여자입니다')
# male_female(jumin1)
# male_female(jumin2)

#2. 사용자의 입력으로 숫자를 받아서 해당 숫자가 짝수인지 홀수인지 구분하는 함수
# def odd(number):
#     if number%2:
#         print('홀수')
#     else:
#         print('짝수')

# odd(3)
# odd(4)

#리스트 안에서 가장 작은 수
# items = [1,2,-5,0,-100]
# def mini(items):
#     print(min(items))
# mini(items)

# 문자열로만 이루어진 리스트를 인자로 넘겼을 때
# 문자열의 길이가 2 이상이고 주어진 문자열의
# 첫번째와 마지막 문자가 같은 문자열의 수를 세는 함수
# words = ['level','asder','tomato','abdda','s']

# def string_func(words):
#     count=0
#     for word in words:
#         if len(word) >=2:
#             if word[0] == word[-1]:
#                 count+=1
#     print(count)

# string_func(words)

# 네이버에서 환율 뽑기
from bs4 import BeautifulSoup
import requests

url = 'https://finance.naver.com/marketindex/'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
# dollor_won=soup.select('#exchangeList > li.on > a.head.usd > div > span.value')[0].text
dollor_won=soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text
print(dollor_won)