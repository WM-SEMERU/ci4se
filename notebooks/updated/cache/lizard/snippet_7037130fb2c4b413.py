def get_units(self, loss_types):
    lst = []
    for lt in loss_types:
        if lt.endswith('_ins'):
            lt = lt[:-4]
        if lt == 'occupants':
            unit = 'people'
        else:
            unit = self.units[lt]
        lst.append(encode(unit))
    return numpy.array(lst)