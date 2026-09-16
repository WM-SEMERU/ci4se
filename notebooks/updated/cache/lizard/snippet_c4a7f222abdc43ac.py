def playpause(self):
    msg = cr.Message()
    msg.type = cr.PLAYPAUSE
    self.send_message(msg)