def push(self, source_file, device_filename, timeout_ms=None):
    mtime = 0
    if isinstance(source_file, six.string_types):
        mtime = os.path.getmtime(source_file)
        source_file = open(source_file)
    self.filesync_service.send(source_file, device_filename, mtime=mtime,
        timeout=timeouts.PolledTimeout.from_millis(timeout_ms))