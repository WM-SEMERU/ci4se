def send(self, sender: PytgbotApiBot):
    return sender.send_chat_action(action=self.action, chat_id=self.receiver)