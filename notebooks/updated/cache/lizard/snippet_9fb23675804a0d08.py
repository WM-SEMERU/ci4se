async def login(cls, url, *, username=None, password=None, insecure=False):
    profile, session = await bones.SessionAPI.login(url=url, username=
        username, password=password, insecure=insecure)
    return profile, cls(session)