def _get_bandgap_eigenval(eigenval_fname, outcar_fname):
    with open(outcar_fname, 'r') as f:
        parser = OutcarParser()
        nelec = next(iter(filter(lambda x: 'number of electrons' in x,
            parser.parse(f.readlines()))))['number of electrons']
    with open(eigenval_fname, 'r') as f:
        eigenval_info = list(EigenvalParser().parse(f.readlines()))
    all_energies = [zip(*x['energies']) for x in eigenval_info if 
        'energies' in x]
    spin_energies = zip(*all_energies)
    gaps = [VaspParser._get_bandgap_from_bands(x, nelec / 2.0) for x in
        spin_energies]
    return min(gaps)