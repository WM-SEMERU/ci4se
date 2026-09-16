def _build_cm(self, cm):
    if cm is None:
        cm = np.ones((self.size, self.size))
    else:
        cm = np.array(cm)
    utils.np_immutable(cm)
    return cm, utils.np_hash(cm)