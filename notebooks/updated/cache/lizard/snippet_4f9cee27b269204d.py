def meyer_penny_program():
    prog = pq.Program()
    ro = prog.declare('ro', memory_size=2)
    picard_register = ro[1]
    answer_register = ro[0]
    then_branch = pq.Program(X(0))
    else_branch = pq.Program(I(0))
    prog.inst(X(0), H(1))
    prog.inst(H(0))
    prog.measure(1, picard_register)
    prog.if_then(picard_register, then_branch, else_branch)
    prog.inst(H(0))
    prog.measure(0, answer_register)
    return prog