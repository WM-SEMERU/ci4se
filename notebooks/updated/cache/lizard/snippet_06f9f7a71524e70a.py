def send_text(self, text):
    if not self.is_token_set:
        raise ValueError('TelepythClient: Access token is not set!')
    stream = StringIO()
    stream.write(text)
    stream.seek(0)
    return self(stream)