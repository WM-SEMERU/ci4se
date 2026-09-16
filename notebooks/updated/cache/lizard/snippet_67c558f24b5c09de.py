def _goto(self, pose, duration, wait, accurate):
    kwargs = {}
    if not accurate:
        kwargs['max_iter'] = 3
    q0 = self.convert_to_ik_angles(self.joints_position)
    q = self.inverse_kinematics(pose, initial_position=q0, **kwargs)
    joints = self.convert_from_ik_angles(q)
    last = self.motors[-1]
    for m, pos in list(zip(self.motors, joints)):
        m.goto_position(pos, duration, wait=False if m != last else wait)