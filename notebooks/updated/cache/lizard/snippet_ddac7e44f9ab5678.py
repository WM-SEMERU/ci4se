def wrap_existing_process(self, pid, stdout_read_fd, stderr_read_fd, port=None
    ):
    stdout_read_file = os.fdopen(stdout_read_fd, 'rb')
    stderr_read_file = os.fdopen(stderr_read_fd, 'rb')
    stdout_streams, stderr_streams = self._get_stdout_stderr_streams()
    self._stdout_tee = io_wrap.Tee(stdout_read_file, *stdout_streams)
    self._stderr_tee = io_wrap.Tee(stderr_read_file, *stderr_streams)
    self.proc = Process(pid)
    self._run.pid = pid
    logger.info('wrapping existing process %i' % pid)
    try:
        self.init_run()
    except LaunchError as e:
        logger.exception('catostrophic launch error')
        wandb.termerror(str(e))
        util.sentry_exc(e)
        self._socket.launch_error()
        return
    if io_wrap.SIGWINCH_HANDLER is not None:
        io_wrap.SIGWINCH_HANDLER.add_fd(stdout_read_fd)
        io_wrap.SIGWINCH_HANDLER.add_fd(stderr_read_fd)
    logger.info('informing user process we are ready to proceed')
    self._socket.ready()
    self._sync_etc(headless=True)