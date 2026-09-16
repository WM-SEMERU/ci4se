def import_locations(self, marker_file):
    self._marker_file = marker_file
    data = utils.prepare_read(marker_file)
    for line in data:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        chunk = line.split('#')
        data = chunk[0]
        comment = chunk[1].strip() if len(chunk) == 2 else None
        latitude, longitude, name = data.split(None, 2)
        name = name.strip()
        name = name[1:name.find(name[0], 1)]
        self[name.strip()] = Xearth(latitude, longitude, comment)