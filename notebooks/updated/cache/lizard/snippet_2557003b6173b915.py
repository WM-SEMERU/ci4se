def new(self, verbose=False):
    response = api(url=self.__url + '/new', verbose=verbose)
    return response