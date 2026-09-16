def streams(self):
    from pyspark.sql.streaming import StreamingQueryManager
    return StreamingQueryManager(self._ssql_ctx.streams())