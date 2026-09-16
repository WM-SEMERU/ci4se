def register_channel_post_handler(self, callback, *custom_filters, commands
    =None, regexp=None, content_types=None, state=None, run_task=None, **kwargs
    ):
    filters_set = self.filters_factory.resolve(self.channel_post_handlers,
        *custom_filters, commands=commands, regexp=regexp, content_types=
        content_types, state=state, **kwargs)
    self.channel_post_handlers.register(self._wrap_async_task(callback,
        run_task), filters_set)