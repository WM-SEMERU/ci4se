def get_email_message(self, message_uid, message_type='text/plain'):
    self._mail.select('inbox')
    result = self._mail.uid('fetch', message_uid, '(RFC822)')
    msg = email.message_from_string(result[1][0][1])
    try:
        for part in msg.walk():
            if part.get_content_type() == message_type:
                return part.get_payload(decode=True)
    except:
        return msg.get_payload(decode=True)