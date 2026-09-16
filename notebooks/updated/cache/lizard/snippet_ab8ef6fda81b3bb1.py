def jobs(self, *args, **kwargs):
    ref = {'exchange': 'jobs', 'name': 'jobs', 'routingKey': [{
        'multipleWords': False, 'name': 'destination'}, {'multipleWords':
        False, 'name': 'project'}, {'multipleWords': True, 'name':
        'reserved'}], 'schema': 'v1/pulse-job.json#'}
    return self._makeTopicExchange(ref, *args, **kwargs)