def on_open(self, info):
    self.ip = info.ip
    self.request = info
    self.open()