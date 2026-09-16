def result(self):
    if not self.tasks:
        self.clean_all()
    tasks_length = len(self.tasks)
    self.logger_function(
        '%s tasks of request, will cost at least %s seconds.' % (
        tasks_length, round(self.req.interval / self.req.n * tasks_length, 2)))
    self.req.x
    for task in self.tasks:
        key, value, fut = task
        if fut.x and fut.cx:
            self.ignore[key].append(value)
    return self.reset_new_request()