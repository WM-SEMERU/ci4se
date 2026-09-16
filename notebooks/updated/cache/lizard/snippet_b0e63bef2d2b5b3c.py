def function_invocation_proxy(fn, proxy_args, proxy_kwargs):
    try:
        return fn(*proxy_args, **proxy_kwargs)
    except TypeError:
        return bool(fn)