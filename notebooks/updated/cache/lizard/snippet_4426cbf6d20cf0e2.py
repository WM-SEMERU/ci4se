def _get_all_objs_of_type(type_, parent):
    return set([obj for obj in parent.__dict__.values() if isinstance(obj,
        type_)])