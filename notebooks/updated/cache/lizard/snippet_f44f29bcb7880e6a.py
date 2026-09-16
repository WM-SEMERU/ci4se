def dump(self):
    print('pagesize=%08x, reccount=%08x, pagecount=%08x' % (self.pagesize,
        self.reccount, self.pagecount))
    self.dumpfree()
    self.dumptree(self.firstindex)