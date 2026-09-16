def _find_common_prefix(self, node1, node2):
    tokens1 = [item.strip() for item in node1.split(self.node_separator)]
    tokens2 = [item.strip() for item in node2.split(self.node_separator)]
    ret = []
    for token1, token2 in zip(tokens1, tokens2):
        if token1 == token2:
            ret.append(token1)
        else:
            break
    return self.node_separator.join(ret)