def parse_bookmark_json(data):
    for entry in data['roots'].values():
        for url, name in parse_bookmark_node(entry):
            yield url, name