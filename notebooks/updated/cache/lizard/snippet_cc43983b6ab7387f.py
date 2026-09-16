def _update_color_hsv(self, event=None):
    if event is None or event.widget.old_value != event.widget.get():
        h = self.hue.get()
        s = self.saturation.get()
        v = self.value.get()
        sel_color = hsv_to_rgb(h, s, v)
        self.red.set(sel_color[0])
        self.green.set(sel_color[1])
        self.blue.set(sel_color[2])
        if self.alpha_channel:
            sel_color += self.alpha.get(),
            self.alphabar.set_color(sel_color)
        hexa = rgb_to_hexa(*sel_color)
        self.hexa.delete(0, 'end')
        self.hexa.insert(0, hexa)
        self.square.set_hsv((h, s, v))
        self.bar.set(h)
        self._update_preview()