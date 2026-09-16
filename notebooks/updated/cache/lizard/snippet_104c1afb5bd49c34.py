def get(key, service=None, profile=None):
    service = _get_service(service, profile)
    return keyring.get_password(service, key)