def from_json(payload):
    if payload is None:
        return None
    if isinstance(payload, dict):
        return Object(**dict([(k, v if not isinstance(v, (dict, list)) else
            Object.from_json(v)) for k, v in payload.iteritems()]))
    elif isinstance(payload, list):
        return payload and [(Object.from_json(v) if isinstance(v, (dict,
            list)) else v) for v in payload]
    else:
        raise ValueError('The payload MUST be a dictionary or a list')