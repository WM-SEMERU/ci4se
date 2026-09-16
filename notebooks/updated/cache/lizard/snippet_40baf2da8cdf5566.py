def shutdown(self):
    logging.info('Shutdown procedures being run!')
    for func in self.shutdown_cleanup.values():
        func()
    session_time = round((time.time() - self.start_time) / 60, 0)
    logging.info('session time: {0} minutes'.format(session_time))
    logging.info('End..')