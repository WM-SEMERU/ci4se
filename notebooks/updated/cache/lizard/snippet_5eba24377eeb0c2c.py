def trim_tree(self, node):
    data_len = len(node[-1])
    if node[1] == -1 and node[2] == -1:
        if data_len == 0:
            return 1
        else:
            return 0
    else:
        if self.trim_tree(node[1]) == 1:
            node[1] = -1
        if self.trim_tree(node[2]) == 1:
            node[2] = -1
        if node[1] == -1 and node[2] == -1:
            if data_len == 0:
                return 1
            else:
                return 0