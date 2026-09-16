def listener(self):
    while 1:
        try:
            data = self.read_eager()
        except EOFError:
            print('*** Connection closed by remote host ***')
            return
        if data:
            self.stdout.write(data)
        else:
            self.stdout.flush()