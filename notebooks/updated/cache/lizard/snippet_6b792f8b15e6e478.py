def mean(self):
    if self._can_use_new_school():
        self._prep_spark_sql_groupby()
        import pyspark.sql.functions as func
        return self._use_aggregation(func.mean)
    self._prep_pandas_groupby()
    return DataFrame.fromDataFrameRDD(self._regroup_mergedRDD().values().
        map(lambda x: x.mean()), self.sql_ctx)