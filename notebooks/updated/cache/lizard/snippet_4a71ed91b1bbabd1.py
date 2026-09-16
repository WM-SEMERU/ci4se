def transition(self, duration, color=None, brightness=None):
    if color == RGB_WHITE:
        self.white()
        color = None
    elif self.color == RGB_WHITE and color is not None:
        self.color = color
        color = None
    if duration == 0:
        if color:
            self.color = color
        if brightness is not None:
            self.brightness = brightness
        return
    if color != self.color or brightness != self.brightness:
        if color is None and brightness == self.brightness:
            return
        if color is None:
            self._transition(duration, brightness=brightness)
        else:
            self._transition(duration, hue_of_color(color), brightness)