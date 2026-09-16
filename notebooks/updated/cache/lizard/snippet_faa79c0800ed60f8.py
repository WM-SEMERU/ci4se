def send(self, sender: PytgbotApiBot):
    return sender.send_game(game_short_name=self.game_short_name, chat_id=
        self.receiver, reply_to_message_id=self.reply_id,
        disable_notification=self.disable_notification, reply_markup=self.
        reply_markup)