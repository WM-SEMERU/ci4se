def hook_decorator(cb_type):

    def decorator_wrapper(*tags_or_func):
        if len(tags_or_func) == 1 and callable(tags_or_func[0]):
            func = tags_or_func[0]
            return HookImpl(cb_type, func)
        else:
            tags = tags_or_func

            def d(func):
                return HookImpl(cb_type, func, tags)
            return d
    return decorator_wrapper