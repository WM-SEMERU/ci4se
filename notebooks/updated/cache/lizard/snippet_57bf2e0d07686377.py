def infer_operands_size(operands):
    size = None
    for oprnd in operands:
        if oprnd.size:
            size = oprnd.size
            break
    if size:
        for oprnd in operands:
            if not oprnd.size:
                oprnd.size = size
    else:
        for oprnd in operands:
            if isinstance(oprnd, X86ImmediateOperand) and not oprnd.size:
                oprnd.size = arch_info.architecture_size