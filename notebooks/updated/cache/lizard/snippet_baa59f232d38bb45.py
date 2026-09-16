def _start_app_and_connect(self):
    self._check_app_installed()
    self.disable_hidden_api_blacklist()
    persists_shell_cmd = self._get_persist_command()
    self.log.info('Launching snippet apk %s with protocol %d.%d', self.
        package, _PROTOCOL_MAJOR_VERSION, _PROTOCOL_MINOR_VERSION)
    cmd = _LAUNCH_CMD % (persists_shell_cmd, self.package)
    start_time = time.time()
    self._proc = self._do_start_app(cmd)
    line = self._read_protocol_line()
    match = re.match('^SNIPPET START, PROTOCOL ([0-9]+) ([0-9]+)$', line)
    if not match or match.group(1) != '1':
        raise ProtocolVersionError(self._ad, line)
    line = self._read_protocol_line()
    match = re.match('^SNIPPET SERVING, PORT ([0-9]+)$', line)
    if not match:
        raise ProtocolVersionError(self._ad, line)
    self.device_port = int(match.group(1))
    self.host_port = utils.get_available_host_port()
    self._adb.forward(['tcp:%d' % self.host_port, 'tcp:%d' % self.device_port])
    self.connect()
    self.log.debug('Snippet %s started after %.1fs on host port %s', self.
        package, time.time() - start_time, self.host_port)