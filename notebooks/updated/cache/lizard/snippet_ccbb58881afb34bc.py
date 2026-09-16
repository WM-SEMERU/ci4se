def readpipe(self, chunk=None):
    read = []
    while True:
        l = sys.stdin.readline()
        if not l:
            if read:
                yield read
                return
            return
        if not chunk:
            yield l
        else:
            read.append(l)
            if len(read) == chunk:
                yield read