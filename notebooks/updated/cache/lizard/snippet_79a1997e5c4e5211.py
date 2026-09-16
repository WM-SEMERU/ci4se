def attach_binary(self, content, filename):
    content_type = guess_content_type(filename)
    payload = {'Name': filename, 'Content': b64encode(content).decode(
        'utf-8'), 'ContentType': content_type}
    self.attach(payload)