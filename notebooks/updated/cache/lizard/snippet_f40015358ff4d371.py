def toascii(self, asciifile, headerfile='', columnnames=(), sep=' ',
    precision=(), usebrackets=True):
    msg = self._toascii(asciifile, headerfile, columnnames, sep, precision,
        usebrackets)
    if len(msg) > 0:
        six.print_(msg)