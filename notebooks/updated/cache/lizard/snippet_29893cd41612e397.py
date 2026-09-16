def tryPrepare(self, pp: PrePrepare):
    rv, msg = self.canPrepare(pp)
    if rv:
        self.doPrepare(pp)
    else:
        self.logger.debug('{} cannot send PREPARE since {}'.format(self, msg))