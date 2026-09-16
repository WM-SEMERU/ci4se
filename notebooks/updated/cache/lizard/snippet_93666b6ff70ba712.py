def _read_or_calc_samples(sampler, modelidx=0, n_samples=100, last_step=
    False, e_range=None, e_npoints=100, threads=None):
    if not e_range:
        modelx, model = _process_blob(sampler, modelidx, last_step=last_step)
    else:
        e_range = validate_array('e_range', u.Quantity(e_range),
            physical_type='energy')
        e_unit = e_range.unit
        energy = np.logspace(np.log10(e_range[0].value), np.log10(e_range[1
            ].value), e_npoints) * e_unit
        data = {'energy': energy, 'flux': np.zeros(energy.shape) * sampler.
            data['flux'].unit}
        chain = sampler.chain[-1] if last_step else sampler.flatchain
        pars = chain[np.random.randint(len(chain), size=n_samples)]
        blobs = []
        p = Pool(threads)
        modelouts = p.map(partial(sampler.modelfn, data=data), pars)
        p.close()
        p.terminate()
        for modelout in modelouts:
            if isinstance(modelout, np.ndarray):
                blobs.append([modelout])
            else:
                blobs.append(modelout)
        modelx, model = _process_blob(blobs, modelidx=modelidx, energy=data
            ['energy'])
    return modelx, model