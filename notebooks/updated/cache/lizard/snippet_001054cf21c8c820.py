def get_nodal_planes(self):
    self.tensor, self.tensor_sigma = self._to_ned()
    self.ref_frame = 'NED'
    _, evect = utils.eigendecompose(self.tensor)
    _, rot_vec = utils.eigendecompose(np.matrix([[0.0, 0.0, -1], [0.0, 0.0,
        0.0], [-1.0, 0.0, 0.0]]))
    rotation_matrix = np.matrix(evect * rot_vec.T).T
    if np.linalg.det(rotation_matrix) < 0.0:
        rotation_matrix *= -1.0
    flip_dc = np.matrix([[0.0, 0.0, -1.0], [0.0, -1.0, 0.0], [-1.0, 0.0, 0.0]])
    rotation_matrices = sorted([rotation_matrix, flip_dc * rotation_matrix],
        cmp=cmp_mat)
    nodal_planes = GCMTNodalPlanes()
    dip, strike, rake = [(180.0 / pi * angle) for angle in utils.
        matrix_to_euler(rotation_matrices[0])]
    nodal_planes.nodal_plane_1 = {'strike': strike % 360, 'dip': dip,
        'rake': -rake}
    dip, strike, rake = [(180.0 / pi * angle) for angle in utils.
        matrix_to_euler(rotation_matrices[1])]
    nodal_planes.nodal_plane_2 = {'strike': strike % 360.0, 'dip': dip,
        'rake': -rake}
    return nodal_planes