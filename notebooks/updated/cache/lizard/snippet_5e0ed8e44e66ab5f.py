def push(self, next_dfa, next_state, node_type, lineno, column):
    dfa, state, node = self.stack[-1]
    new_node = Node(node_type, None, [], lineno, column)
    self.stack[-1] = dfa, next_state, node
    self.stack.append((next_dfa, 0, new_node))