def _getphoto_location(self, pid):
    logger.debug('%s - Getting location from fb' % pid)
    lat = None
    lon = None
    accuracy = None
    resp = self.fb.photos_geo_getLocation(photo_id=pid)
    if resp.attrib['stat'] != 'ok':
        logger.error('%s - fb: photos_geo_getLocation failed with status: %s',
            resp.attrib['stat'])
        return None, None, None
    for location in resp.find('photo'):
        lat = location.attrib['latitude']
        lon = location.attrib['longitude']
        accuracy = location.attrib['accuracy']
    return lat, lon, accuracy