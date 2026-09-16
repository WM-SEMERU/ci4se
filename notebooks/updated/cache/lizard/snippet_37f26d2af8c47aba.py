def del_label(self, name):
    labels_tag = self.root[0]
    labels_tag.remove(self._find_label(name))