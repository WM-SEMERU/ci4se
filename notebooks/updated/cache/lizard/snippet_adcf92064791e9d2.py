def fcs(bits):
    fcs = FCS()
    for bit in bits:
        yield bit
        fcs.update_bit(bit)
    digest = bitarray(endian='little')
    digest.frombytes(fcs.digest())
    for bit in digest:
        yield bit