def add_leaf(self, index, data_object, save=False):
    assert self.type == data_object.type, 'data type mismatch'
    if self._get_child_by_index(index) is not None:
        raise NodeAlreadyExistsError(
            'Leaf data node already exists at this index')
    else:
        data_node = DataNode(parent=self, index=index, data_object=
            data_object, type=self.type)
        if save:
            data_node.full_clean()
            data_node.save()
        self._add_unsaved_child(data_node)
        return data_node