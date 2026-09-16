def _spin(coordinates, theta, around):
    around = np.asarray(around).reshape(3)
    if np.array_equal(around, np.zeros(3)):
        raise ValueError('Cannot spin around a zero vector')
    center_pos = np.mean(coordinates, axis=0)
    coordinates -= center_pos
    coordinates = _rotate(coordinates, theta, around)
    coordinates += center_pos
    return coordinates