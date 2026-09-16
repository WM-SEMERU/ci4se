def _get_values(self, rdn):
    output = {}
    [output.update([(ntv['type'].native, ntv.prepped_value)]) for ntv in rdn]
    return output