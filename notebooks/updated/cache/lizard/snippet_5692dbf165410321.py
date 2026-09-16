def set(self, key, val):
    data = self.get_data(True)
    if data is not None:
        data[key] = val
    else:
        raise RuntimeError('No task is currently running')