def array_repeat(col, count):
    sc = SparkContext._active_spark_context
    return Column(sc._jvm.functions.array_repeat(_to_java_column(col), count))