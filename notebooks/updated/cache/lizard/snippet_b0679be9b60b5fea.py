def get_chat_administrators(self, chat_id):
    result = apihelper.get_chat_administrators(self.token, chat_id)
    ret = []
    for r in result:
        ret.append(types.ChatMember.de_json(r))
    return ret