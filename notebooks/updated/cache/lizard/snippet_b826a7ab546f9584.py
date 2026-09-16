def lbnd(self):
    if not self.istransformed:
        return self.pst.parameter_data.parlbnd.copy()
    else:
        lb = self.pst.parameter_data.parlbnd.copy()
        lb[self.log_indexer] = np.log10(lb[self.log_indexer])
        return lb