def dependencies(self, deps_dict):
    try:
        import pygraphviz as pgv
    except ImportError:
        graph_easy, comma = '', ''
        if self.image == 'ascii' and not os.path.isfile('/usr/bin/graph-easy'):
            comma = ','
            graph_easy = ' graph-easy'
        print(
            "Require 'pygraphviz{0}{1}': Install with 'slpkg -s sbo pygraphviz{1}'"
            .format(comma, graph_easy))
        raise SystemExit()
    if self.image != 'ascii':
        self.check_file()
    try:
        G = pgv.AGraph(deps_dict)
        G.layout(prog='fdp')
        if self.image == 'ascii':
            G.write('{0}.dot'.format(self.image))
            self.graph_easy()
        G.draw(self.image)
    except IOError:
        raise SystemExit()
    if os.path.isfile(self.image):
        print("Graph image file '{0}' created".format(self.image))
    raise SystemExit()