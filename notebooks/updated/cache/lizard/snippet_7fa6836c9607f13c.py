def getActiveSession(cls):
    from pyspark import SparkContext
    sc = SparkContext._active_spark_context
    if sc is None:
        return None
    elif sc._jvm.SparkSession.getActiveSession().isDefined():
        SparkSession(sc, sc._jvm.SparkSession.getActiveSession().get())
        return SparkSession._activeSession
    else:
        return None