def on_board(self, *args):
    if None in (self.board, self.origin, self.destination):
        Clock.schedule_once(self.on_board, 0)
        return
    self._trigger_repoint()