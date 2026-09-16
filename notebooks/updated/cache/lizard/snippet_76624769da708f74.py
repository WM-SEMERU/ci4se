def ip_addresses(self, value):
    if not isinstance(value, list):
        raise ValueError('ip_addresses value must be a list')
    if self.data is None:
        self.data = {}
    self.data['ip_addresses'] = ', '.join(value)