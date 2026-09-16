def dissolved_fardal_stream(hamiltonian, prog_orbit, prog_mass, t_disrupt,
    release_every=1, Integrator=DOPRI853Integrator, Integrator_kwargs=dict(
    ), snapshot_filename=None, output_every=1, seed=None):
    try:
        t = prog_orbit.t
    except AttributeError:
        raise TypeError(
            'Input progenitor orbit must be an Orbit subclass instance.')
    disrupt_ix = np.abs(t - t_disrupt).argmin()
    k_mean = np.zeros((t.size, 6))
    k_disp = np.zeros((t.size, 6))
    k_mean[:, (0)] = 2.0
    k_mean[disrupt_ix:, (0)] = 0.0
    k_disp[:, (0)] = 0.5
    k_mean[:, (1)] = 0.0
    k_disp[:, (1)] = 0.0
    k_mean[:, (2)] = 0.0
    k_disp[:, (2)] = 0.5
    k_mean[:, (3)] = 0.0
    k_disp[:, (3)] = 0.0
    k_mean[:, (4)] = 0.3
    k_disp[:, (4)] = 0.5
    k_mean[:, (5)] = 0.0
    k_disp[:, (5)] = 0.5
    return mock_stream(hamiltonian=hamiltonian, prog_orbit=prog_orbit,
        prog_mass=prog_mass, k_mean=k_mean, k_disp=k_disp, release_every=
        release_every, Integrator=Integrator, Integrator_kwargs=
        Integrator_kwargs, snapshot_filename=snapshot_filename,
        output_every=output_every, seed=seed)