def load_default_values(dsp, path):
    import dill
    with open(path, 'rb') as f:
        dsp.__init__(dmap=dsp.dmap, default_values=dill.load(f))