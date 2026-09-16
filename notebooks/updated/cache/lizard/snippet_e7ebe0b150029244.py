def verify_method(target, method_name, class_level=False):
    attr = target.get_attr(method_name)
    if not attr:
        raise VerifyingDoubleError(method_name, target.doubled_obj
            ).no_matching_method()
    if attr.kind == 'data' and not isbuiltin(attr.object) and not is_callable(
        attr.object):
        raise VerifyingDoubleError(method_name, target.doubled_obj
            ).not_callable()
    if class_level and attr.kind == 'method' and method_name != '__new__':
        raise VerifyingDoubleError(method_name, target.doubled_obj
            ).requires_instance()