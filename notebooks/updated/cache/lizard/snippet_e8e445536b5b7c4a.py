def marshal_json(obj, types=JSON_TYPES, fields=None):
    return marshal_dict(obj, types, fields=fields)