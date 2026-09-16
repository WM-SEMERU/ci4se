def __modify(self, client_id, client_secret, **kwargs):
    params = {'client_id': client_id, 'client_secret': client_secret}
    return self.make_call(self.__modify, params, kwargs)