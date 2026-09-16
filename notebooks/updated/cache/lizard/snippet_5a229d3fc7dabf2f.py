def vMh2_to_m2Lambda(v, Mh2, C):
    if C['phi'] == 0 and C['phiBox'] == 0 and C['phiD'] == 0:
        return _vMh2_to_m2Lambda_SM(v, Mh2)
    else:

        def f0(x):
            m2, Lambda = x
            d = m2Lambda_to_vMh2(m2=m2.real, Lambda=Lambda.real, C=C)
            return np.array([d['v'] - v, d['Mh2'] - Mh2])
        dSM = _vMh2_to_m2Lambda_SM(v, Mh2)
        x0 = np.array([dSM['m2'], dSM['Lambda']])
        try:
            xres = scipy.optimize.newton_krylov(f0, x0)
        except (scipy.optimize.nonlin.NoConvergence, ValueError) as e:
            warnings.warn(
                'Standard optimization method did not converge. The GMRES method is used instead.'
                , Warning)
            try:
                xres = scipy.optimize.newton_krylov(f0, x0, method='gmres',
                    f_tol=1e-07)
            except (scipy.optimize.nonlin.NoConvergence, ValueError) as e:
                raise ValueError(
                    'No solution for m^2 and Lambda found. This problem can be caused by very large values for one or several Wilson coefficients.'
                    )
        return {'m2': xres[0], 'Lambda': xres[1]}