#-*- coding:utf-8 -*-
from flask import Flask, request, abort
import os
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
@app.route('/diff/tmp/<user>/<repo>/<branch>/<filename>')
@app.route('/diff/<user>/<repo>/<branch>/<filename>')
def get_diff(user, repo, branch, filename):
    diff_file = '/tmp/' + user + '/' + repo + '/' + branch + '/' + filename
    if (os.path.exists(diff_file)):
        f = open(diff_file, 'r')
        diff_data = f.read()
        return diff_data
    else:
        abort(404)
def get_web_app():
    return app

def set_data_queue(queue):
    print "setting data queue"
    print queue
    global data_queue
    data_queue = queue

if __name__=='__main__':
    app.run(host='0.0.0.0', port=80)
