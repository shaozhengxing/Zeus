#-*- coding:utf-8 -*-
import os, random, time, atexit
from multiprocessing import Process, Queue
from github_event_handlers import get_handler
from web import get_web_app, set_data_queue
from signal import signal, SIGINT, SIG_IGN, siginterrupt

handler = get_handler()
data_queue = Queue()

set_data_queue(data_queue)

def run_web():
    get_web_app().run(host='0.0.0.0', port=80)

web_process = Process(target=run_web)
web_process.start()

proc_pool = []

def clean_up():
    print "stopping web process"
    web_process.terminate()
    web_process.join(5)
    print "stopping work process"
    for p in proc_pool:
        print "stopping process " + str(p.pid)
        p.terminate()
        p.join(5)

atexit.register(clean_up)

def main():
    while True:
        item = data_queue.get()
        print "data get " + item['type']
        if (item['type'] == 'webhook' and handler.can_handle(item['data'])):
            proc = Process(target=handler.handle, args=(item['data'],))
            proc.start()
            proc_pool.append(proc)
            print 'process {} started'.format(proc.pid)
        time.sleep(0.1)
        alive_pool = []
        for p in proc_pool:
            if (p.is_alive()):
                alive_pool.append(p)
            else:
                p.join(5)
        time.sleep(0.1)

if __name__ == "__main__":
    main()



