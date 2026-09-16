def from_file(self, filename):
    f = open(filename, 'rb')
    while True:
        data = f.read(10480)
        if not data:
            break
        self.update(data)
    f.close()