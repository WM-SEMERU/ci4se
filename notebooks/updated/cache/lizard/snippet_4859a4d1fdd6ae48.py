def alias(self, *alias, **kwargs):
    metadata = kwargs.pop('metadata', None)
    assert not kwargs, 'Unexpected kwargs where passed: %s' % kwargs
    sc = SparkContext._active_spark_context
    if len(alias) == 1:
        if metadata:
            jmeta = sc._jvm.org.apache.spark.sql.types.Metadata.fromJson(json
                .dumps(metadata))
            return Column(getattr(self._jc, 'as')(alias[0], jmeta))
        else:
            return Column(getattr(self._jc, 'as')(alias[0]))
    else:
        if metadata:
            raise ValueError(
                'metadata can only be provided for a single column')
        return Column(getattr(self._jc, 'as')(_to_seq(sc, list(alias))))