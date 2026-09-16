def load(cls, sc, path):
    jmodel = sc._jvm.org.apache.spark.mllib.feature.Word2VecModel.load(sc.
        _jsc.sc(), path)
    model = sc._jvm.org.apache.spark.mllib.api.python.Word2VecModelWrapper(
        jmodel)
    return Word2VecModel(model)