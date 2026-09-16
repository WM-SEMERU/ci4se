def operations(*operations):

    def decorator(method):

        def wrapper(cls, request, start_response, **kwargs):
            result_cache = []
            try:
                yield from method(cls, request, **kwargs)
            except Respond as e:
                status = e.status
                msg = utils.parse_return_annotation(method)[status]['message']
                if status / 100 == 2:
                    e.description = msg
                    raise e
                else:
                    raise CODES_TO_EXCEPTIONS[status](msg)
        method.swagger_ops = operations
        method.signature = inspect.signature(method)
        method.source = inspect.getsource(method)
        method.path_vars = utils.extract_pathvars(method)
        wrapper.__name__ = method.__name__
        wrapper.__doc__ = method.__doc__
        wrapper.__annotations__ = method.__annotations__
        wrapper.swagger_ops = method.swagger_ops
        wrapper.signature = method.signature
        wrapper.source = method.source
        wrapper.path_vars = method.path_vars
        return classmethod(wrapper)
    return decorator