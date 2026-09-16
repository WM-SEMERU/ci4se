def set_imap_cb(self, w, index):
    name = imap.get_names()[index]
    self.t_.set(intensity_map=name)