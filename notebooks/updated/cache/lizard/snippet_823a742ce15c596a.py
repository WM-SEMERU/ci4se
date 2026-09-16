def newkeys(nbits=1024):
    pubkey, privkey = rsa.newkeys(nbits, poolsize=1)
    return pubkey, privkey