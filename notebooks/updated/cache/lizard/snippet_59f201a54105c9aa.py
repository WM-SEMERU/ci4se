def bulk_launch(self, jobs=None, filter=None, all=False):
    json = None
    if jobs is not None:
        schema = JobSchema(exclude=('id', 'status', 'package_name',
            'config_name', 'device_name', 'result_id', 'user_id', 'created',
            'updated', 'automatic'))
        jobs_json = self.service.encode(schema, jobs, many=True)
        json = {self.RESOURCE: jobs_json}
    schema = JobSchema()
    resp = self.service.post(self.base, params={'bulk': 'launch', 'filter':
        filter, 'all': all}, json=json)
    return self.service.decode(schema, resp, many=True)