def start(self, blocking=False):
    self.debug('()')
    super(SensorClient, self).start(blocking=False)
    try:
        a_thread = threading.Thread(target=self._thread_wrapper, args=(self
            ._packet_loop,))
        a_thread.daemon = True
        a_thread.start()
    except:
        self.exception('Failed to run packet loop')
        raise SensorStartException('Packet loop failed')
    self.info('Started')
    super(Sensor, self).start(blocking)