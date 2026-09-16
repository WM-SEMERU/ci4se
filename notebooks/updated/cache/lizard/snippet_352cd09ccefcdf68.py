def filter_children(self):
    real_children = []
    for child in self.children:
        if child.name == '<module>':
            self.local_children.append(child)
        else:
            real_children.append(child)
    self.children = real_children