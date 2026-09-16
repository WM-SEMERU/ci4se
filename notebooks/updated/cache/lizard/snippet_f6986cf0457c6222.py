def __insert_child(self, parent_tree_node, index, tree_node):
    parent_item = self.__mapping[id(parent_tree_node)]
    self.item_model_controller.begin_insert(index, index, parent_item.row,
        parent_item.id)
    properties = {'display': self.__display_for_tree_node(tree_node),
        'tree_node': tree_node}
    item = self.item_model_controller.create_item(properties)
    parent_item.insert_child(index, item)
    self.__mapping[id(tree_node)] = item
    self.item_model_controller.end_insert()