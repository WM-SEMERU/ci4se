def get_hooks(self):
    if self.__hooks is None and self.hooks_class_name is not None:
        hooks_class = util.for_name(self.hooks_class_name)
        if not isinstance(hooks_class, type):
            raise ValueError(
                'hooks_class_name must refer to a class, got %s' % type(
                hooks_class).__name__)
        if not issubclass(hooks_class, hooks.Hooks):
            raise ValueError(
                'hooks_class_name must refer to a hooks.Hooks subclass')
        self.__hooks = hooks_class(self)
    return self.__hooks