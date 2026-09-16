def close(self):
    try:
        self._running = False
        self._read_thread.stop()
        self._device.close()
    except Exception:
        pass
    self.on_close()