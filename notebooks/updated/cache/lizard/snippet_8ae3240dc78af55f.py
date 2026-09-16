def from_prev_calc(cls, prev_calc_dir, copy_chgcar=True, nbands_factor=1.2,
    standardize=False, sym_prec=0.1, international_monoclinic=True,
    reciprocal_density=100, kpoints_line_density=20, small_gap_multiply=
    None, **kwargs):
    vasprun, outcar = get_vasprun_outcar(prev_calc_dir)
    incar = vasprun.incar
    structure = get_structure_from_prev_run(vasprun, outcar, sym_prec=
        standardize and sym_prec, international_monoclinic=
        international_monoclinic)
    if outcar and outcar.magnetization:
        site_magmom = np.array([i['tot'] for i in outcar.magnetization])
        ispin = 2 if np.any(site_magmom[np.abs(site_magmom) > 0.02]) else 1
    elif vasprun.is_spin:
        ispin = 2
    else:
        ispin = 1
    nbands = int(np.ceil(vasprun.parameters['NBANDS'] * nbands_factor))
    incar.update({'ISPIN': ispin, 'NBANDS': nbands})
    files_to_transfer = {}
    if standardize:
        warnings.warn(
            'Use of standardize=True with from_prev_run is not recommended as there is no guarantee the copied files will be appropriate for the standardized structure. copy_chgcar is enforced to be false.'
            )
        copy_chgcar = False
    if copy_chgcar:
        chgcars = sorted(glob.glob(str(Path(prev_calc_dir) / 'CHGCAR*')))
        if chgcars:
            files_to_transfer['CHGCAR'] = str(chgcars[-1])
    if small_gap_multiply:
        gap = vasprun.eigenvalue_band_properties[0]
        if gap <= small_gap_multiply[0]:
            reciprocal_density = reciprocal_density * small_gap_multiply[1]
            kpoints_line_density = kpoints_line_density * small_gap_multiply[1]
    return cls(structure=structure, prev_incar=incar, reciprocal_density=
        reciprocal_density, kpoints_line_density=kpoints_line_density,
        files_to_transfer=files_to_transfer, **kwargs)