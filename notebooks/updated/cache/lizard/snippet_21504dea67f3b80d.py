def phenSpecificEffects(snps, pheno1, pheno2, K=None, covs=None, test='lrt'):
    N = snps.shape[0]
    if K is None:
        K = SP.eye(N)
    assert pheno1.shape[1] == pheno2.shape[1
        ], 'Only consider equal number of phenotype dimensions'
    if covs is None:
        covs = SP.ones(N, 1)
    assert pheno1.shape[1] == 1 and pheno2.shape[1] == 1 and pheno1.shape[0
        ] == N and pheno2.shape[0] == N and K.shape[0] == N and K.shape[1
        ] == N and covs.shape[0] == N, 'shapes missmatch'
    Inter = SP.zeros((N * 2, 1))
    Inter[0:N, (0)] = 1
    Inter0 = SP.ones((N * 2, 1))
    Yinter = SP.concatenate((pheno1, pheno2), 0)
    Xinter = SP.tile(snps, (2, 1))
    Covitner = SP.tile(covs(2, 1))
    lm = simple_interaction(snps=Xinter, pheno=Yinter, covs=Covinter, Inter
        =Inter, Inter0=Inter0, test=test)
    return lm