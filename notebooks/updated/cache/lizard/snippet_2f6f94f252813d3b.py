def from_json(col, schema, options={}):
    sc = SparkContext._active_spark_context
    if isinstance(schema, DataType):
        schema = schema.json()
    elif isinstance(schema, Column):
        schema = _to_java_column(schema)
    jc = sc._jvm.functions.from_json(_to_java_column(col), schema, options)
    return Column(jc)