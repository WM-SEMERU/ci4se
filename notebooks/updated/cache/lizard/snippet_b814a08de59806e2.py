def start_pan(self, x, y, button):
    bd = self.viewer.get_bindings()
    data_x, data_y = self.viewer.get_data_xy(x, y)
    event = PointEvent(button=button, state='down', data_x=data_x, data_y=
        data_y, viewer=self.viewer)
    if button == 1:
        bd.ms_pan(self.viewer, event, data_x, data_y)
    elif button == 3:
        bd.ms_zoom(self.viewer, event, data_x, data_y)