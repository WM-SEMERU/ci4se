def objective_to_model(self, x_objective):
    x_model = []
    for k in range(self.objective_dimensionality):
        variable = self.space_expanded[k]
        new_entry = variable.objective_to_model(x_objective[0, k])
        x_model += new_entry
    return x_model