def cmd_pan(self, x=None, y=None, ch=None):
    viewer = self.get_viewer(ch)
    if viewer is None:
        self.log('No current viewer/channel.')
        return
    pan_x, pan_y = viewer.get_pan()
    if x is None and y is None:
        self.log('x=%f y=%f' % (pan_x, pan_y))
    else:
        if x is not None:
            if y is None:
                y = pan_y
        if y is not None:
            if x is None:
                x = pan_x
        viewer.set_pan(x, y)