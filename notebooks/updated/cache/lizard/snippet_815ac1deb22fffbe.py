def validate(self, csdl, service='facebook'):
    return self.request.post('validate', data=dict(csdl=csdl))