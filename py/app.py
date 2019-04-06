import time

from flask import Flask

app = Flask(__name__)


@app.route('/')
def root():
    return '[py] Hello World'


@app.route('/sleep/')
def sleep():
    time.sleep(1)
    return '[py] Slept for 1 second'


@app.route('/cpu/')
def cpu():
    result = 1
    for i in range(10000000):
        result += i / result
    return f'[py] Result: {result}'


if __name__ == "main":
    app.run()
