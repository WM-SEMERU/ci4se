def comma_separated_list(self, node, subnodes):
    for item in subnodes:
        position = item.last_line, item.last_col
        first, last = find_next_comma(self.lcode, position)
        if first:
            node.op_pos.append(NodeWithPosition(last, first))