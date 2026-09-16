def remove_event(self, name=None, time=None, chan=None):
    self.annot.remove_event(name=name, time=time, chan=chan)
    self.update_annotations()