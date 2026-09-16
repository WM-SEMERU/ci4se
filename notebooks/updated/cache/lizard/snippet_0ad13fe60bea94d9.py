def point_translate(point_in, vector_in):
    try:
        if point_in is None or len(point_in) == 0 or vector_in is None or len(
            vector_in) == 0:
            raise ValueError('Input arguments cannot be empty')
    except TypeError as e:
        print('An error occurred: {}'.format(e.args[-1]))
        raise TypeError('Input must be a list or tuple')
    except Exception:
        raise
    point_out = [(coord + comp) for coord, comp in zip(point_in, vector_in)]
    return point_out