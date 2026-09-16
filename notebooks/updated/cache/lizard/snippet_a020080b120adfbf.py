def upload(self, remote, reader):
    fd = self.open(remote, 'w')
    while True:
        chunk = reader.read(512 * 1024)
        if chunk == b'':
            break
        self.write(fd, chunk)
    self.close(fd)