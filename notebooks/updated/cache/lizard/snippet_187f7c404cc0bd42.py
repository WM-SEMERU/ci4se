def send_text(self, text):
    return self.client.api.send_message(self.room_id, text)