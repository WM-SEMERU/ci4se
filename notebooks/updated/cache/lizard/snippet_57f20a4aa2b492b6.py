def _branch_flow_dc(self, branches, Bf, Pfinj, base_mva):
    il = array([i for i, l in enumerate(branches) if 0.0 < l.rate_a < 
        10000000000.0])
    lpf = -Inf * ones(len(il))
    rate_a = array([(l.rate_a / base_mva) for l in branches])
    upf = rate_a[il] - Pfinj[il]
    upt = rate_a[il] + Pfinj[il]
    Pf = LinearConstraint('Pf', Bf[(il), :], lpf, upf, ['Va'])
    Pt = LinearConstraint('Pt', -Bf[(il), :], lpf, upt, ['Va'])
    return Pf, Pt