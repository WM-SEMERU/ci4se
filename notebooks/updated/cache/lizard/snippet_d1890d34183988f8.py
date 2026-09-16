def length2mesh(length, lattice, rotations=None):
    rec_lattice = np.linalg.inv(lattice)
    rec_lat_lengths = np.sqrt(np.diagonal(np.dot(rec_lattice.T, rec_lattice)))
    mesh_numbers = np.rint(rec_lat_lengths * length).astype(int)
    if rotations is not None:
        reclat_equiv = get_lattice_vector_equivalence([r.T for r in np.
            array(rotations)])
        m = mesh_numbers
        mesh_equiv = [m[1] == m[2], m[2] == m[0], m[0] == m[1]]
        for i, pair in enumerate(([1, 2], [2, 0], [0, 1])):
            if reclat_equiv[i] and not mesh_equiv:
                m[pair] = max(m[pair])
    return np.maximum(mesh_numbers, [1, 1, 1])