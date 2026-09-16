def _deallocator(self):
    lookup = {'c_bool': 'logical', 'c_double': 'double', 'c_double_complex':
        'complex', 'c_char': 'char', 'c_int': 'int', 'c_float': 'float',
        'c_short': 'short', 'c_long': 'long'}
    ctype = type(self.pointer).__name__.replace('LP_', '').lower()
    if ctype in lookup:
        return 'dealloc_{0}_{1:d}d'.format(lookup[ctype], len(self.indices))
    else:
        return None