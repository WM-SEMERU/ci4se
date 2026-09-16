def _create_optimizer(self, X, y, status):
    if self.optimizer is None:
        self.optimizer = 'avltree'
    times, ranks = y
    if self.optimizer == 'simple':
        optimizer = SimpleOptimizer(X, status, self.alpha, self.rank_ratio,
            timeit=self.timeit)
    elif self.optimizer == 'PRSVM':
        optimizer = PRSVMOptimizer(X, status, self.alpha, self.rank_ratio,
            timeit=self.timeit)
    elif self.optimizer == 'direct-count':
        optimizer = LargeScaleOptimizer(self.alpha, self.rank_ratio, self.
            fit_intercept, SurvivalCounter(X, ranks, status, len(ranks),
            times), timeit=self.timeit)
    elif self.optimizer == 'rbtree':
        optimizer = LargeScaleOptimizer(self.alpha, self.rank_ratio, self.
            fit_intercept, OrderStatisticTreeSurvivalCounter(X, ranks,
            status, RBTree, times), timeit=self.timeit)
    elif self.optimizer == 'avltree':
        optimizer = LargeScaleOptimizer(self.alpha, self.rank_ratio, self.
            fit_intercept, OrderStatisticTreeSurvivalCounter(X, ranks,
            status, AVLTree, times), timeit=self.timeit)
    else:
        raise ValueError('unknown optimizer: {0}'.format(self.optimizer))
    return optimizer