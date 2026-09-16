def terminate_obsolete(self):
    chats_terminated = []
    live_chats = Chat.live.all()
    for live_chat in live_chats:
        if live_chat.is_obsolete(self.time_obsolete_offset):
            live_chat.terminate()
            live_chat.save()
            chats_terminated.append(live_chat)
    return chats_terminated