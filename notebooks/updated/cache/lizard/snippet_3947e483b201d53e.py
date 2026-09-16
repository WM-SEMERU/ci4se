def to_threepoint(center, radius, angles=None):
    if angles is None:
        angles = [0.0, np.pi]
    angles = np.asanyarray(angles, dtype=np.float64)
    if angles.shape != (2,):
        raise ValueError('angles must be (2,)!')
    if angles[1] < angles[0]:
        angles[1] += np.pi * 2
    center = np.asanyarray(center, dtype=np.float64)
    if center.shape != (2,):
        raise ValueError('only valid on 2D arcs!')
    angles = np.array([angles[0], angles.mean(), angles[1]], dtype=np.float64)
    three = np.column_stack((np.cos(angles), np.sin(angles))) * radius
    three += center
    return three