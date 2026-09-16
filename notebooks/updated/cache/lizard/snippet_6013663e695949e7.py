def vector(p1, p2):
    return None if len(p1) != len(p2) else np.array([(p2[i] - p1[i]) for i in
        range(len(p1))])