def pressision_try(orbitals, U, beta, step):
    mu, lam = main(orbitals, U, beta, step)
    mu2, lam2 = linspace(0, U * orbitals, step), zeros(step)
    for i in range(99):
        lam2[i + 1] = fsolve(restriction, lam2[i], (mu2[i + 1], orbitals, U,
            beta))
    plot(mu2, 2 * orbitals * fermi_dist(-(mu2 + lam2), beta), label=
        'Test guess')
    legend(loc=0)