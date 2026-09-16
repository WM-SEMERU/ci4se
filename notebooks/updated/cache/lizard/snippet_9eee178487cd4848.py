def getConst(name, timeout=0.1):
    from . import _control
    import time
    timeStamp = time.time()
    while True:
        _control.execQueue.socket.pumpInfoSocket()
        constants = dict(reduce(lambda x, y: x + list(y.items()), elements.
            values(), []))
        timeoutHappened = time.time() - timeStamp > timeout
        if constants.get(name) is not None or timeoutHappened:
            return constants.get(name)
        time.sleep(0.01)