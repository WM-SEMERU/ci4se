def get_errors(self):
    result = []
    while not self.errors.empty():
        try:
            e = self.errors.get(False)
            result.append(e)
        except self.errors.Empty:
            continue
        self.errors.task_done()
    return result