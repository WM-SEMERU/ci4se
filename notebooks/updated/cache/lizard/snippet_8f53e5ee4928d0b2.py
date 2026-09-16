def get_attr_info(binary_view):
    global _ATTR_BASIC
    attr_type, attr_len, non_resident = _ATTR_BASIC.unpack(binary_view[:9])
    return AttrTypes(attr_type), attr_len, bool(non_resident)