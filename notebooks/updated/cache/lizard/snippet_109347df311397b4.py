def get_ranges(self, element, key):
    keys = self.p['keys']
    ranges = self.p['ranges']
    if ranges == {}:
        return {d.name: element.range(d.name, self.data_range) for d in
            element.dimensions()}
    if keys is None:
        specs = ranges
    elif keys and not isinstance(ranges, list):
        raise ValueError(
            'Key list specified but ranges parameter not specified as a list.')
    elif len(keys) == len(ranges):
        try:
            index = keys.index(key)
            specs = ranges[index]
        except:
            raise KeyError('Could not match element key to defined keys')
    else:
        raise ValueError('Key list length must match length of supplied ranges'
            )
    return match_spec(element, specs)