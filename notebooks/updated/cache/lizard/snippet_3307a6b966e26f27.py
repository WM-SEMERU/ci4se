async def login(cls, url, *, username=None, password=None, insecure=False):
    profile = await helpers.login(url=url, username=username, password=
        password, insecure=insecure)
    session = cls(profile.description, profile.credentials)
    session.insecure = insecure
    return profile, session