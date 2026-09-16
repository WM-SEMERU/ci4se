def get_api_required_params(self):
    result = self.required_params
    if type(result) != list:
        raise ValueError('{}.required_params should return list'.format(
            self.__class__.__name__))
    return result