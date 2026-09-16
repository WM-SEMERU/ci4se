def write_graph(self, filename):
    f = open(filename, 'w')
    f.write(self._get_graphviz_data())
    f.close()