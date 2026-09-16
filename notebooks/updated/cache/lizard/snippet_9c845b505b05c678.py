def register_next_step_handler(self, message, callback, *args, **kwargs):
    chat_id = message.chat.id
    self.register_next_step_handler_by_chat_id(chat_id, callback, *args, **
        kwargs)