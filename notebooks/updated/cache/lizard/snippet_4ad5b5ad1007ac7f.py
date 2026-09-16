def selection_r(acquisition_function, samples_y_aggregation, x_bounds,
    x_types, regressor_gp, num_starting_points=100,
    minimize_constraints_fun=None):
    minimize_starting_points = [lib_data.rand(x_bounds, x_types) for i in
        range(0, num_starting_points)]
    outputs = selection(acquisition_function, samples_y_aggregation,
        x_bounds, x_types, regressor_gp, minimize_starting_points,
        minimize_constraints_fun=minimize_constraints_fun)
    return outputs