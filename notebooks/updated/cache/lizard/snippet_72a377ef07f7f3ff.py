def _callback(self, cassandra_future, tornado_future):
    try:
        result = cassandra_future.result()
    except Exception as exc:
        return tornado_future.set_exception(exc)
    tornado_future.set_result(result)