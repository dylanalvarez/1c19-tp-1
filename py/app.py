import time

from flask import Flask

app = Flask(__name__)


@app.route('/')
def ping():
    return 'Hello, World!'


@app.route('/sleep/')
def timeout():
    time.sleep(1)
    return 'Slept for 1 second'


@app.route('/cpu/')
def cpu():
    result = 1
    for i in range(10000000):
        result += i / result
    return f'Result: {result}'


if __name__ == "main":
    app.run()
