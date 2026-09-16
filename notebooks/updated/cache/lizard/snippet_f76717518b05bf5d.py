def json_dumps(obj):
    try:
        return json.dumps(obj, indent=2, sort_keys=True, allow_nan=False)
    except ValueError:
        pass
    json_str = json.dumps(obj, indent=2, sort_keys=True, allow_nan=True)
    json_obj = json.loads(json_str)

    def do_map(obj):
        if obj is None:
            return None
        if isinstance(obj, basestring):
            return obj
        if isinstance(obj, dict):
            res = {}
            for key, value in obj.items():
                res[key] = do_map(value)
            return res
        if isinstance(obj, collections.Iterable):
            res = []
            for el in obj:
                res.append(do_map(el))
            return res
        if math.isnan(obj):
            return 'NaN'
        if math.isinf(obj):
            return 'Infinity' if obj > 0 else '-Infinity'
        return obj
    return json.dumps(do_map(json_obj), indent=2, sort_keys=True, allow_nan
        =False)