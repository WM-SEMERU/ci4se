def remove(self, first, count):
    if first < 0 or count < 1:
        return
    new_range = []
    last = first + count - 1
    for r in self.__range:
        if first <= r.last and r.first <= last:
            if r.first < first:
                new_range.append(IdRange(r.first, first - r.first))
            if last < r.last:
                new_range.append(IdRange(last + 1, r.last - last))
        else:
            new_range.append(r)
    self.__range = new_range