def PG_ISSO_solver(chi, incl):
    ci = math.cos(incl)
    sgnchi = np.sign(ci) * chi
    if sgnchi > 0.99:
        initial_guess = 2
    elif sgnchi < 0:
        initial_guess = 9
    else:
        initial_guess = 5
    rISCO_limit = scipy.optimize.fsolve(ISCO_eq, initial_guess, args=sgnchi)
    if chi < 0:
        initial_guess = 9
    else:
        initial_guess = 6
    rISSO_at_pole_limit = scipy.optimize.fsolve(ISSO_eq_at_pole,
        initial_guess, args=chi)
    if incl in [0, math.pi]:
        solution = rISCO_limit
    elif incl == math.pi / 2:
        solution = rISSO_at_pole_limit
    else:
        initial_guess = max(rISCO_limit, rISSO_at_pole_limit)
        solution = scipy.optimize.fsolve(PG_ISSO_eq, initial_guess, args=(
            chi, ci))
        if solution < 1 or solution > 9:
            initial_guess = min(rISCO_limit, rISSO_at_pole_limit)
            solution = scipy.optimize.fsolve(PG_ISSO_eq, initial_guess,
                args=(chi, ci))
    return solution