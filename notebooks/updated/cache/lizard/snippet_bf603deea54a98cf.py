def infer_order(self, goal, **kwargs):
    x = self.imodel.infer_x(np.array(self._pre_y(goal)), **kwargs)[0]
    return self._post_x(x, goal)