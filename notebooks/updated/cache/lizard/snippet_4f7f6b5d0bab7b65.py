def taskit(func):


    class NewTask(Task):

        def work(self, *args, **kw):
            return func(*args, **kw)
    return NewTask()