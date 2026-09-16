def list(cls, params=None):
    return fields.ListField(name=cls.ENDPOINT, init_class=cls).decode(cls.
        element_from_string(cls._get_request(params=params).text))