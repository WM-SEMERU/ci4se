def _inject_synthetic_dist_requirements(self, dist, req_lib_addr):
    whl_dir, base = split_basename_and_dirname(dist)
    whl_metadata = base.split('-')
    req_name = '=='.join([whl_metadata[0], whl_metadata[1]])
    req = PythonRequirement(req_name, repository=whl_dir)
    self.context.build_graph.inject_synthetic_target(req_lib_addr,
        PythonRequirementLibrary, requirements=[req])