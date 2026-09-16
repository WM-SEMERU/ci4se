def send(self, sender, recipients, cc=None, bcc=None, subject='', body='',
    attachments=None, content='text'):
    self._server.connect()
    self._server.send(sender, recipients, cc, bcc, subject, body,
        attachments, content)
    self._server.disconnect()
    return True