def _format_lat(self, lat):
    if self.ppd in [4, 16, 64, 128]:
        return None
    elif lat < 0:
        return map(lambda x: '{0:0>2}'.format(int(np.abs(x))) + 'S', self.
            _map_center('lat', lat))
    else:
        return map(lambda x: '{0:0>2}'.format(int(x)) + 'N', self.
            _map_center('lat', lat))