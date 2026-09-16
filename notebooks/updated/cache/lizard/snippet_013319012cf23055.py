def geoadd(self, name, *values):
    if len(values) % 3 != 0:
        raise DataError('GEOADD requires places with lon, lat and name values')
    return self.execute_command('GEOADD', name, *values)