def get_by(self, name):
    item = self.controlled_list.get_by(name)
    if item:
        return TodoElementUX(parent=self, controlled_element=item)