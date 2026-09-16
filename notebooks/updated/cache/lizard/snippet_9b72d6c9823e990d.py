def send(self, email, attachments=()):
    msg = email.as_mime(attachments)
    if 'From' not in msg:
        msg['From'] = self.sender_address()
    if self._conn:
        self._conn.sendmail(self.username, email.recipients, msg.as_string())
    else:
        with self:
            self._conn.sendmail(self.username, email.recipients, msg.
                as_string())