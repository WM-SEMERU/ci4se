def __create(self, client_id, client_secret, calls, **kwargs):
    params = {'client_id': client_id, 'client_secret': client_secret,
        'calls': calls}
    return self.make_call(self.__create, params, kwargs)