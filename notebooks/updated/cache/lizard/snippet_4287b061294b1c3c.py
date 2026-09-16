def publish(self, func):
    project = self.session.get_default_project()
    func_name = 'projects/{}/locations/{}/functions/{}'.format(project,
        self.region, func.name)
    func_info = self.get(func.name)
    source_url = None
    archive = func.get_archive()
    if not func_info or self._delta_source(archive, func_name):
        source_url = self._upload(archive, self.region)
    config = func.get_config()
    config['name'] = func_name
    if source_url:
        config['sourceUploadUrl'] = source_url
    for e in func.events:
        e.add(func)
    if func_info is None:
        log.info('creating function')
        response = self.client.execute_command('create', {'location':
            'projects/{}/locations/{}'.format(project, self.region), 'body':
            config})
    else:
        delta = delta_resource(func_info, config, ('httpsTrigger',))
        if not delta:
            response = None
        else:
            update_mask = ','.join(delta)
            log.info('updating function config %s', update_mask)
            response = self.client.execute_command('patch', {'name':
                func_name, 'body': config, 'updateMask': update_mask})
    return response