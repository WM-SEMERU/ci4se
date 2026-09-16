def write(self, data):
    for _ in range(64 - len(data)):
        data.append(0)
    self.report.send(bytearray([0]) + data)
    return