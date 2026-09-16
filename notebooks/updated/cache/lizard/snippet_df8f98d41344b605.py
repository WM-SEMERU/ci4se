def cat_trials(x3d):
    x3d = atleast_3d(x3d)
    t = x3d.shape[0]
    return np.concatenate(np.split(x3d, t, 0), axis=2).squeeze(0)