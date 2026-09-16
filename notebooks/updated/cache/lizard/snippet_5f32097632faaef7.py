def to_json(data, compress=False):
    return json.compress(data) if compress else json.dumps(data)