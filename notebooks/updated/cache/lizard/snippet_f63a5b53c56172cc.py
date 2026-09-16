def class_register(cls):
    cls.handler_registry = {}
    cls.sender_registry = {}
    for method_name in dir(cls):
        method = getattr(cls, method_name)
        if hasattr(method, '_handle'):
            cls.handler_registry.update({method._handle: method_name})
        if hasattr(method, '_sends'):
            cls.sender_registry.update({method._sends: method_name})
    return cls