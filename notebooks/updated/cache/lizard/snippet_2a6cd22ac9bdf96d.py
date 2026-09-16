def substitute_params(self, substitutions):
    param_dict = {}
    for k, v in self.param_dict.items():
        param_dict[k] = replace_substitutions(v, substitutions)
    return param_dict