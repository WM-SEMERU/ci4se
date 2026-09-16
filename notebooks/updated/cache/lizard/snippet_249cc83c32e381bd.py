def deserialize(json, cls=None):
    LOGGER.debug('deserialize(%s)', json)
    out = simplejson.loads(json)
    if isinstance(out, dict) and cls is not None:
        return cls(**out)
    return out