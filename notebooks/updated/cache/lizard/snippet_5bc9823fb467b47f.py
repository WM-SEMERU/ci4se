def send_photo(self, photo, caption='', **options):
    return self.bot.api_call('sendPhoto', chat_id=str(self.id), photo=photo,
        caption=caption, **options)