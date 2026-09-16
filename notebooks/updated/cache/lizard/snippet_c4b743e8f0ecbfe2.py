def get_adjacent_pathways(self, pathway):
    vertex_id = self.pathways[pathway]
    adjacent = self.vertices[vertex_id].get_adjacent_vertex_ids()
    adjacent_pathways = []
    for adjacent_id in adjacent:
        adjacent_pathways.append(self.get_pathway_from_vertex_id(adjacent_id))
    return adjacent_pathways