def solve_loop(slsp, u_span, j_coup):
    zet, lam, eps, hlog, mean_f = [], [], [], [], [None]
    for u in u_span:
        print(u, j_coup)
        hlog.append(slsp.selfconsistency(u, j_coup, mean_f[-1]))
        mean_f.append(slsp.mean_field())
        zet.append(slsp.quasiparticle_weight())
        lam.append(slsp.param['lambda'])
        eps.append(orbital_energies(slsp.param, zet[-1]))
    return np.asarray([zet, lam, eps]), hlog, mean_f