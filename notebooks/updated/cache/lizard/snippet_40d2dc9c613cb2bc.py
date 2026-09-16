def corr(dataset, column, method='pearson'):
    sc = SparkContext._active_spark_context
    javaCorrObj = _jvm().org.apache.spark.ml.stat.Correlation
    args = [_py2java(sc, arg) for arg in (dataset, column, method)]
    return _java2py(sc, javaCorrObj.corr(*args))