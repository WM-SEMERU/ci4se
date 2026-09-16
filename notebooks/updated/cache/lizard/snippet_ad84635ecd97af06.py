def register_next_step_handler_by_chat_id(self, chat_id, callback, *args,
    **kwargs):
    if chat_id in self.next_step_handlers.keys():
        self.next_step_handlers[chat_id].append(Handler(callback, *args, **
            kwargs))
    else:
        self.next_step_handlers[chat_id] = [Handler(callback, *args, **kwargs)]
    if self.next_step_saver is not None:
        self.next_step_saver.start_save_timer()