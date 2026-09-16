def pretty_json(data):
    data = json.loads(data.decode('utf-8'))
    return json.dumps(data, indent=4, sort_keys=True)