def send(self, sender: PytgbotApiBot):
    return sender.send_animation(animation=self.animation, chat_id=self.
        receiver, reply_to_message_id=self.reply_id, duration=self.duration,
        width=self.width, height=self.height, thumb=self.thumb, caption=
        self.caption, parse_mode=self.parse_mode, disable_notification=self
        .disable_notification, reply_markup=self.reply_markup)