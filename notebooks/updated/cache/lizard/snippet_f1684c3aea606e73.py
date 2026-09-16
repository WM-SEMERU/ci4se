def write(self, data):
    for chunk in chunks(data, 512):
        self.wait_to_write()
        self.comport.write(chunk)
    self.comport.flush()