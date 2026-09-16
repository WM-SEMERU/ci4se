def define_models(self, ic, leaves=None, N=1, index=0):
    self.clear_models()
    if leaves is None:
        leaves = self._get_leaves()
    elif type(leaves) == type(''):
        leaves = self.select_leaves(leaves)
    if np.isscalar(N):
        N = np.ones(len(leaves)) * N
    N = np.array(N).astype(int)
    if np.isscalar(index):
        index = np.ones_like(N) * index
    index = np.array(index).astype(int)
    for s, n, i in zip(leaves, N, index):
        s.remove_children()
        s.add_model(ic, n, i)
    self._fix_labels()
    self._N = N
    self._index = index
    self._clear_all_leaves()