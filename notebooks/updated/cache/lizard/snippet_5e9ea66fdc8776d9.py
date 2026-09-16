def encode_params(params, **kwargs):
    cleaned = clean_params(params, **kwargs)
    return json.dumps(cleaned)