def bit_clone(bits):
    new = BitSet(bits.size)
    new.ior(bits)
    return new