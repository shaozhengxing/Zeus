#-*-coding:utf-8-*-
import statuses
import webhook
import events
if __name__ == '__main__':
    user = 'jswh'
    repo = 'OrosOlymPos'
    ref = '7b81047e18ded3722a75a38e43624cca2e2fc213'
    #print statuses.create(user, repo, '7b81047e18ded3722a75a38e43624cca2e2fc213', '测试状态', 'success', 'http://jswh.me', '正在测试', )
    config = {'url':'http://127.0.0.1/api/webhook', 'content_type':'json'}
    events = ['pull_request']
    #print webhook.create(user, repo, config, events=events)
    #print webhook.list_all(user, repo)
    print webhook.delete(user, repo, '8674332')
