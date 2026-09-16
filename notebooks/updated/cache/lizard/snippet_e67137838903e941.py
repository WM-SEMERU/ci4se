def load(cls, fp, **kwargs):
    json_obj = json.load(fp, **kwargs)
    return parse(cls, json_obj)