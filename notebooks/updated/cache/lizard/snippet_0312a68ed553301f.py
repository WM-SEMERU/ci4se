def get_exps(self, path='.'):
    exps = []
    for dp, dn, fn in os.walk(path):
        if 'experiment.cfg' in fn:
            subdirs = [os.path.join(dp, d) for d in os.listdir(dp) if os.
                path.isdir(os.path.join(dp, d))]
            if all(map(lambda s: self.get_exps(s) == [], subdirs)):
                exps.append(dp)
    return exps