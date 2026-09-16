def _f90str(self, value):
    result = repr(str(value)).replace("\\'", "''").replace('\\"', '""')
    result = result.replace('\\\\', '\\')
    return result