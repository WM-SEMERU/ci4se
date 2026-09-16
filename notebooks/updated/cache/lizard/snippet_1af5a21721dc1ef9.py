def save(self, sc, path):
    java_model = sc._jvm.org.apache.spark.mllib.classification.SVMModel(
        _py2java(sc, self._coeff), self.intercept)
    java_model.save(sc._jsc.sc(), path)