def serie(self, serie):
    return dict(plot=self.node(self.graph.nodes['plot'], class_=
        'series serie-%d color-%d' % (serie.index, serie.index)), overlay=
        self.node(self.graph.nodes['overlay'], class_=
        'series serie-%d color-%d' % (serie.index, serie.index)),
        text_overlay=self.node(self.graph.nodes['text_overlay'], class_=
        'series serie-%d color-%d' % (serie.index, serie.index)))