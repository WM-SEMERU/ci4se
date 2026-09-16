def export_chat_invite_link(chat_id, **kwargs):
    params = dict(chat_id=chat_id)
    return TelegramBotRPCRequest('exportChatInviteLink', params=params,
        on_result=lambda result: result, **kwargs)