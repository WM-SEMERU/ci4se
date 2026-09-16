def protect(self, password=None, read_protect=False, protect_from=0):
    args = password, read_protect, protect_from
    return super(NTAG21x, self).protect(*args)