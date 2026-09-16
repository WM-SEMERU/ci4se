def create(self, name, plan, zone, service_type='mongodb', instance_type=
    'mongodb_sharded', version='2.4.6'):
    url = self._url
    request_data = {'name': name, 'service': service_type, 'plan': plan,
        'type': instance_type, 'version': version, 'zone': zone}
    response = requests.post(url, data=json.dumps(request_data), **self.
        _default_request_kwargs)
    if response.status_code == 200:
        logger.info('Successfully created a new instance with: {}'.format(
            request_data))
    else:
        logger.info('Failed to create instance with: {}'.format(request_data))
        logger.info('Response: [{0}] {1}'.format(response.status_code,
            response.content))
    data = self._get_response_data(response)
    return self._concrete_instance(data)