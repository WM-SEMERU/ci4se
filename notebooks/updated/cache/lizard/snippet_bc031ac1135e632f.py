def failedToGetPerspective(self, why):
    log.msg('ReconnectingPBClientFactory.failedToGetPerspective')
    if why.check(pb.PBConnectionLost):
        log.msg('we lost the brand-new connection')
        return
    self.stopTrying()
    log.err(why)