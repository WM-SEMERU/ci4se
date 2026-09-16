def account_mute(self, id, notifications=True):
    id = self.__unpack_id(id)
    params = self.__generate_params(locals(), ['id'])
    url = '/api/v1/accounts/{0}/mute'.format(str(id))
    return self.__api_request('POST', url, params)