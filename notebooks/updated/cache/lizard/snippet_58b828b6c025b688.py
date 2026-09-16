def check_lazy_load_gemeente(f):

    def wrapper(*args):
        gemeente = args[0]
        if (gemeente._centroid is None or gemeente._bounding_box is None or
            gemeente._taal_id is None or gemeente._metadata is None):
            log.debug('Lazy loading Gemeente %d', gemeente.id)
            gemeente.check_gateway()
            g = gemeente.gateway.get_gemeente_by_id(gemeente.id)
            gemeente._taal_id = g._taal_id
            gemeente._centroid = g._centroid
            gemeente._bounding_box = g._bounding_box
            gemeente._metadata = g._metadata
        return f(*args)
    return wrapper