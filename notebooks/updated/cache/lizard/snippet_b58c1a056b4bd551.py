def kill(self, sig=signal.SIGTERM):
    while self.is_alive():
        self.killed = True
        time.sleep(POLLING_DELAY)
        if not self.spawned:
            continue
        if self.process.poll() is None:
            self.process.send_signal(sig)
            try:
                os.waitpid(self.process.pid, getattr(os, 'WNOHANG', 1))
            except OSError:
                pass
        break
    self.join()