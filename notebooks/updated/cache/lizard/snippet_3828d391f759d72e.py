def train(self, rdd, k=4, maxIterations=20, minDivisibleClusterSize=1.0,
    seed=-1888008604):
    java_model = callMLlibFunc('trainBisectingKMeans', rdd.map(
        _convert_to_vector), k, maxIterations, minDivisibleClusterSize, seed)
    return BisectingKMeansModel(java_model)