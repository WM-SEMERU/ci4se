def follow_request_authorize(self, id):
    id = self.__unpack_id(id)
    url = '/api/v1/follow_requests/{0}/authorize'.format(str(id))
    self.__api_request('POST', url)