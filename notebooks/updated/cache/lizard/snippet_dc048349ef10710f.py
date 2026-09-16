def add_notification(self, notification):
    if notification.uuid in self.actions:
        logger.warning('Already existing notification: %s', notification)
        return
    logger.debug('Adding a notification: %s', notification)
    self.actions[notification.uuid] = notification
    self.nb_notifications += 1
    if notification.contact is not None:
        self.add(notification.get_initial_status_brok())