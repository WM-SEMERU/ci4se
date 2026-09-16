def _get_status_code(self, http_status):
    try:
        return int(http_status.split(' ', 1)[0])
    except TypeError:
        _logger.warning('Unable to find status code in HTTP status %r.',
            http_status)
    return 500