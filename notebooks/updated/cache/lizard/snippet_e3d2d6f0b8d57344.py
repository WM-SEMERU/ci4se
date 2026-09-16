def get_drive_api_from_client_secrets(path, reset_creds=False):
    storage = keyring_storage.Storage('tarbell', getpass.getuser())
    credentials = None
    if not reset_creds:
        credentials = storage.get()
    if path and not credentials:
        flow = client.flow_from_clientsecrets(path, scope=OAUTH_SCOPE)
        credentials = tools.run_flow(flow, storage, flags)
        storage.put(credentials)
    return _get_drive_api(credentials)