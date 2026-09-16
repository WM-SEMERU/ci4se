def converts_to_proto(value, msg, raise_err=False):
    result = True
    try:
        dict_to_protobuf.dict_to_protobuf(value, msg)
    except TypeError as type_error:
        if raise_err:
            raise type_error
        result = False
    return result