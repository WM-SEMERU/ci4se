def to_dict(self):
    data = {'aid': self.aid, 'number': self.number, 'element': self.element}
    for coord in {'x', 'y', 'z'}:
        if getattr(self, coord) is not None:
            data[coord] = getattr(self, coord)
    if self.charge is not 0:
        data['charge'] = self.charge
    return data