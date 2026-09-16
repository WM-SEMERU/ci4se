def create_item(self, name):
    item = self.app.create_item(name)
    return TodoListUX(ux=self, controlled_list=item)