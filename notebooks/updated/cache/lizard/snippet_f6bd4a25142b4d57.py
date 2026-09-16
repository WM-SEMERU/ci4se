def set_copy_mode(self, use_copy: bool):
    for group in self.rootItem.children:
        for proto in group.children:
            proto.copy_data = use_copy