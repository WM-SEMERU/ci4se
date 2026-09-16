def computeScaledProbabilities(listOfScales=[1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 
    4.0], listofkValues=[64, 128, 256], kw=32, n=1000, numWorkers=10,
    nTrials=1000):
    args = []
    theta, _ = getTheta(kw)
    for ki, k in enumerate(listofkValues):
        for si, s in enumerate(listOfScales):
            args.append({'k': k, 'kw': kw, 'n': n, 'theta': theta,
                'nTrials': nTrials, 'inputScaling': s, 'errorIndex': [ki, si]})
    result = computeMatchProbabilityParallel(args, numWorkers)
    errors = np.zeros((len(listofkValues), len(listOfScales)))
    for r in result:
        errors[r['errorIndex'][0], r['errorIndex'][1]] = r['pctMatches']
    print('Errors using scaled inputs, for kw=', kw)
    print(repr(errors))
    plotScaledMatches(listofkValues, listOfScales, errors, 
        'images/scalar_effect_of_scale_kw' + str(kw) + '.pdf')