def add(self, tensor, tf_sess=None, key=None, **kwargs):
    if not isinstance(tensor, Tensor):
        tensor = Tensor(tensor, tf_sess, **kwargs)
    if key is None:
        if len(self.roots) == 0:
            key = 0
        else:
            key = max(self.roots.keys()) + 1
    self.roots[key] = tensor