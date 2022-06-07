# 웹서버 프로그램 웹 브라우저에서 http://localhost:5000/로 접속하면 
# index.html을 실행하고 버튼을 이용하여 LED 작동시킴

import random
from flask import Flask, request
from flask import render_template
import RPi.GPIO as GPIO

import threading

app = Flask(__name__)

sum = 0

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/random/on")                       # index.html에서 이 주소를 접속하여 해당 함수를 실행
def random_on():
    global sum
    try:
        num = random.randint(1, 5000)
        sum += num
        return render_template('index.html', num=num)
         # 함수가 'ok'문자열을 반환함
    except :
        return "fail"


if __name__ == "__main__":
    app.run(host="0.0.0.0")