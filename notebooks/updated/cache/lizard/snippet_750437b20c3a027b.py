def edge_to_string(self, e):
    edge = list()
    edge.append(quote_if_necessary(str(e[0])))
    edge.append(self.edge_connect_symbol)
    edge.append(quote_if_necessary(str(e[1])))
    if len(self.edge_attr[e]) is 0:
        return ''.join(edge)
    edge.append('  [')
    for a in self.edge_attr[e]:
        edge.append(a)
        edge.append('=')
        edge.append(quote_if_necessary(str(self.edge_attr[e][a])))
        edge.append(', ')
    edge = edge[:-1]
    edge.append(']')
    return ''.join(edge)