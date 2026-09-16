def run(self):
    self._capture_signals()
    self._start_monitor()
    try:
        while True:
            if not self._run_worker():
                self._wait_for_changes()
            time.sleep(self.reload_interval)
    except KeyboardInterrupt:
        pass
    finally:
        self._stop_monitor()
        self._restore_signals()
    sys.exit(1)