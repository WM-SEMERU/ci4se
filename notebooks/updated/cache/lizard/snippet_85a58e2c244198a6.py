def Domanski_Didion(x, rhol, rhog, mul, mug):
    r
    Xtt = Lockhart_Martinelli_Xtt(x, rhol, rhog, mul, mug)
    if Xtt < 10:
        return (1 + Xtt ** 0.8) ** -0.378
    else:
        return 0.823 - 0.157 * log(Xtt)