def media_update(self, id, description=None, focus=None):
    id = self.__unpack_id(id)
    if focus != None:
        focus = str(focus[0]) + ',' + str(focus[1])
    params = self.__generate_params(locals(), ['id'])
    return self.__api_request('PUT', '/api/v1/media/{0}'.format(str(id)),
        params)