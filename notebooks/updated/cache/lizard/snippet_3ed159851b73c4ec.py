def unable_thread_pool(self, only_read=False):
    if self.enable_thread_pool and hasattr(self, 'thread_pool'
        ) and self.thread_pool is not None:
        self.thread_pool.shutdown()
        self.thread_pool = None
        self.enable_thread_pool = False
        self.logger.debug('Remove thread pool completed')
        return True
    else:
        self.logger.warning('Current not have a thread pool is existent')
        return False