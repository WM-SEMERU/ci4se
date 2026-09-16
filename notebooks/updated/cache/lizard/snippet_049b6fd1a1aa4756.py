def read_blocking(self):
    while True:
        data = self._read()
        if data != None:
            break
    return self._parse_message(data)