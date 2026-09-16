def fromDataFrameRDD(cls, rdd, sql_ctx):
    result = DataFrame(None, sql_ctx)
    return result.from_rdd_of_dataframes(rdd)