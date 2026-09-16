def cov_from_scales(self, scales):
    ord_sc = []
    for stochastic in self.stochastics:
        ord_sc.append(np.ravel(scales[stochastic]))
    ord_sc = np.concatenate(ord_sc)
    if np.squeeze(ord_sc).shape[0] != self.dim:
        raise ValueError("Improper initial scales, dimension don't match",
            (np.squeeze(ord_sc), self.dim))
    return np.eye(self.dim) * ord_sc