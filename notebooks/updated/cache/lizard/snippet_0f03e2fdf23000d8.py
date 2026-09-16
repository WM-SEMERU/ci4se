def cas2mach(Vcas, H):
    Vtas = cas2tas(Vcas, H)
    Mach = tas2mach(Vtas, H)
    return Mach