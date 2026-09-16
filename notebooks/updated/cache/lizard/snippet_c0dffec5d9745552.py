def apply_cut(self, cm):
    inverse = np.logical_not(self.cut_matrix(cm.shape[0])).astype(int)
    return cm * inverse