def get_values(self):
    variable_cpds = {}
    for block in self.probability_block():
        names = self.probability_expr.searchString(block)
        var_name, parents = names[0][0], names[0][1:]
        cpds = self.cpd_expr.searchString(block)
        if 'table' in block:
            arr = np.array([float(j) for i in cpds for j in i])
            arr = arr.reshape((len(self.variable_states[var_name]), arr.
                size // len(self.variable_states[var_name])))
        else:
            arr_length = np.prod([len(self.variable_states[var]) for var in
                parents])
            arr = np.zeros((len(self.variable_states[var_name]), arr_length))
            values_dict = {}
            for prob_line in cpds:
                states = prob_line[:len(parents)]
                vals = [float(i) for i in prob_line[len(parents):]]
                values_dict[tuple(states)] = vals
            for index, combination in enumerate(product(*[self.
                variable_states[var] for var in parents])):
                arr[:, (index)] = values_dict[combination]
        variable_cpds[var_name] = arr
    return variable_cpds