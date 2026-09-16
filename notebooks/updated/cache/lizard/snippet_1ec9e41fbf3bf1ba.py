def stop(self):
    self.my_server.stop()
    self.http_thread.join()
    logging.info('HTTP server: Stopped')