def set_sort_cb(self, w, index):
    name = self.sort_options[index]
    self.t_.set(sort_order=name)