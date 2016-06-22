#-*- coding:utf-8 -*-
import sys
sys.path.append('../..')
from base import BaseTask
from github import statuses,pull_request
import time,os,subprocess,re

class CheckStyle(BaseTask):
    work_dir = '/home/work'
    user_dir = None
    repo_dir = None
    diff_log = None
    def do_task(self) :
        self.change_status('pending', '正在进行编码格式检查...', None)
        diff_file = self.get_diff()
        print "diffed"
        if (diff_file == False or os.path.getsize(diff_file) == 0):
            print 'diff success'
            self.change_status('success', '编码格式检查通过', None)
        else:
            print 'diff failure'
            self.change_status('failure', '编码格式检查失败', 'http://hk.jswh.me/diff' + diff_file )


    def change_status(self, status, description, link):
        print link
        user = self.params['user']
        repo = self.params['repo']
        ref = self.params['sha']
        statuses.create(user, repo, ref, 'style check', status, link, description)

    def get_diff(self):
        self.init_repo()
        diff_file = self.get_log_dir() + '/diff.log';
        print 'diffing'
        files = self.get_changed_files()
        fix = 'php ' + os.path.abspath(os.path.dirname(__file__)) + '/../../tools/php-cs-fixer.phar fix --fixers=-concat_without_spaces,concat_with_spaces'
        fix_all = ''
        for file_path in files:
            fix_all = fix_all + fix + ' ' + file_path + ';'
        os.system(fix_all)
        diff = 'cd ' + self.get_repo_dir() + ' && git diff | cat > ' + diff_file
        os.system(diff)
        return diff_file

    def get_changed_files(self):
        files = pull_request.list_files(self.params['user'], self.params['repo'], self.params['pr_number'])
        file_list = []
        for item in files:
            filename = item['filename']
            file_list.append(self.get_repo_dir() + '/' + item['filename'])
        return file_list

    def init_repo(self):
        self.check_dir()
        if (not os.path.exists(self.get_repo_dir() + '/.git')):
            clone = 'git clone -b' + self.params['branch'] + ' ' + self.params['git_url'] + ' ' + self.get_repo_dir()
            print "print init repo"
            os.system(clone)
        self.reset_repo()
        pull = 'cd ' + self.get_repo_dir() + ' && git pull origin ' + self.params['branch']
        os.system(pull)


    def reset_repo(self):
        print 'resetting repo'
        resset = 'cd ' + self.get_repo_dir() + ' && git reset --hard'
        os.system(resset)

    def check_dir(self):
        if (not os.path.exists(self.get_repo_dir())):
            os.makedirs(self.get_repo_dir())
        if (not os.path.exists(self.get_log_dir())):
            os.makedirs(self.get_log_dir())

    def get_user_dir(self):
        if (not self.user_dir):
            self.user_dir = self.work_dir + '/' + self.params['repo_fullname'].split('/')[0]
        return self.user_dir

    def get_repo_dir(self):
        if (not self.repo_dir):
            self.repo_dir = self.work_dir + '/' + self.params['repo_fullname'] + '/' + self.params['branch']
        return self.repo_dir

    def get_log_dir(self):
        if (not self.diff_log):
            self.diff_log = '/tmp/' + self.params['repo_fullname'] + '/' + self.params['branch']
        return self.diff_log

if __name__ == '__main__':
    task = CheckStyle()
    task.set_params({
        'user':'jswh',
        'repo':'OrosOlymPos',
        'sha':'7b81047e18ded3722a75a38e43624cca2e2fc213',
        'git_url':'git@github.com:jswh/OrosOlymPos.git',
        'repo_fullname':'jswh/OrosOlymPos'
        })
    print task.get_diff()
