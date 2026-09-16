def _path(cls, ndivsm, structure=None, kpath_bounds=None, comment=None):
    if kpath_bounds is None:
        from pymatgen.symmetry.bandstructure import HighSymmKpath
        sp = HighSymmKpath(structure)
        kpath_labels = []
        for labels in sp.kpath['path']:
            kpath_labels.extend(labels)
        kpath_bounds = []
        for label in kpath_labels:
            red_coord = sp.kpath['kpoints'][label]
            kpath_bounds.append(red_coord)
    return cls(mode=KSamplingModes.path, num_kpts=ndivsm, kpts=kpath_bounds,
        comment=comment if comment else 'K-Path scheme')