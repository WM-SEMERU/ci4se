def _update_color_rgb(self, event=None):
    if event is None or event.widget.old_value != event.widget.get():
        r = self.red.get()
        g = self.green.get()
        b = self.blue.get()
        h, s, v = rgb_to_hsv(r, g, b)
        self.hue.set(h)
        self.saturation.set(s)
        self.value.set(v)
        args = r, g, b
        if self.alpha_channel:
            args += self.alpha.get(),
            self.alphabar.set_color(args)
        hexa = rgb_to_hexa(*args)
        self.hexa.delete(0, 'end')
        self.hexa.insert(0, hexa)
        self.square.set_hsv((h, s, v))
        self.bar.set(h)
        self._update_preview()