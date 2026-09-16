def _iparam_objectname(objectname, arg_name):
    if isinstance(objectname, (CIMClassName, CIMInstanceName)):
        objectname = objectname.copy()
        objectname.host = None
        objectname.namespace = None
    elif isinstance(objectname, six.string_types):
        objectname = CIMClassName(objectname)
    elif objectname is None:
        pass
    else:
        raise TypeError(_format(
            'The {0!A} argument of the WBEMConnection operation has invalid type {1} (must be None, a string, a CIMClassName, or a CIMInstanceName)'
            , arg_name, type(objectname)))
    return objectname