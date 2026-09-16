def initiate_shutdown(self):
    sig = getattr(signal, 'SIGKILL', signal.SIGTERM)
    if is_running_from_reloader():
        os.kill(os.getpid(), sig)
    self.server._BaseServer__shutdown_request = True
    self.server._BaseServer__serving = False