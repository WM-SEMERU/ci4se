def pc_anova(self, covariates, num_pc=5):
    from scipy.stats import f_oneway
    if covariates.shape[0] == self.u.shape[0] and len(set(covariates.index) &
        set(self.u.index)) == self.u.shape[0]:
        mat = self.u
    elif covariates.shape[0] == self.v.shape[0] and len(set(covariates.
        index) & set(self.v.index)) == self.v.shape[0]:
        mat = self.v
    anova = pd.Panel(items=['fvalue', 'pvalue'], major_axis=covariates.
        columns, minor_axis=mat.columns[0:num_pc])
    for i in anova.major_axis:
        for j in anova.minor_axis:
            t = [mat[j][covariates[i] == x] for x in set(covariates[i])]
            f, p = f_oneway(*t)
            anova.ix['fvalue', i, j] = f
            anova.ix['pvalue', i, j] = p
    return anova