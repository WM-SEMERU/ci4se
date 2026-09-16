def _compute_register_list(self, operand):
    ret = []
    for reg_range in operand.reg_list:
        if len(reg_range) == 1:
            ret.append(ReilRegisterOperand(reg_range[0].name, reg_range[0].
                size))
        else:
            reg_num = int(reg_range[0].name[1:])
            reg_end = int(reg_range[1].name[1:])
            if reg_num > reg_end:
                raise NotImplementedError(
                    'Instruction Not Implemented: Invalid register range.')
            while reg_num <= reg_end:
                ret.append(ReilRegisterOperand(reg_range[0].name[0] + str(
                    reg_num), reg_range[0].size))
                reg_num = reg_num + 1
    return ret