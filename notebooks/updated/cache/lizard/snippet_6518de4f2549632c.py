def start(self):
    values = self._defn.name, self.server_host, self.server_port
    log.info('Listening for %s telemetry on %s:%d (UDP)' % values)
    super(UdpTelemetryServer, self).start()