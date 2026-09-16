def in6_getLocalUniquePrefix():
    tod = time.time()
    i = int(tod)
    j = int((tod - i) * 2 ** 32)
    tod = struct.pack('!II', i, j)
    mac = RandMAC()
    eui64 = inet_pton(socket.AF_INET6, '::' + in6_mactoifaceid(mac))[8:]
    import hashlib
    globalid = hashlib.sha1(tod + eui64).digest()[:5]
    return inet_ntop(socket.AF_INET6, b'\xfd' + globalid + b'\x00' * 10)