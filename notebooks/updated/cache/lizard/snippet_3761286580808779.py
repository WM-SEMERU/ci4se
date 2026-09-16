def process_action(self):
    if self.publish_version == self.UNPUBLISH_CHOICE:
        actioned = self._unpublish()
    else:
        actioned = self._publish()
    if actioned:
        self._log_action()
    return actioned