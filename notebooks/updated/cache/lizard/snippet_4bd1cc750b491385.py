async def get_buttons(self):
    if not self.buttons and self.reply_markup:
        chat = await self.get_input_chat()
        if not chat:
            return
        try:
            bot = self._needed_markup_bot()
        except ValueError:
            await self._reload_message()
            bot = self._needed_markup_bot()
        self._set_buttons(chat, bot)
    return self._buttons