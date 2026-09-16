def show_time(self, end=False):
    if self.time_label is None:
        return
    elapsed_time = time.monotonic() - self.t0
    if elapsed_time < 0:
        self.t0 = time.monotonic()
        elapsed_time = 0
    if elapsed_time > 24 * 3600:
        fmt = '%d %H:%M:%S'
    else:
        fmt = '%H:%M:%S'
    if end:
        color = '#AAAAAA'
    else:
        color = '#AA6655'
    text = "<span style='color: %s'><b>%s</b></span>" % (color, time.
        strftime(fmt, time.gmtime(elapsed_time)))
    self.time_label.setText(text)