def pbkdf2_bin(data, salt, iterations=1000, keylen=24, hashfunc=None):
    hashfunc = hashfunc or hashlib.sha1
    mac = hmac.new(bytes_(data), None, hashfunc)

    def _pseudorandom(x, mac=mac):
        h = mac.copy()
        h.update(bytes_(x))
        if not PY2:
            return [x for x in h.digest()]
        else:
            return map(ord, h.digest())
    buf = []
    for block in range_(1, -(-keylen // mac.digest_size) + 1):
        rv = u = _pseudorandom(bytes_(salt) + _pack_int(block))
        for i in range_(iterations - 1):
            if not PY2:
                u = _pseudorandom(bytes(u))
            else:
                u = _pseudorandom(''.join(map(chr, u)))
            rv = starmap(xor, zip(rv, u))
        buf.extend(rv)
    if not PY2:
        return bytes(buf)[:keylen]
    else:
        return ''.join(map(chr, buf))[:keylen]