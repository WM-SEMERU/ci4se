def from_private_key(account_name, private_key=None, private_key_path=None,
    storage=None, storage_path=None, api_version='v3', readonly=False,
    http_client=None, ga_hook=None):
    if not private_key:
        if not private_key_path:
            raise GapyError(
                'Must provide either a private_key or a private_key_file')
        if isinstance(private_key_path, basestring):
            private_key_path = open(private_key_path)
        private_key = private_key_path.read()
    storage = _get_storage(storage, storage_path)
    scope = GOOGLE_API_SCOPE_READONLY if readonly else GOOGLE_API_SCOPE
    credentials = SignedJwtAssertionCredentials(account_name, private_key,
        scope)
    credentials.set_store(storage)
    return Client(_build(credentials, api_version, http_client), ga_hook)