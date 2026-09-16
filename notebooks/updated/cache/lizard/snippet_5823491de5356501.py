def message_handler(self, *custom_filters, commands=None, regexp=None,
    content_types=None, state=None, run_task=None, **kwargs):

    def decorator(callback):
        self.register_message_handler(callback, *custom_filters, commands=
            commands, regexp=regexp, content_types=content_types, state=
            state, run_task=run_task, **kwargs)
        return callback
    return decorator