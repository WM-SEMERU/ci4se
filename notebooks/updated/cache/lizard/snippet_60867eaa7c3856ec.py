def export(self, options=None, OutputFile=None, verbose=False):
    PARAMS = set_param(['options', 'OutputFile'], [options, OutputFile])
    response = api(url=self.__url + '/export', PARAMS=PARAMS, method='POST',
        verbose=verbose)
    return response