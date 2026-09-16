def get_variable(self, var_name):
    assert isinstance(var_name, str)
    if isinstance(var_name, str):
        for var in self.variable_list:
            if var.name == var_name:
                return var
        new_var = Variable(var_name)
        self.variable_list.append(new_var)
        return new_var