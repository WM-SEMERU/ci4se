def showxy(self, viewer, data_x, data_y):
    cur_time = time.time()
    elapsed = cur_time - self._cursor_last_update
    if elapsed > self.cursor_interval:
        self._cursor_task.clear()
        self.gui_do_oneshot('field-info', self._showxy, viewer, data_x, data_y)
    else:
        self._cursor_task.data.setvals(viewer=viewer, data_x=data_x, data_y
            =data_y)
        period = self.cursor_interval - elapsed
        self._cursor_task.cond_set(period)
    return True