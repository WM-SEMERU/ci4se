def downstream(self, f, n=1):
    if f.strand == -1:
        return self.left(f, n)
    return self.right(f, n)