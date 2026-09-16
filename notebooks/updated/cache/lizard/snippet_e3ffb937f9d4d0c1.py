def send_sticker(self, sticker: str, reply: Message=None, on_success:
    callable=None, reply_markup: botapi.ReplyMarkup=None):
    self.twx.send_sticker(peer=self, sticker=sticker, reply_to_message_id=
        reply, on_success=on_success, reply_markup=reply_markup)