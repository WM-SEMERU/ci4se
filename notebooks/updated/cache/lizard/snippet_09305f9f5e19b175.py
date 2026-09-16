def _plane2col(plane):
    planes = 'xy', 'yx', 'xz', 'zx', 'yz', 'zy'
    assert plane in planes, 'No such plane found! Please select one of: ' + str(
        planes)
    return getattr(COLS, plane[0].capitalize()), getattr(COLS, plane[1].
        capitalize())