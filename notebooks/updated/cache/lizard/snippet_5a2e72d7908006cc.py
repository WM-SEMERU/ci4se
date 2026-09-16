def send_audio_url(self, recipient_id, audio_url, notification_type=
    NotificationType.regular):
    return self.send_attachment_url(recipient_id, 'audio', audio_url,
        notification_type)