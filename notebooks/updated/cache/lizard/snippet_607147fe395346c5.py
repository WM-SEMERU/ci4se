def update_format(self, format):
    self.format = format
    self.request.update(format=self.format.data)