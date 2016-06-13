#-*- coding:utf-8 -*-
from flask import Flask, request
import github_event_handlers

app = Flask(__name__)
handler = github_event_handlers.get_handler()

print handler;
@app.route('/')
def index():
    return "hello world!"

@app.route('/api/webhook', methods=['POST', 'GET'])
def webhook():
    handler.handle(request.data)
    return "hello world!"

if __name__=='__main__':
    app.run(host='0.0.0.0', port=80)
