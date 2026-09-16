def _visitor_impl(self, arg):
    if (_qualname(type(self)), type(arg)) in _methods:
        method = _methods[_qualname(type(self)), type(arg)]
        return method(self, arg)
    else:
        arg_parent_type = arg.__class__.__bases__[0]
        while arg_parent_type != object:
            if (_qualname(type(self)), arg_parent_type) in _methods:
                method = _methods[_qualname(type(self)), arg_parent_type]
                return method(self, arg)
            else:
                arg_parent_type = arg_parent_type.__bases__[0]
    raise VisitorException('No visitor found for class ' + str(type(arg)))