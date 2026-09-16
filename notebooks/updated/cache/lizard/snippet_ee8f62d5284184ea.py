def retrieve_trace(self, filename=None, dir=None):
    if hasattr(self, 'applicationTrace') and self.applicationTrace is not None:
        logger.debug('Retrieving PE trace: ' + self.applicationTrace)
        if not filename:
            filename = _file_name('pe', self.id, '.trace')
        return self.rest_client._retrieve_file(self.applicationTrace,
            filename, dir, 'text/plain')
    else:
        return None