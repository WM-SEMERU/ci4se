def close(self):
    data = self.data
    self.data = None
    if hasattr(data, 'close'):
        data.close()