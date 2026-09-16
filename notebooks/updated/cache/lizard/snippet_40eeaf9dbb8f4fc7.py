def from_service_account_file(cls, filename, *args, **kwargs):
    credentials = service_account.Credentials.from_service_account_file(
        filename)
    kwargs['credentials'] = credentials
    return cls(*args, **kwargs)