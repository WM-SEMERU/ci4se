def vec(data, dtype=float):
    gl_types = {float: gl.GLfloat, int: gl.GLuint}
    try:
        gl_dtype = gl_types[dtype]
    except KeyError:
        raise TypeError(
            'dtype not recognized.  Recognized types are int and float')
    if gl_dtype == gl.GLuint:
        for el in data:
            if el < 0:
                raise ValueError(
                    'integer ratcave.vec arrays are unsigned--negative values are not supported.'
                    )
    return (gl_dtype * len(data))(*data)