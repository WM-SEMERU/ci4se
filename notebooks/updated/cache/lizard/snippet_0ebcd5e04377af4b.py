def _queuing_thread_func(self):
    self.logger.debug('_queuing_thread_func start')
    try:
        for job_params in self._get_iterator():
            self.config.logger.debug('received %r', job_params)
            if job_params is None:
                if self.config.quit_on_empty_queue:
                    self.wait_for_empty_queue(wait_log_interval=10,
                        wait_reason='waiting for queue to drain')
                    raise KeyboardInterrupt
                self.logger.info(
                    'there is nothing to do.  Sleeping for %d seconds' %
                    self.config.idle_delay)
                self._responsive_sleep(self.config.idle_delay)
                continue
            self.quit_check()
            self.task_queue.put((self.task_func, job_params))
    except Exception:
        self.logger.error('queuing jobs has failed', exc_info=True)
    except KeyboardInterrupt:
        self.logger.debug('queuingThread gets quit request')
    finally:
        self.logger.debug("we're quitting queuingThread")
        self._kill_worker_threads()
        self.logger.debug('all worker threads stopped')
        self.quit = True