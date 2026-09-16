def _get_station_codes(self, force=False):
    if not force and self.station_codes is not None:
        return self.station_codes
    state_urls = self._get_state_urls()
    state_matches = None
    if self.bbox:
        with collection(os.path.join('resources',
            'ne_50m_admin_1_states_provinces_lakes_shp.shp'), 'r') as c:
            geom_matches = [x['properties'] for x in c.filter(bbox=self.bbox)]
            state_matches = [(x['postal'] if x['admin'] != 'Canada' else
                'CN') for x in geom_matches]
    self.station_codes = []
    for state_url in state_urls:
        if state_matches is not None:
            state_abbr = state_url.split('/')[-1].split('.')[0]
            if state_abbr not in state_matches:
                continue
        self.station_codes.extend(self._get_stations_for_state(state_url))
    if self.bbox:
        metadata = self._get_metadata(self.station_codes)
        parsed_metadata = self.parser._parse_metadata(metadata)

        def in_bbox(code):
            lat = parsed_metadata[code]['latitude']
            lon = parsed_metadata[code]['longitude']
            return lon >= self.bbox[0] and lon <= self.bbox[2
                ] and lat >= self.bbox[1] and lat <= self.bbox[3]
        self.station_codes = list(filter(in_bbox, self.station_codes))
    return self.station_codes