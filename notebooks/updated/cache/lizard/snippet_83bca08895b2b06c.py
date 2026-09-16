def search_v1(self, q, resolve=False):
    params = self.__generate_params(locals())
    if resolve == False:
        del params['resolve']
    return self.__api_request('GET', '/api/v1/search', params)