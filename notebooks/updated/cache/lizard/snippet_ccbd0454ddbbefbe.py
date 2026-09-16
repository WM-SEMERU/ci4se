def send_notice(self, text):
    return self.client.api.send_notice(self.room_id, text)