def insert_pattern(self, pattern, index):
    LOGGER.debug("> Inserting '{0}' at '{1}' index.".format(pattern, index))
    self.remove_pattern(pattern)
    self.beginInsertRows(self.get_node_index(self.root_node), index, index)
    pattern_node = PatternNode(name=pattern)
    self.root_node.insert_child(pattern_node, index)
    self.endInsertRows()
    self.pattern_inserted.emit(pattern_node)
    return True