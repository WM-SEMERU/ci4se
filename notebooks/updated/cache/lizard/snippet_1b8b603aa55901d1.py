def ransac(npts, model, n, k, t, d):
    iterations = 0
    bestfit = None
    besterr = np.inf
    while iterations < k:
        maybe_idxs, test_idxs = random_partition(n, npts)
        maybemodel = model.fit(maybe_idxs)
        test_err = model.score(test_idxs, maybemodel)
        also_idxs = test_idxs[test_err < t]
        LOGGER.debug('test_err.min() %f', test_err.min() if test_err.size else
            None)
        LOGGER.debug('test_err.max() %f', test_err.max() if test_err.size else
            None)
        LOGGER.debug('numpy.mean(test_err) %f', np.mean(test_err) if
            test_err.size else None)
        LOGGER.debug('iteration %d, len(alsoinliers) = %d', iterations, len
            (also_idxs))
        if len(also_idxs) > d:
            betteridxs = np.concatenate((maybe_idxs, also_idxs))
            bettermodel = model.fit(betteridxs)
            better_errs = model.score(betteridxs, bettermodel)
            thiserr = np.mean(better_errs)
            if thiserr < besterr:
                bestfit = bettermodel
                besterr = thiserr
        iterations += 1
    return bestfit