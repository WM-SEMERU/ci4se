def __at_om_to_im(self, om):
    original_om = om
    if om[0] == 'U':
        om = om[1:]
        is_um = True
    else:
        is_um = False
    if om == 'r':
        return original_om, O_RDONLY, False, is_um
    elif om == 'w':
        return original_om, O_WRONLY | O_CREAT | O_TRUNC, False, is_um
    elif om == 'a':
        return original_om, O_WRONLY | O_CREAT, False, is_um
    elif om == 'r+':
        return original_om, O_RDWR | O_CREAT, False, is_um
    elif om == 'w+':
        return original_om, O_RDWR | O_CREAT | O_TRUNC, False, is_um
    elif om == 'a+':
        return original_om, O_RDWR | O_CREAT, True, is_um
    else:
        raise Exception('Outer access mode [%s] is invalid.' % original_om)