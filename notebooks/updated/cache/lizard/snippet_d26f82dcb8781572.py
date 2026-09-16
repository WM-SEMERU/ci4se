def stop(self):
    if getattr(self, '_jsc', None):
        try:
            self._jsc.stop()
        except Py4JError:
            warnings.warn(
                'Unable to cleanly shutdown Spark JVM process. It is possible that the process has crashed, been killed or may also be in a zombie state.'
                , RuntimeWarning)
        finally:
            self._jsc = None
    if getattr(self, '_accumulatorServer', None):
        self._accumulatorServer.shutdown()
        self._accumulatorServer = None
    with SparkContext._lock:
        SparkContext._active_spark_context = None