def connect_xmlstream(jid, metadata, negotiation_timeout=60.0,
    override_peer=[], loop=None, logger=logger):
    loop = asyncio.get_event_loop() if loop is None else loop
    options = list(override_peer)
    exceptions = []
    result = yield from _try_options(options, exceptions, jid, metadata,
        negotiation_timeout, loop, logger)
    if result is not None:
        return result
    options = list((yield from discover_connectors(jid.domain, loop=loop,
        logger=logger)))
    result = yield from _try_options(options, exceptions, jid, metadata,
        negotiation_timeout, loop, logger)
    if result is not None:
        return result
    if not options and not override_peer:
        raise ValueError('no options to connect to XMPP domain {!r}'.format
            (jid.domain))
    for exc in exceptions:
        if isinstance(exc, errors.TLSFailure):
            raise exc
    raise errors.MultiOSError('failed to connect to XMPP domain {!r}'.
        format(jid.domain), exceptions)