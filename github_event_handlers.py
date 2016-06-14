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
    git_url = data['pull_request']['head']['repo']['ssh_url']
    fullname = data['pull_request']['head']['repo']['full_name']
    branch = data['pull_request']['head']['ref']
    params = {'user':user, 'repo':repo, 'sha':ref, 'git_url':git_url, 'repo_fullname':fullname, 'branch':branch}

    line = factory.make_pipeline([{'check_style':params}])
    line.run()

handler.set_handler('pull_request.opened', pr_open)
