def enabled(self):
    if not self._notification_enabled:
        self._notification_enabled = self.notification_model.enabled
    return self._notification_enabled