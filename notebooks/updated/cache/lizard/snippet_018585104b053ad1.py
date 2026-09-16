def from_key(api_key, **kwargs):
    h = Heroku(**kwargs)
    h.authenticate(api_key)
    return h