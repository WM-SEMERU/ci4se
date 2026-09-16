def print_model(self, include_unsigned_edges=False):
    sif_str = ''
    for edge in self.graph.edges(data=True):
        n1 = edge[0]
        n2 = edge[1]
        data = edge[2]
        polarity = data.get('polarity')
        if polarity == 'negative':
            rel = '-1'
        elif polarity == 'positive':
            rel = '1'
        elif include_unsigned_edges:
            rel = '0'
        else:
            continue
        sif_str += '%s %s %s\n' % (n1, rel, n2)
    return sif_str