def triangle_strips_to_faces(strips):
    lengths = np.array([len(i) for i in strips])
    blob = np.concatenate(strips)
    tri = np.zeros((len(blob) - 2, 3), dtype=np.int)
    for i in range(3):
        tri[:len(blob) - 3, (i)] = blob[i:-3 + i]
    tri[-1] = blob[-3:]
    length_index = np.cumsum(lengths)[:-1]
    keep = np.ones(len(tri), dtype=np.bool)
    keep[length_index - 2] = False
    keep[length_index - 1] = False
    tri = tri[keep]
    length_index = np.append(0, np.cumsum(lengths - 2))
    flip = np.zeros(length_index[-1], dtype=np.bool)
    for i in range(len(length_index) - 1):
        flip[length_index[i] + 1:length_index[i + 1]][::2] = True
    tri[flip] = np.fliplr(tri[flip])
    return tri