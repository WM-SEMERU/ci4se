def __edges(self, nbunch=None, keys=False):
    for v1, v2, key, data in self.bg.edges(nbunch=nbunch, data=True, keys=True
        ):
        bgedge = BGEdge(vertex1=v1, vertex2=v2, multicolor=data['attr_dict'
            ]['multicolor'], data=data['attr_dict']['data'])
        if not keys:
            yield bgedge
        else:
            yield bgedge, key