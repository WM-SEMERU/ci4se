def print_token(self, token_node_index):
    err_msg = 'The given node is not a token node.'
    assert isinstance(self.nodes[token_node_index], TokenNode), err_msg
    onset = self.nodes[token_node_index].onset
    offset = self.nodes[token_node_index].offset
    return self.text[onset:offset]