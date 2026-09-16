def to_str(obj, encoding='utf-8', **encode_args):
    r
    if isinstance(obj, binary_type):
        return obj
    if isinstance(obj, text_type) or hasattr(obj, text_type_magicmethod):
        return text_type(obj).encode(encoding, **encode_args)
    return binary_type(obj)