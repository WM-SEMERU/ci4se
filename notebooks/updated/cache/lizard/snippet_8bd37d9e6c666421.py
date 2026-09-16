def get_uvec(vec):
    l = np.linalg.norm(vec)
    if l < 1e-08:
        return vec
    return vec / l