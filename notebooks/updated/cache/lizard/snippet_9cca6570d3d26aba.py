def mock_session_with_class(session, cls, url):
    _orig_adapters = session.adapters
    mock_adapter = adapter.ClassAdapter(cls)
    session.adapters = OrderedDict()
    if isinstance(url, (list, tuple)):
        for u in url:
            session.mount(u, mock_adapter)
    else:
        session.mount(url, mock_adapter)
    yield
    session.adapters = _orig_adapters