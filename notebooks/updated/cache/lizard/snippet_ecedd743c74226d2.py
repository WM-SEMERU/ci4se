def save(self, sc, path):
    java_model = (sc._jvm.org.apache.spark.mllib.classification.
        LogisticRegressionModel(_py2java(sc, self._coeff), self.intercept,
        self.numFeatures, self.numClasses))
    java_model.save(sc._jsc.sc(), path)