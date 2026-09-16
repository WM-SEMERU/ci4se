def get_client(key, project):
    cred = get_storage_credentials(key)
    return storage.Client(project=project, credentials=cred)