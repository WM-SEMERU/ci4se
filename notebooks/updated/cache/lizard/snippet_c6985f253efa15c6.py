def get_chat_members_count(self, chat_id):
    result = apihelper.get_chat_members_count(self.token, chat_id)
    return result