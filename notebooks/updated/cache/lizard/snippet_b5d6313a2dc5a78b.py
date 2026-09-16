def _ipv4_text_to_int(self, ip_text):
    if ip_text is None:
        return None
    assert isinstance(ip_text, str)
    return struct.unpack('!I', addrconv.ipv4.text_to_bin(ip_text))[0]