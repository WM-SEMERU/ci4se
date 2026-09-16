def swap_vertices(self, i, j):
    store_vertex_i = self.vertices[i]
    store_vertex_j = self.vertices[j]
    self.vertices[j] = store_vertex_i
    self.vertices[i] = store_vertex_j
    for k in range(len(self.vertices)):
        for swap_list in [self.vertices[k].children, self.vertices[k].parents]:
            if i in swap_list:
                swap_list[swap_list.index(i)] = -1
            if j in swap_list:
                swap_list[swap_list.index(j)] = i
            if -1 in swap_list:
                swap_list[swap_list.index(-1)] = j