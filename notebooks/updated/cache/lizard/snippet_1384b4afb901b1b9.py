def _get_specifications(specifications):
    if not specifications or specifications is object:
        raise ValueError('No specifications given')
    elif inspect.isclass(specifications):
        if Provides.USE_MODULE_QUALNAME:
            if sys.version_info < (3, 3, 0):
                raise ValueError(
                    'Qualified name capability requires Python 3.3+')
            if not specifications.__module__:
                return [specifications.__qualname__]
            return ['{0}.{1}'.format(specifications.__module__,
                specifications.__qualname__)]
        else:
            return [specifications.__name__]
    elif is_string(specifications):
        specifications = specifications.strip()
        if not specifications:
            raise ValueError('Empty specification given')
        return [specifications]
    elif isinstance(specifications, (list, tuple)):
        results = []
        for specification in specifications:
            results.extend(_get_specifications(specification))
        return results
    else:
        raise ValueError('Unhandled specifications type : {0}'.format(type(
            specifications).__name__))