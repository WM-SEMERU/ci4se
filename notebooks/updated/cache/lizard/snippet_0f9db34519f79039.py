def login(cls, username=None, password=None, requests_session=None,
    rate_limit=None):
    requests_session = requests_session or requests.Session()
    session = cls(requests_session, rate_limit)
    username = username or settings.USERNAME
    password = password or settings.PASSWORD
    session.do_login(username, password)
    return session