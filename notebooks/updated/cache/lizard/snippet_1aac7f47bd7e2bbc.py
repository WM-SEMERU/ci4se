def from_labels(cls, labels, inputCol, outputCol=None, handleInvalid=None):
    sc = SparkContext._active_spark_context
    java_class = sc._gateway.jvm.java.lang.String
    jlabels = StringIndexerModel._new_java_array(labels, java_class)
    model = StringIndexerModel._create_from_java_class(
        'org.apache.spark.ml.feature.StringIndexerModel', jlabels)
    model.setInputCol(inputCol)
    if outputCol is not None:
        model.setOutputCol(outputCol)
    if handleInvalid is not None:
        model.setHandleInvalid(handleInvalid)
    return model