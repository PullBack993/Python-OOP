class Worker:

    def work(self):
        print("I'm working!!")


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        if 'Worker' in [w.__name__ for w in worker.__class__.__mro__]:
            self.worker = worker
        else:
            raise AssertionError('`1.Worker` must be of type {}'.format(Worker))

    def manage(self):
        if self.worker is not None:
            self.worker.work()


class SuperWorker(Worker):

    def work(self):
        print("I work very hard!!!")


worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
try:
    manager.set_worker(super_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")
