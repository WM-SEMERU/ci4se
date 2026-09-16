def get_estimates(estimators_tuple, positions, num_workers=1):
    estimators = dict()
    estimators['P(relevant)'], estimators['p(position)'], estimators[
        'p(position|relevant)'] = estimators_tuple
    log_estimates = dict()
    log_estimates['P(relevant)'] = log(estimators['P(relevant)'])
    X = [(position,) for position in positions]
    with Pool(num_workers) as pool:
        first_job = pool.map_async(estimators['p(position)'].score_samples,
            tqdm(array_split(X, num_workers), desc='p(position)'))
        second_job = pool.map_async(estimators['p(position|relevant)'].
            score_samples, tqdm(array_split(X, num_workers), desc=
            'p(position | relevant)'))
        log_estimates['p(position)'] = concatenate(first_job.get())
        log_estimates['p(position|relevant)'] = concatenate(second_job.get())
    log_estimates['P(position,relevant)'] = log_estimates[
        'p(position|relevant)'] + log_estimates['P(relevant)']
    log_estimates['P(relevant|position)'] = log_estimates[
        'P(position,relevant)'] - log_estimates['p(position)']
    return [estimators['P(relevant)']] * len(X), exp(log_estimates[
        'p(position)']), exp(log_estimates['p(position|relevant)']), exp(
        log_estimates['P(position,relevant)']), exp(log_estimates[
        'P(relevant|position)'])