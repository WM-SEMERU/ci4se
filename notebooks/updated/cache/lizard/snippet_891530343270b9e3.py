def api_version(self):
    request_url = '{}/api/0/version'.format(self.instance)
    return_value = self._call_api(request_url)
    return return_value['version']