def deferToGreenletPool(*args, **kwargs):
    reactor = args[0]
    pool = args[1]
    func = args[2]
    d = defer.Deferred()

    def task():
        try:
            reactor.callFromGreenlet(d.callback, func(*args[3:], **kwargs))
        except:
            reactor.callFromGreenlet(d.errback, failure.Failure())
    pool.add(spawn(task))
    return d