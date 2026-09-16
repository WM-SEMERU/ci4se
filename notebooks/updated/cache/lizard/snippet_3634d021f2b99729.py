def set_bgcolor(self, color):
    self.bgcolor = color
    for ax in self.canvas.figure.get_axes():
        if matplotlib.__version__ < '2.0':
            ax.set_axis_bgcolor(color)
        else:
            ax.set_facecolor(color)
    if callable(self.theme_color_callback):
        self.theme_color_callback(color, 'bg')