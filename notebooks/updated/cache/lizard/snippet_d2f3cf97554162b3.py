def change_engine_password(self, password):
    self.make_request(ModificationFailed, method='update', resource=
        'change_engine_password', params={'password': password})