def forward_kinematics(self, joints, full_kinematics=False):
    frame_matrix = np.eye(4)
    if full_kinematics:
        frame_matrixes = []
    if len(self.links) != len(joints):
        raise ValueError(
            'Your joints vector length is {} but you have {} links'.format(
            len(joints), len(self.links)))
    for index, (link, joint_angle) in enumerate(zip(self.links, joints)):
        frame_matrix = np.dot(frame_matrix, np.asarray(link.
            get_transformation_matrix(joint_angle)))
        if full_kinematics:
            frame_matrixes.append(frame_matrix)
    if full_kinematics:
        return frame_matrixes
    else:
        return frame_matrix