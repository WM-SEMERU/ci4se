def get_param(par, args, m1, m2, s1z, s2z):
    if par == 'mchirp':
        parvals = conversions.mchirp_from_mass1_mass2(m1, m2)
    elif par == 'mtotal':
        parvals = m1 + m2
    elif par == 'eta':
        parvals = conversions.eta_from_mass1_mass2(m1, m2)
    elif par in ['chi_eff', 'effective_spin']:
        parvals = conversions.chi_eff(m1, m2, s1z, s2z)
    elif par == 'template_duration':
        parvals = pnutils.get_imr_duration(m1, m2, s1z, s2z, args.f_lower, 
            args.approximant or 'SEOBNRv4')
        if args.min_duration:
            parvals += args.min_duration
    elif par == 'tau0':
        parvals = conversions.tau0_from_mass1_mass2(m1, m2, args.f_lower)
    elif par == 'tau3':
        parvals = conversions.tau3_from_mass1_mass2(m1, m2, args.f_lower)
    elif par in pnutils.named_frequency_cutoffs.keys():
        parvals = pnutils.frequency_cutoff_from_name(par, m1, m2, s1z, s2z)
    else:
        parvals = pnutils.get_freq(par, m1, m2, s1z, s2z)
    return parvals