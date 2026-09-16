def maximum_violation(A_configuration, B_configuration, I, level, extra=None):
    P = Probability(A_configuration, B_configuration)
    objective = define_objective_with_I(I, P)
    if extra is None:
        extramonomials = []
    else:
        extramonomials = P.get_extra_monomials(extra)
    sdpRelaxation = SdpRelaxation(P.get_all_operators(), verbose=0)
    sdpRelaxation.get_relaxation(level, objective=objective, substitutions=
        P.substitutions, extramonomials=extramonomials)
    solve_sdp(sdpRelaxation)
    return sdpRelaxation.primal, sdpRelaxation.dual