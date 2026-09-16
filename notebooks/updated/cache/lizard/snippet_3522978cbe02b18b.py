def authenticate(api_key, api_url, **kwargs):
    muddle = Muddle(**kwargs)
    muddle.authenticate(api_key, api_url)
    return muddle