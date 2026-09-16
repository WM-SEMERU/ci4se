def stop(self):
    super(Icmpecho, self).stop()
    self.monitor_thread.join()
    logging.info('ICMPecho health monitor plugin: Stopped')