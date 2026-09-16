def sanitize_for_serialization(self, obj):
    types = str, int, float, bool, tuple
    if sys.version_info < (3, 0):
        types = types + (unicode,)
    if isinstance(obj, type(None)):
        return None
    elif isinstance(obj, types):
        return obj
    elif isinstance(obj, list):
        return [self.sanitize_for_serialization(sub_obj) for sub_obj in obj]
    elif isinstance(obj, (datetime, date)):
        return obj.isoformat()
    else:
        if isinstance(obj, dict):
            obj_dict = obj
        else:
            obj_dict = {obj.attribute_map[attr]: getattr(obj, attr) for 
                attr, _ in iteritems(obj.swagger_types) if getattr(obj,
                attr) is not None}
        return {key: self.sanitize_for_serialization(val) for key, val in
            iteritems(obj_dict)}