def compress(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), cls=
        CustomEncoder)