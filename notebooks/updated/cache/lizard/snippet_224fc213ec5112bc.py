def _serialize_default(cls, obj):
    if obj is None or cls._is_primitive(obj):
        return obj
    elif cls._is_bytes(obj):
        return obj.decode()
    elif type(obj) == list:
        return cls._serialize_list(obj)
    else:
        dict_ = cls._get_obj_raw(obj)
        return cls._serialize_dict(dict_)