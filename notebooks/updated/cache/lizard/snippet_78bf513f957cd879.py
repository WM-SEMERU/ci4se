def add(self, method_name, completeness=False, **fields):

    def class_decorator(class_obj):
        original_method = getattr(class_obj, method_name)
        if sys.version[0] == '2':
            original_method = original_method.im_func

        def caller(fn, obj, catalogue, config=None, *args, **kwargs):
            config = config or {}
            self.set_defaults(config, fields)
            self.check_config(config, fields)
            return fn(obj, catalogue, config, *args, **kwargs)
        new_method = decorator(caller, original_method)
        setattr(class_obj, method_name, new_method)
        instance = class_obj()
        func = functools.partial(new_method, instance)
        func.fields = fields
        func.model = instance
        func.completeness = completeness
        functools.update_wrapper(func, new_method)
        self[class_obj.__name__] = func
        return class_obj
    return class_decorator