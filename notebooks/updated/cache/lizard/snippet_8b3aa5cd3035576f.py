def get_body_encoding(self):
    assert self.body_encoding != SHORTEST
    if self.body_encoding == QP:
        return 'quoted-printable'
    elif self.body_encoding == BASE64:
        return 'base64'
    else:
        return encode_7or8bit