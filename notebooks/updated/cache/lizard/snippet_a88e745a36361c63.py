def add_version_pattern(self, m):
    if self.version < 7:
        return
    field = iter(tables.version_pattern[self.version][::-1])
    start = len(m) - 11
    for i in range(6):
        for j in range(start, start + 3):
            bit = int(next(field))
            m[i][j] = bit
            m[j][i] = bit