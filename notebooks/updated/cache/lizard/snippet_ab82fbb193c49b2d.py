def waitForGreenlet(g):
    from twisted.internet import reactor
    assert reactor.greenlet == getcurrent(
        ), 'must invoke this in the reactor greenlet'
    d = defer.Deferred()

    def cb(g):
        try:
            d.callback(g.get())
        except:
            d.errback(failure.Failure())
    g.link(d)
    return d