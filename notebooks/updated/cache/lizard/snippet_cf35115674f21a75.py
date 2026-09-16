def revert_to(self):
    response = self.resource.repo.api.http_request('PATCH', self.uri)
    if response.status_code == 204:
        logger.debug('reverting to previous version of resource, %s' % self.uri
            )
        self._current_resource.refresh()
    else:
        raise Exception('HTTP %s, could not revert to resource version, %s' %
            (response.status_code, self.uri))