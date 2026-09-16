def retry_request(self, method, action, body=None, headers=None, params=None):
    max_attempts = self.retries + 1
    for i in range(max_attempts):
        try:
            return self.do_request(method, action, body=body, headers=
                headers, params=params)
        except exceptions.ConnectionFailed:
            if i < self.retries:
                _logger.debug('Retrying connection to Neutron service')
                time.sleep(self.retry_interval)
            elif self.raise_errors:
                raise
    if self.retries:
        msg = _('Failed to connect to Neutron server after %d attempts'
            ) % max_attempts
    else:
        msg = _('Failed to connect Neutron server')
    raise exceptions.ConnectionFailed(reason=msg)