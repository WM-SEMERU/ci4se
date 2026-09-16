def deserialize(cls, cls_target, obj_raw):
    cls._initialize()
    deserializer = cls._get_deserializer(cls_target)
    if deserializer == cls:
        return cls._deserialize_default(cls_target, obj_raw)
    else:
        return deserializer.deserialize(cls_target, obj_raw)