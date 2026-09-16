def _visit_value_and_its_immediate_references(obj, visitor):
    typ = type(obj)
    if typ in _common_types:
        return
    if typ is list or issubclass(typ, (list, tuple)):
        for item in obj:
            _visit_value_and_its_immediate_references(item, visitor)
    elif issubclass(typ, dict):
        for key, value in iteritems(obj):
            _visit_value_and_its_immediate_references(key, visitor)
            _visit_value_and_its_immediate_references(value, visitor)
    elif issubclass(typ, HasProps):
        if issubclass(typ, Model):
            visitor(obj)
        else:
            _visit_immediate_value_references(obj, visitor)