def enable_encryption(self):
    try:
        self.send_state_event('m.room.encryption', {'algorithm':
            'm.megolm.v1.aes-sha2'})
        self.encrypted = True
        return True
    except MatrixRequestError:
        return False