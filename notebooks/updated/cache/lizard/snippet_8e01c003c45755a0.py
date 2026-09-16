def find_method(func):

    def wrapped(*args, **kwargs):
        if len(args) == 3 and func.__name__ in ('find', 'find_one',
            'find_by_id', 'find_by_ids'):
            _param_fields(kwargs, args[2])
            args = args[0], args[1]
        elif 'fields' in kwargs:
            _param_fields(kwargs, kwargs['fields'])
            del kwargs['fields']
        elif 'projection' in kwargs:
            _param_fields(kwargs, kwargs['projection'])
        if 'timeout' in kwargs:
            kwargs['no_cursor_timeout'] = not bool(kwargs['timeout'])
            del kwargs['timeout']
        if 'spec' in kwargs:
            kwargs['filter'] = kwargs['spec']
            del kwargs['spec']
        if kwargs.get('return_document') == 'after':
            kwargs['return_document'] = ReturnDocument.AFTER
        elif kwargs.get('return_document') == 'before':
            kwargs['return_document'] = ReturnDocument.BEFORE
        ret = func(*args, **kwargs)
        if kwargs.get('json'):
            ret = json_clone(ret)
        return ret
    return wrapped