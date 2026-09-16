def rand(seed=None):
    sc = SparkContext._active_spark_context
    if seed is not None:
        jc = sc._jvm.functions.rand(seed)
    else:
        jc = sc._jvm.functions.rand()
    return Column(jc)