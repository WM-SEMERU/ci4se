def pickle(self, f, protocol=-1):
    try:
        import cPickle as pickle
        if isinstance(f, basestring):
            with open(f, 'wb') as f:
                pickle.dump(self, f, protocol)
        else:
            pickle.dump(self, f, protocol)
    except ImportError:
        import pickle
        if isinstance(f, str):
            with open(f, 'wb') as f:
                pickle.dump(self, f, protocol)
        else:
            pickle.dump(self, f, protocol)