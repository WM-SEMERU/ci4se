def timeline_public(self, max_id=None, min_id=None, since_id=None, limit=
    None, only_media=False):
    if max_id != None:
        max_id = self.__unpack_id(max_id)
    if min_id != None:
        min_id = self.__unpack_id(min_id)
    if since_id != None:
        since_id = self.__unpack_id(since_id)
    params_initial = locals()
    if only_media == False:
        del params_initial['only_media']
    url = '/api/v1/timelines/public'
    params = self.__generate_params(params_initial)
    return self.__api_request('GET', url, params)