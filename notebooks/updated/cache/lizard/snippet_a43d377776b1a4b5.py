def _convert_angle_from_pypot(angle, joint, **kwargs):
    angle_internal = angle + joint['offset']
    if joint['orientation-convention'] == 'indirect':
        angle_internal = -1 * angle_internal
    if joint['name'].startswith('l_shoulder_x'):
        angle_internal = -1 * angle_internal
    angle_internal = angle_internal / 180 * np.pi
    return angle_internal