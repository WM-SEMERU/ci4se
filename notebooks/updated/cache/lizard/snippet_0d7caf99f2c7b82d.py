def get_vertex_obj_from_pathway(self, pathway):
    if pathway in self.pathways:
        vertex_id = self.pathways[pathway]
        return self.vertices[vertex_id]
    else:
        return None