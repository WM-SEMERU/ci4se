def split_overlaps(self):
    if not self:
        return
    if len(self.boundary_table) == 2:
        return
    bounds = sorted(self.boundary_table)
    new_ivs = set()
    for lbound, ubound in zip(bounds[:-1], bounds[1:]):
        for iv in self[lbound]:
            new_ivs.add(Interval(lbound, ubound, iv.data))
    self.__init__(new_ivs)