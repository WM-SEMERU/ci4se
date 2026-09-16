def autoescape(filter_func):

    @evalcontextfilter
    @wraps(filter_func)
    def _autoescape(eval_ctx, *args, **kwargs):
        result = filter_func(*args, **kwargs)
        if eval_ctx.autoescape:
            result = Markup(result)
        return result
    return _autoescape