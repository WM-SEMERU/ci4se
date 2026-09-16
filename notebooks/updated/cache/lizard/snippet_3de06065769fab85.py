def count(self, value):
    cnt = 0
    for x in self:
        if x == value:
            cnt += 1
    return cnt