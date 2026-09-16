def missing(self):
    if self.type == BOOLEAN:
        Log.error('programmer error')
    return self.lang[MissingOp(self)]