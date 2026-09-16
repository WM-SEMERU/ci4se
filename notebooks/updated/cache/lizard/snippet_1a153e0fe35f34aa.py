def Verify(self, mempool):
    logger.info('Verifying transaction: %s ' % self.Hash.ToBytes())
    return Helper.VerifyScripts(self)