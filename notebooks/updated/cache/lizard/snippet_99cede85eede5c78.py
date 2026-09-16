def get_json_object(col, path):
    sc = SparkContext._active_spark_context
    jc = sc._jvm.functions.get_json_object(_to_java_column(col), path)
    return Column(jc)