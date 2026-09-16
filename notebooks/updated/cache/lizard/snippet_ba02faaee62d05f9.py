def get_item_notification_session_for_bank(self, item_receiver, bank_id):
    if not self.supports_item_notification():
        raise errors.Unimplemented()
    return sessions.ItemNotificationSession(bank_id, runtime=self._runtime,
        receiver=item_receiver)