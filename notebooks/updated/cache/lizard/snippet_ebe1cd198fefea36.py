def change_status(self, status):

    def cb():
        self.user.update(status=status)
        return status
    return signals.user_update(self, ACTIONS['STATUS'], cb, data={'status':
        self.status})