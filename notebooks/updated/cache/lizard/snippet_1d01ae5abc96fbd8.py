def set_root_path(self, root_path=None, settings_module=None):
    if root_path:
        self.root_path = root_path
        return
    if settings_module:
        self.root_path = os.path.dirname(os.path.abspath(settings_module.
            __file__))
        return
    import inspect
    caller = inspect.stack()[1]
    caller_module = inspect.getmodule(caller[0])
    assert hasattr(caller_module, '__file__'
        ), 'Caller module %s should have __file__ attr' % caller_module
    self.root_path = os.path.dirname(os.path.abspath(caller_module.__file__))