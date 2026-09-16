def _get_go2pydotnode(self):
    go2node = {}
    for goid, goobj in self.godag.go2obj.items():
        txt = self._get_node_text(goid, goobj)
        fillcolor = self.goid2color.get(goid, 'white')
        node = self.pydot.Node(txt, shape='box', style='rounded, filled',
            fillcolor=fillcolor, color='mediumseagreen')
        go2node[goid] = node
    return go2node