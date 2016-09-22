#-*- coding:utf-8 -*-
import sys
sys.path.append('..')
from github import events, statuses
from pipeline import Factory, tasks
from multiprocessing import Process

handler = events.EventHandler()

factory = Factory()
# factory.regist_task('test', tasks.Test)
factory.regist_task('check_style', tasks.CheckStyle)
def get_handler():
    return handler

def pr_open(data):
    print "action: pull_request." + data['action']
    user = data['repository']['owner']['login']
    repo = data['repository']['name']
    ref = data['pull_request']['head']['sha']
    git_url = data['pull_request']['head']['repo']['ssh_url']
    fullname = data['pull_request']['head']['repo']['full_name']
    branch = data['pull_request']['head']['ref']
    pr_number = data['number']
    params = {'user':user, 'repo':repo, 'sha':ref, 'git_url':git_url, 'repo_fullname':fullname, 'branch':branch, 'pr_number':pr_number}

    line = factory.make_pipeline([{'check_style':params}])
    line.run()

handler.set_handler('pull_request.opened', pr_open)
handler.set_handler('pull_request.reopened', pr_open)
handler.set_handler('pull_request.synchronize', pr_open)
handler.set_handler('pull_request.edited', pr_open)
