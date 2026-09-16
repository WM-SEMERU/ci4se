def update_script(self, script_body):
    uri = '{}/script'.format(self.data['uri'])
    return self._helper.update(script_body, uri=uri)