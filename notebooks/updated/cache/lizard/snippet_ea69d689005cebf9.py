def quaternion_from_axis_angle(v):
    theta = np.linalg.norm(v)
    if theta > 0:
        v = v / np.linalg.norm(v)
    ax, ay, az = v
    qx = ax * np.sin(0.5 * theta)
    qy = ay * np.sin(0.5 * theta)
    qz = az * np.sin(0.5 * theta)
    qw = np.cos(0.5 * theta)
    q = np.array([qw, qx, qy, qz])
    return q