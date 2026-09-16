def failedToGetPerspective(self, why, broker):
    log.msg('ReconnectingPBClientFactory.failedToGetPerspective')
    if why.check(pb.PBConnectionLost):
        log.msg('we lost the brand-new connection')
    elif why.check(error.UnauthorizedLogin):
        log.msg('unauthorized login; check worker name and password')
    else:
        log.err(why, 'While trying to connect:')
        reactor.stop()
        return
    broker.transport.loseConnection()