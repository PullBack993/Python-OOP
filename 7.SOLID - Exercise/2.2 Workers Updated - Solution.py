from abc import abstractmethod, ABC
import time


class Workable(ABC):
    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass


class Worker(Workable, Eatable):

    def work(self):
        print("I'm normal 1.Worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(Workable, Eatable):

    def work(self):
        print("I'm super 1.Worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        if 'Workable' in [w.__name__ for w in worker.__class__.__mro__]:
            self.worker = worker
        else:
            raise AssertionError('`1.Worker` must be of type {}'.format(Worker))

class Robot(Workable):

    def work(self):
        print("I'm a robot. I'm working....")


class WorkManager(Manager):
    def manage(self):
        self.worker.work()


class BreakManager(Manager):
    def lunch_break(self):
        self.worker.eat()


work_manager = WorkManager()

break_manager = BreakManager()
work_manager.set_worker(Worker())
break_manager.set_worker(Worker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(SuperWorker())
break_manager.set_worker(SuperWorker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(Robot())
work_manager.manage()
try:
    break_manager.set_worker(Robot())
    break_manager.lunch_break()
except:
    pass
