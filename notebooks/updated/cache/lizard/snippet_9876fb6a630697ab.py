def uid_something_colon(self, node):
    node.op_pos = [NodeWithPosition(node.uid, (node.first_line, node.
        first_col))]
    position = node.body[0].first_line, node.body[0].first_col
    last, first = self.operators[':'].find_previous(position)
    node.op_pos.append(NodeWithPosition(last, first))
    return last