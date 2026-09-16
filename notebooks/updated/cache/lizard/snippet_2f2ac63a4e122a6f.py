def get_projects(self):
    url = urljoin(self.keystone_endpoint, '{}/{}'.format(
        DEFAULT_KEYSTONE_API_VERSION, 'projects'))
    try:
        r = self._make_request(url, self.headers)
        return r.get('projects', [])
    except Exception as e:
        self.logger.warning('Unable to get projects: {}'.format(e))
        raise e