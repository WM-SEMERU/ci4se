def inverse_kinematics(self, target, initial_position=None, **kwargs):
    target = np.array(target)
    if target.shape != (4, 4):
        raise ValueError('Your target must be a 4x4 transformation matrix')
    if initial_position is None:
        initial_position = [0] * len(self.links)
    return ik.inverse_kinematic_optimization(self, target,
        starting_nodes_angles=initial_position, **kwargs)