def _set_attrs_to_values(self, response={}):
    for key in response.keys():
        setattr(self, key, response[key])