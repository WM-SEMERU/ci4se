def get_token(self, token_node_id, token_attrib='token'):
    return self.node[token_node_id][self.ns + ':' + token_attrib]