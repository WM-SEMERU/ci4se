def get_current(self, layout=None, network=None, verbose=False):
    PARAMS = {}
    response = api(url=self.__url + '/get_current', PARAMS=PARAMS, method=
        'POST', verbose=verbose)
    return response