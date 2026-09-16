def sample(self, bqm, beta_range=None, num_reads=10, num_sweeps=1000):
    if not isinstance(num_reads, int):
        raise TypeError("'samples' should be a positive integer")
    if num_reads < 1:
        raise ValueError("'samples' should be a positive integer")
    h, J, offset = bqm.to_ising()
    samples = []
    energies = []
    for __ in range(num_reads):
        sample, energy = ising_simulated_annealing(h, J, beta_range, num_sweeps
            )
        samples.append(sample)
        energies.append(energy)
    response = SampleSet.from_samples(samples, Vartype.SPIN, energies)
    response.change_vartype(bqm.vartype, offset, inplace=True)
    return response