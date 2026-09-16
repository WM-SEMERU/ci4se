def subword(w):
    w = w.reshape(4, 8)
    return SBOX[w[0]] + SBOX[w[1]] + SBOX[w[2]] + SBOX[w[3]]