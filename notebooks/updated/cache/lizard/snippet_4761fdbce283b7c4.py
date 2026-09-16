def trainClassifier(cls, data, numClasses, categoricalFeaturesInfo,
    numTrees, featureSubsetStrategy='auto', impurity='gini', maxDepth=4,
    maxBins=32, seed=None):
    return cls._train(data, 'classification', numClasses,
        categoricalFeaturesInfo, numTrees, featureSubsetStrategy, impurity,
        maxDepth, maxBins, seed)