def kick_user(self, user_id, reason=''):
    try:
        self.client.api.kick_user(self.room_id, user_id)
        return True
    except MatrixRequestError:
        return False