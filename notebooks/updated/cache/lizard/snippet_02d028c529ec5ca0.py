def start_watcher_thread(self):
    watcher_thread = threading.Thread(target=self.run_watcher)
    if self._reload_mode == self.RELOAD_MODE_V_SPAWN_WAIT:
        daemon = False
    else:
        daemon = True
    watcher_thread.setDaemon(daemon)
    watcher_thread.start()
    return watcher_thread