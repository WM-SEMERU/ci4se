def update_config(self):
    dataset = self._top._config.dataset
    session = object_session(self._top._config)
    logger.debug('Updating group config. dataset: {}, type: {}, key: {}'.
        format(dataset.vid, self._top._type, self._key))
    self._config, created = _get_config_instance(self, session, parent_id=
        self._parent._config.id, d_vid=dataset.vid, group=self._key, key=
        self._key, type=self._top._type, dataset=dataset)
    if created:
        self._top._cached_configs[self._get_path()] = self._config
    self._top._add_valid(self._config)
    if created:
        logger.debug('New group config created and linked. config: {}'.
            format(self._config))
    else:
        logger.debug('Existing group config linked. config: {}'.format(self
            ._config))