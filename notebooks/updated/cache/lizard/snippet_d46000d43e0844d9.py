def _dehex(s):
    import re
    import binascii
    s = re.sub(b'[^a-fA-F\\d]', b'', s)
    return binascii.unhexlify(s)