def _equation_of_time(t):
    T = (t - Time('J2000')).to(u.year).value / 100
    poly_pars = 84381.448, 46.815, 0.00059, 0.001813
    eps = u.Quantity(polyval(T, poly_pars), u.arcsec)
    y = np.tan(eps / 2) ** 2
    poly_pars = 280.46646, 36000.76983, 0.0003032
    L0 = u.Quantity(polyval(T, poly_pars), u.deg)
    poly_pars = 357.52911, 35999.05029, 0.0001537
    M = u.Quantity(polyval(T, poly_pars), u.deg)
    poly_pars = 0.016708634, -4.2037e-05, -1.267e-07
    e = polyval(T, poly_pars)
    eot = (y * np.sin(2 * L0) - 2 * e * np.sin(M) + 4 * e * y * np.sin(M) *
        np.cos(2 * L0) - 0.5 * y ** 2 * np.sin(4 * L0) - 5 * e ** 2 * np.
        sin(2 * M) / 4) * u.rad
    return eot.to(u.hourangle)