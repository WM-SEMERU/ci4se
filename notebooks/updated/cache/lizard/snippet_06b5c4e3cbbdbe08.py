def send_action(self, recipient_id, action, notification_type=
    NotificationType.regular):
    return self.send_recipient(recipient_id, {'sender_action': action},
        notification_type)