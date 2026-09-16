def _get_setter_fun(object_type, parameter, private_property_name):
    property_name = parameter.name
    overridden_setters = getmembers(object_type, _has_annotation(
        __SETTER_OVERRIDE_ANNOTATION, property_name))
    if len(overridden_setters) > 0:
        if len(overridden_setters) > 1:
            raise DuplicateOverrideError(
                'Setter is overridden more than once for attribute name : %s' %
                property_name)
        setter_fun = overridden_setters[0][1]
        try:
            setter_fun = setter_fun.im_func
        except AttributeError:
            pass
        s = signature(setter_fun)
        p = [attribute_name for attribute_name, param in s.parameters.items
            () if attribute_name is not 'self']
        if len(p) != 1:
            try:
                qname = setter_fun.__qualname__
            except AttributeError:
                qname = setter_fun.__name__
            raise IllegalSetterSignatureException(
                'overridden setter must have only 1 non-self argument, found '
                 + '%s for function %s' % (len(s.parameters.items()) - 1,
                qname))
        var_name = p[0]
    else:
        sig = Signature(parameters=[Parameter('self', kind=Parameter.
            POSITIONAL_OR_KEYWORD), parameter])

        @with_signature(sig)
        def autoprops_generated_setter(self, **kwargs):
            setattr(self, private_property_name, kwargs.popitem()[1])
        setter_fun = autoprops_generated_setter
        var_name = property_name
    return setter_fun, var_name