def get_chat_member(self, user_id):
    return self.bot.api_call('getChatMember', chat_id=str(self.id), user_id
        =str(user_id))