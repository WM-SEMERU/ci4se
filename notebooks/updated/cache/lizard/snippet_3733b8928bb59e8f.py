def update_configuration(self, timeout=-1):
    uri = '{}/configuration'.format(self.data['uri'])
    return self.update_with_zero_body(uri=uri, timeout=timeout)