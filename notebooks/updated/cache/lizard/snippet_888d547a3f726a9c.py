def prop_unc(jc):
    j, c = jc
    return np.dot(np.dot(j, c), j.T)