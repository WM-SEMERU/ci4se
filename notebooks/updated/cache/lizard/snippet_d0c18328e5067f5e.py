def writexml(self, writer, indent='', addindent='', newl=''):
    writer.write('%s<dataset id="%s" dimensions="%s">%s' % (indent, self.
        datasetid, self.dimensions, newl))
    indent2 = indent + addindent
    for l, x, y in zip(self.labels, self.frames, self.values):
        writer.write('%s<point label="%s" frame="%d" value="%f"/>%s' % (
            indent2, self.int2label[l], x, y, newl))
    writer.write('%s</dataset>%s' % (indent, newl))