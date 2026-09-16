def set_video_config(self, video_config):
    self.video_config = video_config
    if video_config is None:
        self.disable_video()
        return
    py_exe = sys.executable
    port = self.canvas_slave.video_sink.socket_info['port']
    transport = self.canvas_slave.video_sink.socket_info['transport']
    host = self.canvas_slave.video_sink.socket_info['host'].replace('*',
        'localhost')
    self.cleanup_video()
    command = [py_exe, '-m', 'pygst_utils.video_view.video_source',
        'fromjson', '-p', str(port), transport, host, video_config.to_json()]
    logger.info(' '.join(command))
    self.video_source_process = sp.Popen(command)
    logger.info('Launched video source process: %s', self.
        video_source_process.pid)
    self.canvas_slave.enable()