def _compute_orientation(self):
    cyl_mat = self.sim.data.body_xmat[self.cyl_body_id]
    cyl_mat.shape = 3, 3
    cyl_pos = self.sim.data.body_xpos[self.cyl_body_id]
    hole_pos = self.sim.data.body_xpos[self.hole_body_id]
    hole_mat = self.sim.data.body_xmat[self.hole_body_id]
    hole_mat.shape = 3, 3
    v = cyl_mat @ np.array([0, 0, 1])
    v = v / np.linalg.norm(v)
    center = hole_pos + hole_mat @ np.array([0.1, 0, 0])
    t = (center - cyl_pos) @ v / np.linalg.norm(v) ** 2
    d = np.linalg.norm(np.cross(v, cyl_pos - center)) / np.linalg.norm(v)
    hole_normal = hole_mat @ np.array([0, 0, 1])
    return t, d, abs(np.dot(hole_normal, v) / np.linalg.norm(hole_normal) /
        np.linalg.norm(v))