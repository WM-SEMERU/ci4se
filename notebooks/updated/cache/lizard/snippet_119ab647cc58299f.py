def ReadSerializedDict(cls, json_dict):
    if json_dict:
        json_object = cls._ConvertDictToObject(json_dict)
        if not isinstance(json_object, containers_interface.AttributeContainer
            ):
            raise TypeError('{0:s} is not an attribute container type.'.
                format(type(json_object)))
        return json_object
    return None