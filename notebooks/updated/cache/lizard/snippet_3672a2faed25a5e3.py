def get_register_expr(self, register_name, mode='post'):
    reg_info = self._arch_info.alias_mapper.get(register_name, None)
    if reg_info:
        var_base_name, offset = reg_info
    else:
        var_base_name = register_name
    var_name = self._get_var_name(var_base_name, mode)
    var_size = self._arch_info.registers_size[var_base_name]
    ret_val = self._translator.make_bitvec(var_size, var_name)
    if reg_info:
        ret_val = smtfunction.extract(ret_val, offset, self._arch_info.
            registers_size[register_name])
    return ret_val