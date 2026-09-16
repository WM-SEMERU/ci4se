def standardize(self):
    nonmissing = numpy.invert(self.missing)
    nmcount = numpy.sum(nonmissing)
    self.covariates = []
    self.phenotypes = []
    for idx in range(0, self.covar_count):
        x = self.datasource.covariate_data[idx]
        nonmissing = x != PhenoCovar.missing_encoding
        mx = numpy.mean(x[nonmissing])
        sx = numpy.std(x[nonmissing])
        self.covariates.append((x - mx) / sx)
    for idx in range(0, self.pheno_count):
        y = self.datasource.phenotype_data[idx]
        nonmissing = y != PhenoCovar.missing_encoding
        my = numpy.mean(y[nonmissing])
        sy = numpy.std(y[nonmissing])
        self.phenotypes.append((y - my) / sy)