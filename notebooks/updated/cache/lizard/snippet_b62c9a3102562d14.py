def format(self, member_info: bool=False):
    user = self.api_object
    self.__format_user(user)
    if member_info and self.chat.type != CHAT_TYPE_PRIVATE:
        self._add_empty()
        self.__format_member(user)