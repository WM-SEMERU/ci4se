def write_double(self, d):
    if not type(d) is float:
        raise TypeError('expected a float (got:%r)' % (type(d),))
    self.write(struct.pack('%sd' % self.endian, d))