def apply_saved_layout(self):
    num_widgets = self.config.get(self.config_key + '/num_widgets', int)
    if num_widgets:
        sizes = []
        for i in range(num_widgets):
            key = '%s/size_%d' % (self.config_key, i)
            size = self.config.get(key, int)
            sizes.append(size)
        self.setSizes(sizes)
        return True
    return False