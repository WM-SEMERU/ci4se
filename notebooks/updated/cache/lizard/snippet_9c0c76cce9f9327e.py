def CallLoggedAndAccounted(f):

    @functools.wraps(f)
    def Decorator(*args, **kwargs):
        try:
            start_time = time.time()
            result = f(*args, **kwargs)
            latency = time.time() - start_time
            stats_collector_instance.Get().RecordEvent('db_request_latency',
                latency, fields=[f.__name__])
            logging.debug('DB request %s SUCCESS (%.3fs)', f.__name__, latency)
            return result
        except db.Error as e:
            stats_collector_instance.Get().IncrementCounter('db_request_errors'
                , fields=[f.__name__, 'grr'])
            logging.debug('DB request %s GRR ERROR: %s', f.__name__, utils.
                SmartUnicode(e))
            raise
        except Exception as e:
            stats_collector_instance.Get().IncrementCounter('db_request_errors'
                , fields=[f.__name__, 'db'])
            logging.debug('DB request %s INTERNAL DB ERROR : %s', f.
                __name__, utils.SmartUnicode(e))
            raise
    return Decorator