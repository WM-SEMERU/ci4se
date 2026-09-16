def segwit_encode(hrp, witver, witprog):
    ret = bech32_encode(hrp, [witver] + convertbits(witprog, 8, 5))
    if segwit_decode(hrp, ret) == (None, None):
        return None
    return ret