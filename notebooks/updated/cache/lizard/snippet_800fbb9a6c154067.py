def Montillet_Akkari_Comiti(dp, voidage, vs, rho, mu, L=1, Dt=None):
    r
    Re = rho * vs * dp / mu
    if voidage < 0.4:
        a = 0.061
    else:
        a = 0.05
    if not Dt or Dt / dp > 50:
        Dterm = 2.2
    else:
        Dterm = (Dt / dp) ** 0.2
    right = a * Dterm * (1000.0 / Re + 60 / Re ** 0.5 + 12)
    left = dp / L / rho / vs ** 2 * voidage ** 3 / (1 - voidage)
    return right / left