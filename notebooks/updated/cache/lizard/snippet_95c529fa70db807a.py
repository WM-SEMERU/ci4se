def create_point_texture(size, feather=0):
    from pyglet import gl
    assert feather >= 0, 'Expected feather value >= 0'
    coords = range(size)
    texel = (gl.GLfloat * size ** 2)()
    r = size / 2.0
    c = feather + 1.0
    for y in coords:
        col = y * size
        for x in coords:
            d = math.sqrt((x - r) ** 2 + (y - r) ** 2)
            if d < r and 1.0 - 1.0 / (d / r - 1.0) < 100:
                texel[x + col] = c ** 2 / c ** (1.0 - 1.0 / (d / r - 1.0))
            else:
                texel[x + col] = 0
    id = gl.GLuint()
    gl.glGenTextures(1, ctypes.byref(id))
    gl.glBindTexture(gl.GL_TEXTURE_2D, id.value)
    gl.glPixelStorei(gl.GL_UNPACK_ALIGNMENT, 4)
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_LUMINANCE, size, size, 0, gl
        .GL_LUMINANCE, gl.GL_FLOAT, ctypes.byref(texel))
    gl.glFlush()
    return id.value