def guess_payload_class(self, payload):
    plen = len(payload)
    if plen > _NTP_AUTH_MD5_TAIL_SIZE:
        return NTPExtensions
    elif plen == _NTP_AUTH_MD5_TAIL_SIZE:
        return NTPAuthenticator
    return Packet.guess_payload_class(self, payload)