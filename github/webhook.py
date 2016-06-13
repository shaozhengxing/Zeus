#-*- coding:utf-8 -*-
import process

@process.get
def list_all(user, repo):
    return {'api':get_hook_base_api(user, repo), 'data':{}}


@process.get
def get(user, repo, id):
    api = get_hook_base_api(user, repo) + '/' + id
    return {'api':api, 'data':{}}

@process.post
def create(user, repo, config, events, name='web', active=True):
    data = {'name':name, 'config':config, 'events':events, 'active':active}
    return {'api':get_hook_base_api(user, repo), 'data':data}

@process.patch
def edit(user, repo, id, config, events, add_events=None, remove_events=None, active=True):
    api = get_hook_base_api(user, repo) + '/' + id
    data = {'config':config, 'events':events, 'add_events':add_events, 'remove_events':remove_events, 'active':active}
    return {'api':api, 'data':data}

@process.delete
def delete(user, repo, id):
    api = get_hook_base_api(user, repo) + '/' + id
    return {'api':api, 'data':{}}

def get_hook_base_api(user, repo):
    return '/repos/' + user + '/' + repo + '/hooks';

