def send_signature_reminder(self, signature_id):
    connection = Connection(self.token)
    connection.set_url(self.production, self.SIGNS_SEND_REMINDER_URL %
        signature_id)
    return connection.post_request()