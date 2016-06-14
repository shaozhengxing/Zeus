#-*- coding:utf-8 -*-
import json
events = [
    'pull_request.reopen',
    'pull_request.opened'
    ]

class EventHandler():
    handlers = None
    def handle(self, payload):
        data = json.loads(payload)
        event_name = self.get_event(data)
        if event_name in self.handlers:
            handler = self.handlers[event_name]
            return handler(data)
        else:
            self.default_hanlder(data)

    def set_handler(self, event_name, handler):
        if (not self.handlers):
            self.handlers = {}
        self.handlers[event_name] = handler

    def get_event(self, data):
        for valid_event in events:
            parts = valid_event.split('.');
            if (parts[0] in data) and (parts[1] == data['action']):
                return valid_event

    def can_handle(self, data):
        event_name = self.get_event(json.loads(data))
        if (self.handlers and (event_name in self.handlers)):
            return True
        else:
            return False


    def default_hanlder(self, data):
        print "no handler for this data, current handlers"
        print self.handlers

