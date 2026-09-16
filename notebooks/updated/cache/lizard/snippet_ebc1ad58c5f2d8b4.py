def _has_argument(func):
    if hasattr(inspect, 'signature'):
        sig = inspect.signature(func)
        return bool(sig.parameters)
    else:
        return bool(inspect.getargspec(func).args)