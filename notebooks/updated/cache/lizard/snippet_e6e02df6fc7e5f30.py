def get_node_index(self, node):
    if node == self.__root_node:
        return QModelIndex()
    else:
        row = node.row()
        return self.createIndex(row, 0, node
            ) if row is not None else QModelIndex()