def set_pointing_label(self):
    self.pointings[self.current]['label']['text'] = w.plabel.get()
    self.reset()