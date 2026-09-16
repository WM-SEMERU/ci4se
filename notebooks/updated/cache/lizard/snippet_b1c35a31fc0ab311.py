def __add_bgedge(self, bgedge, merge=True):
    if bgedge.vertex1 in self.bg and bgedge.vertex2 in self.bg[bgedge.vertex1
        ] and merge:
        key = min(self.bg[bgedge.vertex1][bgedge.vertex2].keys())
        self.bg[bgedge.vertex1][bgedge.vertex2][key]['attr_dict']['multicolor'
            ] += bgedge.multicolor
        self.bg[bgedge.vertex1][bgedge.vertex2][key]['attr_dict']['data'] = {}
    else:
        self.bg.add_edge(bgedge.vertex1, bgedge.vertex2, attr_dict={
            'multicolor': deepcopy(bgedge.multicolor), 'data': bgedge.data})
    self.cache_valid['overall_set_of_colors'] = False