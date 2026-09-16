def schedule(self, project, spider, settings=None, **kwargs):
    url = self._build_url(constants.SCHEDULE_ENDPOINT)
    data = {'project': project, 'spider': spider}
    data.update(kwargs)
    if settings:
        setting_params = []
        for setting_name, value in iteritems(settings):
            setting_params.append('{0}={1}'.format(setting_name, value))
        data['setting'] = setting_params
    json = self.client.post(url, data=data, timeout=self.timeout)
    return json['jobid']