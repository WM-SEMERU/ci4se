def _read(self, fd, mask):
    try:
        if select.select([fd], [], [], 0)[0]:
            snew = os.read(fd, self.nbytes)
            if PY3K:
                snew = snew.decode('ascii', 'replace')
            self.value.append(snew)
            self.nbytes -= len(snew)
        else:
            snew = ''
        if (self.nbytes <= 0 or len(snew) == 0) and self.widget:
            self.widget.quit()
    except OSError:
        raise IOError('Error reading from %s' % (fd,))