#-*- coding:utf-8 -*-
import sys
sys.path.append('..')
from github import events, statuses
from pipeline import Factory, tasks
from multiprocessing import Process
user = 'jswh'
repo = 'OrosOlymPos'

handler = events.EventHandler()

factory = Factory()
factory.regist_task('test', tasks.Test)
factory.regist_task('check_style', tasks.CheckStyle)
def get_handler():
    return handler

def pr_open(data):
    ref = data['pull_request']['head']['sha']
    params = {'user':user, 'repo':repo, 'sha':ref}
    line = factory.make_pipeline([{'check_style':params}])
    p = Process(target=line.run)
    p.start()
    p.join()

handler.set_handler('pull_request.opened', pr_open)
