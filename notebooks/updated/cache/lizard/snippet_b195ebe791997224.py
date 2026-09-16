def Reynolds(V, D, rho=None, mu=None, nu=None):
    r
    if rho and mu:
        nu = mu / rho
    elif not nu:
        raise Exception(
            'Either density and viscosity, or dynamic viscosity,         is needed'
            )
    return V * D / nu