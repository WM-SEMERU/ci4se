def is_module_function(obj, prop):
    python_version = sys.version_info[0]
    if python_version == 3:
        unicode = str
    if prop and (isinstance(prop, str) or isinstance(prop, unicode)):
        if prop in dir(obj):
            if isinstance(getattr(obj, prop), FunctionType) or isinstance(
                getattr(obj, prop), BuiltinFunctionType) or inspect.ismethod(
                getattr(obj, prop)):
                return True
            else:
                ErrorHandler.prop_is_func_error(obj, prop)
        else:
            ErrorHandler.prop_in_obj_error(obj, prop)
    elif prop:
        ErrorHandler.prop_type_error(prop)
    return False