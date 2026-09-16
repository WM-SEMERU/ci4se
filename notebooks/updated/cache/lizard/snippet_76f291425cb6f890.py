def get_complete_ph_dos(partial_dos_path, phonopy_yaml_path):
    a = np.loadtxt(partial_dos_path).transpose()
    d = loadfn(phonopy_yaml_path)
    structure = get_structure_from_dict(d['primitive_cell'])
    total_dos = PhononDos(a[0], a[1:].sum(axis=0))
    pdoss = {}
    for site, pdos in zip(structure, a[1:]):
        pdoss[site] = pdos.tolist()
    return CompletePhononDos(structure, total_dos, pdoss)