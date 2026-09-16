def ms_rotate(self, viewer, event, data_x, data_y, msg=True):
    if not self.canrotate:
        return True
    msg = self.settings.get('msg_rotate', msg)
    x, y = self.get_win_xy(viewer)
    if event.state == 'move':
        self._rotate_xy(viewer, x, y)
    elif event.state == 'down':
        if msg:
            viewer.onscreen_message('Rotate (drag around center)', delay=1.0)
        self._start_x, self._start_y = x, y
        self._start_rot = viewer.get_rotation()
    else:
        viewer.onscreen_message(None)
    return True