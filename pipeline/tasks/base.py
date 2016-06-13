#-*- coding:utf-8 -*-
from threading import Thread
class BaseTask(Thread):
    next_event = []
    params = {}
    def run(self):
        self.do_task()
    def add_next_event(self, event):
        self.next_event.append(event);

    def set_params(self, params):
        self.params = params

    def do_task(self):
        pass

