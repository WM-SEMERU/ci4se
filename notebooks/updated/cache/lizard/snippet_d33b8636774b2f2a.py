def __send_challenge(self, mfa_id, **kwargs):
    params = {'mfa_id': mfa_id}
    return self.make_call(self.__send_challenge, params, kwargs)