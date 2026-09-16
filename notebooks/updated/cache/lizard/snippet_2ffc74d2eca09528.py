def load(cls, folder):
    popset = PopulationSet.load_hdf(os.path.join(folder, 'popset.h5'))
    sigfile = os.path.join(folder, 'trsig.pkl')
    with open(sigfile, 'rb') as f:
        trsig = pickle.load(f)
    return cls(trsig, popset, folder=folder)