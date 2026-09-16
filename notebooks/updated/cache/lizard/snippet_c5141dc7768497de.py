def __initialize_instance(self):
    config = self.config
    self.instance.auth = self.authentication_class(self.app, config=config)
    init_handlers = handlers if config.auth_mode(
        ) else auth_mode_agnostic_handlers
    for handler in init_handlers:
        if handler.keys is None:
            self.__check_method_in_auth(handler.name, handler.exception)
        elif all(map(config.get, handler.keys)):
            self.__check_method_in_auth(handler.name, handler.exception)
    for handler in init_handlers:
        if handler.name in self.kwargs:
            method = self.kwargs.pop(handler.name)
            setattr(self.instance.auth, handler.name, method)