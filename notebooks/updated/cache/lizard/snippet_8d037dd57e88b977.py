def _map_center(self, coord, val):
    if self.ppd in [4, 8, 16, 32, 64]:
        res = {'lat': 0, 'long': 360}
        return res[coord] / 2.0
    elif self.ppd in [128]:
        res = {'lat': 90, 'long': 90}
        return (val // res[coord] + 1) * res[coord] - res[coord] / 2.0
    elif self.ppd in [256]:
        res = {'lat': 60, 'long': 90}
        return (val // res[coord] + 1) * res[coord] - res[coord] / 2.0