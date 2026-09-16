def _translate_add(self, oprnd1, oprnd2, oprnd3):
    assert oprnd1.size and oprnd2.size and oprnd3.size
    assert oprnd1.size == oprnd2.size
    op1_var = self._translate_src_oprnd(oprnd1)
    op2_var = self._translate_src_oprnd(oprnd2)
    op3_var, op3_var_constrs = self._translate_dst_oprnd(oprnd3)
    if oprnd3.size > oprnd1.size:
        result = smtfunction.zero_extend(op1_var, oprnd3.size
            ) + smtfunction.zero_extend(op2_var, oprnd3.size)
    elif oprnd3.size < oprnd1.size:
        result = smtfunction.extract(op1_var + op2_var, 0, oprnd3.size)
    else:
        result = op1_var + op2_var
    return [op3_var == result] + op3_var_constrs