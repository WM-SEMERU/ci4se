def singleton(cls, session, include=None):
    params = build_request_include(include, None)
    url = session._build_url(cls._resource_path())
    process = cls._mk_one(session, singleton=True, include=include)
    return session.get(url, CB.json(200, process), params=params)