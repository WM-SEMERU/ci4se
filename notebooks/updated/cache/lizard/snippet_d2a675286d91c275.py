def key_press_event(self, widget, event):
    keyname = ''
    self.logger.debug('key press event, key=%s' % keyname)
    return self.make_ui_callback('key-press', keyname)