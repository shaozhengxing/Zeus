#-*- coding:utf-8 -*-
import sys
sys.path.append('../..')
from base import BaseTask
from github import statuses
import time

class CheckStyle(BaseTask):
    def do_task(self) :
        self.change_status('pending', '正在进行编码格式检查...')
        for i in range(1, 30):
            print 'sleep'
            time.sleep(1)
        self.change_status('success', '编码格式检查通过')


    def change_status(self, status, description):
        user = self.params['user']
        repo = self.params['repo']
        ref = self.params['sha']
        print statuses.create(user, repo, ref, 'style check', status, 'http://jswh.me', description)

    def 
