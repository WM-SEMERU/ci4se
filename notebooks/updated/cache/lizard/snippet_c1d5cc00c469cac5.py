def _new_redis_client(self):
    if 'tornadoredis' not in globals():
        import tornadoredis
    kwargs = self._redis_connection_settings()
    LOGGER.info('Connecting to %(host)s:%(port)s DB %(selected_db)s', kwargs)
    return tornadoredis.Client(**kwargs)