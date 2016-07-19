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
    if (data_queue and request.data):
        data_queue.put({'type':'webhook', 'data':request.data})
    else:
        print data_queue
    return "hello world!"
@app.route('/diff/tmp/<user>/<repo>/<branch>/<filename>')
@app.route('/diff/<user>/<repo>/<branch>/<filename>')
def get_diff(user, repo, branch, filename):
    diff_file = '/tmp/' + user + '/' + repo + '/' + branch + '/' + filename
    color = {'-':'red', '+':'#05dc05'}
    if (os.path.exists(diff_file)):
        f = open(diff_file, 'r')
        diff_data = ''
        for line in f:
            if (line[0] == '-' or line[0] == '+'):
                diff_data = diff_data + '<pre style="color:' + color[line[0]] + '">' + line.replace(" ", '.') + '</pre>'
            else:
                diff_data = diff_data + '<pre style="color:#aaa">' + line.replace(" ", '.') + '</pre>'
        f.close()
        return '<html><head><title>diff</title></head><body>' + diff_data + '</body></html>'
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
