def readlines(self):
    continuation = False
    while True:
        yield self.readline(continuation)
        continuation = True