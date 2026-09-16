def loads(cls, s, **kwargs):
    json_obj = json.loads(s, **kwargs)
    return parse(cls, json_obj)