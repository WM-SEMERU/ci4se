def extra_hosts(self, value):
    if value is None:
        self._extra_hosts = value
    elif isinstance(value, list):
        self._extra_hosts = value
    elif isinstance(value, dict):
        converted_extra_hosts = []
        for k, v in sorted(six.iteritems(value)):
            if not is_valid_hostname(k):
                raise ValueError(
                    'each key in extra hosts is required to be a valid hostname. {0} was passed'
                    .format(k))
            if not is_valid_ip(v):
                raise ValueError(
                    'each value in extra hosts is required to be a valid ip address. {0} was passed'
                    .format(v))
            converted_extra_hosts.append('{0}:{1}'.format(k, v))
        self._extra_hosts = converted_extra_hosts
    else:
        raise TypeError(
            'extra hosts must be a dict, list, or None. {0} was passed'.
            format(value))