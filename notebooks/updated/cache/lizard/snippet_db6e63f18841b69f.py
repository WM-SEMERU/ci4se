def jsonify(obj, pretty=False):
    if pretty:
        params = dict(sort_keys=True, indent=2, allow_nan=False, separators
            =(',', ': '), ensure_ascii=False)
    else:
        params = dict(sort_keys=False, indent=None, allow_nan=False,
            separators=(',', ':'), ensure_ascii=False)
    try:
        return json.dumps(obj, **params)
    except (TypeError, ValueError) as error:
        LOGGER.critical(
            'The memote result structure is incompatible with the JSON standard.'
            )
        log_json_incompatible_types(obj)
        raise_with_traceback(error)