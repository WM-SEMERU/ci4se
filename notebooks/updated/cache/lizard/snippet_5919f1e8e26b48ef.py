def _register_hook(hook_name, target, func, *args, **kwargs):
    call = func, args, kwargs
    try:
        getattr(target, hook_name).append(call)
    except AttributeError:
        setattr(target, hook_name, [call])