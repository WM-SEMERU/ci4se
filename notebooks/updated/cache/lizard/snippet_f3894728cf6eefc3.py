def get_false_negative(self, scalar=True):
    ans = pd.Series(PrettyDict([(k, safe_div(np.sum(self.loc[k]) - self[k][
        k], np.sum(self.sum() - self.loc[k]))) for k in self.columns]))
    if not self._scalar_stats and not scalar or self._num_classes != 2:
        return ans
    return ans[self._pos_label]