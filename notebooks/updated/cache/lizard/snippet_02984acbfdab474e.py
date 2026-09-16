def json_description_metadata(description):
    if description[:6] == 'shape=':
        shape = tuple(int(i) for i in description[7:-1].split(','))
        return dict(shape=shape)
    if description[:1] == '{' and description[-1:] == '}':
        return json.loads(description)
    raise ValueError('invalid JSON image description', description)