def _create_function(name, doc=''):

    def _(col):
        sc = SparkContext._active_spark_context
        jc = getattr(sc._jvm.functions, name)(col._jc if isinstance(col,
            Column) else col)
        return Column(jc)
    _.__name__ = name
    _.__doc__ = doc
    return _