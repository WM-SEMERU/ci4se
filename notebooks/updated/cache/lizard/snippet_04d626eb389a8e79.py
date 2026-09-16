def send_chat_action(self, action):
    return self.bot.api_call('sendChatAction', chat_id=self.id, action=action)