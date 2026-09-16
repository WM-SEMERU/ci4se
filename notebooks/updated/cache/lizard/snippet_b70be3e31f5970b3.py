def upstream(self, f, n=1):
    if f.strand == -1:
        return self.right(f, n)
    return self.left(f, n)