def _get_url(self, resource, item, sys_id=None):
    url_str = '%(base_url)s/%(base_path)s/%(resource)s/%(item)s' % {'base_url':
        self.base_url, 'base_path': self.base_path, 'resource': resource,
        'item': item}
    if sys_id:
        return '%s/%s' % (url_str, sys_id)
    return url_str