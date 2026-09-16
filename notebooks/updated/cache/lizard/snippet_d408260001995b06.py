def b64encoded(self):
    if self._b64encoded:
        return text_type(self._b64encoded).strip('\r\n')
    else:
        return base64encode(self.raw)