def padding(self):
    pad = self.ntiles - self.windowsize
    return int((pad - 1) / 2.0), int((pad + 1) / 2.0)