def check_data_types(self, ds):
    fails = []
    total = len(ds.variables)
    for k, v in ds.variables.items():
        if v.dtype.kind != 'S' and all(v.dtype.type != t for t in (np.
            character, np.dtype('|S1'), np.dtype('b'), np.dtype('i2'), np.
            dtype('i4'), np.float32, np.double)):
            fails.append('The variable {} failed because the datatype is {}'
                .format(k, v.datatype))
    return Result(BaseCheck.HIGH, (total - len(fails), total), self.
        section_titles['2.2'], msgs=fails)