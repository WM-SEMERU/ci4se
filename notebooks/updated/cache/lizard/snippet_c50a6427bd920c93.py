def serve(self, liveport=None, host=None, restart_delay=2):
    host = host or '127.0.0.1'
    logger.info('Serving on http://%s:%s' % (host, liveport))
    self.application(host, liveport=liveport)
    try:
        self.watcher._changes.append(('__livereload__', restart_delay))
        LiveReloadHandler.start_tasks()
        IOLoop.instance().start()
    except KeyboardInterrupt:
        logger.info('Shutting down...')