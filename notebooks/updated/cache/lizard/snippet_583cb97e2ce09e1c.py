def get_assessment_notification_session(self, assessment_receiver):
    if not self.supports_assessment_notification():
        raise errors.Unimplemented()
    return sessions.ItemNotificationSession(runtime=self._runtime, receiver
        =assessment_receiver)