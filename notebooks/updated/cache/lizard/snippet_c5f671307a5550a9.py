def pore_diameter(elements, coordinates, com=None):
    if com is None:
        com = center_of_mass(elements, coordinates)
    atom_vdw = np.array([[atomic_vdw_radius[x.upper()]] for x in elements])
    dist_matrix = euclidean_distances(coordinates, com.reshape(1, -1))
    re_dist_matrix = dist_matrix - atom_vdw
    index = np.argmin(re_dist_matrix)
    pored = re_dist_matrix[index][0] * 2
    return pored, index