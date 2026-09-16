def remove_notification_listener(self, notification_id):
    for v in self.notifications.values():
        toRemove = list(filter(lambda tup: tup[0] == notification_id, v))
        if len(toRemove) > 0:
            v.remove(toRemove[0])
            return True
    return False