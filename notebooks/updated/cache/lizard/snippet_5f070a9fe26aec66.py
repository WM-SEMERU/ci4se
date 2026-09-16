def to_web(self, host=None, user=None, password=None):
    response = pybel.to_web(self.model, host=host, user=user, password=password
        )
    return response