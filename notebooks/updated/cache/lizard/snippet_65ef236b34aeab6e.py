def merge_vertices(self):
    unique, inverse = grouping.unique_rows(self.vertices)
    self.vertices = self.vertices[unique]
    if self.colors is not None and len(self.colors) == len(inverse):
        self.colors = self.colors[unique]