def filter(self, result):
    if result is None:
        return True
    reject = result in self.history
    if reject:
        log.debug('result %s, rejected by\n%s', Repr(result), self)
    return reject