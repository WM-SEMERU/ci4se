def _encode_ndef_uri_type(self, data):
    t = 0
    for code, prefix in uri_identifiers:
        if data[:len(prefix)].decode('latin-1').lower() == prefix:
            t = code
            data = data[len(prefix):]
            break
    data = yubico_util.chr_byte(t) + data
    return data