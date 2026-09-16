def main_execute(expr, params=None, scope=None, aggcontext=None, **kwargs):
    if scope is None:
        scope = {}
    if params is None:
        params = {}
    params = {(k.op() if hasattr(k, 'op') else k): v for k, v in params.items()
        }
    new_scope = toolz.merge(scope, params)
    return execute_with_scope(expr, new_scope, aggcontext=aggcontext, **kwargs)