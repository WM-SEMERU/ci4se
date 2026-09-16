def get_all_children(self):
    all_children = set()
    for parent in self.children:
        all_children.add(parent.item_id)
        all_children |= parent.get_all_children()
    return all_children