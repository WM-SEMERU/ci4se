def delay(sig):
    smix = Streamix()
    sig = thub(sig, 3)
    smix.add(0, sig)
    smix.add(280 * ms, 0.1 * sig)
    smix.add(220 * ms, 0.1 * sig)
    return smix