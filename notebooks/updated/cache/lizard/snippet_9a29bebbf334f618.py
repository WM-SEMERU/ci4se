def _prepdata(self):
    if not self._data.get('bbox'):
        self.update_bbox()
    if not self._data.get('crs'):
        self._data['crs'] = {'type': 'name', 'properties': {'name':
            'urn:ogc:def:crs:OGC:2:84'}}