def get_path_data(structure, mode='bradcrack', symprec=0.01, spg=None,
    line_density=60, cart_coords=False, kpt_list=None, labels=None, phonopy
    =False):
    r
    from sumo.symmetry import BradCrackKpath, SeekpathKpath, PymatgenKpath, CustomKpath
    spg = _get_space_group_object(spg, mode)
    if kpt_list:
        kpath = CustomKpath(structure, kpt_list, labels, symprec=symprec)
    elif mode == 'bradcrack':
        kpath = BradCrackKpath(structure, symprec=symprec, spg=spg)
    elif mode == 'seekpath':
        kpath = SeekpathKpath(structure, symprec=symprec)
    elif mode == 'pymatgen':
        kpath = PymatgenKpath(structure, symprec=symprec)
    kpoints, labels = kpath.get_kpoints(line_density=line_density, phonopy=
        phonopy)
    path_str = kpath.path_string
    kpt_dict = kpath.kpoints
    logging.info('Structure information:')
    logging.info('\tSpace group number: {}'.format(kpath._spg_data['number']))
    logging.info('\tInternational symbol: {}'.format(kpath.spg_symbol))
    logging.info('\tLattice type: {}'.format(kpath.lattice_type))
    logging.info('\nk-point path:\n\t{}'.format(path_str))
    logging.info('\nk-points:')
    for label, kpoint in iter(kpt_dict.items()):
        coord_str = ' '.join(['{}'.format(c) for c in kpoint])
        logging.info('\t{}: {}'.format(label, coord_str))
    return kpath, kpoints, labels