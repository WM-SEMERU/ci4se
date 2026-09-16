def stop_message_live_location(self, chat_id=None, message_id=None,
    inline_message_id=None, reply_markup=None):
    return types.Message.de_json(apihelper.stop_message_live_location(self.
        token, chat_id, message_id, inline_message_id, reply_markup))