from flask import Flask, render_template, request
import random
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"

@app.route('/sparta')
def sparta():
    return "This is sparta"

@app.route("/greeting/<string:name>")
def greeting(name):
    return f'반갑습니다! {name}님'

@app.route('/cube/<int:num>')
def cube(num):
    result = num**3 # num*num*num
    return f'{num}의 세제곱은 {result}입니다.'

@app.route('/dinner/<int:person>')
def dinner(person):
    menu = ['짜장면','짬뽕','볶음밥','고추잡채밥','탕수육']
    order = random.sample(menu, k=person)
    return str(order)

@app.route('/lotto')
def lotto():
    lottoNum = random.sample(range(1,46),6)
    return str(lottoNum)

@app.route("/html")
def html():
    return "<h1> This is HTML h1 tag! </h1>"

@app.route("/d_day")
def d_day():
    # import에 from datetime 붙이면
    # today = datetime.datetime.now()
    today = datetime.datetime.now()
    # finish = datetime.datetime(2019,11,27)
    finish = datetime.datetime(2019,11,27)

    remain = finish - today
    return f'우리가 같이 있을 수 있는 시간이 이제 {remain}일 밖에 남지 않았어!'

@app.route("/naver")
def naver():
    return render_template("naver.html")

@app.route("/google")
def google():
    return render_template("google.html")

@app.route('/myday')
def myday():
    today = datetime.now()
    return render_template('myday.html', today=today)

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    name = request.args.get('name')
    age = request.args.get('age')
    return render_template('pong.html', name=name, age=age)

@app.route('/god')
def god():
    return render_template('god.html')

@app.route('/godpong')
def godpong():
    name = request.args.get('name')
    stats = ['귀여움','섹시함','진지함','잘생김','질투심','학점','재력']
    size = ['많이', '적당히', '조금']
    return render_template('godpong.html', name=name, stats=random.sample(stats,3), size=random.sample(size,3))