def locate(substr, str, pos=1):
    sc = SparkContext._active_spark_context
    return Column(sc._jvm.functions.locate(substr, _to_java_column(str), pos))