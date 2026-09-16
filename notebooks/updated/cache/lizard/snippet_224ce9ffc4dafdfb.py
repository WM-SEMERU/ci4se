def GetAnnotatedMethods(cls):
    result = {}
    for i_cls in reversed(inspect.getmro(cls)):
        for name in compatibility.ListAttrs(i_cls):
            cls_method = getattr(i_cls, name)
            if not callable(cls_method):
                continue
            if not hasattr(cls_method, '__http_methods__'):
                continue
            result[name] = RouterMethodMetadata(name=name, doc=cls_method.
                __doc__, args_type=getattr(cls_method, '__args_type__',
                None), result_type=getattr(cls_method, '__result_type__',
                None), category=getattr(cls_method, '__category__', None),
                http_methods=getattr(cls_method, '__http_methods__', set()),
                no_audit_log_required=getattr(cls_method,
                '__no_audit_log_required__', False))
    return result