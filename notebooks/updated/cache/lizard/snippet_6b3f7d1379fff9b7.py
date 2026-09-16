def store_property(url, property_name, value):
    logger.debug('store_property(): Received property_name=%s value=%s' % (
        property_name, value), url=url)
    ri = get_cached_or_new(url)
    ri._set_property(property_name, json.loads(value))
    logger.info('store_property(): property_name=%s saved.' % (
        property_name,), url=url)