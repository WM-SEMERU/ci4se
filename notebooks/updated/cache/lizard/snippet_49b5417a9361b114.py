def send_voice(self, voice, **options):
    return self.bot.api_call('sendVoice', chat_id=str(self.id), voice=voice,
        **options)