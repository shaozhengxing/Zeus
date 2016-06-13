#-*- coding:utf-8 -*-
import time
class Line():
    units = None
    def run(self):
        for unit in self.units:
            unit.work()
            while (unit.is_alive()):
                time.sleep(0.5)

    def push_work_unit(self, unit):
        if (not self.units):
            self.units = []
        self.units.append(unit)


class Unit(object):
    tasks = None

    def add_task(self, task):
        if (not self.tasks):
            self.tasks = []
        self.tasks.append(task)

    def work(self):
        for task in self.tasks:
            task.start()

    def is_alive(self):
        status = 1
        for task in self.tasks:
            status = status and task.is_alive()
        return status


