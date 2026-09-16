def list(self, id):
    id = self.__unpack_id(id)
    return self.__api_request('GET', '/api/v1/lists/{0}'.format(id))