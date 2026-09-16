def _get_program_gates(prog):
    return sorted({i for i in prog if isinstance(i, Gate)}, key=lambda g: g
        .out())