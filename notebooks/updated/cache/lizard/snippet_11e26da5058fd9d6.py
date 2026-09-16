def get_estimators(positions_all, positions_relevant):
    samples_all = [(position,) for _, positions in positions_all.items() for
        position in positions]
    samples_relevant = [(position,) for _, positions in positions_relevant.
        items() for position in positions]
    estimators = dict()
    estimators['P(relevant)'] = len(samples_relevant) / len(samples_all)
    LOGGER.info('Fitting prior p(position) density estimator')
    estimators['p(position)'] = KernelDensity(**KERNEL).fit(samples_all)
    LOGGER.info('Fitting conditional p(position | relevant) density estimator')
    estimators['p(position|relevant)'] = KernelDensity(**KERNEL).fit(
        samples_relevant)
    return estimators['P(relevant)'], estimators['p(position)'], estimators[
        'p(position|relevant)']