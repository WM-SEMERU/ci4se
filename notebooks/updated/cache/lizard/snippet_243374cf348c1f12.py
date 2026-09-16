def nnz(self):
    nnz = 0
    for k in range(len(self.snpost)):
        nn = self.snptr[k + 1] - self.snptr[k]
        na = self.relptr[k + 1] - self.relptr[k]
        nnz += nn * (nn + 1) / 2 + nn * na
    return nnz