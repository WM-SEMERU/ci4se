def autostack(self):
    num_slices = 0
    for v in self.graph.all_variables:
        num_slices += self.mesh_to_impl[v.mesh].size
    if num_slices >= 2 ** 16:
        max_combined_slice_size = 2 ** 27
    else:
        max_combined_slice_size = 2 ** 16
    self.graph.rewrite_stack_variables(mesh_to_impl=self.mesh_to_impl,
        max_combined_slice_size=max_combined_slice_size)