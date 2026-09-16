def make_symbolic_state(project, reg_list, stack_length=80):
    input_state = Identifier.make_initial_state(project, stack_length)
    symbolic_state = input_state.copy()
    for reg in reg_list:
        symbolic_state.registers.store(reg, symbolic_state.solver.BVS(
            'sreg_' + reg + '-', project.arch.bits))
    symbolic_state.regs.sp = input_state.regs.sp
    symbolic_state.regs.bp = input_state.regs.bp
    return symbolic_state