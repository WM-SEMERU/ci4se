def simple_clip_matrix(scale, znear, zfar, aspectratio=1.0):
    m = numpy.zeros((4, 4))
    m[0, 0] = scale / aspectratio
    m[1, 1] = scale
    m[2, 2] = (zfar + znear) / (znear - zfar)
    m[2, 3] = 2 * zfar * znear / (znear - zfar)
    m[3, 2] = -1
    return m