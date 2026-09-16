def ngroups(self):
    if self._can_use_new_school():
        return self._grouped_spark_sql.count()
    self._prep_pandas_groupby()
    return self._mergedRDD.count()