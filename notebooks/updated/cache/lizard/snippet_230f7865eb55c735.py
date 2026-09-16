def parse_log2(fn):
    with open(fn) as f:
        lines = f.readlines()
    if len(lines) == 0:
        sys.stderr.write('Empty log file: {}.\n'.format(fn))
        return None
    logtype = None
    if len([x for x in lines if '--glm standard-beta' in x]):
        logtype = 'linear'
    elif len([x for x in lines if '--glm firth-fallback' in x]):
        logtype = 'logistic'
    if logtype is None:
        return None
        sys.stderr.write('Log file not supported: {}.\n'.format(fn))
    try:
        lines = [x for x in lines if 'remaining after' in x]
        i = 0
        x = lines[i].split()
        samples = int(x[0])
        females = int(x[2][1:])
        males = int(x[4])
        i += 1
        cases = np.nan
        controls = np.nan
        if logtype == 'logistic':
            x = lines[i].split()
            cases = int(x[0])
            controls = int(x[3])
            i += 1
        variants = int(lines[i].split()[0])
    except:
        sys.stderr.write('Error parsing log file: {}.\n'.format(fn))
        return None
    se = pd.Series([samples, females, males, cases, controls, variants],
        index=['samples', 'females', 'males', 'cases', 'controls', 'variants']
        ).dropna()
    return se