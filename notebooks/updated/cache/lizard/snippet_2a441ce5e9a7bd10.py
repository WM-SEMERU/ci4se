def match(self, fname, flevel, ftype):
    if self.filetype == ftype and (self.level is None or self.level == flevel
        ) and fnmatch.fnmatch(fname, self.pattern):
        return self.score
    return 0