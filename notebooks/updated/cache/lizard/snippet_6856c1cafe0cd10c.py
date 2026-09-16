def send_message(self, chat_id, text, **options):
    return self.api_call('sendMessage', chat_id=chat_id, text=text, **options)