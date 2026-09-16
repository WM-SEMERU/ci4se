def kill(self, jid):
    greenlet = self.greenlets.get(jid)
    if greenlet is not None:
        logger.warn('Lost ownership of %s' % jid)
        greenlet.kill()