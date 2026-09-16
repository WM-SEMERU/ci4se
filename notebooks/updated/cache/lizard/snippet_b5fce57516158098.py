def end_output(self, **kwargs):
    self.write_edges()
    self.end_graph()
    if self.has_part('outro'):
        self.write_outro()
    self.close_fileoutput()