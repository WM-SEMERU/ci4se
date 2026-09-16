def send_messages(self, sms_messages):
    if not sms_messages:
        return
    num_sent = 0
    for message in sms_messages:
        if self._send(message):
            num_sent += 1
    return num_sent