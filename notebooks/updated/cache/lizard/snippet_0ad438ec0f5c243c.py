def cuid(self):
    identifier = 'c'
    millis = int(time.time() * 1000)
    identifier += _to_base36(millis)
    count = _pad(_to_base36(self.counter), BLOCK_SIZE)
    identifier += count
    identifier += self.fingerprint
    identifier += _random_block()
    identifier += _random_block()
    return identifier