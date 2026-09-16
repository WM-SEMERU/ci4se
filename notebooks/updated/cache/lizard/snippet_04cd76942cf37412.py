def update(self, asns):
    data = {'asns': asns}
    asns_ids = [str(env.get('id')) for env in asns]
    return super(ApiV4As, self).put('api/v4/as/%s/' % ';'.join(asns_ids), data)