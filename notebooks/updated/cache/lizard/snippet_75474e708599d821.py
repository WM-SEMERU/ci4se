def importable(obj):
    try:
        return look_up(object_name(obj)) is obj
    except (AttributeError, TypeError, ImportError):
        return False