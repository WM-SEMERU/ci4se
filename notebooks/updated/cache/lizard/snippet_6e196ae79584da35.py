def is_classvar(tp):
    if NEW_TYPING:
        return tp is ClassVar or isinstance(tp, _GenericAlias
            ) and tp.__origin__ is ClassVar
    try:
        from typing import _ClassVar
        return type(tp) is _ClassVar
    except:
        return False