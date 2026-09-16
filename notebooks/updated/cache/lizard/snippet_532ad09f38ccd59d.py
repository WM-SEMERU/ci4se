def solutions_as_2d_trajectories(self, x_axis, y_axis):
    if not self.solutions:
        raise Exception(
            'No intermediate solutions returned. Re-run inference with return_intermediate_solutions=True'
            )
    index_x = self.parameter_index(x_axis)
    index_y = self.parameter_index(y_axis)
    x, y = [], []
    for parameters, initial_conditions in self.solutions:
        all_values = parameters + initial_conditions
        x.append(all_values[index_x])
        y.append(all_values[index_y])
    return x, y