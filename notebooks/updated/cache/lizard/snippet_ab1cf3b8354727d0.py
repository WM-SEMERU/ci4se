def runExperiment6(dirName):
    resultsFilename = os.path.join(dirName, 'combined_results.pkl')
    results = runExperiment({'numSequences': 50, 'seqLength': 10,
        'numObjects': 50, 'numFeatures': 500, 'trialNum': 8, 'numLocations':
        100, 'settlingTime': 1, 'figure': '6', 'numRepetitions': 30,
        'basalPredictedSegmentDecrement': 0.001, 'stripStats': False})
    with open(resultsFilename, 'wb') as f:
        cPickle.dump(results, f)