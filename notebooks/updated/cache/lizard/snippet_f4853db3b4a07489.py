def streamify(self, state, frame):
    return '%s%s' % (self.fmt.pack(len(frame)), frame)