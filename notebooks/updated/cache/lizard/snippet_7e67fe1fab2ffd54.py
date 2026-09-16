def tas2mach(Vtas, H):
    a = vsound(H)
    Mach = Vtas / a
    return Mach