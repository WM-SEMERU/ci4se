def migrate(self, host, port, key, destination_db, timeout, copy=False,
    replace=False):
    command = [b'MIGRATE', host, ascii(port).encode('ascii'), key, ascii(
        destination_db).encode('ascii'), ascii(timeout).encode('ascii')]
    if copy is True:
        command.append(b'COPY')
    if replace is True:
        command.append(b'REPLACE')
    return self._execute(command, b'OK')