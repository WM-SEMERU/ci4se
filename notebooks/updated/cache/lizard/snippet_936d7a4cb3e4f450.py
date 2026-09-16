def estimate_library_complexity(df, algorithm='RNA-seq'):
    DEFAULT_CUTOFFS = {'RNA-seq': (0.25, 0.4)}
    cutoffs = DEFAULT_CUTOFFS[algorithm]
    if len(df) < 5:
        return {'unique_starts_per_read': 'nan', 'complexity': 'NA'}
    model = sm.ols(formula='starts ~ reads', data=df)
    fitted = model.fit()
    slope = fitted.params['reads']
    if slope <= cutoffs[0]:
        complexity = 'LOW'
    elif slope <= cutoffs[1]:
        complexity = 'MEDIUM'
    else:
        complexity = 'HIGH'
    return {'Unique Starts Per Read': float(slope)}