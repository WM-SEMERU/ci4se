def write_to_file(self, out_data):
    full_var_name = self.consensus_type + '_' + self.variable
    if '-hour' in self.consensus_type:
        if full_var_name not in out_data.variables.keys():
            var = out_data.createVariable(full_var_name, 'f4', ('y', 'x'),
                zlib=True, least_significant_digit=3, shuffle=True)
        else:
            var = out_data.variables[full_var_name]
        var.coordinates = 'y x'
    else:
        if full_var_name not in out_data.variables.keys():
            var = out_data.createVariable(full_var_name, 'f4', ('time', 'y',
                'x'), zlib=True, least_significant_digit=3, shuffle=True)
        else:
            var = out_data.variables[full_var_name]
        var.coordinates = 'time y x'
    var[:] = self.data
    var.units = self.units
    var.long_name = self.consensus_type + '_' + self.variable
    return