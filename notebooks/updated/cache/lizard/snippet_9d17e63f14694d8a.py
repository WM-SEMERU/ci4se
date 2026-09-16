def send_preview(self, recipients, personalize='fallback'):
    body = {'PreviewRecipients': [recipients] if isinstance(recipients, str
        ) else recipients, 'Personalize': personalize}
    response = self._post(self.uri_for('sendpreview'), json.dumps(body))