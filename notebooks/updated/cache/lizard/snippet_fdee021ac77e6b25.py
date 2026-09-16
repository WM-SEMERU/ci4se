def decode(self):
    if _debug:
        IOChainMixIn._debug('decode')
    iocb = self.ioChain
    if self.ioState == COMPLETED:
        if _debug:
            IOChainMixIn._debug('    - completed: %r', self.ioResponse)
        iocb.ioState = COMPLETED
        iocb.ioResponse = self.ioResponse
    elif self.ioState == ABORTED:
        if _debug:
            IOChainMixIn._debug('    - aborted: %r', self.ioError)
        iocb.ioState = ABORTED
        iocb.ioError = self.ioError
    else:
        raise RuntimeError('invalid state: %d' % (self.ioState,))