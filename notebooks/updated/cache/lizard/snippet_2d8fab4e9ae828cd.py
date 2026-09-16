def lattice_2_lmpbox(lattice, origin=(0, 0, 0)):
    a, b, c = lattice.abc
    xlo, ylo, zlo = origin
    xhi = a + xlo
    m = lattice.matrix
    xy = np.dot(m[1], m[0] / a)
    yhi = np.sqrt(b ** 2 - xy ** 2) + ylo
    xz = np.dot(m[2], m[0] / a)
    yz = (np.dot(m[1], m[2]) - xy * xz) / (yhi - ylo)
    zhi = np.sqrt(c ** 2 - xz ** 2 - yz ** 2) + zlo
    tilt = None if lattice.is_orthogonal else [xy, xz, yz]
    rot_matrix = np.linalg.solve([[xhi - xlo, 0, 0], [xy, yhi - ylo, 0], [
        xz, yz, zhi - zlo]], m)
    bounds = [[xlo, xhi], [ylo, yhi], [zlo, zhi]]
    symmop = SymmOp.from_rotation_and_translation(rot_matrix, origin)
    return LammpsBox(bounds, tilt), symmop