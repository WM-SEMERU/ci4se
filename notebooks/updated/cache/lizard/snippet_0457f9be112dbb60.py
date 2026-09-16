def account_unblock(self, id):
    id = self.__unpack_id(id)
    url = '/api/v1/accounts/{0}/unblock'.format(str(id))
    return self.__api_request('POST', url)