#-*- coding:utf-8 -*-
from line import Line,Unit
class Factory(object):
    registed_tasks = {}

    def regist_task(self, name, task):
        self.registed_tasks[name] = task


    def make_pipeline(self, pipline_def = None):
        line = Line()
        for tasks in pipline_def:
            unit = Unit()
            for (name, params) in tasks.items():
                task = self.registed_tasks[name]()
                task.set_params(params)
                unit.add_task(task)
            line.push_work_unit(unit)
        return line
