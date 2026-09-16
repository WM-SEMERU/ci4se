def _method(self, *args, **kwargs):
    yield self.resource_handler.handle(self.__resource_view_type__, *args,
        **kwargs)