def decode(self, a_bytes, encoding):
    try:
        return a_bytes.decode(encoding), encoding
    except Exception as e:
        ind = self.catch_position_in_UnicodeDecodeError_message(str(e))
        return a_bytes[:ind].decode(encoding) + self.decode(a_bytes[ind + 2
            :], encoding)[0], encoding