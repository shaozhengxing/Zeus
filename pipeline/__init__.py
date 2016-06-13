import time, os
from factory import Factory
from multiprocessing import Process
import tasks
if __name__ == '__main__':
    from tasks import Test
    test_task = Test()
    factory = Factory()
    factory.regist_task('test', Test)
    factory.regist_task('test2', Test)
    line = factory.make_pipeline([{'test': {'num':'1', 'sleep':1},'test2': {'num':'3', 'sleep':1}}, {'test': {'num': '2', 'sleep':1}}])
    p = Process(target=line.run)
    p.start()
    p.join()


