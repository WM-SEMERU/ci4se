def average_cationic_radius(self):
    if 'Ionic radii' in self._data:
        radii = [v for k, v in self._data['Ionic radii'].items() if int(k) > 0]
        if radii:
            return sum(radii) / len(radii)
    return 0