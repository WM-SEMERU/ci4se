def run(self):
    prev_frame_time = time.time()
    while True:
        self._win.switch_to()
        self._win.dispatch_events()
        now = time.time()
        self._update(now - prev_frame_time)
        prev_frame_time = now
        self._draw()
        self._win.flip()