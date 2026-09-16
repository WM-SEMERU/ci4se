def close(self):
    if self.bOwnership and self.value not in (None, INVALID_HANDLE_VALUE):
        if Handle.__bLeakDetection:
            print('CLOSE HANDLE (%d) %r' % (self.value, self))
        try:
            self._close()
        finally:
            self._value = None