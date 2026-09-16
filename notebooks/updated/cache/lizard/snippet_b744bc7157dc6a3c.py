def get_chat_from_phone_number(self, number, createIfNotFound=False):
    for chat in self.get_all_chats():
        if not isinstance(chat, UserChat) or number not in chat.id:
            continue
        return chat
    if createIfNotFound:
        self.create_chat_by_number(number)
        self.wait_for_login()
        for chat in self.get_all_chats():
            if not isinstance(chat, UserChat) or number not in chat.id:
                continue
            return chat
    raise ChatNotFoundError('Chat for phone {0} not found'.format(number))