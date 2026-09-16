def connect(token, protocol=RtmProtocol, factory=WebSocketClientFactory,
    factory_kwargs=None, api_url=None, debug=False):
    if factory_kwargs is None:
        factory_kwargs = dict()
    metadata = request_session(token, api_url)
    wsfactory = factory(metadata.url, **factory_kwargs)
    if debug:
        warnings.warn('debug=True has been deprecated in autobahn 0.14.0')
    wsfactory.protocol = lambda *a, **k: protocol(*a, **k)._seedMetadata(
        metadata)
    connection = connectWS(wsfactory)
    return connection