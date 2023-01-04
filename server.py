# -*- coding:utf-8 -*-
import flask
from flask_cors import CORS
import socket
import _thread
import openai
import json


def accept(connection, address):
    # print(address)

    http_buf = connection.recv(0x1000)
    print(http_buf)

    connection.send(b'HTTP/1.1 200 OK\r\nServer:Apache\r\n\r\nhellowolrd!')

    connection.close()


def worker():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 1001))
    sock.listen(5)
    while True:
        connection, address = sock.accept()
        _thread.start_new_thread(accept, (connection, address))


app = flask.Flask(__name__)
CORS(app)

# http://127.0.0.1:1000/get_data


@app.route('/get_data')
def get_data():
    json_data = {
        "data1": [48, 57, 55, 80, 67, 67, 29, 19, 20, 15, 5, 11, 3, 100, 190],
        "data2": [1, 57, 55, 300, 67, 67, 29, 19, 20, 15, 5, 11, 3, 10, 190]
    }
    return json_data


@app.route('/')
def root_html():
    return flask.render_template('main.html')


@app.route('/test', methods=["post"])
def test():
    # 请求头
    print(flask.request.headers)

    question = flask.request.form.get('send')
    # print(flask.request.form.get('send'))

    # print(len(question))
    if len(question) == 0:
        return "请输入问题"

    openai.api_key = "your key"

    print('问题 {}'.format(question))
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=question,
        temperature=1,
        max_tokens=2000,
    )
    js = json.loads(str(response))
    text = str(js['choices'][0]['text'])
    text.strip()
    print(text)
    return text

@app.route('/main.css')
def css():
    return flask.render_template('main.css')


@app.route('/main.js')
def js():
    return flask.render_template('main.js')


# 后端ip
host_ip = "127.0.0.1"
# 端口号
host_port = 1000

# _thread.start_new_thread(worker,())

app.run(host=host_ip, port=host_port)
