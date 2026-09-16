def parse_json(content):
    try:
        json_content = json.loads(content)
        return _recursive_strip(json_content)
    except json.JSONDecodeError:
        raise InvalidContent('content is not a json string.')