def update_evt_types(self):
    self.event_types = self.parent.notes.annot.event_types
    self.idx_evt_type.clear()
    self.frequency['norm_evt_type'].clear()
    for ev in self.event_types:
        self.idx_evt_type.addItem(ev)
        self.frequency['norm_evt_type'].addItem(ev)