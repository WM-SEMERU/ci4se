def import_locations(self, gpsdata_file, checksum=True):
    r
    self._gpsdata_file = gpsdata_file
    data = utils.prepare_read(gpsdata_file)
    parsers = {'GPGGA': Fix, 'GPRMC': Position, 'GPWPL': Waypoint, 'GPGLL':
        LoranPosition, 'LCGLL': LoranPosition}
    if not checksum:
        logging.warning(
            'Disabling the checksum tests should only be usedwhen the device is incapable of emitting the correct values!'
            )
    for line in data:
        if not line[1:6] in parsers:
            continue
        if checksum:
            values, checksum = line[1:].split('*')
            if not calc_checksum(values) == int(checksum, 16):
                raise ValueError('Sentence has invalid checksum')
        else:
            values = line[1:].split('*')[0]
        elements = values.split(',')
        parser = getattr(parsers[elements[0]], 'parse_elements')
        self.append(parser(elements[1:]))