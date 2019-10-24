# pip install flask
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Happy Hacking!'

@app.route('/lotto')
def lotto():
    import random
    numbers = range(1,46)
    print(list(numbers))
    lotto = random.sample(numbers,6)
    print(sorted(lotto))
    return str(sorted(lotto))
# ctrl + c로 서버종료
# $ flask run