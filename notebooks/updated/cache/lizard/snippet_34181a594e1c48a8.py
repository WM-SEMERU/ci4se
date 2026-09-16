def get(self, key):
    if isinstance(key, tuple):
        try:
            x, y = float(key[0]), float(key[1])
        except IndexError:
            raise ValueError('Two values are required for a coordinate pair')
        except ValueError:
            raise ValueError(
                'Only float or float-coercable values can be passed')
        key = '{0},{1}'.format(x, y)
    return self[self.lookups[key]]