def query(self, *args):
    log('calling client.query')
    self._connect()
    try:
        self.sendConn.send(args)
        res = self.receive()
        while self.isUnilateralResponse(res):
            res = self.receive()
        return res
    except EnvironmentError as ee:
        raise WatchmanEnvironmentError(
            'I/O error communicating with watchman daemon', ee.errno, ee.
            strerror, args)
    except WatchmanError as ex:
        ex.setCommand(args)
        raise