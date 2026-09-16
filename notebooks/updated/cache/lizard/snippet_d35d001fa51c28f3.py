def send_video(self, video, caption='', **options):
    return self.bot.api_call('sendVideo', chat_id=str(self.id), video=video,
        caption=caption, **options)