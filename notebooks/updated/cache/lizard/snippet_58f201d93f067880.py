def mach2tas(Mach, H):
    a = vsound(H)
    Vtas = Mach * a
    return Vtas