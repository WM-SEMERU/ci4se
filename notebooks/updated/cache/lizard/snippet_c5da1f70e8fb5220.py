def transform_32_33(inst, new_inst, i, n, offset, instructions, new_asm):
    add_size = xdis.op_size(new_inst.opcode, opcode_33)
    if inst.opname in ('MAKE_FUNCTION', 'MAKE_CLOSURE'):
        prev_inst = instructions[i - 1]
        assert prev_inst.opname == 'LOAD_CONST'
        assert isinstance(prev_inst.arg, int)
        load_fn_const = Instruction()
        load_fn_const.opname = 'LOAD_CONST'
        load_fn_const.opcode = opcode_33.opmap['LOAD_CONST']
        load_fn_const.line_no = None
        prev_const = new_asm.code.co_consts[prev_inst.arg]
        if hasattr(prev_const, 'co_name'):
            fn_name = new_asm.code.co_consts[prev_inst.arg].co_name
        else:
            fn_name = 'what-is-up'
        const_index = len(new_asm.code.co_consts)
        new_asm.code.co_consts = list(new_asm.code.co_consts)
        new_asm.code.co_consts.append(fn_name)
        load_fn_const.arg = const_index
        load_fn_const.offset = offset
        load_fn_const.starts_line = False
        load_fn_const.is_jump_target = False
        new_asm.code.instructions.append(load_fn_const)
        load_const_size = xdis.op_size(load_fn_const.opcode, opcode_33)
        add_size += load_const_size
        new_inst.offset = offset + add_size
        pass
    return add_size