def saveAsJSON(self, fp, writeBytes=False):
    if writeBytes:
        fp.write(dumps(self.params, sort_keys=True).encode('UTF-8'))
        fp.write(b'\n')
        for record in self.records():
            fp.write(dumps(record, sort_keys=True).encode('UTF-8'))
            fp.write(b'\n')
    else:
        fp.write(six.u(dumps(self.params, sort_keys=True)))
        fp.write(six.u('\n'))
        for record in self.records():
            fp.write(six.u(dumps(record, sort_keys=True)))
            fp.write(six.u('\n'))