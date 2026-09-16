def send_chat_action(self, chat_id: Union[int, str], action: Union[
    ChatAction, str], progress: int=0):
    if isinstance(action, str):
        action = ChatAction.from_string(action).value
    elif isinstance(action, ChatAction):
        action = action.value
    if 'Upload' in action.__name__:
        action = action(progress=progress)
    else:
        action = action()
    return self.send(functions.messages.SetTyping(peer=self.resolve_peer(
        chat_id), action=action))