def render_template(template):

    def outer_wrapper(callable_or_dict=None, statuscode=None, **kwargs):

        def wrapper(request, *args, **wrapper_kwargs):
            if callable(callable_or_dict):
                params = callable_or_dict(request, *args, **wrapper_kwargs)
            else:
                params = callable_or_dict
            if params is None or isinstance(params, dict):
                resp = render(request, template, params, **kwargs)
            else:
                resp = params
            if statuscode:
                resp.status_code = statuscode
            return resp
        return wrapper
    return outer_wrapper