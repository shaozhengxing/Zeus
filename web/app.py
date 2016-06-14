#-*- coding:utf-8 -*-
from flask import Flask, request

app = Flask(__name__)
data_queue = None

@app.route('/')
def index():
    return "hello world!"

@app.route('/api/webhook', methods=['POST', 'GET'])
def webhook():
    if (data_queue):
        data_queue.put({'type':'webhook', 'data':request.data})
    else:
        print data_queue
    return "hello world!"

def get_web_app():
    return app

def set_data_queue(queue):
    print "setting data queue"
    print queue
    global data_queue
    data_queue = queue

if __name__=='__main__':
    app.run(host='0.0.0.0', port=80)
