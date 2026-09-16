def imageSchema(self):
    if self._imageSchema is None:
        ctx = SparkContext._active_spark_context
        jschema = ctx._jvm.org.apache.spark.ml.image.ImageSchema.imageSchema()
        self._imageSchema = _parse_datatype_json_string(jschema.json())
    return self._imageSchema