def pbkdf2(digestmod, password, salt, count, dk_length):

    def pbkdf2_function(pw, salt, count, i):
        r = u = hmac.new(pw, salt + struct.pack('>i', i), digestmod).digest()
        for i in range(2, count + 1):
            u = hmac.new(pw, u, digestmod).digest()
            r = bytes(i ^ j for i, j in zip(r, u))
        return r
    dk, h_length = b'', digestmod().digest_size
    blocks = dk_length // h_length + (1 if dk_length % h_length else 0)
    for i in range(1, blocks + 1):
        dk += pbkdf2_function(password, salt, count, i)
    return dk[:dk_length]