def angle(array_of_xyzs):
    ab = array_of_xyzs[0] - array_of_xyzs[1]
    cb = array_of_xyzs[2] - array_of_xyzs[1]
    return np.arccos(np.dot(ab, cb) / (np.sqrt(ab[0] ** 2 + ab[1] ** 2 + ab
        [2] ** 2) * np.sqrt(cb[0] ** 2 + cb[1] ** 2 + cb[2] ** 2)))