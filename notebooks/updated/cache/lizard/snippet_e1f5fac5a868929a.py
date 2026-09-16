def zoomset_cb(self, setting, value, channel):
    if not self.gui_up:
        return
    info = channel.extdata._info_info
    if info is None:
        return
    scale_x, scale_y = value
    if scale_x == scale_y:
        text = self.fv.scale2text(scale_x)
    else:
        textx = self.fv.scale2text(scale_x)
        texty = self.fv.scale2text(scale_y)
        text = 'X: %s  Y: %s' % (textx, texty)
    info.winfo.zoom.set_text(text)