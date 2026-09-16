def clear_step_handler(self, message):
    chat_id = message.chat.id
    self.clear_step_handler_by_chat_id(chat_id)