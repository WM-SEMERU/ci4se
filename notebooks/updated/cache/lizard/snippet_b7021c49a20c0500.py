def get_sectie_by_id_and_afdeling(self, id, afdeling):
    try:
        aid = afdeling.id
    except AttributeError:
        aid = afdeling
        afdeling = self.get_kadastrale_afdeling_by_id(aid)
    afdeling.clear_gateway()

    def creator():
        url = self.base_url + '/municipality/%s/department/%s/section/%s' % (
            afdeling.gemeente.id, afdeling.id, id)
        h = self.base_headers
        p = {'geometry': 'full', 'srs': '31370'}
        res = capakey_rest_gateway_request(url, h, p).json()
        return Sectie(res['sectionCode'], afdeling, self._parse_centroid(
            res['geometry']['center']), self._parse_bounding_box(res[
            'geometry']['boundingBox']), res['geometry']['shape'])
    if self.caches['long'].is_configured:
        key = 'get_sectie_by_id_and_afdeling_rest#%s#%s' % (id, aid)
        sectie = self.caches['long'].get_or_create(key, creator)
    else:
        sectie = creator()
    sectie.set_gateway(self)
    return sectie