def pounce(self, file, show=False):
    file = os.path.abspath(os.path.normpath(os.path.realpath(file)))
    self._write('pounce:%d:%s\n' % (int(show), file))
    return self