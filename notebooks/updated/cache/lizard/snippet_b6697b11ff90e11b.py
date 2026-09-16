def get_quad_by_id(self, mosaic, quad_id):
    path = 'basemaps/v1/mosaics/{}/quads/{}'.format(mosaic['id'], quad_id)
    return self._get(self._url(path)).get_body()