def get_origin(tp):
    if NEW_TYPING:
        if isinstance(tp, _GenericAlias):
            return tp.__origin__ if tp.__origin__ is not ClassVar else None
        if tp is Generic:
            return Generic
        return None
    if isinstance(tp, GenericMeta):
        return _gorg(tp)
    if is_union_type(tp):
        return Union
    return None