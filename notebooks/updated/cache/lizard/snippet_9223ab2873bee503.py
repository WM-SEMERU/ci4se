def load_transform(fname):
    if fname is None:
        return np.eye(4)
    if fname.endswith('.mat'):
        return np.loadtxt(fname)
    elif fname.endswith('.lta'):
        with open(fname, 'rb') as fobj:
            for line in fobj:
                if line.startswith(b'1 4 4'):
                    break
            lines = fobj.readlines()[:4]
        return np.genfromtxt(lines)
    raise ValueError('Unknown transform type; pass FSL (.mat) or LTA (.lta)')