#-*- coding:utf-8 -*-
import process

@process.post
def create(user, repo, sha, status_name, state, target_url=None,  description=None):
    api = '/repos/' + user + '/' + repo + '/statuses/' + sha
    data = {'state':state, 'target_url':target_url, 'description':description, 'context':status_name}
    return {'api':api, 'data':data}
