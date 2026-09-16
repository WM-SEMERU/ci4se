def align_nab(tar, ref):
    rot_trans_1 = find_transformations(tar['N'].array, tar['CA'].array, ref
        ['N'].array, ref['CA'].array)
    apply_trans_rot(tar, *rot_trans_1)
    rot_ang_ca_cb = dihedral(tar['CB'], ref['CA'], ref['N'], ref['CB'])
    tar.rotate(rot_ang_ca_cb, ref['N'].array - ref['CA'].array, ref['N'].array)
    return