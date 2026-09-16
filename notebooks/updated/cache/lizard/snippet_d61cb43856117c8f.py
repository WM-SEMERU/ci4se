def synch(self, asset_manager_id, **params):
    self.logger.info('Synching Assets.')
    url = '%s/synch/%s' % (self.endpoint, asset_manager_id)
    response = self.session.put(url, params=params)
    if response.ok:
        count = response.json().get('count', 0)
        self.logger.info('Synched %s Assets.', count)
        return count
    else:
        self.logger.error(response.text)
        response.raise_for_status()