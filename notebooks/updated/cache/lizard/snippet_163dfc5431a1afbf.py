def enable_static_ip_config(self, ip_address, network_mask):
    if not isinstance(ip_address, basestring):
        raise TypeError('ip_address can only be an instance of type basestring'
            )
    if not isinstance(network_mask, basestring):
        raise TypeError(
            'network_mask can only be an instance of type basestring')
    self._call('enableStaticIPConfig', in_p=[ip_address, network_mask])