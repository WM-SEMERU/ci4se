def __find_smallest(self):
    minval = sys.maxsize
    for i in range(self.n):
        for j in range(self.n):
            if not self.row_covered[i] and not self.col_covered[j]:
                if minval > self.C[i][j]:
                    minval = self.C[i][j]
    return minval