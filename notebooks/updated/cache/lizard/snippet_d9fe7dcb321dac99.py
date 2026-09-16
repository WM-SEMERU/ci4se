def copy(self, project, name=None, strategy=None):
    strategy = strategy or AppCopyStrategy.CLONE
    project = Transform.to_project(project)
    data = {'project': project, 'strategy': strategy}
    if name:
        data['name'] = name
    extra = {'resource': self.__class__.__name__, 'query': {'id': self.id,
        'data': data}}
    logger.info('Copying app', extra=extra)
    app = self._api.post(url=self._URL['copy'].format(id=self.id), data=data
        ).json()
    return App(api=self._api, **app)