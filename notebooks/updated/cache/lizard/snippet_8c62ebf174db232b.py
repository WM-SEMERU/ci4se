def register_pre_checkout_query_handler(self, callback, *custom_filters,
    state=None, run_task=None, **kwargs):
    filters_set = self.filters_factory.resolve(self.
        pre_checkout_query_handlers, *custom_filters, state=state, **kwargs)
    self.pre_checkout_query_handlers.register(self._wrap_async_task(
        callback, run_task), filters_set)