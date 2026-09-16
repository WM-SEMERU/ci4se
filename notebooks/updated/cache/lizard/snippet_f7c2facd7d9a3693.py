def unban_chat_member(chat_id, user_id, **kwargs):
    params = dict(chat_id=chat_id, user_id=user_id)
    return TelegramBotRPCRequest('unbanChatMember', params=params,
        on_result=lambda result: result, **kwargs)