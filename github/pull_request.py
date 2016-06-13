#-*-coding:utf-8-*-
import process
@process.get
def pull_request_list(user, repo):
    api = '/repos/' + user + '/' + repo + '/pulls'
    return {'api':api, 'data':{}}
