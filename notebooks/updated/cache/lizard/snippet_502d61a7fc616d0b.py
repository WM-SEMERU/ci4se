def commit(self):
    if self.session is not None:
        logger.info('committing transaction in %s' % self)
        tmp = self.stable
        self.stable, self.session = self.session, None
        self.istable = 1 - self.istable
        self.write_istable()
        tmp.close()
        self.lock_update.release()
    else:
        logger.warning("commit called but there's no open session in %s" % self
            )