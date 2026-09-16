def subproduct(self, ext):
    fname, fpath = self.subproductPath(ext)
    return fname, fpath, self.subproductUpToDate(fpath)