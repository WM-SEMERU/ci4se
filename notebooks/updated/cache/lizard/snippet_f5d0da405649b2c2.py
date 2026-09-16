def get_final_from_initial(mass1, mass2, spin1x=0.0, spin1y=0.0, spin1z=0.0,
    spin2x=0.0, spin2y=0.0, spin2z=0.0, approximant='SEOBNRv4'):
    args = mass1, mass2, spin1x, spin1y, spin1z, spin2x, spin2y, spin2z
    args = ensurearray(*args)
    input_is_array = args[-1]
    origshape = args[0].shape
    args = [a.ravel() for a in args[:-1]]
    mass1, mass2, spin1x, spin1y, spin1z, spin2x, spin2y, spin2z = args
    final_mass = numpy.zeros(mass1.shape)
    final_spin = numpy.zeros(mass1.shape)
    for ii in range(final_mass.size):
        m1 = mass1[ii]
        m2 = mass2[ii]
        spin1 = [spin1x[ii], spin1y[ii], spin1z[ii]]
        spin2 = [spin2x[ii], spin2y[ii], spin2z[ii]]
        _, fm, fs = lalsim.SimIMREOBFinalMassSpin(m1, m2, spin1, spin2,
            getattr(lalsim, approximant))
        final_mass[ii] = fm * (m1 + m2)
        final_spin[ii] = fs
    final_mass = final_mass.reshape(origshape)
    final_spin = final_spin.reshape(origshape)
    return formatreturn(final_mass, input_is_array), formatreturn(final_spin,
        input_is_array)