def tags(self, where, archiver='', timeout=DEFAULT_TIMEOUT):
    return self.query('select * where {0}'.format(where), archiver, timeout
        ).get('metadata', {})