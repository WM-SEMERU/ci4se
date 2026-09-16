def add_handler(self, handler, args=None, kwargs=None):
    args = [] if args is None else args
    kwargs = {} if kwargs is None else kwargs
    handler_instance = handler(self, *args, **kwargs)
    if isinstance(handler_instance, RightsHandler):
        self.rights = handler_instance
    if handler_instance not in self.handlers:
        self.handlers.append(handler_instance)