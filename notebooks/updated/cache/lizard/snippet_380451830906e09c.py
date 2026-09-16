def decrypt_text(self, text, *args, **kwargs):
    b = text.encode('utf-8')
    token = base64.b64decode(b)
    return self.decrypt(token, *args, **kwargs).decode('utf-8')