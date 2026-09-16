def _get_sushy_manager(self, manager_id):
    manager_url = parse.urljoin(self._sushy.get_manager_collection_path(),
        manager_id)
    try:
        return self._sushy.get_manager(manager_url)
    except sushy.exceptions.SushyError as e:
        msg = self._(
            'The Redfish Manager "%(manager)s" was not found. Error %(error)s'
            ) % {'manager': manager_id, 'error': str(e)}
        LOG.debug(msg)
        raise exception.IloError(msg)