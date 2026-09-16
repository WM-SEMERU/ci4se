def parallel_snr_func(num, binary_args, phenomdwave, signal_type,
    noise_interpolants, prefactor, verbose):
    wave = phenomdwave(*binary_args)
    out_vals = {}
    for key in noise_interpolants:
        hn_vals = noise_interpolants[key](wave.freqs)
        snr_out = csnr(wave.freqs, wave.hc, hn_vals, wave.fmrg, wave.fpeak,
            prefactor=prefactor)
        if len(signal_type) == 1:
            out_vals[key + '_' + signal_type[0]] = snr_out[signal_type[0]]
        else:
            for phase in signal_type:
                out_vals[key + '_' + phase] = snr_out[phase]
    if verbose > 0 and (num + 1) % verbose == 0:
        print('Process ', num + 1, 'is finished.')
    return out_vals