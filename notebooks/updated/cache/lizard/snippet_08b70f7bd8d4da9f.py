def bestfit(self):
    try:
        import statsmodels.api as sm
    except:
        raise Exception(
            'statsmodels is required: please run pip install statsmodels')
    x = pd.Series(list(range(1, len(self) + 1)), index=self.index)
    x = sm.add_constant(x)
    model = sm.OLS(self, x)
    fit = model.fit()
    vals = fit.params.values
    best_fit = fit.fittedvalues
    best_fit.formula = '%.2f*x+%.2f' % (vals[0], vals[1])
    return best_fit