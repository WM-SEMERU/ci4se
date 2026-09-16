def host_stanzas(self, config_access):
    defn_lines = self.resolve_defn(config_access)
    for val_dict in self.variable_iter(config_access.get_variables()):
        subst = list(self.apply_substitutions(defn_lines, val_dict))
        host = subst[0]
        lines = [ConfigOutput.to_line('Host', [host])] + subst[1:]
        yield host, lines