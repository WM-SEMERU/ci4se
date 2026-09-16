def pause(self):
    if self.state == STATE_PLAYING:
        self._player.set_state(Gst.State.PAUSED)
        self.state = STATE_PAUSED