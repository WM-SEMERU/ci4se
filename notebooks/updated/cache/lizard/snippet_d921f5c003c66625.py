def areasAndLengths(self, polygons, lengthUnit, areaUnit, calculationType):
    url = self._url + '/areasAndLengths'
    params = {'f': 'json', 'lengthUnit': lengthUnit, 'areaUnit': {
        'areaUnit': areaUnit}, 'calculationType': calculationType}
    if isinstance(polygons, list) and len(polygons) > 0:
        p = polygons[0]
        if isinstance(p, Polygon):
            params['sr'] = p.spatialReference['wkid']
            params['polygons'] = [poly.asDictionary for poly in polygons]
        del p
    else:
        return (
            'No polygons provided, please submit a list of polygon geometries')
    return self._get(url=url, param_dict=params, securityHandler=self.
        _securityHandler, proxy_url=self._proxy_url, proxy_port=self.
        _proxy_port)