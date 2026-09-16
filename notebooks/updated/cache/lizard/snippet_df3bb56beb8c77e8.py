def list_gemeenten(self, gewest=2, sort=1):
    try:
        gewest_id = gewest.id
    except AttributeError:
        gewest_id = gewest
        gewest = self.get_gewest_by_id(gewest_id)
    gewest.clear_gateway()

    def creator():
        res = crab_gateway_request(self.client, 'ListGemeentenByGewestId',
            gewest_id, sort)
        return [Gemeente(r.GemeenteId, r.GemeenteNaam, r.NISGemeenteCode,
            gewest) for r in res.GemeenteItem if r.TaalCode == r.
            TaalCodeGemeenteNaam]
    if self.caches['permanent'].is_configured:
        key = 'ListGemeentenByGewestId#%s#%s' % (gewest_id, sort)
        gemeenten = self.caches['permanent'].get_or_create(key, creator)
    else:
        gemeenten = creator()
    for g in gemeenten:
        g.set_gateway(self)
    return gemeenten