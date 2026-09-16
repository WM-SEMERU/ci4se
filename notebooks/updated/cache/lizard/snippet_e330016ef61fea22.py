def solve(self, print_solution=False):
    self._cp_solver = cp_model.CpSolver()
    status = self._cp_solver.Solve(self._model)
    if status != cp_model.OPTIMAL:
        if status == cp_model.FEASIBLE:
            logging.warning('A potentially suboptimal solution was found.')
        else:
            logging.error('Solver returned status %d.', status)
            raise SolverError(
                'The solver could not solve the problem and returned status {}.'
                .format(status))
    if print_solution:
        print_cp_model_solution.print_solution(self._model, self._cp_solver)
    layout = []
    for mtf_dimension_name in self._layout_validator.splittable_mtf_dimension_names:
        for mesh_dimension_name in self._layout_validator.mesh_dimension_name_to_size:
            value = self._cp_solver.Value(self._global_vars[
                mtf_dimension_name, mesh_dimension_name])
            if value:
                layout.append(mtf_dimension_name + ':' + mesh_dimension_name)
    layout.sort()
    return ';'.join(layout)