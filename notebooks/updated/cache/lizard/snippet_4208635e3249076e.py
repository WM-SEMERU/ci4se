def annotated(self):
    annotated_vertices = {vertex: AnnotatedVertex(id=vertex_id, annotation=
        six.text_type(vertex)) for vertex_id, vertex in zip(itertools.count
        (), self.vertices)}
    annotated_edges = [AnnotatedEdge(id=edge_id, annotation=six.text_type(
        edge), head=annotated_vertices[self.head(edge)].id, tail=
        annotated_vertices[self.tail(edge)].id) for edge_id, edge in zip(
        itertools.count(), self.edges)]
    return AnnotatedGraph(vertices=annotated_vertices.values(), edges=
        annotated_edges)