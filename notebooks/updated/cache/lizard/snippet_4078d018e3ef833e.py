def list_kadastrale_afdelingen_by_gemeente(self, gemeente, sort=1):
    try:
        gid = gemeente.id
    except AttributeError:
        gid = gemeente
        gemeente = self.get_gemeente_by_id(gid)
    gemeente.clear_gateway()

    def creator():
        url = self.base_url + '/municipality/%s/department' % gid
        h = self.base_headers
        p = {'orderbyCode': sort == 1}
        res = capakey_rest_gateway_request(url, h, p).json()
        return [Afdeling(id=r['departmentCode'], naam=r['departmentName'],
            gemeente=gemeente) for r in res['departments']]
    if self.caches['permanent'].is_configured:
        key = 'list_kadastrale_afdelingen_by_gemeente_rest#%s#%s' % (gid, sort)
        afdelingen = self.caches['permanent'].get_or_create(key, creator)
    else:
        afdelingen = creator()
    for a in afdelingen:
        a.set_gateway(self)
    return afdelingen