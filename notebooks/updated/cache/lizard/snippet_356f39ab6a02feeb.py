def toArray(self):
    A = np.zeros((self.numRows, self.numCols), dtype=np.float64, order='F')
    for k in xrange(self.colPtrs.size - 1):
        startptr = self.colPtrs[k]
        endptr = self.colPtrs[k + 1]
        if self.isTransposed:
            A[k, self.rowIndices[startptr:endptr]] = self.values[startptr:
                endptr]
        else:
            A[self.rowIndices[startptr:endptr], k] = self.values[startptr:
                endptr]
    return A