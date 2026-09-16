def feed_backend_arthur(backend_name, backend_params):
    feed_arthur()
    logger.debug('Items available for %s', arthur_items.keys())
    if not get_connector_from_name(backend_name):
        raise RuntimeError('Unknown backend %s' % backend_name)
    connector = get_connector_from_name(backend_name)
    klass = connector[3]
    backend_cmd = init_backend(klass(*backend_params))
    tag = backend_cmd.backend.tag
    logger.debug('Getting items for %s.', tag)
    if tag in arthur_items:
        logger.debug('Found items for %s.', tag)
        for item in arthur_items[tag]:
            yield item