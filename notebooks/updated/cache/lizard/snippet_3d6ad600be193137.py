def try_collect(self, timeframe):
    try:
        result = self.collect(timeframe)
    except Exception as e:
        exc_type, exc_val, exc_tb = sys.exc_info()
        e.original_traceback = exc_tb
        raise
    return result