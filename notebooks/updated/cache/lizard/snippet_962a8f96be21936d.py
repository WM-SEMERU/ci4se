def create_python_worker(self, func, *args, **kwargs):
    worker = PythonWorker(func, args, kwargs)
    self._create_worker(worker)
    return worker