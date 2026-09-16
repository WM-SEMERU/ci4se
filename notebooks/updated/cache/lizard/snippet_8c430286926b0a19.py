def _JRStaeckelIntegrandSquared(u, E, Lz, I3U, delta, u0, sinh2u0, v0,
    sin2v0, potu0v0, pot):
    sinh2u = nu.sinh(u) ** 2.0
    dU = (sinh2u + sin2v0) * potentialStaeckel(u, v0, pot, delta) - (sinh2u0 +
        sin2v0) * potu0v0
    return E * sinh2u - I3U - dU - Lz ** 2.0 / 2.0 / delta ** 2.0 / sinh2u