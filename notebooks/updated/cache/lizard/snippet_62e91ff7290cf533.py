def fetch_blob(cls, username, password, multifactor_password=None,
    client_id=None):
    session = fetcher.login(username, password, multifactor_password, client_id
        )
    blob = fetcher.fetch(session)
    fetcher.logout(session)
    return blob