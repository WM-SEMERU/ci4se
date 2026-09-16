def Append(self, value, timestamp):
    timestamp = self._NormalizeTime(timestamp)
    if self.data and timestamp < self.data[-1][1]:
        raise RuntimeError('Next timestamp must be larger.')
    self.data.append([value, timestamp])