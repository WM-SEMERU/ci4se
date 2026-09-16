def merge_request(self, request_id):
    request_url = '{}pull-request/{}/merge'.format(self.create_basic_url(),
        request_id)
    return_value = self._call_api(request_url, method='POST')
    LOG.debug(return_value)