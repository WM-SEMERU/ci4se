def attribute_changed(self, node, column):
    index = self.get_attribute_index(node, column)
    if index is not None:
        self.dataChanged.emit(index, index)
        return True
    else:
        return False