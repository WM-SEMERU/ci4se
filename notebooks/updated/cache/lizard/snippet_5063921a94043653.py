def return_type(rettype):

    def wrap(f):

        @functools.wraps(f)
        def converter(*pargs, **kwargs):
            result = f(*pargs, **kwargs)
            try:
                result = rettype(result)
            except ValueError as e:
                http_status(500, 'Return Value Conversion Failed')
                content_type('application/json')
                return {'error': str(e)}
            return result
        return converter
    return wrap