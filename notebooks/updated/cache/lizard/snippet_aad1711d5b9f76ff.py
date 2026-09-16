def intersection(self, other):
    inter = MOC()
    for order, cells in other:
        for cell in cells:
            for i in self._compare_operation(order, cell, True, 'inter'):
                inter.add(*i)
    return inter