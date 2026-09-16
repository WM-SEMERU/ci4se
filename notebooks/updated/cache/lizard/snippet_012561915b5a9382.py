def shipping_query_handler(self, *custom_filters, state=None, run_task=None,
    **kwargs):

    def decorator(callback):
        self.register_shipping_query_handler(callback, *custom_filters,
            state=state, run_task=run_task, **kwargs)
        return callback
    return decorator