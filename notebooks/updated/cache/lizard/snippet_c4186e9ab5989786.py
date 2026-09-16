def check_length_of_init_values(design_3d, init_values):
    if init_values.shape[0] != design_3d.shape[2]:
        msg_1 = 'The initial values are of the wrong dimension. '
        msg_2 = 'They should be of dimension {}'.format(design_3d.shape[2])
        raise ValueError(msg_1 + msg_2)
    return None